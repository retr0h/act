import logging

import click
import rich
import yaml

from act import cmd_util
from act import topo

LOG = logging.getLogger(__name__)
ACT_FILE = "act.yaml"


@cmd_util.click_group_ex()
@click.pass_context
def graph(ctx):
    """Graph sub command."""


@cmd_util.click_command_ex()
@click.option(
    "--filename",
    "stream",
    default=ACT_FILE,
    envvar="ACT_FILE",
    type=click.File("rb"),
    help=f"Path to the act file. [{ACT_FILE}]",
)
@click.argument("node", nargs=1, required=False)
@click.pass_context
def ls(ctx, stream, node):
    """List the graph."""

    ctx.obj["args"]["stream"] = stream
    d = yaml.safe_load(stream)

    if node:
        output = topo.get_topo_for(node, d)
    else:
        output = topo.get_topo(d)

    LOG.info("Task graph:")
    rich.pretty.pprint(output, expand_all=True)


graph.add_command(ls)
