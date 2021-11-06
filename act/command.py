import logging
import os

from act import exec

LOG = logging.getLogger(__name__)


class Command:
    """The class responsible for executing command sections.

    section:
      env:
        FOO: bar
      cmd: |
        set -e
        /some/command
    """

    def __init__(self, section, config):
        self._section = section
        self._config = config

        self._cmd = section.get("cmd")
        self._cwd = section.get("cwd", os.getcwd())

    @property
    def cmd(self):
        return self._cmd

    @cmd.setter
    def cmd(self, value):
        self._cmd = value

    @property
    def env(self):
        default_env = self._config.env
        env = self._section.get("env", {})

        for k, v in env.items():
            expanded = os.path.expandvars(v)
            default_env[k] = os.path.expanduser(expanded)

        return default_env

    def run(self):
        if self.cmd:
            exec.run(
                self.cmd,
                env=self.env,
                cwd=self._cwd,
                quiet=(not self._config.debug),
                echo=self._config.debug,
            )
