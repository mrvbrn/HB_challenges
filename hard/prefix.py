"""Example code for modeling tries, and searching them by prefix.

Joel Burton <joel@joelburton.com>
"""


class LetterStack(object):
    """Simple letter-based stack based on a list, useful for tries.

    Stacks can be built using a linked list or an array; we'll just
    use the built-in Python list-type (array) for this.

        >>> s = LetterStack()
        >>> s.is_empty()
        True

    As a convenience, we can pass in a string during instantiation,
    and it seeds the stack with those letters:

        >>> s = LetterStack("ab")
        >>> s.is_empty()
        False

    We can push and pop things off:

        >>> s.push("c")
        >>> s.push("d")
        >>> s.pop()
        'd'

    As a convenience, it will construct a word of the letters of the
    current stack, from the top:

        >>> s.as_word()
        'abc'
    """

    def __init__(self, initial=""):
        """Create a stack.

        If initial is given, add each letter to the stack.
        """

        self._stack = list(initial)

    def push(self, letter):
        """Add letter to stack.

            >>> s = LetterStack()
            >>> s.push('a')

        Let's make sure it's there:

            >>> s.peek()
            'a'
        """

        self._stack.append(letter)

    def pop(self):
        """Remove & return last letter on stack.

            >>> s = LetterStack('ab')
            >>> s.pop()
            'b'
            >>> s.pop()
            'a'
        """

        return self._stack.pop()

    def peek(self):
        """Examine most-recent pushed letter.

            >>> s = LetterStack('ab')
            >>> s.peek()
            'b'

        This does not change the stack--so we can peek as much as we want:

            >>> s.peek()
            'b'

        Of course, when we pull things off, we'll see the new top:

            >>> s.pop()  # remove it!
            'b'
            >>> s.peek()
            'a'
        """

        return self._stack[-1]

    def is_empty(self):
        """Return True/False for if stack is empty.

            >>> s = LetterStack()
            >>> s.is_empty()
            True

            >>> s.push('a')
            >>> s.is_empty()
            False
        """

        return not self._stack

    def as_word(self):
        """Return stack contents as a word. Does NOT change the stack.

        >>> s = LetterStack('abc')
        >>> s.as_word()
        'abc'

        >>> s.push('d')
        >>> s.as_word()
        'abcd'
        """

        return "".join(self._stack)


class TrieNode(object):
    """Node in a trie.

    Trie nodes are normal tree nodes -- except they have a method to construct
    all words below themselves. To do so, they look for special COMPLETE_WORD
    nodes.
    """

    # This is just some marker element for "this is the end of a valid word".
    #
    # We don't care what it really *is* -- we just need it to have a unique
    # identity so we can say things like "if some_node is COMPLETE_WORD".
    # So, we'll make an instance of object() -- this is a pretty useless thing
    # to have, but it *will* have a unique identity, so we can use it for
    # comparisons. This is a pretty common Python idiom (some other people
    # would make it an instance of an empty dictionary or empty list --
    # just because those will have unique identities, too -- but that can
    # seem a little less obvious, since empty-lists and empty-dictionaries
    # tend to be used more in code for useful things.)
    #
    # Some people call these kind of markers a "nonce".

    COMPLETE_WORD = object()

    def __init__(self, letter, children=None):
        """Construct a node from a letter and, optionally, a list of child nodes."""\

        self.data = letter
        self.children = children or []

    def find_child_words(self):
        """Given a find all child words below this node.

        For a node without children, this returns nothing:

            >>> n = TrieNode('z')
            >>> n.find_child_words()
            []

        For a node with a child word, return it:

            >>> n = TrieNode('t', [TrieNode.COMPLETE_WORD])
            >>> n.find_child_words()
            ['']

        For a node with a bunch of child words, return in DFS-order:

                   a
               /---\
              c     d
             / \    |
            e   t   *
            |   |
            *   *

            >>> n = TrieNode('a', [TrieNode('c',
            ...                     [TrieNode('e', [TrieNode.COMPLETE_WORD]),
            ...                      TrieNode('t', [TrieNode.COMPLETE_WORD])]),
            ...                    TrieNode('d', [TrieNode.COMPLETE_WORD])])
            >>> n.find_child_words()
            ['ce', 'ct', 'd']

        """

        def _find_child_words(node, words, word):

            if node is TrieNode.COMPLETE_WORD:
                words.append(word.as_word())
                return

            word.push(node.data)

            # Add letters to stack
            for n in node.children:
                _find_child_words(n, words, word)

            # Before we return, pull last letter off stack
            if not word.is_empty():
                word.pop()

        found_words = []

        for start_n in self.children:
            _find_child_words(start_n, found_words, LetterStack())

        return found_words


