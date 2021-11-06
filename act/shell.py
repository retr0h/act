import click
import click_completion

import act
from act import cmd
from act import cmd_util
from act import logger

ACT_FILE = "act.yaml"

click_completion.init()
logger.configure()


@cmd_util.click_group_ex()
@click.option(
    "--debug/--no-debug",
    default=False,
    help="Enable or disable debug mode. Default is disabled.",
)
@click.version_option(version=act.__version__)
@click.option(
    "--filename",
    "stream",
    default=ACT_FILE,
    envvar="ACT_FILE",
    type=click.File("rb"),
    help=f"Path to the act file. [{ACT_FILE}]",
)
@click.pass_context
def main(ctx, debug, stream):  # pragma: no cover
    """
    \b
               _
     ___  ___ | |_
    | .'||  _||  _|
    |__,||___||_|

    act - A simple task runner.

    """  # noqa: H404,H405
    ctx.obj = {}
    ctx.obj["args"] = {}
    ctx.obj["args"]["debug"] = debug
    ctx.obj["args"]["stream"] = stream


main.add_command(cmd.graph.graph)
main.add_command(cmd.exec.exec)
