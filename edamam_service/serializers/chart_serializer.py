from edamam_service.models import Chart
from rest_framework import serializers

class ChartSerializer(serializers.ModelSerializer):
    class Meta:
        model = Chart
        fields = ('id', 'image_url', 'ingredient_count', 'name', 'url')
