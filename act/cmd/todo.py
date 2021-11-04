import click

from act import cmd_util


@cmd_util.click_command_ex()
@click.pass_context
def todo(ctx):
    """TODO."""

    ctx_args = ctx.obj.get("args")
    args = {"debug": ctx_args["debug"]}
    command_args = {}

    click.echo(args)
    click.echo(command_args)
