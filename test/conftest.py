import subprocess

import click
import click.testing
import pytest


@pytest.fixture
def runner():
    return click.testing.CliRunner()


@pytest.fixture
def patched_logger_critical(mocker):
    return mocker.patch("logging.Logger.critical")


@pytest.fixture
def stream():
    return """
        a:
          cmd: {}
          needs:
            - b
        b:
          cmd: {}
          needs:
            - c
        c:
          cmd: {}
          needs:
            - d
        command:
          env:
            foo: bar
          cmd: cmd
"""


@pytest.fixture
def command_args(stream):
    return {
        "debug": False,
        "stream": stream,
    }


@pytest.fixture
def patched_run(mocker):
    m = mocker.patch("act.exec.run")
    m.return_value = subprocess.CompletedProcess(
        args="foo",
        returncode=0,
        stdout="out",
        stderr="",
    )

    return m
