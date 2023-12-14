from django.test import TestCase
from contact.forms import ContactModelForm


class TestForm(TestCase):
    def test_site_contact_is_valid(self):
        new_msg = ContactModelForm(data={
            'fullname': 'Pegah Mousavi',
            'email': 'pegah.mousavi@gmail.com',
            'subject': 'alireza',
            'phone': '09366046959',
            'message': "تو کل این دنیا مطمئنم کسی از تو بیشتر دوسم نداره...."
        })

        self.assertTrue(new_msg.is_valid())

    def test_site_contact_is_false(self):
        form = ContactModelForm(data={})
        self.assertFalse(form.is_valid())
