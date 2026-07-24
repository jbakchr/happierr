from happierr.models.response import Response
from happierr.models.error_guide import ErrorGuide


IMPORT_ERROR = ErrorGuide(
    error_type="ImportError",
    what_is_it=(
        "Python found the requested module, "
        "but could not import the requested "
        "name from it."
    ),
    mental_model=(
        "Importing has two steps.\n\n"
        "First, Python finds the module.\n"
        "Second, Python imports the requested "
        "name.\n\n"
        "ImportError usually means the first "
        "step succeeded but the second step "
        "failed."
    ),
    common_causes=[
        "The requested name does not exist.",
        "The name is misspelled.",
        "The module API has changed.",
        "The import statement is incorrect.",
        "A circular import exists.",
    ],
    what_to_try_next=[
        "Check the spelling of the imported name.",
        "Review the module documentation.",
        "Verify that the name actually exists.",
        "Check for recent library changes.",
        "Look for circular imports.",
    ],
    related_concepts=[
        "imports",
        "modules",
        "packages",
        "namespaces",
        "circular imports",
    ],
    reminder=(
        "Python successfully found the module. "
        "The issue is usually with what is being "
        "imported from it.\n\n"
        "This is a common error.\n"
        "The code failed. Not the developer."
    ),
)

def build(error_text: str) -> Response:
    return Response(
        raw_error=error_text,
        error_type="ImportError",
        title="Python found the module, but the requested name was not available.",
        what_happened=(
            "Python successfully located the module you were importing "
            "from, but the specific name you requested could not be imported."
        ),
        why_this_happens=(
            "The requested name may not exist in the module. "
            "It may be misspelled, or the module may have changed "
            "and no longer exposes that name."
        ),
        next_step=(
            "Check the spelling of the imported name and review "
            "the module documentation to see what can be imported."
        ),
    )