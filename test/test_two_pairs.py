import pytest
from src.yatzy import Yatzy

@pytest.mark.pairs
def test_two_pairs():
    '''
    Two pairs:
    If there are two pairs of dice with the same number, the
    player scores the sum of these dice.
    '''
    # La categoria se llama "two pairs": la abstraccion del metodo
    # no es adecuada.
    # Mantengo notacion snake_case
    # El algoritmo del metodo no es optimo, es complicado e ilegible.

    assert 8 == Yatzy.two_pairs(1, 1, 2, 3, 3)
    assert 0 == Yatzy.two_pairs(1, 1, 2, 3, 4)
    assert 6 == Yatzy.two_pairs(1, 1, 2, 2, 2)
    assert 0 == Yatzy.two_pairs(1, 2, 3, 4, 5)
    assert 0 == Yatzy.two_pairs(4, 4, 4, 4, 5)