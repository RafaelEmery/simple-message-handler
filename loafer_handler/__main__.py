import argparse

from loafer.managers import LoaferManager

from .routes import routes
from .logger import logger
from .handler import OrderCanceledHandler


parser = argparse.ArgumentParser(description='manual run')
parser.add_argument('--flag', type=str, help='define the manual running')
args = parser.parse_args()

if args.flag == 'manual':
    from uuid import uuid4
    import asyncio
    
    loop = asyncio.get_event_loop()

    logger.info('starting manual service...')
    handler = OrderCanceledHandler()
    message = {
        'order_id': str(uuid4()),
        'status': 'canceled',
        'reason': 'shit happens :D'
    }
    loop.run_until_complete(handler.handle(message))

    loop.close()
else: 
    service = LoaferManager(routes=routes)
    logger.info('starting service...')
    # FIXME: error on LoaferManager run - type object '_asyncio.Task' has no attribute 'all_tasks'
    service.run()
