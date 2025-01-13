import pytest
from src.yatzy import Yatzy

@pytest.mark.full
def test_full_house():
    assert 8 == Yatzy.full_house(1, 1, 2, 2, 2)
    assert 0 == Yatzy.full_house(2, 2, 3, 3, 4)

def test_full_house1():
    assert 0 == Yatzy.full_house(4, 4, 4, 4, 4)
 
def test_full_house2():
    assert 0 == Yatzy.full_house(4, 4, 4, 1, 2) 