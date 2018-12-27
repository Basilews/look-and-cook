import requests
import json
from pprint import pprint

with open('src/data.json') as f:
    data = json.load(f)

pprint(data)

url = "https://api.telegram.org/bot<ваш_токен>/"


def get_updates_json(request):
    response = requests.get(request + 'getUpdates')
    return response.json()


def last_update(data):
    results = data['result']
    total_updates = len(results) - 1
    return results[total_updates]