from django.contrib import messages
from django.http import HttpRequest, HttpResponse, JsonResponse
from django.shortcuts import render, redirect
from django.views import View
from django.views.generic import ListView, DetailView
from cars.models import Cars
from contact.models import Contacts
import MySQLdb



def check_had_inquired(request, user_id, car_id):
    if not Contacts.objects.filter(user_id_id=user_id, car_title_id=car_id).exists():
        save_permission = True
    else:
        save_permission = False
    return_message(request, save_permission)
    return save_permission


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
    response = check_had_inquired(request, user_id, car_title)
    if response:
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


def return_message(request, permission):
    if permission:
        messages.success(request, 'Successfully added.')
    else:
        messages.error(request, 'You have already inquired about this car.')


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
        return redirect('cars-detail-page', slug=slug)


class SearchCars(View):
    def get(self, request: HttpRequest):
        searched_word = request.GET.get('keyword')
        search_response = Cars.objects.filter(title__icontains=searched_word).all()
        return render(request, 'car/car_search.html', context={
            'data': search_response
        })


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


def shayan_test(request:HttpRequest):
    dbconnect = MySQLdb.connect("localhost", "root", "pegah", "car_zonedb")

    cursor = dbconnect.cursor()
    cursor.execute("SELECT * from Cars")

    data = cursor.fetchone()

    dbconnect.close()
    return JsonResponse({'data': data})
    # return HttpResponse(print())