import json
import requests
from src.infrastructure.city_api import BASE_URL, API_KEY


def get_city_by_name(name):
    url = f'{BASE_URL}city?name={name}'
    headers = {'X-Api-Key': API_KEY}

    response = requests.get(url, headers=headers)

    print(json.dumps(response.json(), indent=4))

    if response.status_code != 200:
        raise Exception(f'Request failed with status {response.status_code}')

    return response.json()[0]
