from .logger import logger

from .clients import order_client, package_client, package_canceled_topic
from .models import OrderPackages, Package

class OrderCanceledHandler:
    async def handle(self, message, *args) -> bool:
        logger.info(f'[OrderCanceledHandler] started processing message - {message}')
        
        try:
            packages: OrderPackages = order_client.get_order_packages(message.order_id)
            
            if len(packages.result) < 1:
                logger.info(f'[OrderCanceledHandler] order {message.order_id} has no packages to cancel')
                return True
            
            for package in packages.result:
                canceled_package = self._cancel_package(package.id, package.name)
                package_canceled_topic.publish_message(canceled_package)
            
            logger.info(f'[OrderCanceledHandler] successfully processed message - {message}')
            return True   
        except Exception as e:
            logger.error(f'[OrderCanceledHandler] error processing message - {e}')
            return False
    
    def _cancel_package(self, id: str, name: str) -> Package:
        try:
            package = Package(id=id, name=name, status='canceled')
            package_client.update_package(id, package)
            
            return package
        except Exception as e:
            raise Exception(f'error canceling package {id} - {e}')