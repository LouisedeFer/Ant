
# Third party
import logging

import pygame

# First party
from .dir import Dir

logger = logging.getLogger("foo")

class Tile:
    """
    A square tile in the game.

    Includes a color.
    """

    def __init__(self,text: str , color: pygame.Color) -> None:
        """Definition of tile."""
        self._color = color
        self._text=text

    def __repr__(self) -> str :
        """Text of the tile."""
        return "WHITE" if self._color == pygame.Color("white") else "BLACK"


    @property
    def color(self) -> pygame.Color:
        """The color of the tile."""
        return self._color

    @color.setter
    def color(self, color: pygame.Color) -> None:
        """Change the color of the tile."""
        self._color = color

    @property
    def text(self) -> str :
        """The text of the tile."""
        return self._text

    @text.setter
    def text(self, text : str) -> None :
        """Change the text of the tile."""
        self._text=text

    def draw(self, screen: pygame.Surface, size: int, row : int, col : int) -> None:
        """Draw the tile on screen."""
        rect = pygame.Rect(col * size, row * size, size, size)
        pygame.draw.rect(screen, self.color, rect)
