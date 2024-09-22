from django.shortcuts import render
from rest_framework import generics
from rest_framework import viewsets
from .serializers import UserRegistrationSerializer, UserLoginSerializer, UserProfileSerializer
from django.contrib.auth import authenticate
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth import get_user_model
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication

# Create your views here.
class RegistrationView(generics.CreateAPIView):
    serializer_class = UserRegistrationSerializer

class LoginView(viewsets.ViewSet):
    def create(self, request):
        serializer = UserLoginSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        email = serializer.validated_data['email']
        password = serializer.validated_data['password']
        user = authenticate(email=email, password=password)

        if user:
            token, created = Token.objects.get_or_create(user=user)
            return Response({'token': token.key}, status=status.HTTP_200_OK)
        else:
            return Response({'error': 'Invalid email or password'}, status=status.HTTP_401_UNAUTHORIZED)

class ProfileView(viewsets.ViewSet):
    permission_classes = [IsAuthenticated]  
    authentication_classes = [TokenAuthentication]
    
    def retrieve(self, request, id=None):  
        CustomUser = get_user_model()
        try:
            user = CustomUser.objects.get(pk=id) 
        except CustomUser.DoesNotExist:
            return Response({'error': 'User not found'}, status=status.HTTP_404_NOT_FOUND)
        
        serializer = UserProfileSerializer(user)
        return Response(serializer.data, status=status.HTTP_200_OK)
