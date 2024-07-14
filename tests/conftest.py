import pytest
from uuid import uuid4
from unittest.mock import patch

from loafer_handler.models import Package


@pytest.fixture
def order_packages_mock():
    with patch('loafer_handler.handler.order_client.get_order_packages') as mock:
        yield mock

@pytest.fixture
def package_client_mock():
    with patch('loafer_handler.handler.package_client.update_package') as mock:
        yield mock

@pytest.fixture
def package_canceled_topic_mock():
    with patch('loafer_handler.handler.package_canceled_topic.publish_message') as mock:
        yield mock

@pytest.fixture
def fake_order_packages():
    return [Package(id=str(uuid4()), name='first package', status='pending'), Package(id=str(uuid4()), name='second package', status='pending')]

@pytest.fixture
def fake_order_id():
    return str(uuid4())