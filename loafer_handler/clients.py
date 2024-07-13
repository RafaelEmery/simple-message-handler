import json
from requests import get, patch
from boto3 import client
from typing import Any

from .config import settings
from .models import OrderPackages, Package


api_base_url = f'http://localhost:{settings.API_MOCKS_PORT}'
package_canceled_topic_arn = f'arn:aws:sns:us-east-1:000000000000:{settings.PACKAGE_CANCELED_TOPIC_NAME}'


class OrderClient:
    def __init__(self, base_url: str) -> None:
        self.base_url = base_url
        
    def get_order_packages(self, id: str) -> OrderPackages:
        response = get(f'{self.base_url}/orders/{id}/packages')
        response.raise_for_status()
        response_json = response.json()
        
        return OrderPackages(**response_json)
    
class PackageClient:
    def __init__(self, base_url) -> None:
        self.base_url = base_url
        
    def update_package(self, id: str, package: Package) -> None:
        body = package.to_dict()
        body_json = json.dumps(body)
        
        response = patch(f'{self.base_url}/packages/{id}', data=body_json, headers={'Content-Type': 'application/json'})
        response.raise_for_status()


class SNSClient:
    def __init__(self, topic_arn, endpoint_url) -> None:
        self.topic_arn = topic_arn
        self.client = client('sns', endpoint_url)
    
    def publish_message(self, payload: Any):
        self.client.publish(
            TopicArn=self.topic_arn,
            Message=json.dumps(payload)
        )
        pass
    

order_client = OrderClient(api_base_url)
package_client = PackageClient(api_base_url)
package_canceled_topic = SNSClient(package_canceled_topic_arn, settings.LOCALSTACK_ENDPOINT)