from rest_framework import serializers
from .models import Recipe


class RecipeSerializer(serializers.ModelSerializer):
    """Return all recipes (title and average rating)"""
    class Meta:
        model = Recipe
        fields = ['title', 'average_rating']


class RecipeOneSerializer(serializers.ModelSerializer):
    """Serializer for details of an recipe"""
    class Meta:
        model = Recipe
        fields = '__all__'
