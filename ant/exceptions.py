class AntError(Exception):  # noqa: D100
    """Exception super-class for all Ant errors."""

    def __init__(self, msg: str) -> None:
        """Object initialization."""
        super().__init__(msg)

class IntRangeError(AntError):
    """Exception for integer range error."""

    def __init__(self, label: str, value: int, low: int, high: int) -> None:
        """Object initialization."""
        super().__init__(f"{label} value must be between {low} and {high}."
                         f" {value} is not allowed.")
