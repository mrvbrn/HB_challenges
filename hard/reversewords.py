"""Reverse word order, keeping spaces.

As a simple case, an empty string returns an empty string:

    >>> rev("")
    ''

A simple word is also the same:

    >>> rev("hello")
    'hello'

Here, we reverse the order of the words, preserving the space between:

    >>> rev("hello world")
    'world hello'

Here, we reverse the worlds, preserving space---so it it should start with
the 3 spaces that came after world, etc:

    >>> rev(" hello  world   ")
    '   world  hello '

To prove the alternate solution works:

    >>> rev2(" hello  world   ")
    '   world  hello '

"""


def rev(s):
    """Reverse word-order in string, preserving spaces."""
    words = s.split(" ")
    words.reverse()
   
    return " ".join(words)
def rev2(s):
    """Reverse word-order in string, preserving spaces."""
    words = s.split(" ")
    words.reverse()
    return " ".join(words)


if __name__ == '__main__':
    import doctest
    if doctest.testmod().failed == 0:
        print("\n*** ALL TESTS PASSED; NICE JOB! ***\n")
