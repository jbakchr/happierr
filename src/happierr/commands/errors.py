import typer

from happierr.messages.guides import ERROR_GUIDES


def errors() -> None:
    guides = "\n".join(
        f"• {name}"
        for name in sorted(ERROR_GUIDES)
    )

    typer.echo(
        f"""
Available Error Guides

{guides}

Example

happierr explain TypeError
""".strip()
    )