import logging

import click

from act import cmd_util
from act import command
from act import config
from act import topo

LOG = logging.getLogger(__name__)


@cmd_util.click_command_ex()
@click.argument("phase", nargs=1, required=True)
@click.pass_context
def exec(ctx, phase):
    """Execute the provided phase."""

    command_args = cmd_util.get_command_args(ctx)
    c = config.Config(command_args)
    phase = topo.get_topo_for(phase, c.data)

    for group in phase:
        for task in group:
            section = c.data.get("command")
            cmd = command.Command(section, config=c)
            cmd_util.execute_commands(cmd, task)
