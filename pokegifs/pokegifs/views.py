import requests
import json
from django.http import JsonResponse


def pokemon_view(request, id):
    api_url = "http://pokeapi.co/api/v2/pokemon/{}/".format(id)
    res = requests.get(api_url)
    body = json.loads(res.content)
    name = body["name"]
    types = []
    for type in body['types']:
        types.append(type["type"]["name"])

    return JsonResponse({
        "name": name,
        "id": id,
        "types": types,
    })
