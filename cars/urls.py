from django.urls import path
from . import views
urlpatterns = [
    path('', views.CarsListView.as_view(), name='cars-list-page'),
    path('<slug:slug>/', views.CarsDetailView.as_view(), name='cars-detail-page'),
    path('search', views.SearchCars.as_view(), name='search-car-page'),
]