import sys

from happierr.messages.module_not_found import (
    build_response as build_module_not_found_response,
)

from happierr.messages.import_error import (
    build as build_import_error_response,
)

from happierr.patterns.module_not_found import (
    matches as matches_module_not_found,
)

from happierr.patterns.import_error import (
    matches as matches_import_error,
)

from happierr.messages.syntax_error import (
    build_response as build_syntax_error_response,
)

from happierr.patterns.syntax_error import (
    matches as matches_syntax_error,
)

from happierr.messages.file_not_found import (
    build_response as build_file_not_found_response,
)

from happierr.patterns.file_not_found import (
    matches as matches_file_not_found,
)

from happierr.renderers.console_renderer import (
    render,
)


def run() -> None:

    error_text = sys.stdin.read()

    if matches_module_not_found(error_text):

        response = build_module_not_found_response(
            error_text
        )

        render(response)

        return

    if matches_import_error(error_text):

        response = build_import_error_response(
            error_text
        )

        render(response)

        return

    if matches_syntax_error(error_text):

        response = build_syntax_error_response(
            error_text
        )

        render(response)

        return

    if matches_file_not_found(error_text):

        response = build_file_not_found_response(
            error_text
        )

        render(response)

        return


    print(error_text)