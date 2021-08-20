from django.db import models
from Ingredient.models import Ingredient
from User.models import User

class Recipe(models.Model):
    """Recipe model"""
    title = models.CharField(max_length=100)
    text = models.TextField()
    num_voters = models.IntegerField(default=0)
    average_rating = models.FloatField(default=0)
    author = models.ForeignKey(User, on_delete=models.SET_NULL, related_name='recipes', null=True)
    ingredients = models.ManyToManyField(Ingredient)

    def __str__(self):
        return self.title