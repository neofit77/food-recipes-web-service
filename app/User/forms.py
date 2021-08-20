from django import forms
from .models import User


class RegistrationForm(forms.Form):
    """Registration form"""
    username = forms.CharField(max_length=40, required=True)
    first_name = forms.CharField(max_length=40, required=True)
    last_name = forms.CharField(max_length=40, required=True)
    email = forms.EmailField(required=False)
    password = forms.CharField(max_length=50, required=True)
    password2 = forms.CharField(max_length=40, required=True,label='Repeat password')

    class Meta:
        model = User
        fields = ['username', 'email', 'first_name', 'last_name', 'password1', 'password2']

