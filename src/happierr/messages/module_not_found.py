import re

from happierr.models.response import Response


def build_response(error_text: str) -> Response:
    module_name = "unknown"

    match = re.search(
        r"No module named '(.+?)'",
        error_text,
    )

    if match:
        module_name = match.group(1)

    return Response(
        raw_error=error_text,
        error_type="ModuleNotFoundError",
        title="🙂 Good news",
        what_happened=(
            "Python attempted to import a "
            "module that could not be found.\n\n"
            f'The module "{module_name}" is '
            "not installed."
        ),
        why_this_happens=(
            "This is one of the most common "
            "Python errors developers "
            "encounter."
        ),
        next_step=(
            f"pip install {module_name}"
        ),
    )