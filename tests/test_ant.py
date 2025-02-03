import pygame

import project


def test_ant_creation() -> None :
    """Test the creation of the ant."""
    assert project.Ant(1,2, project.Dir.UP).row==1
    assert project.Ant(1,2, project.Dir.UP).column==2
    assert project.Ant(1,2, project.Dir.UP).dir==project.Dir.UP

def test_direction_ant() -> None : 
    """Test if the ant change its direction properly."""

def test_turn_right() -> None : 
    """Test if turning right is well done."""
    directions=[project.Dir.UP, project.Dir.RIGHT, project.Dir.DOWN, project.Dir.LEFT ]
    directions_perm=[project.Dir.RIGHT, project.Dir.DOWN, project.Dir.LEFT,project.Dir.UP ]
    for i in range (len(directions)) :
        ant_0=project.Ant(1,2, directions[i])
        ant_0.turn_right()
        assert ant_0.dir==directions_perm[i]

def test_turn_left() -> None : 
    """Test if turning left is well done."""
    directions=[project.Dir.UP, project.Dir.LEFT, project.Dir.DOWN, project.Dir.RIGHT ]
    directions_perm=[project.Dir.LEFT, project.Dir.DOWN, project.Dir.RIGHT,project.Dir.UP ]
    for i in range (len(directions)) :
        ant_0=project.Ant(1,2, directions[i])
        ant_0.turn_left()
        assert ant_0.dir==directions_perm[i]