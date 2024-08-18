from django.urls import path
from .views import list_books
from .views import LibraryDetailView
from django.contrib.auth.views import LoginView
from django.contrib.auth.views import LogoutView
from . import views
from . import admin_view
from . import librarian_view
from . import member_view

urlpatterns = [
  path('books/', list_books, name='list_books'),
  path('library/<int:pk>', LibraryDetailView.as_view(), name='library_list'),
  path('login/', LoginView.as_view(template_name='login.html'), name='login'),
  path('logout/', LogoutView.as_view(template_name='logout.html'), name='logout'),
  path('register/', views.register, name='register'),
  path('admin/', admin_view.admin_view, name='admin_view'),
  path('librarian/', librarian_view.librarian_view, name='librarian_view'),
  path('member/', member_view.member_view, name='member_view')
]