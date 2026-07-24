import typer

from happierr.messages.guides import ERROR_GUIDES
from happierr.renderers.console_renderer import (
    render_error_guide,
)


def explain(error_name: str) -> None:
    if error_name.lower() == "list":
        guides = "\n".join(
            f"• {name}"
            for name in sorted(ERROR_GUIDES)
        )

        typer.echo(
            f"""
Available Error Guides

{guides}

Example

happierr explain ModuleNotFoundError
"""
        )

        return

    guide = ERROR_GUIDES.get(error_name)

    if guide is None:
        typer.echo(
            f"Unknown error type: {error_name}\n"
        )

        typer.echo(
            "Run:\n"
            "  happierr explain list\n"
            "to see available error guides."
        )

        raise typer.Exit(code=1)

    render_error_guide(guide)