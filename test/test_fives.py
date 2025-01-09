import pytest
from src.yatzy import Yatzy

@pytest.fixture
def inyector():
    # es el setup de unittest o de JUnit
    tirada = Yatzy(4, 5, 6, 4, 5)
    return tirada


def test_fives(inyector):
    '''
    The player scores the sum of the dice that reads five
    '''
    valorEsperado = 10
    assert valorEsperado == inyector.fives()