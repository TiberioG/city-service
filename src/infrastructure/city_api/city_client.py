import json
import requests
from src.infrastructure.aws.secret_client import get_secret

API_KEY = get_secret('api-ninjas')
BASE_URL = 'https://api.api-ninjas.com/v1/'


def get_city_by_name(name):
    url = f'{BASE_URL}city?name={name}'
    headers = {'X-Api-Key': API_KEY}

    response = requests.get(url, headers=headers)

    print(json.dumps(response.json(), indent=4))

    if response.status_code != 200:
        raise Exception(f'Request failed with status {response.status_code}')

    return response.json()[0]
