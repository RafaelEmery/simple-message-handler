from boto3 import client
from json import dumps
from uuid import uuid4

sns_client = client(
    'sns',
    endpoint_url='http://localhost:4566'
)
topic_arn = 'arn:aws:sns:us-east-1:000000000000:order_canceled'
payload = {
    'order_id': str(uuid4()),
    'status': 'canceled',
    'reason': 'shit happens :D'
}

response = sns_client.publish(
    TopicArn=topic_arn,
    Message=dumps(payload)
)

print(f'message published at {topic_arn} - {dumps(payload)}')