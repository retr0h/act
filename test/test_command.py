import os

import magicattr
import pytest

from act import command
from act import config


@pytest.fixture
def _config_instance(command_args):
    return config.Config(command_args)


@pytest.fixture
def _instance(_config_instance):
    section = _config_instance.data.get("command")

    return command.Command(section, config=_config_instance)


@pytest.mark.parametrize(
    "attr, x",
    [
        ("cmd", "cmd"),
        ("env['foo']", "bar"),
    ],
)
def test_properties(_instance, attr, x):
    assert x == magicattr.get(_instance, attr)


def test_run(_instance, patched_run):
    _instance.run()

    patched_run.assert_called_with(
        "cmd", env={"foo": "bar"}, cwd=os.getcwd(), quiet=True, echo=False
    )


def test_run_does_not_run_when_no_command(_instance, patched_run):
    _instance.cmd = None

    assert not patched_run.called
