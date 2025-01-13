import pytest
from src.yatzy import Yatzy

@pytest.mark.chance
def test_chance():
    '''
    Chance
    The player scores the sum of all dice, no matter what they read.
    '''
    # iterar sobre *args evita codigo cableado a 5 argumentos
    assert 15 == Yatzy.chance(1, 2, 3, 4, 5)
    assert 14 == Yatzy.chance(1, 1, 3, 3, 6)
    assert 21 == Yatzy.chance(4, 5, 5, 6, 1)
