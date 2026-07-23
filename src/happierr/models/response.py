from dataclasses import dataclass


@dataclass
class Response:
    raw_error: str
    error_type: str
    title: str
    what_happened: str
    why_this_happens: str
    next_step: str