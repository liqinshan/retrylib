# -*- coding:utf-8 -*-

from functools import wraps
import logging

__author__ = "lqs"

# logging.basicConfig(format='%(asctime)s %(levelname)s %(message)s', level=logging.DEBUG)
# default_logger = logging.getLogger(__name__)


def retry(max_retries=1, exceptions=(Exception,), logger=None):
    def outer(func):
        @wraps(func)
        def inner(*args, **kwargs):
            for x in range(1, max_retries+1):
                try:
                    return func(*args, **kwargs)
                except exceptions as e:
                    if logger is None:
                        logging.error(str(e))
                    else:
                        logger.error(str(e))
                    continue
        return inner
    return outer
