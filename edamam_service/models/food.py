from django.db import models

class Food(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    name = models.CharField(max_length=100, blank=False)
    # Has many recipes

    class Meta:
        ordering = ('created',)

    def __str__(self):
        return self.name
