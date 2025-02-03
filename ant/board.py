from .game_object import GameObject
from .ant import Ant
from .tile import Tile
import pygame

class Board(GameObject) :
    """Handle game object."""

    def __init__(self) -> None :
        """Board initialization."""
        super().__init__()
        self._dict_color={}

    @property
    def dictionary(self) -> dict :
        """Return the dictionary of the movement."""
        return self._dict_color

    def color_board(self, ant : Ant, step : int ) -> None :
        """Coloration of the board."""
        if self._dict_color[ant.line][ant.column]==pygame.Color("black") :
            self._dict_color[ant.line][ant.column]==pygame.Color("black")
        else : 
            self._dict_color[ant.line][ant.column]==pygame.Color("white")



#les cles du dictionnaire sont les lignes
#chaque clé contient une liste de cases blanche ou noire
#il faut s'arranger pour que les lignes existent
