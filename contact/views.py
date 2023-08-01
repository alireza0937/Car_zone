from django.contrib import messages
from django.http import HttpRequest
from django.shortcuts import render, redirect
from django.views import View

from contact.forms import ContactModelForm
from contact.models import SiteContact


def save_users_contact_forms(request):
    fullname = request.POST.get("fullname")
    email = request.POST.get('email')
    subject = request.POST.get('subject')
    phone = request.POST.get('phone')
    message = request.POST.get('message')
    contact_form = SiteContact(fullname=fullname,
                               email=email,
                               subject=subject,
                               phone=phone,
                               message=message)
    contact_form.save()


class SiteContactView(View):
    def get(self, request: HttpRequest):
        form = ContactModelForm()
        return render(request, 'contact/contact.html', context={
            'form': form
        })

    def post(self, request: HttpRequest):
        form = ContactModelForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Successfully Sent')
            return redirect('contact-page')

