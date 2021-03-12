"""Given a binary string s and an integer k.

Return True if every binary code of length k is a substring of s. Otherwise, return False.

 

Example 1:

Input: s = "00110110", k = 2
Output: true
Explanation: The binary codes of length 2 are "00", "01", "10" and "11". They can be all found as substrings at indicies 0, 1, 3 and 2 respectively.
Example 2:

Input: s = "00110", k = 2
Output: true

"""
def hasAllCodes(s, k):
    res = set()
    for i in range(k, len(s)+1):
        res.add(s[i-k:i])
    return True if len(res) == 2**k else False