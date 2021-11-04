import logging
import sys

import enrich.logging

from act import console

LOG = logging.getLogger(__name__)


def configure():
    """Configure the root logger.

    All other loggers will inherit the configuration we set here.
    """

    # Keep using root logger because we do want to process messages from other
    # libraries.
    logger = logging.getLogger()
    handler = enrich.logging.RichHandler(
        console=console.konsole, show_time=False, show_path=False, markup=True
    )
    logger.addHandler(handler)
    logger.propagate = False
    logger.setLevel(logging.INFO)


def get_logger(name):
    """Return a child logger.

    Returned logger inherits configuration from the lpollo ogger.
    """

    return logging.getLogger("act." + name)


def sysexit(code=1):
    """Perform a system exit with given code, default 1."""

    sys.exit(code)


def sysexit_with_message(msg, code=1):
    """Exit with an error message."""

    LOG.critical(msg)
    sysexit(code)
