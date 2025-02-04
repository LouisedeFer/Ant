from __future__ import annotations

import pygame

from .tile import Tile

# Constants

WHITE = pygame.Color("white")
BLACK = pygame.Color("black")


class Board :
    """The board."""

    """The board has a dictionary of list of tiles, the keys are the lines and the position
     in the list of one tile is its column.
      Every tile has a text and a color. """

    def __init__(self, dictionary : dict[tuple[int,int], Tile]) -> None :
        """Board initialization."""
        self._dictionary=dictionary

    @property
    def dictionary(self) -> dict[tuple[int,int], Tile] :
        """Return the dictionary of the tiles."""
        return self._dictionary

    @dictionary.setter
    def dictionary(self, dictionary : dict[tuple[int,int] , Tile]) -> None :
        self._dictionary=dictionary

    def __contains__(self, coord: object) -> bool:
        """Check if an integer is a key of the dictionary."""
        #if not isinstance(coord, tuple[int,int]):
            #return False
        return coord in self.dictionary


    def change_color(self, row : int , column : int) -> None :
        """Change the color of the tile when the ant moves."""
        if self.dictionary[(row, column)].text == "X" :
            self.dictionary[(row, column)].text= " "
            self.dictionary[(row, column) ].color= pygame.Color("white")
        else :
            self.dictionary[(row, column)].text="X"
            self.dictionary[(row, column)].color=pygame.Color("black")

    def add_tile(self, row : int, column : int) -> None :
        """Add a tile and adapt the dictionary."""
        self.dictionary[(row, column)]=Tile(" ", WHITE)

    def draw(self, screen : pygame.Surface, size : int) -> None :
        for coord, tile in self.dictionary.items() :
            tile.draw(screen, size, coord[0], coord[1])




