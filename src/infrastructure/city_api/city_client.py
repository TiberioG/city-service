import json
import requests
from src.infrastructure.city_api import BASE_URL, API_KEY


def call_city_api(name, limit=1):
    url = f'{BASE_URL}city?name={name}&limit={limit}'
    headers = {'X-Api-Key': API_KEY}

    response = requests.get(url, headers=headers)

    if response.status_code != 200:
        raise Exception(f'Request failed with status {response.status_code}')


    return response.json()
