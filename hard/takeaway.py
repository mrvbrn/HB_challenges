"""Takeaway game.

    >>> can_win(1)
    False

    >>> can_win(2)
    True

    >>> can_win(3)
    True

    >>> can_win(4)
    True

    >>> can_win(5)
    True

    >>> can_win(6)
    True

    >>> can_win(7)
    False

    >>> can_win(8)
    False

    >>> can_win(9)
    True

    >>> can_win(10)
    True
"""


def can_win(n):
    """Can this player win takeaway?"""
    if n < 2:
        return False

    for move in [2,3,5]:
        if not can_win(n - move):
            return True
    return False
   
       



if __name__ == '__main__':
    import doctest

    if doctest.testmod().failed == 0:
        print("\n*** ALL TESTS PASSED; NICE JOB!\n")
