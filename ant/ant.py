#First party
from .dir import Dir
from .game_object import GameObject

#Constants

class Ant(GameObject) :
    """The ant."""

    def __init__(self, line : int, column : int, direction : Dir) -> None:
        """Ant initialization."""
        super().__init__()
        self._line=line
        self._column=column
        self._dir=direction

    @property
    def dir(self) -> Dir :
        """Ant direction."""
        return self._dir

    @dir.setter
    def dir(self, direction: Dir) -> None:
        self._dir = direction

    @property
    def line(self) -> int :
        """Return the line where the ant is."""
        return self._line

    @property
    def column(self) -> int :
        """Return the column where the ant is."""
        return self._column

    def move(self, orientation : int) -> None :
        """Movement of the ant."""
        

#si l'orientation est 0 on fait +90 à la direction et si elle est 1 on fait -90





