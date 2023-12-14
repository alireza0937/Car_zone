from django.test import TestCase, Client
from django.urls import reverse
from cars.models import Cars


class TestViews(TestCase):

    def setUp(self):
        self.client = Client()
        self.list_url = reverse('cars-list-page')
        self.new_obj = Cars.objects.create(
            title='test',
            state='test',
            city='test',
            color='test',
            model='test',
            year=1990,
            condition='test',
            price=2000,
            description='test',
            features='',
            body_style='test',
            engine='test',
            transmission='test',
            fuel_type='test',
            no_of_owner='test',
            interior='test',
            is_featured=False,
            passenger=4,
            doors=5,
            vin_no=2,
            miles=3,
        )
        self.detail_url = reverse('cars-detail-page', kwargs={'slug': self.new_obj.slug})
        self.search = reverse('search-car-page') + f'?keyword={self.new_obj.title}'

    def test_CarsListView_GET(self):
        response = self.client.get(self.list_url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'car/car.html')

    def test_CarsDetailView(self):
        response = self.client.get(self.detail_url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'car/cars_details.html')

    def test_SearchCars(self):
        response = self.client.get(self.search)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'car/car_search.html')
