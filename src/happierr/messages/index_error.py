from happierr.models.error_guide import ErrorGuide


INDEX_ERROR = ErrorGuide(
    error_type="IndexError",
    what_is_it=(
        "Python attempted to access a position "
        "in a sequence that does not exist."
    ),
    mental_model=(
        "Lists, tuples, strings, and other "
        "sequences store items in positions "
        "called indexes.\n\n"
        "Python starts counting at 0.\n\n"
        "If you ask for a position outside the "
        "available range, Python raises "
        "IndexError.\n\n"
        "Think of it like trying to take the "
        "10th book from a shelf that only "
        "contains 3 books."
    ),
    common_causes=[
        "The index is larger than the sequence size.",
        "The sequence is empty.",
        "An off-by-one mistake was made.",
        "Loop logic produced an invalid index.",
        "Data contains fewer items than expected.",
    ],
    what_to_try_next=[
        "Check the length of the sequence.",
        "Print the value of the index being used.",
        "Verify whether the sequence is empty.",
        "Review loop boundaries and range() calls.",
        "Use len() to understand the valid index range.",
    ],
    related_concepts=[
        "lists",
        "tuples",
        "strings",
        "indexes",
        "len()",
        "range()",
    ],
    reminder=(
        "IndexError means Python successfully "
        "found the sequence.\n\n"
        "The problem is that the requested "
        "position does not exist within it.\n\n"
        "This is a common Python error.\n\n"
        "The code failed. Not the developer."
    ),
)