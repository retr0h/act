import subprocess_tee

from act import exceptions


def run(
    cmd, env=None, debug=False, echo=False, quiet=True, check=True, cwd=None
):
    """Execute the given command and returns subprocess.CompletedProcess.

    :param cmd: :
      - a string or list of strings (similar to subprocess.run)
    :param debug: An optional bool to toggle debug output.
    :raises: subprocess.CalledProcessError
    :returns: subprocess.CompletedProcess
    """
    stdout = None
    stderr = None

    result = subprocess_tee.run(
        cmd,
        env=env,
        stdout=stdout,
        stderr=stderr,
        echo=echo or debug,
        quiet=quiet,
        cwd=cwd,
    )

    if result.returncode != 0 and check:
        raise exceptions.ExecCalledProcessError(
            returncode=result.returncode,
            cmd=result.args,
            output=result.stdout,
            stderr=result.stderr,
        )

    return result
