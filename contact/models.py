from django.db import models
from cars.models import Cars
from user.models import User
from django import forms


class Contacts(models.Model):
    car_title = models.ForeignKey(Cars, on_delete=models.CASCADE)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=300)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=150)
    email = models.EmailField()
    phone_number = models.CharField(blank=True, null=True, max_length=100)
    subject = models.CharField(max_length=500)
    description = models.TextField()
    create_date = models.DateField(auto_now_add=True)
    response = models.TextField(blank=True, null=True)
    is_response = models.BooleanField(default=False)

    def __str__(self):
        return self.email

    class Meta:
        verbose_name_plural = 'Contacts'
        db_table = 'Contacts'


class ContactModelForm(forms.ModelForm):
    class Meta:
        model = Contacts
        fields = '__all__'
