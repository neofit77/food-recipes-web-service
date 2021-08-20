from django import forms
from .models import Recipe

class CreateRecipeForm(forms.Form):
    """Form that recipe create"""
    title = forms.CharField(max_length=100)
    text = forms.CharField(max_length=1000)
    num_voters = forms.IntegerField()
    average_rating = forms.FloatField()
    ingredients = forms.CharField()