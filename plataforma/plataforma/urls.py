from django.contrib import admin
from django.urls import path, include
from eventos import views
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('eventos.urls')),
    path('', include('django.contrib.auth.urls')),
]