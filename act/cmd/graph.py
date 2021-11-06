import logging

import click
import rich

from act import cmd_util
from act import config
from act import topo

LOG = logging.getLogger(__name__)


@cmd_util.click_group_ex()
@click.pass_context
def graph(ctx):
    """Graph sub command."""


@cmd_util.click_command_ex()
@click.argument("phase", nargs=1, required=False)
@click.pass_context
def ls(ctx, phase):
    """List the graph."""

    command_args = cmd_util.get_command_args(ctx)
    c = config.Config(command_args)

    if phase:
        output = topo.get_topo_for(phase, c.data)
    else:
        output = topo.get_topo(c.data)

    LOG.info("Task graph:")
    rich.pretty.pprint(output, expand_all=True)


graph.add_command(ls)
