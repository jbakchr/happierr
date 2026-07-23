import typer

from happierr.commands.main import run

app = typer.Typer(
    no_args_is_help=False,
    help=(
        "Translate technical failures "
        "into human encouragement."
    ),
)


@app.callback(invoke_without_command=True)
def main():
    run()


if __name__ == "__main__":
    app()
