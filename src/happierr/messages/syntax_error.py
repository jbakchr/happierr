from happierr.models.error_guide import ErrorGuide
from happierr.models.response import Response


SYNTAX_ERROR = ErrorGuide(
    error_type="SyntaxError",
    what_is_it=(
        "Python found code that does not follow "
        "the rules of Python syntax."
    ),
    mental_model=(
        "Before Python runs a program, it reads "
        "and validates the code.\n\n"
        "If Python encounters something it does "
        "not understand, it stops and raises "
        "SyntaxError.\n\n"
        "Think of it like reading a sentence "
        "with missing punctuation or mismatched "
        "parentheses. Python cannot continue "
        "until the structure makes sense."
    ),
    common_causes=[
        "Missing parentheses.",
        "Missing quotation marks.",
        "Missing colons after statements such as if or for.",
        "Unmatched brackets or parentheses.",
        "Incorrect indentation.",
        "Typing mistakes in Python keywords.",
    ],
    what_to_try_next=[
        "Read the line mentioned in the error message.",
        "Check the surrounding lines for missing punctuation.",
        "Look for unmatched parentheses, brackets, or quotes.",
        "Verify indentation is consistent.",
        "Check for spelling mistakes in Python keywords.",
    ],
    related_concepts=[
        "parser",
        "indentation",
        "statements",
        "expressions",
        "parentheses",
        "quotation marks",
    ],
    reminder=(
        "SyntaxError means Python could not "
        "understand the structure of the code.\n\n"
        "It does not mean your logic is wrong.\n"
        "It does not mean you are a bad developer.\n\n"
        "The code failed. Not the developer."
    ),
)

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