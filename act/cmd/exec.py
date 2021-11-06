import logging

import click

from act import cmd_util
from act import command
from act import config
from act import console
from act import exceptions
from act import logger
from act import topo

LOG = logging.getLogger(__name__)


def execute_commands(cmd, task):
    with console.konsole.status(f"[bold green]Executing {task} commands..."):
        try:
            cmd.run()
            LOG.info(f"Completed {task} commands.")
        except exceptions.ExecCalledProcessError as e:
            logger.sysexit_with_message(f"\n{e.stderr}\n{e}")


@cmd_util.click_command_ex()
@click.argument("phase", nargs=1, required=True)
@click.pass_context
def exec(ctx, phase):
    """Execute the provided phase."""

    command_args = cmd_util.get_command_args(ctx)
    c = config.Config(command_args)

    phases = c.data.keys()
    if phase not in phases:
        joined_phases = ", ".join(phases)
        msg = f"Phase '{phase}' not found. Try one of: '{joined_phases}'."
        logger.sysexit_with_message(msg)

    for group in topo.get_topo_for(phase, c.data):
        for task in group:
            section = c.data.get("command")
            cmd = command.Command(section, config=c)
            execute_commands(cmd, task)
