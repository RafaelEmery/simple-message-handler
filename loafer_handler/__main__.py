import logging

from loafer.managers import LoaferManager

from .routes import routes


logger = logging.getLogger(__name__)


service = LoaferManager(routes=routes)
logger.info('starting service...')
service.run()