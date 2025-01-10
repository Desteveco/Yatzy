import pytest
from src.yatzy import Yatzy

def test_one_pair():
    assert 6 == Yatzy().score_pair(3, 4, 3, 5, 6)
    assert 10 == Yatzy().score_pair(5, 3, 3, 3, 5)
    assert 12 == Yatzy().score_pair(5, 3, 6, 6, 5)
