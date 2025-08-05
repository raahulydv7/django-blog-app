from django.db import models
from django.contrib.auth.models import User


class UserProfile(models.Model):
    user  = models.ForeignKey(User, on_delete=models.CASCADE)
    bio = models.TextField(blank=True)
    fname = models.CharField(max_length=50,null=True,blank=True)
    lname = models.CharField(max_length=50,null=True,blank=True)
    mob = models.CharField(max_length=10,null=True,blank=True)
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def get_full_name(self):
        return f"{self.fname or ''} {self.lname or ''}".strip()
    
