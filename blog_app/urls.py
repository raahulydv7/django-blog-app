from django.urls import path
from .views import register_user,home,login_user,logout_user,create_post,update_post, delete_post
urlpatterns = [
    path('', home, name='home'),
    path('register/', register_user, name='register'),
    path('login/', login_user, name='login'),
    path('logout/', logout_user, name='logout'),
    path('add-post/', create_post, name='add-post'),
    path('edit-post/<int:pk>/', update_post, name='edit-post'),
    path('delete-post/<int:pk>/', delete_post, name='delete-post'),
]
