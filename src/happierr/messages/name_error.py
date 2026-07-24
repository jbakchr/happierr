from happierr.models.error_guide import ErrorGuide


NAME_ERROR = ErrorGuide(
    error_type="NameError",
    what_is_it=(
        "Python encountered a name that it "
        "does not recognize."
    ),
    mental_model=(
        "When Python sees a variable, function, "
        "or object name, it tries to find a "
        "matching definition.\n\n"
        "If Python cannot find that name, it "
        "raises NameError.\n\n"
        "Think of it like looking up a contact "
        "in your phone. If the contact does not "
        "exist, there is nothing to call."
    ),
    common_causes=[
        "A variable was never created.",
        "A variable name is misspelled.",
        "A function name is misspelled.",
        "A name is used before it is defined.",
        "Code is referring to a name that is outside the current scope.",
    ],
    what_to_try_next=[
        "Check the spelling of the name.",
        "Verify the name was defined before being used.",
        "Review variable and function declarations.",
        "Check indentation and scope.",
        "Read the full error message to see which name Python could not find.",
    ],
    related_concepts=[
        "variables",
        "functions",
        "scope",
        "assignment",
        "namespaces",
    ],
    reminder=(
        "NameError means Python does not know "
        "what the requested name refers to.\n\n"
        "This often happens because something "
        "was misspelled or has not been defined "
        "yet.\n\n"
        "This is a common Python error.\n\n"
        "The code failed. Not the developer."
    ),
)