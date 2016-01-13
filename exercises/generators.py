"""Övningar på generators"""
from math import sqrt

def cubes(x=0):
    """Implementera en generator som skapar en serie med kuber (i ** 3).

    Talserien utgår från de positiva heltalen: 1, 2, 3, 4, 5, 6, ...
    Talserien som skapas börjar således: 1, 8, 27, 64, 125, 216, ...

    Talserien ska inte ha något slut.
    """
    while True:
        x += 1
        yield x**3
        

def primes(i=1):
    """Implementera en generator som returnerar primtal.

    Talserien som förväntas börjar alltså: 2, 3, 5, 7, 11, 13, 17, 19, 23, ...
    """
    def _prime(x):
        for i in range(2, int(sqrt(x)) + 1):
            if x % i == 0:
                return False
        return True
    
    while True:    
        i += 1
        if _prime(i) == True:
            yield i



        

def fibonacci():
    """Implementera en generator som returnerar de berömda fibonacci-talen.

    Fibonaccis talserie börjar med 0 och 1. Nästa tal är sedan summan av de
    två senaste.

    Alltså börjar serien: 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, ...

    """
    first = None
    second = -1
    summa = 1

    while True:
        first = second
        second = summa 
        summa = first + second
        yield summa 


def alphabet():
    """En generator som returnerar namnen på tecknen i det hebreiska alfabetet.

    Iteratorn returnerar namnen för de hebreiska bokstäverna i alfabetisk
    ordning. Namnen och ordningen är:

    Alef, Bet, Gimel, Dalet, He, Vav, Zayin, Het, Tet, Yod, Kaf, Lamed, Mem,
    Nun, Samekh, Ayin, Pe, Tsadi, Qof, Resh, Shin, Tav

    """
    alph = ["Alef", "Bet", "Gimel", "Dalet", "He", "Vav", "Zayin", "Het", "Tet", "Yod", "Kaf", "Lamed", "Mem", "Nun", "Samekh", "Ayin", "Pe", "Tsadi", "Qof", "Resh", "Shin", "Tav"]

    index = -1

    while True:
        index += 1
        if index < 22:
            yield alph[index]
        else:
            raise StopIteration 




def permutations():
    """En generator som returnerar alla permutationer av en inmatad sträng.

    Då strängen 'abc' matas in fås: 'abc', 'acb', 'bac', 'bca', 'cba', 'cab'
    """
    pass


def look_and_say():
    """En generator som implementerar look-and-say-talserien.

    Sekvensen fås genom att man läser ut och räknar antalet siffror i
    föregående tal.

    1 läses 'en etta', alltså 11
    11 läses 'två ettor', alltså 21
    21 läses 'en tvåa, en etta', alltså 1211
    1211 läses 'en etta, en tvåa, två ettor', alltså 111221
    111221 läses 'tre ettor, två tvåor, en etta', alltså 312211
    """
    count = 0

    chars = list()
    def sequence(text):
        for index in range(len(text)):
            chars.append(text[index])

    for i in chars:
        count += 1
        val = "{}, {}".fomrat(count, i)