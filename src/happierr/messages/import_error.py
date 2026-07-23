from happierr.models.response import Response


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