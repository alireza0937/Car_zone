from django.urls import path
from . import views
urlpatterns = [
    path('', views.SiteContactView.as_view(), name='contact-page'),

]