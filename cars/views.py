from django.contrib import messages
from django.http import HttpRequest
from django.shortcuts import render, redirect
from django.urls import reverse
from django.views import View
from django.views.generic import ListView, DetailView
from cars.models import Cars
from contact.models import Contacts


def save_customers_inquiry(request):
    first_name = request.POST.get('first_name')
    last_name = request.POST.get('last_name')
    user_id = request.POST.get('user_id')
    customer_need = request.POST.get('customer_need')
    car_title = request.POST.get('car_title')
    city = request.POST.get('city')
    state = request.POST.get('state')
    email = request.POST.get('email')
    phone = request.POST.get('phone')
    message = request.POST.get('message')
    entered_info = Contacts(car_title_id=car_title,
                            user_id_id=user_id,
                            first_name=first_name,
                            last_name=last_name,
                            city=city,
                            state=state,
                            email=email,
                            phone_number=phone,
                            subject=customer_need,
                            description=message)
    entered_info.save()


class CarsListView(ListView):
    model = Cars
    template_name = 'car/car.html'
    paginate_by = 4
    context_object_name = 'car'

    def get_queryset(self):
        data = super(CarsListView, self).get_queryset()
        return data


class CarsDetailView(DetailView):
    model = Cars
    template_name = 'car/cars_details.html'
    context_object_name = 'car'

    def post(self, request: HttpRequest, slug):

        save_customers_inquiry(request)
        messages.success(request, 'Your feedback successfully saved')
        return redirect('cars-detail-page',slug=slug)


class SearchCars(View):
    def get(self, request: HttpRequest):

        searched_word = request.GET.get('keyword')
        searched_Condition = request.GET.get('Condition')
        searched_location = request.GET.get('location')
        searched_year = request.GET.get('year')
        searched_category = request.GET.get('category')
        if searched_word is not None:
            search_response = Cars.objects.filter(title__icontains=searched_word).all()
            return render(request, 'car/car_search.html', context={
                'data': search_response
            })
        else:
            print(searched_word, searched_Condition, searched_location, searched_year, searched_category)


def search_box(request: HttpRequest):
    type = Cars.objects.values_list('body_style', flat=True).distinct()
    year = Cars.objects.values_list('year', flat=True).distinct()
    location = Cars.objects.values_list('city', flat=True).distinct()
    condition = Cars.objects.values_list('condition', flat=True).distinct()
    transmission = Cars.objects.values_list('transmission', flat=True).distinct()
    data = {
        'type': type,
        'year': year,
        'condition': condition,
        'transmission': transmission,
        'location': location
    }
    return render(request, 'car/include/search_box.html', context=data)
