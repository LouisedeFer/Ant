import ant


def test_texte_direction() -> None :
    """Test if the right text is used."""
    assert ant.Dir.UP.texte()=="UP"
    assert ant.Dir.DOWN.texte()=="DOWN"
    assert ant.Dir.LEFT.texte()=="LEFT"
    assert ant.Dir.RIGHT.texte()=="RIGHT"
