"""Find segments comprising >2 points.

Given a list of points in a 2d space, find segments that use 3+ of those
points. Return this as a list of segments, where each segment is a list
of the component points. (For clarity, sort the output).

There are no 3+ segments here::

    >>> (sameline([(0, 0), (1,1), (3,2), (4,3)]))
    []

There are two 3+ segments here::

    >>> (sameline([(0,0), (1,1), (2,3), (3,2), (3,3), (3,4)]))
    [[(0, 0), (1, 1), (3, 3)], [(3, 2), (3, 3), (3, 4)]]

These are the same input point, in a different order --- the output should
be exactly the same, though.

    >>> (sameline([(3,4), (3,3), (3,2), (2,3), (1,1), (0,0)]))
    [[(3, 4), (3, 3), (3, 2)], [(3, 3), (1, 1), (0, 0)]]

Other examples::

    >>> (sameline([(0,0), (3,4)]))
    []

    >>> (sameline([(0,0), (2,1), (2,0), (4,2), (2,2)]))
    [[(0, 0), (2, 1), (4, 2)], [(2, 1), (2, 0), (2, 2)]]

    >>> (sameline([(0., 0.), (1., 1.), (3., 4.), (2., 2.)]))
    [[(0.0, 0.0), (1.0, 1.0), (2.0, 2.0)]]

    >>> (sameline([(0,0), (3,4), (7, 21)]))
    []
"""

from collections import defaultdict
import itertools


def sameline(pts):
    """Find segments comprising >2 points."""

    out = []
    for p1, p2, p3 in itertools.combinations(pts, 3):
        x1, y1 = p1
        x2, y2 = p2
        x3, y3 = p3

        if (x1 - x3) * (y1 - y2) == (y1 - y3) * (x1 - x2):
            out.append([p1, p2, p3])
    return out


if __name__ == '__main__':
    import doctest

    if doctest.testmod().failed == 0:
        print("\n*** ALL TESTS PASSED. YOU'RE NOT OUT OF LINE!\n")
