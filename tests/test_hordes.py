# coding: utf-8
from hordes import Ville

def test_ville():
    """Initialize a Ville and check basic properties"""
    v = Ville()

    assert v.scie == False
    v.scie = True
    assert v.scie == True

    assert v.manufacture == False
    v.manufacture = True
    assert v.manufacture == True

    assert v.chantiers is not None

