def sleep_in(weekday, vacation):
    """
    The parameter weekday is True if it is a weekday.
    The parameter vacation is True if we are on vacation.
    We sleep in if it is not a weekday or we're on vacation.
    Return True if we sleep in.
    
    >>> sleep_in(False, False)
    True
    >>> sleep_in(True, False)
    False
    >>> sleep_in(False, True)
    True
    
    """
    return not weekday or vacation

def monkey_trouble(a_smile, b_smile):
    """
    We have two monkeys, a and b.
    
    The parameters a_smile and b_smile indicate if each is smiling.
    
    We are in trouble if they are both smiling or if neither 
    of them is smiling.
    
    Return True if we are in trouble.
    
    >>> monkey_trouble(True, True)
    True
    >>> monkey_trouble(False, False)
    True
    >>> monkey_trouble(True, False)
    False
    
    """
    return not a_smile ^ b_smile


def sum_double(a, b):
    """
    Given two int values, return their sum.
    Unless the two values are the same, then return double their sum.
    
    >>> sum_double(1, 2)
    3
    >>> sum_double(3, 2)
    5
    >>> sum_double(2, 2)
    8
    
    """
    sum = a + b
    if (a == b):
        return 2 * sum
    return sum

def diff21(n):
    """
    Given an int n, return the absolute difference between n and 21,
    except return double the absolute difference if n is over 21.
    
    >>> diff21(19)
    2
    >>> diff21(10)
    11
    >>> diff21(21)
    0
    >>> diff21(22)
    2
    
    """
    if n <= 21:
        return abs(21 - n)
    else:
        return 2 * abs(21 - n)

def parrot_trouble(talking, hour):
    """
    We have a loud talking parrot.
    
    The "hour" parameter is the current hour time in the range 0..23.
    
    We are in trouble if the parrot is talking and the hour is
    before 7 or after 20.
    
    Return True if we are in trouble.
    
    >>> parrot_trouble(True, 6)
    True
    >>> parrot_trouble(True, 7)
    False
    >>> parrot_trouble(False, 6)
    False
    >>> parrot_trouble(True, 20)
    False
    
    """
    if talking:
        return not 6 < hour < 21
    return False

def makes10(a, b):
    """
    Given 2 ints, a and b.
    
    Return True if one if them is 10 or if their sum is 10.
    
    >>> makes10(9, 10)
    True
    >>> makes10(9, 9)
    False
    >>> makes10(1, 9)
    True
    
    """
    return 10 in [a,b] or a + b == 10

if __name__ == '__main__':
    import doctest
    doctest.testmod()
