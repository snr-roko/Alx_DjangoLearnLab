from django.urls import path
from .views import BookList
from rest_framework.routers import DefaultRouter
from django.urls import include
from .views import BookViewSet
router = DefaultRouter()

router.register(r'books', BookViewSet)

urlpatterns = [
  path('', include(router.urls)),
  path('api/books/', BookList.as_view(), name='BookList')
]