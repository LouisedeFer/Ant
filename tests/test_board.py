import pygame  # noqa: D100

import ant

# Constants
WHITE=pygame.Color("white")
RED=pygame.Color("red")

def test_board_creation()-> None :
    """Test the creation of the board."""
    dic_init={(0,0) : ant.Tile(" ",WHITE), (1,0) : ant.Tile("X",RED)}
    board_dic=ant.board.Board(dic_init).dictionary
    assert board_dic==dic_init
    assert len(board_dic)==2

def test_contains_tile() -> None :
    """Test if contains is well implemented."""
    dic_init={(0,0) : ant.Tile(" ",WHITE), (1,0) : ant.Tile("X",RED)}
    board=ant.board.Board(dic_init)
    assert (0,0) in board
    assert (2,0) not in board


def test_board_change_color() -> None :
    """Test if the color is changed properly."""
    dic_init={(0,0) : ant.Tile(" ",WHITE), (1,0) : ant.Tile("X",RED)}
    ant_0=ant.Ant(0,0, ant.Dir.UP)
    ant.board.Board(dic_init).change_color(ant_0.row, ant_0.column)
    assert ant.board.Board(dic_init).dictionary[(0,0)].color==RED


def test_board_add_tile() -> None :
    """Test if the tiles are added properly."""
    dic_init={(0,0) : ant.Tile(" ",WHITE), (1,0) : ant.Tile("X",RED)}
    dic_1={(0,0) : ant.Tile(" ",WHITE), (1,0) : ant.Tile("X",RED), (0,1) : ant.Tile(" ", WHITE)}
    board_0=ant.board.Board(dic_init)
    board_0.add_tile(0,1)
    assert board_0.dictionary==dic_1

