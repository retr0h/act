import functools

import yaml


class Config:
    def __init__(self, command_args):
        self._command_args = command_args

        self._stream = self._command_args["stream"]

    @property
    def debug(self):
        return self._command_args["debug"]

    @property
    def env(self):
        return {}

    @property
    @functools.lru_cache()
    def data(self):
        return self._get_config()

    def _get_config(self):
        return yaml.safe_load(self._stream)

    def __str__(self):  # pragma: no cover
        return str(self.__class__) + ": " + str(self.__dict__)
