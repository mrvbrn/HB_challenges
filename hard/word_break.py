"""Parse an unbroken sentence into possible words.

Example:

    >>> sentences = parse('iatenoodlesfordinnertonight', vocab)

    >>> for s in sorted(sentences):
    ...    print(s)
    i a ten oodles for dinner to night
    i a ten oodles for dinner tonight
    i a ten oodles ford inner to night
    i a ten oodles ford inner tonight
    i ate noodles for dinner to night
    i ate noodles for dinner tonight
    i ate noodles ford inner to night
    i ate noodles ford inner tonight

"""

vocab = {'i', 'a', 'ten', 'oodles', 'ford', 'inner', 'to', 'night',
         'ate', 'noodles', 'for', 'dinner', 'tonight'}


def parse(phrase, vocab):
    """Break a string into words.

    Input:
        - string of words without space breaks
        - vocabulary (set of allowed words)

    Output:
        set of all possible ways to break this down, given a vocab
    """
    possible_breaks = set()
    for word in vocab:
        if word == phrase:
            possible_breaks.add(word)

        elif phrase.startswith(word):
            rest = phrase[len(word):]
            word_and_rest = {word + " " + parsed
                             for parsed in parse(rest, vocab)}
            possible_breaks.update(word_and_rest)
    return possible_breaks


if __name__ == '__main__':
    import doctest

    if doctest.testmod().failed == 0:
        print("\n*** ALL TESTS PASSED; GREAT JOB! ***\n")

