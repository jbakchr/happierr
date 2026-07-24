import typer

from happierr.commands.main import run
from happierr.commands.explain import explain


app = typer.Typer(
    no_args_is_help=False,
    help=(
        "Translate technical failures "
        "into understanding."
    ),
)


@app.callback(invoke_without_command=True)
def main(
    ctx: typer.Context,
):
    if ctx.invoked_subcommand is None:
        run()


@app.command("explain")
def explain_command(error_name: str):
    """
    Explain a Python error.
    """
    explain(error_name)


if __name__ == "__main__":
    app()