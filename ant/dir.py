# Standard
import enum

class Dir(enum.Enum):
    """Direction of movement."""

    UP = (0, -1)
    DOWN = (0, 1)
    LEFT = (-1, 0)
    RIGHT = (1, 0)

    @property
    def x(self) -> int:
        """Column index."""
        return self.value[0]

    @property
    def y(self) -> int:
        """Line index."""
        return self.value[1]

    def texte(self) -> str:
        """Return the text part of the dir object."""
        if self==Dir.UP :
            return "UP"
        if self==Dir.DOWN :
            return "DOWN"
        if self==Dir.LEFT :
            return "LEFT"
        return "RIGHT"

