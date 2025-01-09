import pytest
from src.yatzy import Yatzy

def test_one_pair():
    assert 6 == Yatzy().score_pair(3, 4, 3, 5, 6)
    assert 10 == Yatzy().score_pair(5, 3, 3, 3, 5)
    assert 12 == Yatzy().score_pair(5, 3, 6, 6, 5)
'''def test_pair():
    
    Pair:
    The player scores the sum of the two highest matching dice.
    
    # El algoritmo del metodo no es optimo, es complicado e ilegible.
    # La abstraccion, el nombre del metodo, no es adecuada
    # puesto que la categoria se llama pair.
    assert 8 == Yatzy.pair(3, 3, 3, 4, 4)
    assert 12 == Yatzy.pair(1, 1, 6, 2, 6)
    assert 6 == Yatzy.pair(3, 3, 3, 4, 1)
    assert 6 == Yatzy.pair(3, 3, 3, 3, 1)
    assert 0 == Yatzy.pair(1, 2, 3, 4, 5)'''