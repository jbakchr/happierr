import re

from happierr.models.response import Response
from happierr.models.error_guide import ErrorGuide


MODULE_NOT_FOUND = ErrorGuide(
    error_type="ModuleNotFoundError",
    what_is_it=(
        "Python could not find the requested "
        "module or package."
    ),
    mental_model=(
        "When Python encounters an import "
        "statement, it searches known locations "
        "for the requested module."
    ),
    common_causes=[
        "The package is not installed.",
        "The package name is misspelled.",
        "The wrong virtual environment is active.",
    ],
    what_to_try_next=[
        "Check the package name.",
        "Verify the package is installed.",
        "Verify the active virtual environment.",
    ],
    related_concepts=[
        "imports",
        "modules",
        "packages",
        "pip",
        "virtual environments",
    ],
    reminder=(
        "This is a common Python error. "
        "The code failed. Not the developer."
    ),
)


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