from django.urls import path
from . import views


urlpatterns = [
   path('home/', views.RecipesView.as_view(), name='recipes'),

]