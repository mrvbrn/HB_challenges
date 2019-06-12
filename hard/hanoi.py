"""Tower of Hanoi."""


class Stack(object):
    """Stack.

    Enforce Hanoi rules -- only a smaller disk can be put on a bigger disk.

    >>> s = Stack([3, 2, 1])
    """

    def __init__(self, items=None):
        """Create stack.

        >>> s = Stack()

        >>> s = Stack([3, 2, 1])

        >>> s = Stack([1, 2, 3])
        Traceback (most recent call last):
        ...
        AssertionError: Illegal initial value
        """

        # Ensure initial set up is legal
        if items:
            assert sorted(items, reverse=True) == list(items), "Illegal initial value"
            self.items = list(items)
        else:
            self.items = []

    def push(self, item):
        """Push disk onto stack.

        >>> s = Stack()
        >>> s.push(3)
        >>> s.push(2)
        >>> s.push(4)
        Traceback (most recent call last):
        ...
        AssertionError: Illegal play
        """

        assert not self.items or self.items[-1] > item, "Illegal play"
        self.items.append(item)

    def pop(self):
        """Pop items off stack.

        >>> s = Stack()
        >>> s.push(2)
        >>> s.push(1)
        >>> s.pop()
        1
        >>> s.pop()
        2
        >>> s.pop()
        Traceback (most recent call last):
        ...
        IndexError: pop from empty list
        """

        return self.items.pop()

    def is_empty(self):
        """Is stack empty?

        >>> s = Stack()
        >>> s.is_empty()
        True

        >>> s.push(1)
        >>> s.is_empty()
        False

        >>> s.pop()
        1
        >>> s.is_empty()
        True
        """

        return not self.items

    def __repr__(self):
        return repr(self.items)


def move(n, source, helper, target):
    """Move disks from one stack to another.

    Move `n` disks from `source` to `target`, using the
    middle stack, `helper`, as a temporary place.
    Movements must follow Hanoi rules.

    For example, it's easy to move one::

        >>> s1 = Stack([1])
        >>> s2 = Stack()
        >>> s3 = Stack()
        >>> move(1, s1, s2, s3)
        >>> s1, s2, s3
        ([], [], [1])

    Moving three::

        >>> s1 = Stack([3, 2, 1])
        >>> s2 = Stack()
        >>> s3 = Stack()
        >>> move(3, s1, s2, s3)
        >>> print((s1, s2, s3))
        ([], [], [3, 2, 1])
    """
    if n > 0:
        move(n-1, source, target, helper)
        target.push(source.pop())
        move(n-1, helper, source, target)



def hanoi(num_disks):
    """Create tower `num_disks` high and move move disks.

    Returns tuple of the three stacks, showing the disks on each stack,
    from lowest-to-highest.

    For example, with no disks:

        >>> hanoi(0)
        ([], [], [])

    With one disk:

        >>> hanoi(1)
        ([], [], [1])

    With two disks:

        >>> hanoi(2)
        ([], [], [2, 1])

    With three disks:

        >>> hanoi(3)
        ([], [], [3, 2, 1])

    With nine disks:

        >>> hanoi(9)
        ([], [], [9, 8, 7, 6, 5, 4, 3, 2, 1])
    """

    # Make stacks -- the first will have all the disks on them
    one = Stack(list(range(num_disks, 0, -1)))
    two = Stack()
    three = Stack()

    # Move them
    move(num_disks, one, two, three)

    # Return tuple of stacks
    return one, two, three


if __name__ == "__main__":
    import doctest
    if doctest.testmod().failed == 0:
        print("\n*** ALL TESTS PASSED. NICE STACKING!\n")

