import pytest
from src.yatzy import Yatzy

def test_constructor():
    tirada = Yatzy(1, 1, 1, 1, 1)
    for dado in tirada.dice:
        assert 1 == dado