import pytest
from src.yatzy import Yatzy
@pytest.fixture
def inyector():
    # es el setup de unittest o de JUnit
    tirada = Yatzy(4, 5, 6, 4, 5)
    return tirada

@pytest.mark.sixes
def test_sixes(inyector):
    '''
    The player scores the sum of the dice that reads six
    '''
    valorEsperado = 6
    assert valorEsperado == inyector.sixes()