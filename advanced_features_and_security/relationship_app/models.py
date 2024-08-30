from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.models import BaseUserManager

# Create your models here.
class Author(models.Model):
  name = models.CharField(max_length=255)

  def __str__(self):
    return self.name

class Book(models.Model):
  title = models.CharField(max_length=255)
  author = models.ForeignKey(Author, on_delete=models.CASCADE, related_name='books')

  def __str__(self):
    return self.name
  
  class Meta:
        permissions = [
            ("can_add_book", "Can add book"),
            ("can_change_book", "Can change book"),
            ("can_delete_book", "Can delete book"),
        ]

class Library(models.Model):
  name = models.CharField(max_length=255)
  books = models.ManyToManyField(Book, related_name='libraries')

  def __str__(self):
    return self.name

class Librarian(models.Model):
  name = models.CharField(max_length=255)
  library = models.OneToOneField(Library, on_delete=models.CASCADE, related_name='librarian')

  def __str__(self):
    return self.name
  
class CustomUser(AbstractUser):
   date_of_birth = models.DateField(null=True, blank=True)
   profile_photo = models.ImageField(upload_to='./profile_photos', null=True, blank=True)

  
class UserProfile(models.Model):
    ROLE_CHOICES = [
        ('Admin', 'Admin'),
        ('Librarian', 'Librarian'),
        ('Member', 'Member'),
    ]

    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)  # Change to CustomUser
    role = models.CharField(max_length=10, choices=ROLE_CHOICES)

    def __str__(self):
        return f"{self.user.username} - {self.role}"


@receiver(post_save, sender=CustomUser)  # Change to CustomUser
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        UserProfile.objects.create(user=instance)

@receiver(post_save, sender=CustomUser)  # Change to CustomUser
def save_user_profile(sender, instance, **kwargs):
    instance.userprofile.save()



class CustomUserManager(BaseUserManager):
  def create_user(self, username, date_of_birth=None, profile_photo=None, password=None):
        user = self.model(username=username, date_of_birth=date_of_birth, profile_photo=profile_photo)
        user.set_password(password)
        user.save(using=self._db)
        return user

  def create_superuser(self, username, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')

        return self.create_user(username, email, password=password, **extra_fields)
      

