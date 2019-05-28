"""Evaluate a poker hand.

A higher straight flush beats a lower one::

    >>> straight_flush1 = Hand("As Ks Qs Js 10s")
    >>> straight_flush2 = Hand("6s 5s 4s 3s  2s")

    >>> straight_flush1 > straight_flush2
    True

A higher 4-of-kind rank beats lower::

    >>> four_kind1 = Hand("6c 6d 6s 6h 2c")
    >>> four_kind2 = Hand("5s 5d 5s 5h Ah")

    >>> four_kind1 > four_kind2
    True

For full house, higher-of-triplet wins. If tied,
higher-of-pair wins::

    >>> full_house1 = Hand("3c 3d 3s 2h 2s")
    >>> full_house2 = Hand("2c 2d 2s Ah As")

    >>> full_house1 > full_house2
    True

For flush, higher ranks win::

    >>> flush1 = Hand("9s 8s 6s 4s 2s")
    >>> flush2 = Hand("9s 7s 6s 4s 2s")

    >>> flush1 > flush2
    True

for straight, higher ranks win::

    >>> straight1 = Hand("Ah Kc Qd Jc 10h")
    >>> straight2 = Hand("6s 5c 4c 3d  2h")

    >>> straight1 > straight2
    True

For straights, as a special case, A can be used as a low card,
coming below 2. In this case, a straight of A2345 loses to
23456::

    >>> straight3 = Hand("5c 4c 3d 2h Ah")

    >>> straight2 > straight3
    True

For three of kind, high triplet wins:

    >>> three1 = Hand("7s 7c 7d 2h 3d")
    >>> three2 = Hand("6s 6c 6d Ah 2d")

    >>> three1 > three2
    True

(Of course, for a tie, use remaining cards)

    >>> three3 = Hand("6s 6c 6d Qh Jd")

    >>> three2 > three3
    True

For two pair, use hi-pair, then lo-pair, then remaining::

    >>> two_pair1 = Hand("6s 6c 2h 2s 9d")
    >>> two_pair2 = Hand("5s 5c 4h 4s 9d")

    >>> two_pair1 > two_pair2
    True

For pair, use pair then remaining::

    >>> pair1 = Hand("6s 6c 2h 3s 9d")
    >>> pair2 = Hand("5s 5c 4h 6s 9d")

    >>> pair1 > pair2
    True

For no combos, use rank of cards::

    >>> none1 = Hand("As 7d 5c 4d 3h")
    >>> none2 = Hand("As 7d 5c 4d 2h")

    >>> none1 > none2
    True

Overall::

    >>> straight_flush1 > four_kind1
    True

    >>> four_kind1 > full_house1
    True

    >>> full_house1 > flush1
    True

    >>> flush1 > straight1
    True

    >>> straight1 > three1
    True

    >>> three1 > two_pair1
    True

    >>> two_pair1 > pair1
    True

    >>> pair1 > none1
    True

"""

RANK_NAME_TO_RANK = {
    "2": 2,
    "3": 3,
    "4": 4,
    "5": 5,
    "6": 6,
    "7": 7,
    "8": 8,
    "9": 9,
    "10": 10,
    "J": 11,
    "Q": 12,
    "K": 13,
    "A": 14,
}


class Card(object):
    """Playing card."""

    def __init__(self, name):
        """Create a card.

            rank: 2-10 or 11=J, 12=Q, 13=K, 14=A
            suit: h, d, c, s

        We create cards by name::

            >>> ks = Card("Ks")

            >>> ks.rank
            13
            >>> ks.suit
            's'
            >>> ks.name
            'Ks'

        Other examples::

            >>> ac = Card("Ac")
            >>> ac.rank
            14

            >>> td = Card("10d")
            >>> td.rank
            10
        """

        rank = name[0:-1]  # "10" is 2 chars
        suit = name[-1]

        assert rank in RANK_NAME_TO_RANK, "Bad rank: %s" % name
        assert suit in "hdcs", "Bad suit: %s" % name

        self.name = name
        self.rank = RANK_NAME_TO_RANK.get(rank)
        self.suit = suit

    def __str__(self):
        """Public print representation of a card."""

        return self.name

    def __repr__(self):
        """Debugging representation of a card."""

        return "<Card %s>" % self.name


class Hand(object):
    """Hand of poker cards."""

    def __init__(self, cards):
        """Add cards to hand.

            >>> h1 = Hand([Card("As"),
            ...            Card("Ks"),
            ...            Card("Qs"),
            ...            Card("Js"),
            ...            Card("10s")])

            >>> h1.cards
            [<Card As>, <Card Ks>, <Card Qs>, <Card Js>, <Card 10s>]

        As a convenience, you can list the card names instead and
        this will turn them into Card objects before adding them::

            >>> h2 = Hand("As Ks Qs Js 10s")

            >>> h2.cards
            [<Card As>, <Card Ks>, <Card Qs>, <Card Js>, <Card 10s>]
        """

        if type(cards) is str:
            cards = cards.split()

        self.cards = [c if type(c) is Card else Card(c) for c in cards]
            
        assert len(self.cards) == 5, "Hands must have 5 cards."

    def __repr__(self):
        """Display hand.

        To make testing easier, we'll sort hand before displaying it.
        There's no formal order for suits, so we'll just use
        alphabetical order for display purposes:

            >>> h2 = Hand("8d 7s 7h 7c 7d")
            >>> h2
            <Hand 8d 7c 7d 7h 7s>
        """

        hand = sorted(self.cards,
                      key=lambda c: (14 - c.rank, c.suit))

        return "<Hand %s>" % (" ".join(str(c) for c in hand))

    def eval(self):
        """Evaluate the value of a hand."""

    def __eq__(self, other):
        """Are these two hands equal?

            >>> h1 = Hand("2d 3d 4d 5d 6d")
            >>> h2 = Hand("6d 5d 4d 3d 2d")

            >>> h1 == h2
            True
        """

        return self.eval() == other.eval()

    def __ne__(self, other):
        """Are these two hands not equal?

            >>> h1 = Hand("2d 3d 4d 5d 6d")
            >>> h2 = Hand("6d 5d 4d 3d 2d")

            >>> h1 != h2
            False
        """

        return self.eval() != other.eval()

    def __lt__(self, other):
        """Is this hand lower-ranked than the other hand?

            >>> h1 = Hand("2d 3d 4d 5d 6d")
            >>> h2 = Hand("3d 4d 5d 6d 7d")

            >>> h1 < h2
            True
        """

        return self.eval() < other.eval()

    def __le__(self, other):
        """Is this hand lower-ranked than the other hand?

            >>> h1 = Hand("2d 3d 4d 5d 6d")
            >>> h2 = Hand("3d 4d 5d 6d 7d")

            >>> h1 <= h2
            True
        """

        return self.eval() <= other.eval()


if __name__ == '__main__':
    import doctest

    if doctest.testmod().failed == 0:
        print("\n*** ALL TESTS PASSED; WE CAN BET ON YOU!\n")

