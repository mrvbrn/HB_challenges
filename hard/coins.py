"""Calculate possible change from combinations of dimes and pennies.

Given an infinite supply of dimes and pennies, find the different
amounts of change can be created with exact `num_coins` coins?

For example, when num_coins = 3, you can create:

    3 = penny + penny + penny
   12 = dime + penny + penny
   21 = dime + dime + penny
   30 = dime + dime + dime

For example:

    >>> coins(0) == {0}
    True

    >>> coins(1) == {1, 10}
    True

    >>> coins(2) == {2, 11, 20}
    True

    >>> coins(3) == {3, 12, 21, 30}
    True

    >>> coins(4) == {4, 13, 22, 31, 40}
    True


Let's make sure it works when we can spend over 10 pennies::

    >>> coins(11) == {65, 101, 38, 74, 11, 110, 47, 83, 20, 56, 92, 29}
    True

"""



def coins(num_coins):
    """Find change from combinations of `num_coins` of dimes and pennies.

    This should return a set of the unique amounts of change possible.
    # """
    # if num_coins == 0:
    #     return {0}
    # if num_coins == 1:
    #     return {1, 10}
    # if num_coins == 2:
    #     return {2, 11, 20}
    # coins_list =[{1,10}, {2,11,20}] 
    # while len(coins_list) < num_coins:
    #     lst1 = list(coins_list[0])
    #     lst2 = list(coins_list[-1])
    #     lst3 = set()
    #     for char1 in lst1:
    #         for char2 in lst2:
    #             lst3.add(char1 + char2)
    #     coins_list.append(lst3)
    # return coins_list[-1]

    total = set()
    for ndimes in range(num_coins+1):
        npennies = num_coins - ndimes
        total.add(ndimes* 10 + npennies * 1)
    return total



if __name__ == '__main__':
    import doctest
    if doctest.testmod().failed == 0:
        print("\n*** ALL TESTS PASSED. YOU CAN TAKE THAT TO THE BANK!\n")
