from django.contrib.sites.shortcuts import get_current_site
from django.http import HttpRequest, HttpResponse
from django.shortcuts import render, redirect
from django.template.loader import render_to_string
from django.urls import reverse
from django.utils.encoding import force_bytes
from django.utils.http import urlsafe_base64_encode
from django.views import View
from user.forms import RegistrationModelForm
from django.contrib import messages
from django.contrib.auth import login, logout, authenticate
from django.core.mail import send_mail, EmailMessage
from .models import User
from config.settings import EMAIL_HOST_USER
from django.utils.crypto import get_random_string
from .token import account_activation_token
import redis


def activate(request, uidb64, token):
    return redirect('index-page')


def send_activation_code_to_email(request: HttpRequest, user, to_email):
    mail_subject = 'Activate Your Account'
    message = render_to_string(template_name='user/activate_account.html', context={
        'user': user.username,
        'domain': get_current_site(request).domain,
        'uid': urlsafe_base64_encode(force_bytes(user.pk)),
        'token': account_activation_token.make_token(user),
        'protocol': 'https' if request.is_secure() else 'http'

    })
    email = EmailMessage(mail_subject, message, to=[to_email])
    if email.send():
        messages.success(request, "activation code has been sent to your email")
    else:
        messages.error(request, "Email didn't sent.")


def send_activation_code(user):
    user.email_activation_code = get_random_string(20)
    user.is_active = False
    user.save()


class RegisterView(View):
    def get(self, request):
        register_form = RegistrationModelForm()
        return render(request, 'user/register.html', context={
            'form': register_form
        })

    def post(self, request: HttpRequest):
        register_form = RegistrationModelForm(request.POST)
        if register_form.is_valid():
            register_form.save()
            user_details = User.objects.get(email=request.POST.get('email'))
            send_activation_code_to_email(request, user_details, user_details.email)
            return redirect(reverse('login-page'))

        register_form = RegistrationModelForm()
        messages.error(request, "Something went wrong.")
        return render(request, 'user/register.html', context={
            'form': register_form
        })


def active_account(request: HttpRequest, activation_code):
    user_detail = User.objects.filter(email_activation_code=activation_code).first()
    if user_detail is not None:
        user_detail.is_active = True
        user_detail.save()
        messages.success(request, 'Your Account Activated.')
        return redirect(reverse('index-page'))
    else:
        messages.error(request, 'Code is incorrect.')
        return redirect(reverse('registration-page'))


class LoginView(View):
    def get(self, request):
        return render(request, 'user/login.html')

    def post(self, request: HttpRequest):
        username = request.POST.get('username')
        password = request.POST.get('Password')
        connection = redis.Redis(host='localhost', port=6379, decode_responses=True)
        client_ip = request.META.get("REMOTE_ADDR")
        if connection.exists(client_ip):
            connection.incr(client_ip)
        else:
            connection.set(client_ip, 1, 20)
        if int(connection.get(client_ip)) > 5:
            return HttpResponse(status=403)
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user=user)
            return redirect(reverse('index-page'))

        else:
            messages.info(request, 'Username or Password is incorrect.')
            return render(request, 'user/login.html')


def logout_button(request: HttpRequest):
    logout(request)
    return redirect(reverse('index-page'))


class ForgetPassWordView(View):
    def get(self, request: HttpRequest):
        return render(request, 'user/forget_password.html')

    def post(self, request: HttpRequest):
        entered_email = request.POST.get('email')
        if User.objects.filter(email=entered_email).exists():
            send_mail(
                subject="Reset Account Password",
                message="Here is the message.",
                from_email=EMAIL_HOST_USER,
                recipient_list=[entered_email],
                fail_silently=True
            )

            messages.success(request, "Check Your Email")
            return redirect(reverse('forget-password-page'))

        messages.error(request, 'The Email Is Incorrect.')
        return redirect(reverse('forget-password-page'))
