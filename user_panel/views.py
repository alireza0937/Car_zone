from django.http import HttpRequest
from django.shortcuts import render
from django.views import View
from contact.models import Contacts
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required


@method_decorator(login_required, name='dispatch')
class UserPanel(View):
    def get(self, request: HttpRequest):
        all_inquires = Contacts.objects.filter(user_id_id=request.user.id).all()
        return render(request, 'user_panel/dashboard.html', context={
            'all_inquires': all_inquires
        })
