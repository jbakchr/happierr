# patterns/import_error.py

def matches(error_text: str) -> bool:
    return "ImportError" in error_text
