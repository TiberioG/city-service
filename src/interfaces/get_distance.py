import json

from src.application.distance_service import haversine_two_cities_km


def handler(event, context):
    try:
        body = json.loads(event['body'])

        res = haversine_two_cities_km(body.get('city1'), body.get('city2'))
        return_body = {
            'distance': res,
            'unit': 'kilometers' #todo make this configurable
        }

        return {
            'statusCode': 200,
            'body':
                json.dumps(return_body)
        }
    # todo add more specific exceptions
    except Exception as e:
        print(e)
        return {
            'statusCode': 500,
            'body': json.dumps(e)
        }

