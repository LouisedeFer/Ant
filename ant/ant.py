#First party

# Third party
import importlib.resources

import pygame  # type: ignore
import math
import logging

from .board import Board
from .dir import Dir
from .tile import Tile

logger = logging.getLogger("foo")

#Constants
MIN_COL=11
MIN_ROW=11

class Ant :
    """The ant."""

    def __init__(self, row : int, column : int, direction : Dir) -> None:
        """Ant initialization."""
        self._row=row
        self._column=column
        self._dir=direction
        self._font= None | pygame.font.Font
        self._coordinates=(-MIN_COL//2, -MIN_ROW//2)

    @property
    def dir(self) -> Dir :
        """Ant direction."""
        return self._dir

    @dir.setter
    def dir(self, direction: Dir) -> None:
        """Change the direction of the ant."""
        self._dir = direction

    @property
    def row(self) -> int :
        """Return the line where the ant is."""
        return self._row

    @row.setter
    def row(self, row : int) -> None :
        """Change the row of the ant."""
        self._row=row

    @property
    def column(self) -> int :
        """Return the column where the ant is."""
        return self._column

    @column.setter
    def column(self, column: int) -> None :
        """Change the column of the ant."""
        self._column=column

    @property
    def coordonates(self) -> tuple[int, int] :
        """Left Up Coordonates of the board printed."""
        return self._coordinates


    def turn_right(self) -> None :
        """Turn right."""
        if self.dir==Dir.UP :
            self.dir=Dir.RIGHT
        elif self.dir == Dir.RIGHT :
            self.dir=Dir.DOWN
        elif self.dir==Dir.DOWN :
            self.dir=Dir.LEFT
        else :
            self.dir=Dir.UP

    def turn_left(self) -> None :
        """Turn left."""
        if self.dir==Dir.UP :
            self.dir=Dir.LEFT
        elif self.dir == Dir.LEFT :
            self.dir=Dir.DOWN
        elif self.dir==Dir.DOWN :
            self.dir=Dir.RIGHT
        else :
            self.dir=Dir.UP

    def change_direction(self, dictionnaire_tiles : dict[tuple[int, int], Tile]) -> None :
        """Change the direction of the ant, the color of the tile known."""
        row,col=self.row, self.column
        current_color=dictionnaire_tiles[(row, col)].text
        if current_color== " " :
            self.turn_right()
        else :
            self.turn_left()


    def move_and_change_color(self, board : Board) -> None :
        """Movement of the ant and changement of the colors of the tiles."""
        self.change_direction(board.dictionary)
        board.change_color(self.row, self.column)#change the color of the tile where the ant is
        self.column +=self.dir.x
        self.row+=self.dir.y
        #test if the new tile exists (the contains operator has been redifined, test if a tuple of integer is a key):
        if (self.row, self.column) not in board.dictionary :
            board.add_tile(self.row, self.column)
        (min_r, min_c), (max_r, max_c) = board.top_corner, board.bottom_corner
        if self.row < min_r or self.row > max_r or self.column < min_c or self.column > max_c: # the ant goes out of the window
            #Update the board
            board.top_corner = (self.row - MIN_ROW//2, self.column - MIN_COL//2)
            board.bottom_corner = (self.row + MIN_ROW//2, self.column + MIN_COL//2)
            board.update_global_coordinates()


    def draw_ant(self, screen : pygame.Surface, size : int, min_r : int, min_c : int) -> None:
        """Draw the ant on screen."""
        ant=pygame.image.load("ant.png")
        ant=pygame.transform.scale(ant,(size-2, size-2) )
        ant_pivoted=pygame.transform.rotate(ant,self.dir.angle())
        screen.blit(ant_pivoted, ((self._column-min_c)*size, (self._row-min_r)*size))









