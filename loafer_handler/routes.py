from loafer.ext.aws.routes import SNSQueueRoute

from .config import settings
from .handler import OrderCanceledHandler

options = {"endpoint_url": settings.LOCALSTACK_ENDPOINT}

routes = (
    SNSQueueRoute(
        provider_queue=settings.CANCELED_ORDERS_QUEUE_NAME,
        provider_options=options,
        handler=OrderCanceledHandler(),
    ),
)
