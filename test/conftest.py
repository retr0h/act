import click
import click.testing
import pytest


@pytest.fixture
def runner():
    return click.testing.CliRunner()


@pytest.fixture
def patched_logger_critical(mocker):
    return mocker.patch("logging.Logger.critical")
