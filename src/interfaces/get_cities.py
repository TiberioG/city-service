import json

from src.application.city_service import get_cities


def handler(event, context):

    city_name = event.get('queryStringParameters').get('name')

    city = get_cities(city_name)
    return {
        'statusCode': 200,
        'body': json.dumps(city)
    }
