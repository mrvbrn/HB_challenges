"""Convert a hexadecimal string, like '1A', into it's decimal equivalent.

    >>> hex_convert('6')
    6

    >>> hex_convert('10')
    16

    >>> hex_convert('FF')
    255

    >>> hex_convert('FFFF')
    65535
"""


def hex_convert(hex_in):
    """Convert a hexadecimal string, like '1A', into it's decimal equivalent."""
    decimal_alphabet = {"A" : 10, "B" : 11, "C" : 12, "D" : 13, "E" : 14, "F" : 15}
    decimal_number = "0123456789"

    hex_in_list = list(hex_in)
    hex_in_list.reverse()
    n = 0
    total = 0
    while n < len(hex_in):
        if hex_in_list[n] in decimal_number:
            total += 16 ** n * int(hex_in_list[n])
        else:
            total += 16 ** n * decimal_alphabet[hex_in_list[n]]
        n += 1
    return total



if __name__ == "__main__":
    import doctest
    if doctest.testmod().failed == 0:
        print("\n*** ALL TESTS PASS. YOU'RE TERRIFIC!\n")
