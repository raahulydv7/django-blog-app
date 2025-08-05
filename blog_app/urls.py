from django.urls import path
from .views import register_user,home

urlpatterns = [
    path('register/', register_user, name='register'),
]
