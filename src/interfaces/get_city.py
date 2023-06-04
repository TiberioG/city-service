import json

import boto3
from botocore.exceptions import ClientError

from src.application.city_service import get_city_by_name


def handler(event, context):
    print(event)

    city_name = event.get('queryStringParameters').get('city_name')

    city = get_city_by_name(city_name)
    return {
        'statusCode': 200,
        'body': json.dumps(city)
    }
