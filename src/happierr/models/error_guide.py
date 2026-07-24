from dataclasses import dataclass


@dataclass(frozen=True)
class ErrorGuide:
    error_type: str
    what_is_it: str
    mental_model: str
    common_causes: list[str]
    what_to_try_next: list[str]
    related_concepts: list[str]
    reminder: str