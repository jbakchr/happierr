from happierr.models.response import Response


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