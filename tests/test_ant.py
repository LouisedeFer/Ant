import ant
import pygame


def test_ant_creation() -> None :
    """Test the creation of the ant."""
    assert ant.Ant(1,2, ant.Dir.UP).row==1
    assert ant.Ant(1,2, ant.Dir.UP).column==2
    assert ant.Ant(1,2, ant.Dir.UP).dir==ant.Dir.UP

def test_direction_ant() -> None : 
    """Test if the ant change its direction properly."""
    ant_0=ant.Ant(0,0, ant.Dir.UP)
    dicti={(0,0): ant.Tile(" ",pygame.Color("white"))}
    ant_0.change_direction(dicti)
    assert ant_0.dir==ant.Dir.RIGHT
    ant_0=ant.Ant(0,0, ant.Dir.UP)
    dicti={(0,0): ant.Tile("X",pygame.Color("red"))}
    ant_0.change_direction(dicti)
    assert ant_0.dir==ant.Dir.LEFT



def test_turn_right() -> None : 
    """Test if turning right is well done."""
    directions=[ant.Dir.UP, ant.Dir.RIGHT, ant.Dir.DOWN, ant.Dir.LEFT ]
    directions_perm=[ant.Dir.RIGHT, ant.Dir.DOWN, ant.Dir.LEFT,ant.Dir.UP ]
    for i in range (len(directions)) :
        ant_0=ant.Ant(1,2, directions[i])
        ant_0.turn_right()
        assert ant_0.dir==directions_perm[i]

def test_turn_left() -> None : 
    """Test if turning left is well done."""
    directions=[ant.Dir.UP, ant.Dir.LEFT, ant.Dir.DOWN, ant.Dir.RIGHT ]
    directions_perm=[ant.Dir.LEFT, ant.Dir.DOWN, ant.Dir.RIGHT,ant.Dir.UP ]
    for i in range (len(directions)) :
        ant_0=ant.Ant(1,2, directions[i])
        ant_0.turn_left()
        assert ant_0.dir==directions_perm[i]