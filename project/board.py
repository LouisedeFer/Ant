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

    def __init__(self, dictionary : dict[int, list[Tile]]) -> None :
        """Board initialization."""
        self._dictionary=dictionary

    @property
    def dictionary(self) -> dict[int, list[Tile]] :
        """Return the dictionary of the tiles."""
        return self._dictionary

    @dictionary.setter
    def dictionary(self, dictionary : dict[int, list[Tile]]) -> None :
        self._dictionary=dictionary

    def __contains__(self, other: object) -> bool:
        """Check if an integer is a key of the dictionary."""
        if not isinstance(other, int):
            return False
        return other in self.dictionary


    def change_color(self, row : int , column : int) -> None :
        """Change the color of the tile when the ant moves."""
        if self.dictionary[row][column].text == "X" :
            self.dictionary[row][column].text= " "
            self.dictionary[row][column].color= pygame.Color("white")
        else :
            self.dictionary[row][column].text="X"
            self.dictionary[row][column].color=pygame.Color("black")

    def add_tile(self, row : int, column : int) -> None :
        """Add a tile and adapt the dictionary."""
        if 0<= row < len(self.dictionary) :
            #just add a column
            if column ==len(self.dictionary[row]) :
                for key in self.dictionary:
                    self.dictionary[key].append(Tile(" ",WHITE ))
                    #change the indexation properly and add the columns to the dict
            else :
                #make sure the first column is always 0
                for key in self.dictionary :
                    self.dictionary[key].insert(0, Tile(" ",WHITE))
        elif row < 0 :
            #make sure the first row is always 0
            length_dic, length_list=len(self.dictionary),len(self.dictionary[0])
            for key in range(length_dic,0, -1):
                self.dictionary[key] = self.dictionary[key-1]
            self.dictionary[0]=[Tile(" ",WHITE) for i in range(length_list)]
            # add a line with white tiles
        else :
            length_list=len(self.dictionary[0])
            self.dictionary[row] = [Tile(" ",WHITE) for i in range(length_list)]




