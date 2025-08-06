from django.contrib import admin
from .models import UserProfile,Posts

@admin.register(UserProfile)
class UserProfileAdmin(admin.ModelAdmin):
    list_display = ['id', 'user', 'created_at']
    search_fields = ['id', 'user__username']
    list_filter = ['created_at']
    ordering = ['-created_at']

@admin.register(Posts)
class PostsAdmin(admin.ModelAdmin):
    list_display = ['id', 'user', 'description', 'created_at']
    search_fields = ['id', 'user__username', 'description']
    list_filter = ['created_at']
    ordering = ['-created_at']
    
