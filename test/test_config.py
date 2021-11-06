import magicattr
import pytest

from act import config


@pytest.fixture
def _instance(command_args):
    return config.Config(command_args)


@pytest.mark.parametrize(
    "attr, x",
    [
        ("debug", False),
        ("env", {}),
    ],
)
def test_config(fs, _instance, attr, x):
    assert x == magicattr.get(_instance, attr)
