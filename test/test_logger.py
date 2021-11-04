import logging

import pytest

from act import logger


def test_configure():
    assert logger.LOG.parent.level == 30

    logger.configure()

    assert logger.LOG.parent.level == 20
    assert not logger.LOG.parent.propagate


def test_get_logger():
    result = logger.get_logger(__name__)

    assert isinstance(result, logging.Logger)


def test_sysexit():
    with pytest.raises(SystemExit) as e:
        logger.sysexit()

    assert 1 == e.value.code


def test_sysexit_with_custom_code():
    with pytest.raises(SystemExit) as e:
        logger.sysexit(2)

    assert 2 == e.value.code


def test_sysexit_with_message(patched_logger_critical):
    with pytest.raises(SystemExit) as e:
        logger.sysexit_with_message("foo")

    assert 1 == e.value.code

    patched_logger_critical.assert_called_once_with("foo")


def test_sysexit_with_message_and_custom_code(patched_logger_critical):
    with pytest.raises(SystemExit) as e:
        logger.sysexit_with_message("foo", 2)

    assert 2 == e.value.code

    patched_logger_critical.assert_called_once_with("foo")
