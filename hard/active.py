"""Find window of time when most authors were active.

For example::

    >>> data = [
    ...    ('Alice', 1901, 1950),
    ...    ('Bob',   1920, 1960),
    ...    ('Carol', 1908, 1945),
    ...    ('Dave',  1951, 1960),
    ... ]

    >>> most_active(data)
    (1920, 1945)

(Alice, Bob, and Carol were all active then).

If there's more than one period, find the earliest::

    >>> data = [
    ...    ('Alice', 1901, 1950),
    ...    ('Bob',   1920, 1960),
    ...    ('Carol', 1908, 1945),
    ...    ('Dave',  1951, 1960),
    ...    ('Eve',   1955, 1985),
    ... ]

    >>> most_active(data)
    (1920, 1945)

(Alice, Bob, Carol were active 1920-1945. Bob, Dave, and Eve were active 1951-1960.
Since there's a tie, the first was returned)
"""


def most_active(bio_data):
    """Find window of time when most authors were active."""
    # finish_date1 = []
    # start_date1 = []
    # for bio in bio_data:
    #     finish_date1.append(bio[-1])
    #     start_date1.append(bio[-2])
    # min_finish = min(finish_date1)
    # start_date2 = []
    # for date in start_date1:
    #     if date < min_finish:
    #         start_date2.append(date)
    # max_start= max(start_date2)
    # return (max_start, min_finish)


    century = [0] * 100
    for name, start, end in bio_data:
        for year in range(start, end+1):
            century[year - 1900] += 1

    best = 0
    in_best = True
    start = 0
    end = 100

    for year, num_activate in enumerate(century):
        if num_activate > best:
            best = num_activate
            in_best = True
            start = year
        elif num_activate < best and in_best:
            end = year - 1
            in_best = False

    return start + 1900, end + 1900


if __name__ == '__main__':
    import doctest
    if doctest.testmod().failed == 0:
        print("\n*** ALL TESTS PASSED. YAY!\n")