"""Pivot linked list around a value.

Given a singly linked list and a data value, rearrange linked list so that
all items with data less than value are at the start and all items greater
than or equal to the value are at the end.

For example:

    >>> ll = LinkedList([7, 6, 2, 3, 9, 1, 1])

    >>> ll.pivot(5)

    >>> ll.print_list()
    2 3 1 1 7 6 9 

If the given pivot value is in the list, it should appear in the second
half (with other greater-than-or-equal-to values):

    >>> ll = LinkedList([7, 6, 2, 5, 3, 5, 9, 1, 1])

    >>> ll.pivot(5)

    >>> ll.print_list()
    2 3 1 1 7 6 5 5 9 

"""


class Node(object):
    """Node in a linked list."""

    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList(object):
    """Singly-Linked list."""

    def __init__(self, values=None):
        """Set up list with optional starting data."""

        self.head = None
        self.tail = None

        if values:
            for value in values:
                self.add_data(value)

    def add_data(self, value):
        """Add node with given data.

            >>> ll = LinkedList()
            >>> ll.add_data(2)
            >>> ll.add_data(1)
            >>> ll.print_list()
            2 1 
        """

        node = Node(value)
        self.add_node(node)

    def add_node(self, node):
        """Add node.

            >>> ll = LinkedList()
            >>> ll.add_node(Node(2))
            >>> ll.add_node(Node(1))
            >>> ll.print_list()
            2 1 
            >>> ll.tail.data
            1
        """

        if self.head is None:
            self.head = node

        else:
            curr = self.head
            while curr.next:
                curr = curr.next

            curr.next = node

        self.tail = node

    def print_list(self):
        """Print list as space-separated data."""

        curr = self.head

        while curr:
            print(curr.data, end=' ')
            curr = curr.next

        print()

    def pivot(self, pivot):
        """Pivot list around value."""

        right = LinkedList()
        left = LinkedList()

        current = self.head
        while current:
            follow = current.next
            current.next = None
            if current.data < pivot:
                right.add_node(current)
            elif current.data >= pivot:
                left.add_node(current)
            current = follow

        right.tail.next = left.head
        left.tail.next = None

        self.head = right.head
        self.tail = left.tail



