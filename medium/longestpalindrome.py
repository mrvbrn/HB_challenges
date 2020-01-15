""" given a string s, your task is to find this longest possible palindrome

>>> maximalpalindrome("aaabb")
"ababa"

>>>maximalpalindrome("aaabbbcc")
"abcacba"



"""
# def maximalpalindrome(s):





def comb(data):
    if len(data) <= 1:
        return [data]
    res = []
    for i, c in enumerate(data):
        for r in comb(data[:i]+data[i+1:]):
            res.append([c]+r)
           
    return res

