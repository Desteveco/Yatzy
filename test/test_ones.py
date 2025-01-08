import pytest
from src.yatzy import Yatzy

def test_ones():
    '''
    The player scores the sum of the dice that reads one
    '''
    assert 0 == Yatzy.ones(3, 3, 3, 4, 5)
    assert 5 == Yatzy.ones(1, 1, 1, 1, 1)