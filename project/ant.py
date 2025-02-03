#First party

# Third party
import importlib.resources

import pygame  # type: ignore

from .board import Board
from .dir import Dir
from .tile import Tile

#Constants

class Ant :
    """The ant."""

    def __init__(self, row : int, column : int, direction : Dir) -> None:
        """Ant initialization."""
        self._row=row
        self._column=column
        self._dir=direction
        self._font= None | pygame.font.Font

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

    def change_direction(self, dictionnaire_tiles : dict[int, list[Tile]]) -> None :
        """Change the direction of the ant, the color of the tile known."""
        row,col=self.row, self.column
        current_color=dictionnaire_tiles[row][col].text
        if current_color== " " :
            self.turn_right()
        else :
            self.turn_left()


    def move_and_change_color(self, board : Board) -> None :
        """Movement of the ant and changement of the colors of the tiles."""
        self.change_direction(board.dictionary)
        board.change_color(self.row, self.column)#change the color of the tile the ant is
        self.column +=self.dir.x
        self.row+=self.dir.y
        #test if the new tile exists (the contains operator has been redifined, test if an integer is a key):
        if self.row in board.dictionary and 0 <= self.column < len(board.dictionary[self.row]) :
            #if yes, simply change the color
            board.change_color(self.row, self.column)
        else :
            #if no, create a new tile and adapt the dictionary
            board.add_tile(self.row, self.column)
            board.change_color(self.row, self.column)

    def draw_ant(self, screen: pygame.Surface, size: int) -> None:
        """Draw the ant on screen."""
        if self._font is None :
            with importlib.resources.path("project", "Police.ttf") as f:
                self._font=pygame.font.Font(f, 32)
        text = self._font.render("ant", True, pygame.Color("red")) 
        x, y = self.column*size + size/3, self.row*size + size/3 # Define the position where to write the ant.
        screen.blit(text, (x, y))







