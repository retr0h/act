import subprocess

import pytest

from act import exec


def test_run():
    cmd = ["ls", "-l"]
    x = exec.run(cmd)

    assert 0 == x.returncode


def test_run_returns_exit_code_on_invalid_cmd():
    cmd = ["invalid"]
    x = exec.run(cmd, check=False)

    assert 0 != x.returncode


def test_run_raises_on_invalid_cmd():
    cmd = ["invalid"]

    with pytest.raises(subprocess.CalledProcessError):
        exec.run(cmd)
