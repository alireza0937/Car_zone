from django.test import TestCase
from cars.models import Cars


class TestModels(TestCase):

    def setUp(self):
        self.new_obj = Cars.objects.create(
            title='pegah mousavi khatibi',
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

        self.new_obj2 = Cars.objects.create(
            title='pegah mousavi khatibi',
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

    def test_car_slug_field(self):
        self.assertEqual(self.new_obj.slug, 'pegah-mousavi-khatibi')
        self.assertEqual(self.new_obj2.slug, 'pegah-mousavi-khatibi')

        self.assertEqual(self.new_obj.__str__(), 'pegah mousavi khatibi')
        self.assertEqual(self.new_obj2.__str__(), 'pegah mousavi khatibi')



