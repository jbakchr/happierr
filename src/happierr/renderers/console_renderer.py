from rich.console import Console
from rich.panel import Panel

from happierr.models.response import Response

console = Console()


def render(response: Response) -> None:

    console.print()

    console.print(
        Panel(
            response.raw_error.strip(),
            title="[bold red]Original Error[/bold red]",
            border_style="red",
        )
    )

    console.print()

    body = f"""
[bold green]{response.title}[/bold green]

[bold]Error Type[/bold]

{response.error_type}

[bold]What Happened[/bold]

→ {response.what_happened}

[bold]Why This Happens[/bold]

→ {response.why_this_happens}

[bold]What To Try Next[/bold]

→ {response.next_step}
"""

    console.print(
        Panel(
            body,
            title="[bold green]happierr[/bold green]",
            border_style="green",
        )
    )

    console.print()