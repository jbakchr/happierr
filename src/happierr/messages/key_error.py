from happierr.models.error_guide import ErrorGuide


KEY_ERROR = ErrorGuide(
    error_type="KeyError",
    what_is_it=(
        "Python attempted to access a dictionary "
        "key that does not exist."
    ),
    mental_model=(
        "Dictionaries store values using keys.\n\n"
        "When Python sees:\n\n"
        "data['name']\n\n"
        "it looks for a key named 'name'.\n\n"
        "If that key is not present in the "
        "dictionary, Python raises KeyError."
    ),
    common_causes=[
        "The key does not exist.",
        "The key name is misspelled.",
        "The expected data is missing.",
        "The dictionary structure is different than expected.",
        "Data from an external source contains different keys.",
    ],
    what_to_try_next=[
        "Check whether the key exists.",
        "Verify the spelling of the key.",
        "Print the dictionary contents.",
        "Use dict.keys() to inspect available keys.",
        "Consider using dict.get() when a key may be missing.",
    ],
    related_concepts=[
        "dictionaries",
        "keys",
        "values",
        "dict.get()",
        "data structures",
    ],
    reminder=(
        "KeyError means Python successfully "
        "found the dictionary.\n\n"
        "The problem is that the requested "
        "key was not present inside it.\n\n"
        "This is a common Python error.\n\n"
        "The code failed. Not the developer."
    ),
)