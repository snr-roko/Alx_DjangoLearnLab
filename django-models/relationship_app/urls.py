from django.urls import path
from .views import list_books
from .views import LibraryDetailView
from .views import user_login
from .views import user_logout
from .views import user_register

urlpatterns = [
  path('books/', list_books, name='list_books'),
  path('library/<int:pk>', LibraryDetailView.as_view(), name='library_list'),
  path('login/', user_login, name='login'),
    path('logout/', user_logout, name='logout'),
    path('register/', user_register, name='register')
]