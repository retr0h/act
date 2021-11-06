import subprocess


class ExecCalledProcessError(subprocess.CalledProcessError):
    """Raise our own version of `subprocess.CalledProcessError`."""
