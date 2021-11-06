from act import cmd_util


def test_click_group_ex(runner):
    @cmd_util.click_group_ex(name="foo")
    def group():
        pass

    result = runner.invoke(group, "--help", color=True)
    x = [
        "\x1b[33mUsage: \x1b[0mfoo [OPTIONS] COMMAND [ARGS]...",
        "",
        "\x1b[33mOptions\x1b[0m:",
        "  \x1b[32m--help\x1b[0m  Show this message and exit.",
    ]

    assert not result.exception
    assert x == result.output.splitlines()


def test_click_command_ex(runner):
    @cmd_util.click_command_ex(name="foo")
    def cmd():
        pass

    result = runner.invoke(cmd, "--help", color=True)
    x = [
        "\x1b[33mUsage: \x1b[0mfoo [OPTIONS]",
        "",
        "\x1b[33mOptions\x1b[0m:",
        "  \x1b[34m--help\x1b[0m  Show this message and exit.",
    ]

    assert not result.exception
    assert x == result.output.splitlines()


def test_get_command_args(mocker):
    ctx = mocker.Mock(
        obj={
            "args": {
                "debug": True,
                "stream": "stream",
            }
        }
    )

    x = dict(debug=True, stream="stream")
    assert x == cmd_util.get_command_args(ctx)
