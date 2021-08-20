from rest_framework import serializers
from rest_framework_simplejwt.tokens import RefreshToken, TokenError
from .models import User
from django.contrib import auth
from rest_framework.exceptions import AuthenticationFailed
from django.contrib.auth.hashers import make_password

class LoginSerializer(serializers.ModelSerializer):
    password = serializers.CharField()
    username = serializers.CharField()
    access = serializers.CharField()
    refresh = serializers.CharField()

    class Meta:
        model = User
        fields = ['password', 'username', 'access', 'refresh']

    def validate(self, attrs):
        password = attrs.get('password', '')
        username = attrs.get('username','')
        user = auth.authenticate(username=username, password=password)

        if not user:
            raise AuthenticationFailed('Invalid credentials, try again')

        return {
            'password': user.password,
            'username': user.username,
            'access': user.tokens()['access'],
            'refresh': user.tokens()['refresh']
        }


class RegisterSerializer(serializers.ModelSerializer):
    """Registration serializer"""

    class Meta:
        model = User
        fields = ['username', 'password', 'first_name', 'last_name', 'email']

    def validate(self, attrs):
        password = attrs.get('password', '')
        first_name = attrs.get('first_name', '')
        last_name = attrs.get('last_name', '')
        username = attrs.get('username', '')
        email = attrs.get('email', '')

        if not username:
            raise serializers.ValidationError('Username must not be empty')
        if not password:
            raise serializers.ValidationError('Password must not be empty')
        if not first_name:
            raise serializers.ValidationError('First name must not be empty')
        if not last_name:
            raise serializers.ValidationError('Last name must not be empty')

        return {
            'password':make_password(password),
            'first_name': first_name,
            'last_name': last_name,
            'username': username,
            'email': email
        }



