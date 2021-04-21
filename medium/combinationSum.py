"""
Given an array of distinct integers nums and a target integer target, return the number of possible combinations that add up to target.

The answer is guaranteed to fit in a 32-bit integer.

 

Example 1:

Input: nums = [1,2,3], target = 4
Output: 7
Explanation:
The possible combination ways are:
(1, 1, 1, 1)
(1, 1, 2)
(1, 2, 1)
(1, 3)
(2, 1, 1)
(2, 2)
(3, 1)
Note that different sequences are counted as different combinations.
Example 2:

Input: nums = [9], target = 3
Output: 0

"""

#recursive solution

def combinationSum4(nums, target):

    memo = {}
    def dfs(wanted):
        if wanted == 0:
            return 1
        elif wanted<0:
            return 0
        if wanted in memo:
            return memo[wanted]

        result = 0
        for num in nums:
            result += dfs(wanted-num)
        memo[wanted] = result
        return result
    return dfs(target)