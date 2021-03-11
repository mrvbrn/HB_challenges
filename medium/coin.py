"""
You are given coins of different denominations and a total amount of money amount. 
Write a function to compute the fewest number of coins that you need to make up that amount.
 If that amount of money cannot be made up by any combination of the coins, return -1.

You may assume that you have an infinite number of each kind of coin.

Input: coins = [1,2,5], amount = 11
Output: 3
Explanation: 11 = 5 + 5 + 1

Input: coins = [2], amount = 3
Output: -1

"""




def coinChange(coins: List[int], amount):
    if amount == 0:
        return 0
    elif min(coins)>amount:
        return -1
    else:
        coins.sort()
        answer = self.helper(amount, coins, {})
        if answer != float('inf'):
            return answer
        else:
            return -1
def helper(amount, coins, memo):
    if amount == 0:
        return 0
    elif amount in memo:
        return memo[amount]
    memo[amount] = float('inf')
    for coin in coins:
        if amount-coin>=0:
            memo[amount] = min(memo[amount], (self.helper(amount-coin, coins, memo)+1))
    return memo[amount]
        