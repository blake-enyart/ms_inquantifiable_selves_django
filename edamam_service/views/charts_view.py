from django.http import JsonResponse
from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.response import Response

from ..services.recipe_service import RecipeService
from edamam_service.models import Recipe, Food
from edamam_service.serializers import RecipeSerializer

class ChartList(generics.CreateAPIView, APIView):
    queryset = Recipe.objects.all()
    serializer_class = RecipeSerializer

    def get(self, request, format=None):
        query = request.query_params['q']
        in_db = Food.objects.filter(name=query)

        if in_db:
            queryset = in_db[0].recipes.all()
            serializer = RecipeSerializer(queryset, many=True)
            return Response(serializer.data)
        else:
            recipe_service = RecipeService(query)
            response = recipe_service.get_recipes()
            recipe_service.save_to_db()

            new_food = Food.objects.filter(name=query)
            queryset = new_food[0].recipes.all()
            serializer = RecipeSerializer(queryset, many=True)
            return Response(serializer.data)

class ChartDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Recipe.objects.all()
    serializer_class = RecipeSerializer
