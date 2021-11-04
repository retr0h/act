import click
import click_completion

import act
from act import cmd
from act import cmd_util
from act import logger

click_completion.init()
logger.configure()


@cmd_util.click_group_ex()
@click.option(
    "--debug/--no-debug",
    default=False,
    help="Enable or disable debug mode. Default is disabled.",
)
@click.version_option(version=act.__version__)
@click.pass_context
def main(ctx, debug):  # pragma: no cover
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


main.add_command(cmd.graph.graph)