class Trie(object):
    """A trie is a tree where each node is a letter.

    They're often used to construct word trees, as might be used
    to find all words starting with a particular prefix.

    A path that creates a valid word, like "a"->"c"->"t" will end with a
    COMPLETE_WORD node in the children of "t", to show that it is valid.
    A path that, by itself, is not a valid word will not (so there will
    be no such marker in the list of children of "c", as "ac" is not a word).

    For example:

              a                   b
        /-----|-----\            / \
       *      c      t          a   e
             / \    / \        /   / \
            e   t  *   e      t   *   t
            |   |      |      |       |
            *   *      *      *       *

    (where * is the "end-of-valid-word" node marker).

    This is a trie of "a", "ace", "act", "ate", "bat", "be", "bet".
    Note that "b" "ac" and "ba" are not words -- there are no end-of-word nodes
    that follow these directly.
    """

    def __init__(self, words):
        """Make a trie out of words.

            >>> trie = Trie(["a", "ace", "act", "ate", "bat", "be", "bet"])

            >>> trie.root.find_child_words()
            ['a', 'ace', 'act', 'ate', 'bat', 'be', 'bet']
        """

        self.root = TrieNode(None)

        for word in words:
            self.add(word)

    def add(self, word):
        """Add word to trie.

        Adds word to trie. This creates whatever nodes are needed so there
        is a path of letters from the root for this word. It adds a
        complete-word marker as a child of the last letter, so it's marked
        as a word.


        We'll add an test the word 'at', which should add the following to
        our trie:

         a
         |
         t
         |
         *

            >>> t = Trie('')
            >>> t.add('at')
            >>> len(t.root.children)
            1
            >>> t.root.children[0].data
            'a'
            >>> len(t.root.children[0].children)
            1
            >>> t.root.children[0].children[0].data
            't'
            >>> len(t.root.children[0].children[0].children)
            1
            >>> t.root.children[0].children[0].children[0] is TrieNode.COMPLETE_WORD
            True

        If the word is already in our trie, adding it again has no effect:

            >>> t.add('at')
            >>> len(t.root.children)
            1
            >>> len(t.root.children[0].children)
            1
            >>> len(t.root.children[0].children[0].children)
            1
        """

        node = self.root

        for letter in word:
            found = False
            for child in node.children:
                if child is not TrieNode.COMPLETE_WORD and child.data == letter:
                    found = child
                    break
            if not found:
                found = TrieNode(letter)
                node.children.append(found)

            node = found

        if TrieNode.COMPLETE_WORD not in node.children:
            # If this word wasn't already in our trie, make sure it's marked
            # as a complete word.
            node.children.append(TrieNode.COMPLETE_WORD)

    def find_prefix_words(self, prefix):
        """Find words with a prefix.

        :prefix: string of prefix

        - Navigates through the trie for each letter in the prefix
        - Returns a list of each word that uses this prefix, making sure
          to append the prefix to the returned list of words.

              a                   b
        /-----|-----\            / \
       *      c      t          a   e
             / \    / \        /   / \
            e   t  *   e      t   *   t
            |   |      |      |       |
            *   *      *      *       *

            >>> trie = Trie(["a", "ace", "act", "ate", "bat", "be", "bet"])

        If we provide an empty string for the prefix, this returns
        all child words of the entire trie:

            >>> trie.find_prefix_words('')
            ['a', 'ace', 'act', 'ate', 'bat', 'be', 'bet']

        Otherwise, it navigates to the end of that prefix, and finds
        all child words:

            >>> trie.find_prefix_words('a')
            ['a', 'ace', 'act', 'ate']

            >>> trie.find_prefix_words('ac')
            ['ace', 'act']

            >>> trie.find_prefix_words('ace')
            ['ace']

        (note that they must be valid words; 'ac' does not appear, as it is
        not a word -- there's no complete-marker in the children of 'a'->'c')

        If the prefix can't be found, it returns no found words:

            >>> trie.find_prefix_words('z')
            []

        Let's add a node with *no* children:

            >>> trie.root.children.append(TrieNode('z'))

        That's not very helpful -- this isn't a complete word, and it has no
        other children. Some people might even say our trie is no longer valid.
        Let's make sure this doesn't break things, though -- it should
        truthfully return no-words-with-that-prefix still:

            >>> trie.find_prefix_words('z')
            []
        """

        # Find prefix

        # Get list of suffixes from this point downward. This doesn't
        # include the prefix itself -- so four our sample trie, above,
        # 'ac' -> [e', 't']

        # Return list of words, joining the prefix to each suffix


if __name__ == '__main__':
    import doctest
    if doctest.testmod().failed == 0:
        print("\n*** ALL TESTS PASSED! YOU'RE A TRIE-MASTER!\n")
