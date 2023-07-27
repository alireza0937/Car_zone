from django.urls import path
from . import views

urlpatterns = [
    path('', views.UserPanel.as_view(), name='dashboard-page'),


]
