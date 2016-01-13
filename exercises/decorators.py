"""Övningar på decorators"""

from functools import wraps

def memoize(f):
    
    """Implementera memoization (cache).

    Detta är den enklaste typen av cache som helt enkelt lagrar alla returvärden
    för de anropsvärden som används.
    """
    #global memo
    memo = dict()
    
    @wraps(f)
    def nsa(*args, **kwargs):
#        value = "{}: {}".format(f.__name__, f())
#        memo.append(value)
        try:
            print('Searching for memoized value...')
            return memo[(args, tuple(sorted(kwargs.items())))]
        except KeyError:
            print('Calculating and storing value.')
            value = f(*args, **kwargs)
            memo[(args, tuple(sorted(kwargs.items())))] = value
            return value
    
    return nsa
    
    #Varför kan inte denna funktion skrivas utan "outer func"? Hur skriver man om man också vill kunna använda funktioner som kräver argument?
    
def rovarsprak(f):
    """
    Översätt utdata till rövarspråket.

    Funktionen som dekoreras kan antas returnera textsträngar. Dessa översätts
    av decoratorn till rövarspråket.
    """
    
    consonants = ["b", "c", "d", "f", "g", "h", "j", "k", "l", "m", "n", "p", "q", "r", "s", "t", "v", "x", "z"]
    vowels = ["a", "e", "i", "o", "u", "y"]
    letters = list()

    def sequence(text):
        for index in range(len(text)):
            letters.append(text[index])

    @wraps(f)
    def change():
        string = f()
        sequence(string)
        output = list()

        for letter in letters:
            if letter in consonants:
                output.extend([letter, "o", letter, ])
            elif letter in vowels:
                output.append(letter)
            elif letter == " ":
                output.append(" ")
            else:
                pass

        return "".join(output)
    
    return change
        
@memoize
def hej(x):
    return x

@memoize
def test_fun():
    return 'testord'


#def min_funk(x, y, z, option = None):
def min_funk(*args, **kwargs):
    print(args)
    print(tuple(sorted(kwargs.items())))

#min_funk(5, 7, 11, option = 'abc')