from src.infrastructure.aws.secret_client import get_secret

API_KEY = get_secret('api-ninjas')
BASE_URL = 'https://api.api-ninjas.com/v1/'

