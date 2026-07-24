import typer

from happierr.commands.errors import errors
from happierr.commands.explain import explain
from happierr.commands.main import run

app = typer.Typer()


@app.callback(invoke_without_command=True)
def main(
    ctx: typer.Context,
):
    if ctx.invoked_subcommand is None:
        run()


@app.command("explain")
def explain_command(
    error_name: str,
):
    explain(error_name)


@app.command("errors")
def errors_command():
    errors()


if __name__ == "__main__":
    app()