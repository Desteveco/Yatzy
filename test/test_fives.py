import pytest
from src.yatzy import Yatzy

@pytest.mark.fives
def test_fives():
    assert 10 == Yatzy.fives(4, 4, 4, 5, 5)
    assert 15 == Yatzy.fives(4, 4, 5, 5, 5)
    assert 20 == Yatzy.fives(4, 5, 5, 5, 5)

    '''Change object to a function
    Pass specific arguments rather than a whole object
    '''