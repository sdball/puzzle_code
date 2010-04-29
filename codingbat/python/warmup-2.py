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

def string_bits(str):
    """
    Given a string, return a new string made of every other
    char starting with the first, so "Hello" yields "Hlo". 
    
    >>> string_bits('Hello')
    'Hlo'
    >>> string_bits('Hi')
    'H'
    >>> string_bits('Heeololeo')
    'Hello'
    
    """
    return ''.join([str[n] for n in xrange(0, len(str), 2)])

def string_splosion(str):
    """
    Given a non-empty string like "Code" return a
    string like "CCoCodCode". 
    
    >>> string_splosion('Code')
    'CCoCodCode'
    >>> string_splosion('abc')
    'aababc'
    >>> string_splosion('ab')
    'aab'
    
    """
    chunks = []
    for i in xrange(1, len(str) + 1):
        chunks.append(str[:i])
    return ''.join(chunks)

if __name__ == '__main__':
    import doctest
    doctest.testmod()
