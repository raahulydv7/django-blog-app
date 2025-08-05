from django.urls import path
from .views import register_user,home,login_user

urlpatterns = [
    path('', home, name='home'),
    path('register/', register_user, name='register'),
    path('login/', login_user, name='login'),
]
