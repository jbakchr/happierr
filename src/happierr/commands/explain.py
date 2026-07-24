import typer

from happierr.messages.guides import ERROR_GUIDES
from happierr.renderers.console_renderer import render_error_guide


def explain(error_name: str):
    guide = ERROR_GUIDES.get(error_name)

    if guide is None:
        typer.echo(
            f"Unknown error type: {error_name}"
        )
        raise typer.Exit(code=1)

    render_error_guide(guide)