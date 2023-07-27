from django.urls import path
from . import views

urlpatterns = [
    path('', views.Home.as_view(), name='index-page'),
    path('about-us/', views.about_us, name='aboutUs-page'),
    path('services/', views.services, name='services-page'),
]