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
        return Yatzy.FIFTY if dice.count(dice[0]) == 5 else Yatzy.ZERO
        
    '''Rename variables to make the code more readable
    Move an expression inline
    Use return instead of a loop control variable'''

    @classmethod
    def ones(cls, *dice):
        return cls.__sum_repeated_numbers(Pip.ONE.value, *dice)
    '''Convert a set of type codes to a class
    Combine similar routines by a paramenter
    Change value objets to reference objects
    '''

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
    Change value objets to reference objects
    '''


    @classmethod
    def fours(cls, *dice):
        return cls.__sum_repeated_numbers(Pip.FOUR.value, *dice)
    '''Convert a set of type codes to a class
    Combine similar routines by a paramenter
    Change value objets to reference objects
    '''

    @classmethod
    def fives(cls, *dice):
        return cls.__sum_repeated_numbers(Pip.FIVE.value, *dice)
    '''Convert a set of type codes to a class
    Combine similar routines by a paramenter
    Change value objets to reference objects
    '''

    @classmethod
    def sixes(cls, *dice):
        return cls.__sum_repeated_numbers(Pip.SIX.value, *dice)
    '''Convert a set of type codes to a class
    Combine similar routines by a paramenter
    Change value objets to reference objects
    '''
    @staticmethod
    def __numbers_repeated(*dice, times):
        return set([number for number in dice if dice.count(number) >= times])
    
    @staticmethod
    def score_pair(*dice):
        return Pip.TWO.value*max(Yatzy.__numbers_repeated(*dice, times=Pip.TWO.value))

    @staticmethod
    def two_pairs(*dice):
        TWO = Pip.TWO.value
        pairs = Yatzy.__numbers_repeated(*dice, times=TWO)
        return Pip.TWO.value*sum(pairs) if len(pairs) == Pip.TWO.value else Yatzy.ZERO
        

    @staticmethod
    def four_of_a_kind(*dice):
        repeated = Yatzy.__numbers_repeated(*dice, times=Pip.FOUR.value)
        return Pip.FOUR.value * max(repeated) if repeated else Yatzy.ZERO
        

    @staticmethod
    def three_of_a_kind(*dice):
        repeated = Yatzy.__numbers_repeated(*dice, times=Pip.THREE.value)
        return Pip.THREE.value * max(repeated) if repeated else Yatzy.ZERO

    @staticmethod
    def small_straight(d1, d2, d3, d4, d5):
        tallies = [0] * 6
        tallies[d1 - 1] += 1
        tallies[d2 - 1] += 1
        tallies[d3 - 1] += 1
        tallies[d4 - 1] += 1
        tallies[d5 - 1] += 1
        if (tallies[0] == 1 and
                tallies[1] == 1 and
                tallies[2] == 1 and
                tallies[3] == 1 and
                tallies[4] == 1):
            return 15
        return 0

    @staticmethod
    def large_straight(d1, d2, d3, d4, d5):
        tallies = [0] * 6
        tallies[d1 - 1] += 1
        tallies[d2 - 1] += 1
        tallies[d3 - 1] += 1
        tallies[d4 - 1] += 1
        tallies[d5 - 1] += 1
        if (tallies[1] == 1 and
                tallies[2] == 1 and
                tallies[3] == 1 and
                tallies[4] == 1
                and tallies[5] == 1):
            return 20
        return 0

    @staticmethod
    def full_house(*dice):
        if Yatzy.__exactly_numbers_repeated(*dice, times=Pip.THREE.value) and Yatzy.__exactly_numbers_repeated(*dice, times=Pip.TWO.value) and Yatzy.yatzy(*dice) != Yatzy.FIFTY:
            return Yatzy.chance(*dice) 
        return Yatzy.ZERO

    @staticmethod    
    def __exactly_numbers_repeated(*dice, times):
        return set([number for number in dice if dice.count(number) == times])

if __name__ == "__main__": 
    
    
    assert 0 == Yatzy.twos(3, 3, 3, 4, 5)
    assert 4 == Yatzy.twos(2, 3, 2, 5, 1)
