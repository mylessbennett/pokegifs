import json
import requests
import os

key = os.environ.get("GIPHY_KEY")

res = requests.get("http://pokeapi.co/api/v2/pokemon/pikachu/")
body = json.loads(res.content)
print(body["name"])


url = "http://api.giphy.com/v1/gifs/feqkVgjJpYtjy?api_key={}&q=pikachu".format(key)

res = requests.get(url)
body = json.loads(res.content)
print(body['data']['url'])
