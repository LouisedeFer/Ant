import project
import pygame

# Constants
WHITE=pygame.Color("white")
BLACK=pygame.Color("black")

def test_board_creation()-> None :
    """Test the creation of the board."""
    board_init={0 : [project.Tile(" ",WHITE)], 1 : [project.Tile("X",BLACK)]}
    board_dic=project.board.Board(board_init).dictionary
    assert board_dic==board_init
    assert len(board_dic)==2

def test_board_change_color() -> None : 
    """Test if the color is changed properly."""
    board_init={0 : [project.Tile(" ",WHITE)], 1 : [project.Tile("X",BLACK)]}
    ant_0=project.Ant(0,0, project.Dir.UP)
    project.board.Board(board_init).change_color(ant_0.row, ant_0.column)
    assert project.board.Board(board_init).dictionary[0][0].color==BLACK


def test_board_add_tile() -> None :
    """Test if the tiles are added properly."""
    dic_init={0 : [project.Tile(" ",WHITE)], 1 : [project.Tile("X",BLACK)]}
    dic_1={0 : [project.Tile(" ",WHITE),project.Tile(" ",WHITE)], 1 : [project.Tile("X",BLACK), project.Tile(" ",WHITE)]}
    dic_2={0 : [project.Tile(" ",WHITE), project.Tile(" ",WHITE),project.Tile(" ",WHITE)], 1 : [project.Tile(" ",WHITE), project.Tile("X",BLACK), project.Tile(" ",WHITE)]}
    dict_3={0: [project.Tile(" ",WHITE)], 1 : [project.Tile(" ",WHITE)], 2 : [project.Tile("X",BLACK)]}

    board_0=project.board.Board(dic_init)
    board_0.add_tile(0,1)
    assert board_0.dictionary==dic_1
    board_0.add_tile(0,-1)
    assert board_0.dictionary== dic_2
    """board_0=project.board.Board(dic_init)
    board_0.add_tile(2,0)
    assert board_0.dictionary==dict_3"""
    dic_init={0 : [project.Tile(" ",WHITE)], 1 : [project.Tile("X",BLACK)]}
    board_0=project.board.Board(dic_init)
    board_0.add_tile(-1,0)
    assert board_0.dictionary==dict_3
