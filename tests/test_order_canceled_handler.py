import pytest
from unittest.mock import MagicMock

from loafer_handler.handler import OrderCanceledHandler
from loafer_handler.models import Package


@pytest.mark.asyncio
async def test_handle_with_packages(
    fake_order_packages,
    fake_order_id,
    order_packages_mock,
    package_client_mock,
    package_canceled_topic_mock,
):
    order_packages_mock.return_value = MagicMock(result=fake_order_packages)
    package_client_mock.return_value = None
    package_canceled_topic_mock.return_value = None

    message = MagicMock(order_id=fake_order_id)
    handler = OrderCanceledHandler()
    result = await handler.handle(message)

    assert result is True
    order_packages_mock.assert_called_once_with(fake_order_id)
    assert package_client_mock.call_count == len(fake_order_packages)
    assert package_canceled_topic_mock.call_count == len(fake_order_packages)


@pytest.mark.asyncio
async def test_handle_with_no_packages(
    fake_order_id, order_packages_mock, package_client_mock, package_canceled_topic_mock
):
    order_packages_mock.return_value = MagicMock(result=[])
    package_client_mock.return_value = None
    package_canceled_topic_mock.return_value = None

    message = MagicMock(order_id=fake_order_id)
    handler = OrderCanceledHandler()
    result = await handler.handle(message)

    assert result is True
    order_packages_mock.assert_called_once_with(fake_order_id)
    assert package_client_mock.call_count == 0
    assert package_canceled_topic_mock.call_count == 0


@pytest.mark.asyncio
async def test_handle_with_error_on_order_endpoint(
    fake_order_id, order_packages_mock, package_client_mock, package_canceled_topic_mock
):
    order_packages_mock.side_effect = Exception("test exception on order endpoint")

    message = MagicMock(order_id=fake_order_id)
    handler = OrderCanceledHandler()
    result = await handler.handle(message)

    assert result is False
    order_packages_mock.assert_called_once_with(fake_order_id)
    assert package_client_mock.call_count == 0
    assert package_canceled_topic_mock.call_count == 0


@pytest.mark.asyncio
async def test_handle_with_error_on_update_packages_endpoint(
    fake_order_packages,
    fake_order_id,
    order_packages_mock,
    package_client_mock,
    package_canceled_topic_mock,
):
    order_packages_mock.return_value = MagicMock(result=fake_order_packages)
    package_client_mock.side_effect = Exception(
        "test endpoint on update package endpoint"
    )

    message = MagicMock(order_id=fake_order_id)
    handler = OrderCanceledHandler()
    result = await handler.handle(message)

    canceled_first_package = Package(
        id=fake_order_packages[0].id,
        name=fake_order_packages[0].name,
        status="canceled",
    )

    assert result is False
    order_packages_mock.assert_called_once_with(fake_order_id)
    package_client_mock.assert_called_once_with(
        fake_order_packages[0].id, canceled_first_package
    )
    assert package_canceled_topic_mock.call_count == 0


@pytest.mark.asyncio
async def test_handle_with_error_on_sns_topic(
    fake_order_packages,
    fake_order_id,
    order_packages_mock,
    package_client_mock,
    package_canceled_topic_mock,
):
    order_packages_mock.return_value = MagicMock(result=fake_order_packages)
    package_client_mock.return_value = None
    package_canceled_topic_mock.side_effect = Exception("test endpoint on sns topic")

    message = MagicMock(order_id=fake_order_id)
    handler = OrderCanceledHandler()
    result = await handler.handle(message)

    assert result is False
    order_packages_mock.assert_called_once_with(fake_order_id)
    assert package_client_mock.call_count == 1
    assert package_canceled_topic_mock.call_count == 1
