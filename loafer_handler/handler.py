import logging


logger = logging.getLogger(__name__)

class OrderCanceledHandler:
    async def handle(self, message, *args) -> bool:
        logging.info(f'[OrderCanceledHandler] started processing message - {message}')
        
        return True