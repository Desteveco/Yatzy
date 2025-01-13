import pytest
from src.yatzy import Yatzy

@pytest.mark.twos
def test_twos():
    '''
    The player scores the sum of the dice that reads two
    '''
    assert 0 == Yatzy.twos(3, 3, 3, 4, 5)
    assert 4 == Yatzy.twos(2, 3, 2, 5, 1)