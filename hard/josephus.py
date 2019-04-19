"""Given num_people in circle, kill [kill_every]th person, return survivor.

    >>> find_survivor(4, 2)
    1

    >>> find_survivor(41, 3)
    31

As a sanity case, if never skip anyone, the last person will be our survivor:

    >>> find_survivor(10, 1)
    10

"""


def find_survivor(num_people, kill_every):
    """Given num_people in circle, kill [kill_every]th person, return survivor."""
    num_people_list = []
    for i in range(1, num_people+1):
        num_people_list.append(i)

    kill_every -= 1
    idx = kill_every
    while len(num_people_list) > 1:
        num_people_list.pop(idx)
        idx = (idx + kill_every) % len(num_people_list)
    return num_people_list[0]

 




if __name__ == '__main__':
    import doctest
    if doctest.testmod().failed == 0:
        print("\n*** ALL TEST PASSED. W00T!\n")
