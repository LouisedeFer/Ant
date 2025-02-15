from __future__ import annotations  # noqa: D100

import logging
from typing import TYPE_CHECKING

import pygame  # type: ignore

from .tile import Tile

if TYPE_CHECKING:
    from .ant import Ant

# Constants

WHITE = pygame.Color("white")
RED = pygame.Color("red")

MIN_COL=11
MIN_ROW=11

logger = logging.getLogger("foo")


class Board :
    """The board."""

    """The board has a dictionary of list of tiles, the keys are the lines and the position
     in the list of one tile is its column.
      Every tile has a text and a color. """

    def __init__(self, dictionary : dict[tuple[int,int], Tile]) -> None :
        """Board initialization."""
        self._dictionary=dictionary
        self._global_coordinates=(-MIN_ROW//2, -MIN_COL//2), (MIN_ROW//2, MIN_COL//2)
        self._top_corner = (-MIN_ROW//2, -MIN_COL//2)
        self._bottom_corner = (MIN_ROW//2, MIN_COL//2)

    @property
    def dictionary(self) -> dict[tuple[int,int], Tile] :
        """Return the dictionary of the tiles."""
        return self._dictionary

    @dictionary.setter
    def dictionary(self, dictionary : dict[tuple[int,int] , Tile]) -> None :
        self._dictionary=dictionary

    @property
    def global_coordinates(self) -> tuple[tuple[int, int], tuple[int, int]] :
        """The global coordinates."""
        return self._global_coordinates

    def update_global_coordinates(self)-> None:
        """Update the global coordinates."""
        (min_r, min_c), (max_r, max_c) = (self.top_corner, self.bottom_corner)
        (mr, mc), (Mr, Mc) = self.global_coordinates
        self._global_coordinates = (min(mr, min_r), min(mc, min_c)), (max(max_r, Mr), max(Mc, max_c))
        logger.info("Update the global coordinates")

    @property
    def top_corner(self) -> tuple[int, int] :
        """Coordinates of the top corner."""
        return self._top_corner

    @top_corner.setter
    def top_corner(self, corner : tuple[int, int]) -> None :
        self._top_corner = corner

    @property
    def bottom_corner(self) -> tuple[int, int] :
        """Coordinates of the bottom corner."""
        return self._bottom_corner

    @bottom_corner.setter
    def bottom_corner(self, corner : tuple[int, int]) -> None :
        self._bottom_corner = corner

    def __contains__(self, coord: tuple[int,int]) -> bool:
        """Check if an integer is a key of the dictionary."""
        return coord in self.dictionary


    def change_color(self, row : int , column : int) -> None :
        """Change the color of the tile when the ant moves."""
        if self.dictionary[(row, column)].text == "X" :
            self.dictionary[(row, column)].text= " "
            self.dictionary[(row, column) ].color= pygame.Color("white")
        else :
            self.dictionary[(row, column)].text="X"
            self.dictionary[(row, column)].color=pygame.Color("red")

    def add_tile(self, row : int, column : int) -> None :
        """Add a tile and adapt the dictionary."""
        self.dictionary[(row, column)]=Tile(" ", WHITE)

    def draw(self, screen : pygame.Surface, size : int, min_r : int, max_r : int, min_c : int, max_c : int) -> None :
        """Draw the board."""
        #first draw the white tiles
        white_tile=Tile(text = " ", color = WHITE)
        for r in range(max_r-min_r+1) :
            for c in range(max_c-min_c+1) :
                white_tile.draw(screen, size, r,c )

        #draw the tiles of the dictionary
        for coord, tile in self.dictionary.items() :
            tile.draw(screen, size, coord[0]-min_r, coord[1]-min_c)

        #draw the red lines
        for r in range(max_r-min_r+1) :
            pygame.draw.line(screen, RED, (0,r*size), ((max_c-min_c+1)*size,r*size))
        for c in range(max_c-min_c+1) :
            pygame.draw.line(screen, RED, (c*size,0), (c*size, (max_r-min_r+1)*size))






