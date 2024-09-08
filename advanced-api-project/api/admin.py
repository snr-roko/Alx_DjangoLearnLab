# admin.py

from django.contrib import admin
from .models import Author, Book

# Registering the models with the Django admin.
admin.site.register(Author)
admin.site.register(Book)
