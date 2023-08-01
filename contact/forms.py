from django import forms
from contact.models import SiteContact


class ContactModelForm(forms.ModelForm):
    class Meta:
        model = SiteContact
        fields = '__all__'

        widgets = {
            'fullname': forms.TextInput(attrs={
                'placeholder': 'Fullname',


            }),
            'email': forms.TextInput(attrs={
                'placeholder': 'Email',

            }),
            'subject': forms.TextInput(attrs={
                'placeholder': 'Subject'
            }),
            'phone': forms.TextInput(attrs={
                'placeholder': 'Phone Number'
            }),
            'message': forms.Textarea(attrs={
                'placeholder': 'Write Your Message',
                'style': 'width: 700px; height: 100px;'
            })
        }
