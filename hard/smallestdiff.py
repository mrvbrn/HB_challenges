"""Given two lists, find the smallest difference between any two nums.

For example, given the lists:

  {10, 20, 14, 16, 18}
  {30, 23, 54, 33, 96}

The result would be 3, since 23 - 20 = 3 is the smallest difference of
any pair of numbers in those lists.

IMPORTANT: you must solve this with an algorithm that is faster than
O(ab)---that is, you cannot compare each item of list a against
each item of list b (that would be O(ab) time).

Joel Burton <joel@joelburton.com>.

Adapted from a problem in `Cracking the Coding Interview, 6th Edition`.
Gayle Laakmann McDowell, Career Cup (Palo Alto, CA). 2015.
"""


def smallest_diff(a, b):
    """Return smallest diff between all items in a and b.

        >>> smallest_diff([10, 20, 30, 40], [15, 25, 33, 45])
        3
    """

    a.sort()
    b.sort()

    ia = 0
    ib = 0
    best = None
    while ia < len(a) and ib < len(b):
        diff = abs(a[ia] - b[ib])

        if diff == 0:
            return 0
        if best is None or best > diff:
            best = diff

        if a[ia] > b[ib]:
            ib += 1
        else:
            ia+=1
    return best





if __name__ == '__main__':
    import doctest
    if doctest.testmod().failed == 0:
        print("\n*** ALL TESTS PASSED. NICE WORK!\n")
