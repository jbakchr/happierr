from happierr.models.response import Response
from happierr.models.error_guide import ErrorGuide


FILE_NOT_FOUND = ErrorGuide(
    error_type="FileNotFoundError",
    what_is_it=(
        "Python attempted to access a file "
        "or directory that it could not find."
    ),
    mental_model=(
        "When Python opens a file, it follows "
        "the path that was provided.\n\n"
        "If the file cannot be found at that "
        "location, Python raises "
        "FileNotFoundError.\n\n"
        "Think of it like following directions "
        "to a house. If the house is not at the "
        "expected address, you cannot continue."
    ),
    common_causes=[
        "The file does not exist.",
        "The file name is misspelled.",
        "The file path is incorrect.",
        "The program is running from a different directory than expected.",
        "The file was moved or deleted.",
    ],
    what_to_try_next=[
        "Verify that the file exists.",
        "Check the spelling of the file name.",
        "Review the file path.",
        "Check the current working directory.",
        "Use an absolute path to confirm the correct location.",
    ],
    related_concepts=[
        "files",
        "directories",
        "paths",
        "current working directory",
        "relative paths",
        "absolute paths",
    ],
    reminder=(
        "FileNotFoundError means Python could "
        "not find a file at the specified "
        "location.\n\n"
        "The file may be missing, moved, or "
        "referenced with the wrong path.\n\n"
        "This is a common error.\n"
        "The code failed. Not the developer."
    ),
)

def build_response(error_text: str) -> Response:
    return Response(
        raw_error=error_text,
        error_type="FileNotFoundError",
        title=(
            "Python was asked to open a file that it could not find."
        ),
        what_happened=(
            "Your code attempted to open or access a file, "
            "but Python could not locate it."
        ),
        why_this_happens=(
            "The file may not exist, the filename may be "
            "misspelled, or the path may point to the "
            "wrong location."
        ),
        next_step=(
            "Verify that the file exists and double-check "
            "the filename and path being used."
        ),
    )