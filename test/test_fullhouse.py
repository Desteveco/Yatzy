import pytest
from src.yatzy import Yatzy

@pytest.mark.full
def test_fullHouse():
    assert 8 == Yatzy.fullHouse(1, 1, 2, 2, 2)
    assert 0 == Yatzy.fullHouse(2, 2, 3, 3, 4)
    assert 0 == Yatzy.fullHouse(4, 4, 4, 4, 4)
    assert 0 == Yatzy.fullHouse(4, 4, 4, 1, 2)  