from happierr.models.error_guide import ErrorGuide


VALUE_ERROR = ErrorGuide(
    error_type="ValueError",
    what_is_it=(
        "Python received a value that has the "
        "correct type but an invalid value."
    ),
    mental_model=(
        "Some operations expect values that "
        "follow certain rules.\n\n"
        "Even when the type is correct, a value "
        "may still be unacceptable.\n\n"
        "ValueError usually means Python "
        "understood what kind of data it "
        "received, but could not use the "
        "specific value that was provided."
    ),
    common_causes=[
        "Converting text that does not represent a number.",
        "Providing an invalid option or argument.",
        "Passing a value outside an allowed range.",
        "Supplying data in an unexpected format.",
        "Using a value that violates a function's requirements.",
    ],
    what_to_try_next=[
        "Read the full error message carefully.",
        "Inspect the value being passed to the operation.",
        "Verify the expected format or range.",
        "Print the value before the error occurs.",
        "Review the function documentation.",
    ],
    related_concepts=[
        "types",
        "values",
        "functions",
        "arguments",
        "data validation",
    ],
    reminder=(
        "ValueError usually means the type was "
        "acceptable, but the specific value was "
        "not.\n\n"
        "This is different from TypeError, "
        "which happens when Python receives the "
        "wrong type of object.\n\n"
        "This is a common Python error.\n\n"
        "The code failed. Not the developer."
    ),
)