import json

from src.application.city_service import get_city_by_name


def handler(event, context):

    city_name = event.get('queryStringParameters').get('name')

    city = get_city_by_name(city_name)
    return {
        'statusCode': 200,
        'body': json.dumps(city)
    }
