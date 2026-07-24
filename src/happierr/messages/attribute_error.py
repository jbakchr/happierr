from happierr.models.error_guide import ErrorGuide


ATTRIBUTE_ERROR = ErrorGuide(
    error_type="AttributeError",
    what_is_it=(
        "Python found the object, but the "
        "requested attribute or method does "
        "not exist on that object."
    ),
    mental_model=(
        "Objects in Python have attributes "
        "and methods.\n\n"
        "When you access something using dot "
        "notation, Python checks whether the "
        "object provides that attribute.\n\n"
        "AttributeError means the object "
        "exists, but the attribute you "
        "requested does not."
    ),
    common_causes=[
        "A method name is misspelled.",
        "An attribute name is misspelled.",
        "The object is a different type than expected.",
        "The attribute exists on a different object type.",
        "A library API has changed.",
    ],
    what_to_try_next=[
        "Check the spelling of the attribute name.",
        "Verify the object's type.",
        "Review the object's documentation.",
        "Use dir() to inspect available attributes.",
        "Inspect where the object was created.",
    ],
    related_concepts=[
        "objects",
        "attributes",
        "methods",
        "classes",
        "dot notation",
    ],
    reminder=(
        "AttributeError means Python found "
        "the object successfully.\n\n"
        "The issue is usually that the "
        "requested attribute or method does "
        "not exist on that type of object.\n\n"
        "This is a common Python error.\n\n"
        "The code failed. Not the developer."
    ),
)
