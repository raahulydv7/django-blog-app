from django.db import models
from django.contrib.auth.models import User


class UserProfile(models.Model):
    user  = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(blank=True)
    fname = models.CharField(max_length=50,null=True,blank=True)
    lname = models.CharField(max_length=50,null=True,blank=True)
    mob = models.CharField(max_length=10,null=True,blank=True)
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    followers = models.ManyToManyField(
    'self', symmetrical=False, related_name='following', blank=True
    )

    def __str__(self):
        return self.user.username

    def get_full_name(self):
        return f"{self.fname or ''} {self.lname or ''}".strip()

    def follower_count(self):
        return self.followers.count()  

    def following_count(self):
        return self.user.following.count()
    
class Posts(models.Model):
    user  = models.ForeignKey(User, on_delete=models.CASCADE)
    description = models.TextField(blank=True)
    image = models.ImageField(upload_to='post_images/', blank=True, null=True)
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.user.username