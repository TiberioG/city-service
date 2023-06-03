import json

from src.application.distance_service import haversine_between_two_cities


def handler(event, context):

    print(event)

    res = haversine_between_two_cities(event.get('city1'), event.get('city2'))
    return {
        'statusCode': 200,
        'body': json.dumps(res)
    }
