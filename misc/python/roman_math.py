def multiply(x, y):
    """
    Multiply x and y using the Roman multiplication system.
    
    1. Write down the numbers next to each other.
        4   5
    2. Halve the first and double the second, writing them down a column.
       Discard any remainder if the number being halved is odd.
        4   5
        2   10
    3. Repeat as long as possible.
        4   5
        2   10
        1   20
    4. Moving down the column, if the number in the first column is even
       cross out the corresponding number from the second column.
        4   -5-
        2   -10-
        1   20
    5. Add up the numbers in the second column that aren't crossed out.
            20
    6. Done.
    
    >>> multiply(4, 5)
    20
    
    >>> multiply(1, 1)
    1
    
    >>> multiply(1, 0)
    0
    
    >>> multiply(4219, 5910)
    24934290
    
    >>> multiply(-65, 59)
    -3835
    
    >>> multiply(-1, -10)
    10
    
    """
    # we're already done
    if x == 1:
        return y
    
    # this algorithm needs positive numbers
    # but we'll preserve the originals to determine the correct sign
    #   for the product
    import math
    my_x = int(math.fabs(x))
    my_y = int(math.fabs(y))
    
    # the roman multiplication algorithm in one pass
    product = 0
    while my_x >= 1:
        if my_x % 2 == 1:
            product += my_y
        my_x /= 2
        my_y *= 2
    
    # get the correct sign on the product
    if (x > 0 and y > 0):
        return product
    else:
        if (x < 0 and y < 0):
            return product
        else:
            return -product

if __name__ == '__main__':
    import doctest
    doctest.testmod()
