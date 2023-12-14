from django.test import SimpleTestCase
from django.urls import resolve, reverse

from cars.views import CarsListView, SearchCars, CarsDetailView


class TestCars(SimpleTestCase):

    def test_cars_list_page(self):
        url = reverse('cars-list-page')
        response = resolve(url)
        self.assertEquals(response.func.view_class, CarsListView)

    def test_cars_detail_page(self):
        url = reverse('cars-detail-page', args=['some-slug'])
        response = resolve(url)
        self.assertEquals(response.func.view_class, CarsDetailView)

    def test_search_car_page(self):
        url = reverse('search-car-page')
        response = resolve(url)
        self.assertEquals(response.func.view_class, SearchCars)
