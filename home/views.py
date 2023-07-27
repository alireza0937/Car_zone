from django.http import HttpRequest
from django.shortcuts import render
from django.views.generic import TemplateView
from cars.models import Cars
from site_setting.models import Setting, Contact
from team.models import Team


class Home(TemplateView):
    template_name = 'home/index.html'

    def get_context_data(self, **kwargs):
        context = super(Home, self).get_context_data()
        context['all_members'] = Team.objects.all()
        context['slider'] = Setting.objects.filter(is_active=True).all()
        context['featured_cars'] = Cars.objects.filter(is_featured=True).all()
        context['all_cars'] = Cars.objects.order_by('-created_date').all()[:6]
        return context


def header_components(request):
    contact_information = Contact.objects.filter(is_active=True).first()

    data = {
        'contact_information': contact_information
    }
    return render(request, 'share/header.html', context=data)


def header_components2(request):
    return render(request, 'share/header2.html')


def footer_components(request):
    contact_information = Contact.objects.filter(is_active=True).first()
    data = {
        'contact_information': contact_information
    }
    return render(request, 'share/footer.html', context=data)


def about_us(request: HttpRequest):
    return render(request, 'home/about.html')


def services(request):
    return render(request, 'home/services.html')
