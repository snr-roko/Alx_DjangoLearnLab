from django.urls import path
from .views import LoginView, RegistrationView, ProfileView

urlpatterns = [
    path('login/', LoginView.as_view({'post': 'create'}), name='login'),
    path('register/', RegistrationView.as_view(), name='register'),
    path('profile/<int:id>', ProfileView.as_view({'get': 'retrieve'}), name='profile')
]