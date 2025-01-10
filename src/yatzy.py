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

    def score_pair(self, d1, d2, d3, d4, d5):
        counts = [0] * 6
        counts[d1 - 1] += 1
        counts[d2 - 1] += 1
        counts[d3 - 1] += 1
        counts[d4 - 1] += 1
        counts[d5 - 1] += 1
        at = 0
        for at in range(6):
            if (counts[6 - at - 1] == 2):
                return (6 - at) * 2
        return 0

    @staticmethod
    def two_pairs(d1, d2, d3, d4, d5):
        counts = [0] * 6
        counts[d1 - 1] += 1
        counts[d2 - 1] += 1
        counts[d3 - 1] += 1
        counts[d4 - 1] += 1
        counts[d5 - 1] += 1
        n = 0
        score = 0
        for i in range(6):
            if (counts[6 - i - 1] >= 2):
                n = n + 1
                score += (6 - i)

        if (n == 2):
            return score * 2
        else:
            return 0

    @staticmethod
    def four_of_a_kind(_1, _2, d3, d4, d5):
        tallies = [0] * 6
        tallies[_1 - 1] += 1
        tallies[_2 - 1] += 1
        tallies[d3 - 1] += 1
        tallies[d4 - 1] += 1
        tallies[d5 - 1] += 1
        for i in range(6):
            if (tallies[i] >= 4):
                return (i + 1) * 4
        return 0

    @staticmethod
    def three_of_a_kind(d1, d2, d3, d4, d5):
        t = [0] * 6
        t[d1 - 1] += 1
        t[d2 - 1] += 1
        t[d3 - 1] += 1
        t[d4 - 1] += 1
        t[d5 - 1] += 1
        for i in range(6):
            if (t[i] >= 3):
                return (i + 1) * 3
        return 0

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
    def fullHouse(d1, d2, d3, d4, d5):
        tallies = []
        _2 = False
        i = 0
        _2_at = 0
        _3 = False
        _3_at = 0

        tallies = [0] * 6
        tallies[d1 - 1] += 1
        tallies[d2 - 1] += 1
        tallies[d3 - 1] += 1
        tallies[d4 - 1] += 1
        tallies[d5 - 1] += 1

        for i in range(6):
            if (tallies[i] == 2):
                _2 = True
                _2_at = i + 1

        for i in range(6):
            if (tallies[i] == 3):
                _3 = True
                _3_at = i + 1

        if (_2 and _3):
            return _2_at * 2 + _3_at * 3
        else:
            return 0
        


if __name__ == "__main__": 
    
    
    assert 0 == Yatzy.twos(3, 3, 3, 4, 5)
    assert 4 == Yatzy.twos(2, 3, 2, 5, 1)
