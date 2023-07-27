from django.http import HttpRequest
from django.shortcuts import render
from django.views import View
from django.views.generic import ListView, DetailView
from cars.models import Cars


def save_customers_inquiry():
    pass


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
        print(request.POST.get('email'))


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
