from .clients import edamam_client

class RecipeService(object):
    def __init__(self, query):
        self.query = query

    @cached_property
    def get_recipes(self):
        return edamam_client.get_json(self.query)['hits']

    
