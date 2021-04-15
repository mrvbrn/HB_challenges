"""
Given two strings s1 and s2, write a function to return true if s2 contains the permutation of s1. In other words, one of the first string's permutations is the substring of the second string.


Example 1:

Input: s1 = "ab" s2 = "eidbaooo"
Output: True
Explanation: s2 contains one permutation of s1 ("ba").


Example 2:

Input:s1= "ab" s2 = "eidboaoo"
Output: False
"""

def checkInclusion(s1, s2):
    d1 = collections.Counter(s1)
    d2 = collections.Counter(s2[:len(s1)])
    print(d2)
    for i in range(len(s2)-len(s1)):
        if d1 == d2:
            return True
        c = s2[i+len(s1)]
        print(c)
        if c in d2:
            d2[c]+=1
        else:
            d2[c]=1
        d2[s2[i]]-=1
        if d2[s2[i]] == 0:
            del d2[s2[i]]
    if d1 == d2:
        return True
    return False