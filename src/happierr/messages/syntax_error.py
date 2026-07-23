from happierr.models.response import Response


def build_response(error_text: str) -> Response:
    return Response(
        raw_error=error_text,
        error_type="SyntaxError",
        title=(
            "Python could not understand "
            "how this code is structured."
        ),
        what_happened=(
            "Python encountered code that does not follow "
            "the rules of Python syntax."
        ),
        why_this_happens=(
            "A quote, parenthesis, colon, comma, or other "
            "required piece of syntax may be missing or "
            "placed incorrectly."
        ),
        next_step=(
            "Carefully review the line mentioned in the "
            "error message and look for missing or "
            "unexpected characters."
        ),
    )