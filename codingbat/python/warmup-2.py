def string_times(str, n):
    """
    Given a string and a non-negative int n.
    
    Return a larger string that is n copies of the original
    string.

    >>> string_times('Hi', 2)
    'HiHi'
    >>> string_times('Hi', 3)
    'HiHiHi'
    >>> string_times('Hi', 1)
    'Hi'
    
    """
    return str * n

def front_times(str, n):
    """
    Given a string and a non-negative int n.
    
    We'll say that the front of the string is the first 3
    chars, or whatever is there if the string is less than
    length 3. Return n copies of the front.

    >>> front_times('Chocolate', 2)
    'ChoCho'
    >>> front_times('Chocolate', 3)
    'ChoChoCho'
    >>> front_times('Abc', 3)
    'AbcAbcAbc'
    
    """
    return str[:3] * n

if __name__ == '__main__':
    import doctest
    doctest.testmod()
