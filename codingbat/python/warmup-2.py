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
    return ''.join([str[:i] for i in xrange(1, len(str) + 1)])

def last2(str):
    """
    Given a string, return the count of the number of times
    that a substring length 2 appears in the string and also
    as the last 2 chars of the string, so "hixxxhi" yields 1
    (we won't count the end substring). 
    
    >>> last2('hixxhi')
    1
    >>> last2('xaxxaxaxx')
    1
    >>> last2('axxxaaxx')
    2
    >>> last2('xxxx')
    2
    
    """
    return len([n for n in xrange(len(str) - 2) if str[n:n+2] == str[-2:]])

def array_count9(nums):
    """
    Given an array of ints, return the number of 9's in the array. 
    
    >>> array_count9([1, 2, 9])
    1
    >>> array_count9([1, 9, 9])
    2
    >>> array_count9([1, 9, 9, 3, 9])
    3
    
    """
    return len([n for n in nums if n == 9])

def array_front9(nums):
    """
    Given an array of ints, return True if one of the first
    4 elements in the array is a 9. The array length may be
    less than 4.
    
    >>> array_front9([1, 2, 9, 3, 4])
    True
    >>> array_front9([1, 2, 3, 4, 9])
    False
    >>> array_front9([1, 2, 3, 4, 5])
    False
    
    """
    return 9 in nums[:4]

def array123(nums):
    """
    Given an array of ints, return True if it contains [1, 2, 3].
    
    >>> array123([1, 1, 2, 3, 1])
    True
    >>> array123([1, 1, 2, 4, 1])
    False
    >>> array123([1, 1, 2, 1, 2, 3])
    True
    >>> array123([1,2,3,1,2,3])
    True
    >>> array123([])
    False
    >>> array123([3,2,1,3,2,1])
    False
    
    """
    for i in xrange(len(nums) - 2):
        if nums[i] == 1 and nums[i+1] == 2 and nums[i+2] == 3:
            return True
    return False

def string_match(a, b):
    """
    Given 2 strings, a and b, return the number of the
    positions where they contain the same length 2
    substring. So "xxcaazz" and "xxbaaz" yields 3, since
    the "xx", "aa", and "az" substrings appear in the
    same place in both strings. 
    
    >>> string_match('xxcaazz', 'xxbaaz')
    3
    >>> string_match('abc', 'abc')
    2
    >>> string_match('abc', 'axc')
    0
    
    """
    pass

if __name__ == '__main__':
    import doctest
    doctest.testmod()
