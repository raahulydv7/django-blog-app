from django.urls import path
from .views import (
    register_user, login_user, logout_user,
    home, user_profile, update_user_profile, follow, unfollow, search_users, create_post, update_post, delete_post
)

urlpatterns = [
    path('', home, name='home'),

    # 🔐 Authentication
    path('register/', register_user, name='register'),
    path('login/', login_user, name='login'),
    path('logout/', logout_user, name='logout'),

    # 👤 Profile
    path('profile/<int:pk>/', user_profile, name='user-profile'),
    path('update-profile/<int:pk>/', update_user_profile, name='update-user-profile'),

    # 👤 follow, unfollow
    path('follow/<int:pk>/', follow, name='follow-user'),
    path('unfollow/<int:pk>/', unfollow, name='unfollow-user'),

    # 👤 search
    path('search-users/', search_users, name='search-users'),

    # 📝 Post management
    path('add-post/', create_post, name='add-post'),
    path('edit-post/<int:post_id>/', update_post, name='edit-post'),
    path('delete-post/<int:post_id>/', delete_post, name='delete-post'),
]
