import pytest
from src.yatzy import Yatzy

@pytest.mark.threes
def test_threes():
    '''
    The player scores the sum of the dice that reads three
    '''
    assert 0 == Yatzy.threes(1, 1, 1, 1, 1)
    assert 9 == Yatzy.threes(3, 3, 3, 4, 5)