# Edamam client module

import requests
import json
from django.conf import settings

def get_json(query):
    url = f"https://api.edamam.com/search?app_id={settings.APP_ID}&app_key={settings.API_KEY}&q={query}"
    response = requests.get(url)
    return json.loads(response.text)
