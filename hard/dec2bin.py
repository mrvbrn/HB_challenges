"""Convert a decimal number to binary representation.

For example::

And finally, using division:

    >>> dec2bin_division(0)
    '0'

    >>> dec2bin_division(1)
    '1'

    >>> dec2bin_division(2)
    '10'

    >>> dec2bin_division(4)
    '100'

    >>> dec2bin_division(15)
    '1111'


"""


def dec2bin_division(num):
    """Convert a decimal number to binary representation."""
    if num == 0:
        return "0"
    decimal = []
    
    while num > 0:
        binary = num % 2
        decimal.append(str(binary))
        num = num // 2

    return "".join(reversed(decimal))



if __name__ == '__main__':
    import doctest
    if doctest.testmod().failed == 0:
        print("\n*** ALL TEST PASSED. W00T!\n")
