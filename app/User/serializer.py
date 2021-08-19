from rest_framework import serializers
from rest_framework_simplejwt.tokens import RefreshToken, TokenError
from .models import User
from django.contrib import auth
from rest_framework.exceptions import AuthenticationFailed

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


class RegisterSelializer(serializers.ModelSerializer):

    def validate(self, attrs):
        password = attrs['password']
        first_name = attrs['first_name']


    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email']