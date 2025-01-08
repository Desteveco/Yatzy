import pytest
from src.yatzy import Yatzy

@pytest.fixture
def inyector():
    # es el setup de unittest o de JUnit
    tirada = Yatzy(4, 5, 6, 4, 5)
    return tirada


def test_fours(inyector):
    '''
    The player scores the sum of the dice that reads four
    '''
    # es necesario un objeto de tipo Yatzy ya creado
    valorEsperado = 8
    # No puedo testear con fixtures = inyeccion de dependencias
    # los metodos estaticos como chance()
    assert valorEsperado == inyector.fours()