from .logger import logger

from .clients import OrderClient, PackageClient

class OrderCanceledHandler:
    async def handle(self, message, *args) -> bool:
        logger.info(f'[OrderCanceledHandler] started processing message - {message}')
        
        # Get all packages
        # If has at least one package
        # Update all packages to canceled 
        # Publish message on SNS topic
        
        return True