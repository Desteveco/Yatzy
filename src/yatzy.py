from .pips import Pip
class Yatzy:

    ZERO = 0
    FIFTY = 50

    @staticmethod
    def chance(*dice):
        return sum(dice)
    '''Rename variable to make the code clearer'''

    @staticmethod
    def yatzy(*dice):
        return Yatzy.FIFTY if len(set(dice)) == 1 else Yatzy.ZERO  
    '''Rename variables to make the code more readable
    Move an expression inline
    Use return instead of a loop control variable'''

    @classmethod
    def ones(cls, *dice):
        return cls.__sum_repeated_numbers(Pip.ONE.value, *dice)
    '''Convert a set of type codes to a class
    Combine similar routines by a paramenter
    Change value objets to reference objects'''

    @classmethod
    def __sum_repeated_numbers(cls, n, *dice):
        return sum(n for i in dice if i == n)  
    '''Rename to a more significant method name
    Move an expression inline'''
    
    @classmethod
    def twos(cls, *dice):
        return cls.__sum_repeated_numbers(Pip.TWO.value, *dice)

    @classmethod
    def threes(cls, *dice):
        return cls.__sum_repeated_numbers(Pip.THREE.value, *dice)
    '''Convert a set of type codes to a class
    Combine similar routines by a paramenter
    Change value objets to reference objects'''

    @classmethod
    def fours(cls, *dice):
        return cls.__sum_repeated_numbers(Pip.FOUR.value, *dice)
    '''Convert a set of type codes to a class
    Combine similar routines by a paramenter
    Change value objets to reference objects'''

    @classmethod
    def fives(cls, *dice):
        return cls.__sum_repeated_numbers(Pip.FIVE.value, *dice)
    '''Convert a set of type codes to a class
    Combine similar routines by a paramenter
    Change value objets to reference objects'''

    @classmethod
    def sixes(cls, *dice):
        return cls.__sum_repeated_numbers(Pip.SIX.value, *dice)
    '''Convert a set of type codes to a class
    Combine similar routines by a paramenter
    Change value objets to reference objects'''
    
    @staticmethod
    def __numbers_repeated(*dice, times):
        return set([number for number in dice if dice.count(number) >= times])
    '''Create a method to not repeat code
    Replace an expression with a routine
    Combine similar routines by parameterizing them'''

    @staticmethod
    def score_pair(*dice):
        return Pip.TWO.value*max(Yatzy.__numbers_repeated(*dice, times=Pip.TWO.value))
    '''Combine similar routines by parameterizing them'''

    @staticmethod
    def two_pairs(*dice):
        TWO = Pip.TWO.value
        pairs = Yatzy.__numbers_repeated(*dice, times=TWO)
        return Pip.TWO.value*sum(pairs) if len(pairs) == Pip.TWO.value else Yatzy.ZERO
    '''Combine similar routines by parameterizing them'''

    @staticmethod
    def four_of_a_kind(*dice):
        repeated = Yatzy.__numbers_repeated(*dice, times=Pip.FOUR.value)
        return Pip.FOUR.value * max(repeated) if repeated else Yatzy.ZERO
    '''Combine similar routines by parameterizing them'''

    @staticmethod
    def three_of_a_kind(*dice):
        repeated = Yatzy.__numbers_repeated(*dice, times=Pip.THREE.value)
        return Pip.THREE.value * max(repeated) if repeated else Yatzy.ZERO
    '''Combine similar routines by parameterizing them'''

    @staticmethod
    def small_straight(*dice):
        if set(dice) == Pip.small_straight(*dice):
            return Yatzy.chance(*dice)
        return Yatzy.ZERO
    '''Move an expression inline
    Encapsule a collection'''

    @staticmethod
    def large_straight(*dice):
        if set(dice) == Pip.large_straight(*dice):
            return Yatzy.chance(*dice)
        return Yatzy.ZERO
    '''Move an expression inline
    Encapsule a collection'''

    @staticmethod
    def full_house(*dice):
        if Yatzy.__exactly_numbers_repeated(*dice, times=Pip.THREE.value) and Yatzy.__exactly_numbers_repeated(*dice, times=Pip.TWO.value) and Yatzy.yatzy(*dice) != Yatzy.FIFTY:
            return Yatzy.chance(*dice) 
        return Yatzy.ZERO
    '''Combine similar routines by parameterizing them'''

    @staticmethod    
    def __exactly_numbers_repeated(*dice, times):
        return set([number for number in dice if dice.count(number) == times])
    '''Create a method to not repeat code
    Replace an expression with a routine
    Combine similar routines by parameterizing them'''

if __name__ == "__main__": 
    
    
    assert 0 == Yatzy.twos(3, 3, 3, 4, 5)
    assert 4 == Yatzy.twos(2, 3, 2, 5, 1)
