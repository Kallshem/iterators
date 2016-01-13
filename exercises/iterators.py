"""Övningar på iterators"""
from math import sqrt

class Cubes():
    """En iterator som skapar en serie med kuber (i ** 3).

    Talserien utgår från de positiva heltalen: 1, 2, 3, 4, 5, 6, ...
    Talserien som skapas börjar således: 1, 8, 27, 64, 125, 216, ...

    Talserien ska inte ha något slut.

    """
    def __init__(self):
        self.n = 0        

    def cube(x):
        return (x ** 3)

    def __next__(self):
        self.n += 1
        return Cubes.cube(self.n)

    def __iter__(self):
        return self


# class CubesDeluxe():
#     class SuperCube():
#         def __init__(self):
#             self.i = 0

#         def __next__(self):
#             self.i += 1
#             return self.i

#     def __iter__(self):
#         return CubesDeluxe.SuperCube()

class Primes():
    """En iterator som returnerar primtal.

    Talserien som förväntas börjar alltså: 2, 3, 5, 7, 11, 13, 17, 19, 23, ...

    """
    
    def __init__(self):
        self.n = 1
        


    @staticmethod
    def _prime(x):
        for i in range(2, int(sqrt(x)) + 1):
            if x % i == 0:
                return False
        return True

    def __next__(self):
        while True:
            self.n += 1
            if Primes._prime(self.n):
                return self.n
        

    def __iter__(self):
        return self



class Fibonacci():
    """En iterator som returnerar de berömda fibonacci-talen.

    Fibonaccis talserie börjar med 0 och 1. Nästa tal är sedan summan av de
    två senaste.

    Alltså börjar serien: 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, ...

    """
    def __init__(self):
        self.first = None
        self.second = -1
        self.sum = 1

    def fibcci(self):
        self.sum = self.first + self.second        
        return self.sum

    def __next__(self):
        self.first = self.second
        self.second = self.sum
        return Fibonacci.fibcci(self)

    def __iter__(self):
        return self


class Alphabet():
    """En iterator som returnerar namnen på tecknen i det hebreiska alfabetet.

    Iteratorn returnerar namnen för de hebreiska bokstäverna i alfabetisk
    ordning. Namnen och ordningen är:

    Alef, Bet, Gimel, Dalet, He, Vav, Zayin, Het, Tet, Yod, Kaf, Lamed, Mem,
    Nun, Samekh, Ayin, Pe, Tsadi, Qof, Resh, Shin, Tav

    """
    def __init__(self):
        self.x = -1
    
    def abc(x):
        alph = ["Alef", "Bet", "Gimel", "Dalet", "He", "Vav", "Zayin", "Het", "Tet", "Yod", "Kaf", "Lamed", "Mem", "Nun", "Samekh", "Ayin", "Pe", "Tsadi", "Qof", "Resh", "Shin", "Tav"]
        return alph[x]

    def __next__(self):
        self.x += 1
        if self.x < 22:
            return Alphabet.abc(self.x)
        else:
            raise StopIteration

    def __iter__(self):
        return self
        
class Permutations():
    """En iterator som returnerar alla permutationer av en inmatad sträng.

    Då strängen 'abc' matas in fås: 'abc', 'acb', 'bac', 'bca', 'cba', 'cab'
    """
    pass



class LookAndSay():
    """En iterator som implementerar look-and-say-talserien.

    Sekvensen fås genom att man läser ut och räknar antalet siffror i
    föregående tal.

    1 läses 'en etta', alltså 11
    11 läses 'två ettor', alltså 21
    21 läses 'en tvåa, en etta', alltså 1211
    1211 läses 'en etta, en tvåa, två ettor', alltså 111221
    111221 läses 'tre ettor, två tvåor, en etta', alltså 312211
    """

    def __init__(self):
        pass


        
