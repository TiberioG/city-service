import json

import boto3
from botocore.exceptions import ClientError

from src.infrastructure.city_api.city_client import get_city_by_name


def handler(event, context):

    a = get_city_by_name('Berlin')

    return {
        'statusCode': 200,
        'body': json.dumps(a)
    }
