from __future__ import annotations

import boto3
import os
from botocore.exceptions import ClientError


def get_secret(secret_name: str) -> str | None:
    """
    :param secret_name: aws key of the secret
    :return:  the secret string value, remember to use a plaintext secret
    in AWS, otherwise this will return a string encoding a json object
    """
    session = boto3.session.Session()
    client = session.client(
        service_name='secretsmanager',
        region_name=os.getenv('AWS_REGION')
    )
    try:
        get_secret_value_response = client.get_secret_value(
            SecretId=secret_name
        )
        print(get_secret_value_response)

        return get_secret_value_response.get('SecretString')
    except ClientError as e:
        return None
