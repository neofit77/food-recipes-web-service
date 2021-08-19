from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.renderers import TemplateHTMLRenderer
from rest_framework.response import Response
from rest_framework import status


class RecipesView(APIView):
    """Listview template for all recipes"""
    template_name = 'Recipe/recipes.html'
    renderer_classes = [TemplateHTMLRenderer]

    def get(self, request):
        print(request.COOKIES)
        return Response(status=status.HTTP_200_OK)


