from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Recipe
from .serializer import RecipeSerializer,RecipeOneSerializer
from rest_framework_simplejwt.backends import TokenBackend
from User.models import User

class RecipesView(APIView):
    """Get all recipes"""

    def get(self, request):
        recipes = Recipe.objects.all()
        serializer = RecipeSerializer(data=recipes, many=True)
        serializer.is_valid()
        return Response({'recipes': serializer.data})


class RecipeDetails(APIView):
    """View for one recipe"""
    def get(self, request, id):
        recipe = Recipe.objects.get(pk=id)
        serializer = RecipeOneSerializer(recipe)
        return Response({'recipes': serializer.data})


class CreateRecipe(APIView):
    """Create recipe"""
    def post(self, request):
        print(request.data)
        recipe = RecipeOneSerializer(data=request.data)
        if recipe.is_valid(raise_exception=True):
            recipe.save()
        return Response({'recipes': recipe})


class RecipeRating(APIView):
    """Recipe rating"""
    def get(self, request, id, grades):

        recipe = Recipe.objects.get(id=id)

        # detected curent user trought token
        token = request.META.get('HTTP_AUTHORIZATION', " ").split(' ')[1]
        valid_data = TokenBackend(algorithm='HS256').decode(token, verify=False)
        user_id = valid_data['user_id']

        if str(recipe.author.id) == str(user_id):
            raise ValueError('You can rating only others recipes')

        try:
            rating=int(grades)
            if rating > 5 or rating < 1:
                raise ValueError('Your rating is not valid')

            sum_rating = int(recipe.num_voters) * float(recipe.average_rating)
            num_voters = recipe.num_voters + 1
            new_average = sum_rating/num_voters

        except:
            raise TypeError('Number of voters or average rating are wrong type')

        recipe.num_voters = num_voters
        recipe.average_rating = new_average
        recipe.save()
        serializer = RecipeOneSerializer(recipe)

        return Response({'recipes': serializer.data})


class RecipesOwnView(APIView):
    """Get all recipes"""

    def get(self, request):

        # detected curent user trought token
        token = request.META.get('HTTP_AUTHORIZATION', " ").split(' ')[1]
        valid_data = TokenBackend(algorithm='HS256').decode(token, verify=False)
        user_id = valid_data['user_id']

        user = User.objects.get(id=user_id)
        recipes = Recipe.objects.filter(author = user)
        serializer = RecipeSerializer(data=recipes, many=True)
        serializer.is_valid()
        return Response({'recipes': serializer.data})


