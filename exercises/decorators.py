"""Övningar på decorators"""

from functools import wraps

def memoize(f):
    
    """Implementera memoization (cache).

    Detta är den enklaste typen av cache som helt enkelt lagrar alla returvärden
    för de anropsvärden som används.
    """
    global memo
    memo = list()
    
    @wraps(f)
    def nsa():
        value = "{}: {}".format(f.__name__, f())
        memo.append(value)
    
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
        
@rovarsprak
def hej(x):
    return x

@memoize
def test_fun():
    return 'testord'
