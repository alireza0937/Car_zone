from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import User


class RegistrationForm(forms.Form):
    user_name = forms.CharField(max_length=150,
                                widget=forms.TextInput(attrs={
                                    'placeholder': 'Username'
                                }))
    email = forms.EmailField(widget=forms.TextInput(attrs={
        'placeholder': 'Email'
    }))
    password = forms.CharField(max_length=50,
                               widget=forms.TextInput(attrs={
                                   'placeholder': 'Password'
                               }))
    password_repeat = forms.CharField(max_length=50,
                                      widget=forms.TextInput(attrs={
                                          'placeholder': 'Repeat-Password'
                                      }))


class RegistrationModelForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
