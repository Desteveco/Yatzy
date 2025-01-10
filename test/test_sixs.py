import pytest
from src.yatzy import Yatzy

@pytest.mark.sixes
def test_sixes_test():
    assert 0 == Yatzy.sixes(4, 4, 4, 5, 5)
    assert 6 == Yatzy.sixes(4, 4, 6, 5, 5)
    assert 18 == Yatzy.sixes(6, 5, 6, 6, 5)

    '''Change object to a function
    Pass specific arguments rather than a whole object
    '''