"""Given a rof of length n and prices f rod of length i where 1<=i<=n  find the optimal way to
cut rods in order to maximize profit
"""


def rod_cut(price, n):
    if n == 0:
        return 0

    max_value = float('-inf')
    for i in range(1, n+1):
        cost = price[i-1]+rod_cut(price, n-i)

        if cost>max_value:
            max_value = cost
    return max_value

if __name__ == '__main__':

    price = [1,5,8,9,10,17,17,20]
    n = 4

    print("Profit is", rod_cut(price, n))