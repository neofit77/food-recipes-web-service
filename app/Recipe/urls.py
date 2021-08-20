from django.urls import path
from . import views


urlpatterns = [
   path('home/', views.RecipesView.as_view(), name='recipes'),
   path('create/', views.CreateRecipe.as_view(), name='create'),
   path('detail/<id>/', views.RecipeDetails.as_view()),
   path('rating/<id>/<grades>/', views.RecipeRating.as_view()),
   path('own_recipes/', views.RecipesOwnView.as_view())

]