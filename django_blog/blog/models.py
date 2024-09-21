from django.db import models
from django.conf import settings
from django.contrib.auth.models import User
from django.contrib.auth.models import AbstractUser

# Create your models here.
class CustomUser(AbstractUser):
    bio = models.TextField(blank=True)    
    profile_picture = models.ImageField(upload_to='profile_pics/', null=True, blank=True)   

class Post(models.Model):
    title = models.CharField(max_length=200)
    published_date = models.DateTimeField(auto_now_add=True)
    content = models.TextField()
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    def __str__(self):
        return self.title
    
 
