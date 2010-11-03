def isPalindrome(string):
    """
    True if string is a palindrome (same forwards and backwards).
    
    >>> isPalindrome('abba')
    True
    
    >>> isPalindrome('abc')
    False
    
    >>> isPalindrome('amanaplanacanalpanama')
    True
    
    >>> isPalindrome('racecar')
    True
    
    >>> isPalindrome('racer')
    False
    
    """
    return string == ''.join(reversed(string))

def isPalindromeRecursion(string):
    """
    True if string is a palindrome. Using recursion.
    
    >>> isPalindromeRecursion('abba')
    True
    
    >>> isPalindromeRecursion('abc')
    False
    
    >>> isPalindromeRecursion('amanaplanacanalpanama')
    True
    
    >>> isPalindromeRecursion('racecar')
    True
    
    >>> isPalindromeRecursion('racer')
    False
    
    """
    if len(string) == 1:
        return True
    if len(string) == 2:
        return string[0] == string[1]
    if string[0] == string[-1]:
        return isPalindromeRecursion(string[1:-1])
    return False

if __name__ == '__main__':
    import doctest
    doctest.testmod()
