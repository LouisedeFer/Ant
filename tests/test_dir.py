import ant  # noqa: D100


def test_texte_direction() -> None :
    """Test if the right text is used."""
    assert ant.Dir.UP.texte()=="UP"
    assert ant.Dir.DOWN.texte()=="DOWN"
    assert ant.Dir.LEFT.texte()=="LEFT"
    assert ant.Dir.RIGHT.texte()=="RIGHT"

def test_angle_direction() -> None :
    """Test if the right angle is used."""
    assert ant.Dir.UP.angle()==0
    assert ant.Dir.DOWN.angle()==180
    assert ant.Dir.LEFT.angle()==90
    assert ant.Dir.RIGHT.angle()==270

