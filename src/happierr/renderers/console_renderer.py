from rich.console import Console
from rich.panel import Panel

from happierr.models.response import Response
from happierr.models.error_guide import ErrorGuide
from happierr.messages.guides import ERROR_GUIDES

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


def render_error_guide(
    guide: ErrorGuide,
) -> None:
    common_causes = "\n".join(
        f"• {cause}"
        for cause in guide.common_causes
    )

    what_to_try_next = "\n".join(
        f"• {step}"
        for step in guide.what_to_try_next
    )

    related_concepts = "\n".join(
        f"• {concept}"
        for concept in guide.related_concepts
    )

    content = f"""
[bold green]{guide.error_type}[/bold green]

What Is It
──────────
{guide.what_is_it}


Mental Model
────────────
{guide.mental_model}


Common Causes
─────────────
{common_causes}


What To Try Next
────────────────
{what_to_try_next}


Related Concepts
────────────────
{related_concepts}


Remember
────────
{guide.reminder}
"""

    console.print()
    console.print(
        Panel(
            content,
            title="[bold green]happierr explain[/bold green]",
            expand=True,
            border_style="green",
        )
    )
    console.print()


def render_error_library() -> None:
    console.print()

    content = f"""
[bold green]Available Error Guides[/bold green]

[italic green]happierr[/italic green] currently includes [bold]{len(ERROR_GUIDES)}[/bold] explanations and learning guides for the following Python errors.


Import Errors
─────────────

• ModuleNotFoundError
• ImportError


Language Errors
───────────────

• SyntaxError
• NameError


Type & Value Errors
───────────────────

• TypeError
• ValueError


Object & Collection Errors
──────────────────────────

• AttributeError
• KeyError
• IndexError


File Errors
───────────

• FileNotFoundError


Try
───

happierr explain TypeError


Remember
────────

Understanding reduces panic.

[italic]The code failed. Not the developer.[/italic]
"""
    
    console.print(
        Panel(
            content,
            title="[bold green]happierr[/bold green]",
            expand=True,
            border_style="green",
        )
    )

    console.print()