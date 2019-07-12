from django.http import JsonResponse
from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.response import Response

from ..services.recipe_service import RecipeService
from edamam_service.models import Chart
from edamam_service.serializers import ChartSerializer

class ChartList(generics.CreateAPIView, APIView):
    queryset = Chart.objects.all()
    serializer_class = ChartSerializer

    def get(self, request, format=None):
        query = request.query_params['q']
        in_db = Chart.objects.filter(name=query)

        if in_db:
            queryset = in_db
            serializer = ChartSerializer(queryset, many=True)
            return Response(serializer.data)
        else:
            recipe_service = RecipeService(query)
            response = recipe_service.get_recipes()
            return JsonResponse(response, safe=False)

class ChartDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Chart.objects.all()
    serializer_class = ChartSerializer
