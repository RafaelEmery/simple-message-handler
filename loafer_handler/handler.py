from .logger import logger


class OrderCanceledHandler:
    async def handle(self, message, *args) -> bool:
        logger.info(f'[OrderCanceledHandler] started processing message - {message}')
        
        return True