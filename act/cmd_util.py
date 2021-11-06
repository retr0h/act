import logging

import click
import click_help_colors

from act import console
from act import exceptions
from act import logger

LOG = logging.getLogger(__name__)


def click_group_ex(**kwargs):
    """Return colorized version of click.group()."""

    return click.group(
        cls=click_help_colors.HelpColorsGroup,
        help_headers_color="yellow",
        help_options_color="green",
        **kwargs,
    )


def click_command_ex(**kwargs):
    """Return extended version of click.command()."""

    return click.command(
        cls=click_help_colors.HelpColorsCommand,
        help_headers_color="yellow",
        help_options_color="blue",
        **kwargs,
    )


def get_command_args(ctx):
    args = ctx.obj.get("args")
    args.update(
        {
            "debug": args["debug"],
            "stream": args["stream"],
        }
    )

    return args


def execute_commands(cmd, task):
    with console.konsole.status(f"[bold green]Executing {task} commands..."):
        try:
            cmd.run()
            LOG.info(f"Completed {task} commands.")
        except exceptions.ExecCalledProcessError as e:
            logger.sysexit_with_message(f"\n{e.stderr}\n{e}")
