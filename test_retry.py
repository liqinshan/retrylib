from __future__ import print_function

import logging
import pytest
from retry_deco import retry

logging.basicConfig(format="%(asctime)s %(levelname)s %(message)s", level=logging.DEBUG)
logger = logging.getLogger(__name__)


@retry(max_retries=3, exceptions=(OSError, IOError), logger=logger)
def test_normal():
    print("test output")


@retry(max_retries=3, exceptions=(OSError, IOError), logger=logger)
def test_os_err():
    raise OSError("OSError")


@retry(max_retries=3, exceptions=(OSError, IOError), logger=logger)
def test_attr_err():
    with pytest.raises(AttributeError):
        raise AttributeError("AttributeError")
