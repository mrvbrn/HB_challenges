"""Merge sort.

    >>> nums = [3, 5, 10, 2, 1, 9, 7, 6, 4, 8]
    >>> merge_sort(nums)
    >>> nums
    [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

"""


def merge_sort(lst):
    """Divide and conquer: reduce to lists of 0-1 items, then recombine."""


    if len(lst) < 2:
        return lst
    mid = int(len(lst) / 2)
    lst1 = merge_sort(lst[:mid])
    lst2 = merge_sort(lst[mid:])

    return make_merge(lst1, lst2)

def make_merge(lst1, lst2):
    result_list = []
    while len(lst1) > 0 or len(lst2) > 0:
        if lst1 == []:
            result_list.append(lst2.pop(0))
        elif lst2== []:
            result_list.append(lst1.pop(0))
        elif lst1[0] > lst2[0]:
            result_list.append(lst2.pop(0))
        else:
            result_list.append(lst1.pop(0))
    return result_list




if __name__ == '__main__':
    import doctest
    if doctest.testmod().failed == 0:
        print("\n*** ALL TESTS PASSED. AWESOME WORK!\n")
