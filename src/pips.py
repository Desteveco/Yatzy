from enum import Enum, unique

@unique
class Pip(Enum):
    ONE = 1
    TWO = 2
    THREE = 3
    FOUR = 4
    FIVE = 5
    SIX = 6
    SEVEN = 7

    def small_straight(*dice):
        return {i for i in range(Pip.ONE.value, Pip.SIX.value)}
    
    def large_straight(*dice):
        return {i for i in range(Pip.TWO.value, Pip.SEVEN.value)}