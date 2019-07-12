from .clients import edamam_client
from ..models import Food, Recipe

class RecipeService(object):
    def __init__(self, query):
        self.query = query

    def get_recipes(self):
        return edamam_client.get_json(self.query)['hits']

    def save_to_db(self):
        recipes = self.get_recipes()
        new_food = Food(name=self.query)
        new_food.save()
        for recipe in recipes:
            recipe = recipe['recipe']
            new_food.recipes.create(
                image_url=recipe['image'],
                ingredient_count=len(recipe['ingredients']),
                name = recipe['label'],
                url = recipe['url']
            )
        return None
