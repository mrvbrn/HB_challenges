"""Given already-sorted lists, `a` and `b`, return sorted list of both.

You may not use sorted() or .sort().

Check edge cases of empty lists:

    >>> sort_ab([], [])
    []

    >>> sort_ab([1, 2,3], [])
    [1, 2, 3]

    >>> sort_ab([], [1, 2, 3])
    [1, 2, 3]

Check:

    >>> sort_ab([1, 3, 5, 7], [2, 6, 8, 10])
    [1, 2, 3, 5, 6, 7, 8, 10]
"""


def sort_ab(a, b):
    """Given already-sorted lists, `a` and `b`, return sorted list of both.

    You may not use sorted() or .sort().
    """
    sorted_list = []
    i1 = 0
    i2 = 0
    while i1 < len(a) and i1 < len(b):
        if a[i1] < b[i2]:
            sorted_list.append(a[i1])
            i1 += 1
        else:
            sorted_list.append(b[i2])
            i2 += 1
    sorted_list.extend(a[i1:])
    sorted_list.extend(b[i2:])
    return sorted_list




if __name__ == '__main__':
    import doctest
    if doctest.testmod().failed == 0:
        print("\n*** ALL TESTS PASSED. YOU'RE A MERGE CHAMPION!!\n")
