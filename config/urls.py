from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('home.urls')),
    path('cars/', include("cars.urls")),
    path('user/', include("user.urls")),
    path('accounts/', include("allauth.urls")),
    path('dashboard/', include("user_panel.urls")),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
