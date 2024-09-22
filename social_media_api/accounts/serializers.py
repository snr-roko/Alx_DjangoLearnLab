from rest_framework import serializers
from django.contrib.auth import get_user_model
from django.contrib.auth.hashers import make_password

CustomUser = get_user_model()

class UserRegistrationSerializer(serializers.ModelSerializer):
    password1 = serializers.CharField(write_only=True)
    password2 = serializers.CharField(write_only=True)
    class Meta:
        model = CustomUser
        fields = ['first_name', 'last_name', 'email', 'username', 'profile_picture', 'bio', 'password1', 'password2']

    def validate(self, data):
        if data['password1'] != data['password2']:
            return serializers.ValidationError('Passwords do not match')
        return data
    def create(self, validated_data):
        validated_data.pop('password2')
        validated_data['password'] = make_password(validated_data.pop('password1'))
        return super().create(validated_data)
        
class UserLoginSerializer(serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.CharField(write_only=True)

class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ['profile_picture', 'email', 'first_name', 'last_name', 'username']