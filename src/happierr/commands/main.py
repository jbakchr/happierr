import sys

from happierr.messages.module_not_found import (
    build_response,
)

from happierr.patterns.module_not_found import (
    matches,
)

from happierr.renderers.console_renderer import (
    render,
)


def run() -> None:

    error_text = sys.stdin.read()

    if matches(error_text):

        response = build_response(
            error_text
        )

        render(response)

        return

    print(error_text)