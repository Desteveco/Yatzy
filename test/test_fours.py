import pytest
from src.yatzy import Yatzy

@pytest.mark.fours
def test_fours_test():
    assert 12 == Yatzy.fours(4, 4, 4, 5, 5)
    assert 8 == Yatzy.fours(4, 4, 5, 5, 5)
    assert 4 == Yatzy.fours(4, 5, 5, 5, 5)