from django.urls import path
from . import views

urlpatterns = [
    path('register', views.RegisterView.as_view(), name='registration-page'),
    path('register/<activation_code>', views.active_account, name='active-user'),
    path('login', views.LoginView.as_view(), name='login-page'),
    path('logout', views.logout_button, name='logout-link'),
    path('user_panel', views.logout_button, name='user_panel-page'),
    path('forget-password', views.ForgetPassWordView.as_view(), name='forget-password-page'),
    path('activate/<uidb64>/<token>', views.activate, name='activate')



]
