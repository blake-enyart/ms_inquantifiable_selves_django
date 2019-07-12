from django.db import models
from .food import Food

class Recipe(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    image_url = models.TextField(blank=False)
    ingredient_count = models.PositiveIntegerField(blank=False)
    name = models.CharField(max_length=200, blank=False)
    url = models.TextField(blank=False, db_index=True)
    foods = models.ManyToManyField(Food, related_name='recipes')

    class Meta:
        ordering = ('created',)

    def __str__(self):
        sb = []
        for key in self.__dict__:
            value = self.__dict__[key]
            sb.append(f"{key}={value}")

        return ', '.join(sb)
