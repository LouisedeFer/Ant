import pygame

from .ant import Ant
from .board import Board
from .cmd_line import read_args
from .dir import Dir
from .langton_ant import LangtonAnt
from .tile import Tile


def main() -> None:
    """Read arguments and start the simulation."""
    # Read command line arguments
    args = read_args()

    ant=Ant(0,0, Dir.UP)
    board=Board({(0,0): Tile(" ", pygame.Color("white"))})
    # Start automata
    if args.play:
        #LangtonAnt().ant_play(ant, board, args.steps)
        pass
    else:
        LangtonAnt().ant_auto(ant,board, args.steps)