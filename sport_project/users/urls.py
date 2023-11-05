from django.urls import path, include
import django.contrib.auth.urls
from . import views
from .views import Register

urlpatterns = [
    path('', include('django.contrib.auth.urls')),
    path('register/', Register.as_view(), name='register'),


]
