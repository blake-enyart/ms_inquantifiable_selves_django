from edamam_service.models import Recipe
from rest_framework import serializers

class RecipeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Recipe
        fields = ('id', 'image_url', 'ingredient_count', 'name', 'url')
