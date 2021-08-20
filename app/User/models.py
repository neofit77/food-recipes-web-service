from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.db import models
from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth.hashers import make_password

class UserManager(BaseUserManager):
    """Overide default methods for django User model"""

    def create_user(self, username, email, password=None):
        """Overide create_user method"""
        if username is None:
            raise TypeError('Users should have a username')

        user = self.model(username=username, email=self.normalize_email(email))

        user.set_password(make_password(password))
        user.save()
        return user

    def create_superuser(self, username, email, password):
        """Overide method that create superuser"""
        if password is None:
            raise TypeError('Password should not be none')

        user = self.create_user(username, email, password)
        user.is_superuser = True
        user.is_staff = True
        user.save()
        return user


class User(AbstractBaseUser, PermissionsMixin):
    """Overide built django class User"""
    username = models.CharField(max_length=40, unique=True)
    email = models.EmailField(max_length=40, unique=True)
    first_name = models.CharField(max_length=40)
    last_name = models.CharField(max_length=40)
    company_name = models.CharField(max_length=100, default='')
    company_domain = models.CharField(max_length=50, default='')
    city = models.CharField(max_length=60, default='')
    is_staff = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField(auto_now=True)


    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email']

    objects = UserManager()

    def __str__(self):
        return self.username

    def tokens(self):
        refresh = RefreshToken.for_user(self)
        return {
            'refresh': str(refresh),
            'access': str(refresh.access_token)
        }


