"""
Utility functions for generating standardized IDs.
"""


def generate_id(prefix: str, number: int, width: int = 4) -> str:
    """
    Generate a standardized identifier.

    Example:
        generate_id("STU", 1)
        -> STU0001
    """

    return f"{prefix}{number:0{width}d}"