from happierr.models.error_guide import ErrorGuide


TYPE_ERROR = ErrorGuide(
    error_type="TypeError",
    what_is_it=(
        "Python encountered an operation that "
        "cannot be performed with the given "
        "types of objects."
    ),
    mental_model=(
        "In Python, every value has a type.\n\n"
        "Some operations only work with certain "
        "types.\n\n"
        "TypeError usually means the values "
        "exist, but Python does not know how to "
        "perform the requested operation using "
        "those types."
    ),
    common_causes=[
        "Using incompatible types together.",
        "Passing the wrong type to a function.",
        "Providing too many or too few arguments.",
        "Using an object in a way it does not support.",
        "Mixing strings and numbers in calculations.",
    ],
    what_to_try_next=[
        "Check the types of the values involved.",
        "Review the function's expected arguments.",
        "Convert values to compatible types if appropriate.",
        "Inspect the full error message for details.",
        "Use type() to understand what Python received.",
    ],
    related_concepts=[
        "types",
        "functions",
        "arguments",
        "strings",
        "integers",
        "objects",
    ],
    reminder=(
        "TypeError usually means Python "
        "understood what you asked it to do, "
        "but the values involved were not "
        "compatible with that operation.\n\n"
        "This is one of the most common Python "
        "errors developers encounter.\n\n"
        "The code failed. Not the developer."
    ),
)