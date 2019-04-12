import random


def find_lucky(n):
    nums = list(range(1,11))
    lucky_nums = []
    for i in range(n):
        num = random.choice(nums)
        nums.remove(num)
        lucky_nums.append(num)
    return lucky_nums


def find_range(llist):
    if len(llist) == 0:
        return(None, None)
    elif len(llist) == 1:
        return (llist[0], llist[0])
    else:
        max_num = llist[0]
        for i1 in llist[1:]:
            if i1 > max_num:
                max_num = i1
        min_num = llist[0]
        for i2 in llist[1:]:
            if i2 < min_num:
                min_num = i2
        return (min_num, max_num)

def fizzbuzz():
    for i in range(1,20):
        if i % 3 == 0:
            print('fizz')
        elif i % 5 == 0:
            print('buzz')
        elif i % 3 == 0 and i % 5 == 0:
            print('fizzbuzz')
        else:
            print(i)

def has_more_vowels(word):
    vowels = "aeiou"
    count_vowel = 0
    count_non_vowel = 0
    for letter in word:
        if letter.lower() in vowels:
            count_vowel += 1
        else:
            count_non_vowel += 1
    return count_vowel > count_non_vowel

def concat_lists(list1, list2):
    for i in list2:
        list1.append(i)
    return list1

def has_unique_chars(word):
    return len(word) == len(set(word))

def is_prime(num):
    if num < 2:
        return False
    for i in range(2, num):
        if num % i == 0:
            return False
    return True

def is_palindrome(word):
    # reverse_word = ""
    # i = len(word) - 1
    # while i >= 0:
    #     reverse_word += word[i]
    #     i -= 1
    # return word == reverse_word

    for i in range(len(word)// 2):
        if word[i] != word [-i - 1]:
            return False
    return True


def find_largest_smaller_than(nums, xnumber):
    if nums[0] > xnumber:
        return None
    if nums[-1] < xnumber:
        return len(nums) - 1
    for i, num in enumerate(nums):
        if num >= xnumber:
            return i - 1

def find_largest_smaller_than_bisect(nums, xnumber):
    from bisect import bisect_left
    if nums[0] > xnumber:
        return None
    position = bisect_left(nums, xnumber)
    return position - 1

def dec2bin(num):
    if num == 0:
        return 0
    lst = []
    while num > 0:
        lst.append(str(num % 2))
        num //= 2
    return "".join(reversed(lst))

def translate_leet(phrase):
    leet_dict = {'a':'@', 'o':'0', 'e':'3', 'l':'1', 's':'5', 't':'7'}
    new_phrase = ""
    for letter in phrase:
        if letter.lower() in leet_dict.keys():
            new_phrase += leet_dict[letter.lower()]
        else:
            new_phrase += letter
    return new_phrase

def find_longest_word(words):
    longest = len(words[0])
    for word in words:
        if len(word) > longest:
            longest = len(word)
    return longest

def max_num(num_list):
    max_num = num_list[0]
    for num in num_list:
        if num > max_num:
            max_num = num
    return max_num

def max_of_three(num1, num2, num3):
    if num1 >= num2 and num1>=num3:
        return num1
    elif num2 >= num1 and num2>= num3:
        return num2
    elif num3 >= num2 and num3 >= num1:
        return num3

def is_pangram(sentence):
    alphabet = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
    for letter in sentence:
        if letter.lower() in alphabet:
            alphabet.remove(letter.lower())
    return len(alphabet) == 0


def pig_latin(phrase):
    vowels = ['a', 'e', 'i', 'o', 'u']
    words = phrase.split(" ")
    new_phrase = []
    for word in words:
        if word[0].lower() in vowels:
            new_phrase.append(word + "yay")
        else:
            new_phrase.append(word[1:] + word[0].lower() + "ay")
    return " ".join(new_phrase)


# def deduped(items):
#     new_items = []
#     for item in items:
#         if item not in new_items:
#             new_items.append(item)
#     return new_items


"""optimeze solution"""

def deduped(items):
    seen = set()
    result = []
    for item in items:
        if item not in seen:
            result.append(item)
            seen.add(item)
    return result

def replace_vowels(chars):
    vowels = ['a', 'e', 'i', 'o', 'u']
    result = []
    for char in chars:
        if char.lower() in vowels:
            result.append("*")
        else:
            result.append(char)
    return result










