import logging

import enrich
import enrich.console
import rich.console
import rich.syntax

LOG = logging.getLogger(__name__)
THEME = rich.theme.Theme(
    {
        "info": "dim cyan",
        "warning": "magenta",
        "danger": "bold red",
        "scenario": "green",
        "action": "green",
        "section_title": "bold cyan",
        "logging.level.notset": rich.style.Style(dim=True),
        "logging.level.debug": rich.style.Style(color="white", dim=True),
        "logging.level.info": rich.style.Style(color="blue"),
        "logging.level.warning": rich.style.Style(color="red"),
        "logging.level.error": rich.style.Style(color="red", bold=True),
        "logging.level.critical": rich.style.Style(color="red", bold=True),
        "logging.level.success": rich.style.Style(color="green", bold=True),
    }
)


konsole = enrich.console.Console(theme=THEME, record=True, redirect=True)
