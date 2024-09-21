from django.urls import path
from .views import register, profile, home, posts
from django.contrib.auth.views import LoginView, LogoutView

urlpatterns = [
    path('register/', register, name='register'),
    path('login/', LoginView.as_view(template_name='blog/login.html'), name='login'),
    path('logout/', LogoutView.as_view(next_page='login'), name='logout'),
    path('profile/', profile, name='profile'),
    path('posts/', posts, name='posts'),
    path('', home, name='home')
]