import sys
import requests

words_to_check = sys.argv[1:]

# This dictionary is a newline-separated list of words, in the format of:
# `Word/FLAGS`, where `FLAGS` describes possible permutations of that word, See
# https://cgit.freedesktop.org/libreoffice/dictionaries/tree/en/affDescription.txt
DICTIONARY_URL = "https://cgit.freedesktop.org/libreoffice/dictionaries/plain/en/en_US.dic"

response = requests.get(DICTIONARY_URL)
word_definitions = response.text.splitlines()

# The first line contains the number of words, which we don't need
word_definitions.pop(0)

# Compile your dictionary
words = []
for word_definition in word_definitions:   
    word = word_definition.split("/")[0]   

    if len(word_definition.split("/")) > 1:   
        flags = word_definition.split("/")[1]
    else:
        flags = ""

    words.append({"word": word, "flags": flags})


#Find each word that's in the dictionary
# for word in words:   
#     for index, word_to_check in enumerate(words_to_check):
#         if word["word"] == word_to_check:
#             print(f"{word_to_check} is a word")
#             words_to_check.pop(index)

# # Any words remaining must not be words
# for word_to_check in words_to_check:
#     print(f"{word_to_check} is not a word")



for word in words:   
    for index, word_to_check in enumerate(words_to_check):
        if (word["word"] == word_to_check):
            if (word_to_check[0] == word_to_check[0].lower()):
                print(f"{word_to_check} is a word")
                words_to_check.pop(index)
            else:
                print(f"{word_to_check} is not a word")
                words_to_check.pop(index)

# Any words remaining must not be words
for word_to_check in words_to_check:
    print(f"{word_to_check} is not a word")
    






