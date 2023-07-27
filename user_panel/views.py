from django.http import HttpRequest
from django.shortcuts import render
from django.views import View


class UserPanel(View):
    def get(self,request: HttpRequest):
        return render(request, 'user_panel/dashboard.html')
