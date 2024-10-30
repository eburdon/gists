"""
python3 -i french_deck.py

BY IMPLEMENTING SPECIAL TYPES, YOUR OBJECTS CAN BEHAVE LIKE
THE BUILT-IN TYPES.
* debug, logging - special str representation. __repr__
* emulating sequences

copied from https://github.com/fluentpython/example-code-2e/blob/master/01-data-model/frenchdeck.py
"""
import collections

Card = collections.namedtuple('Card', ['rank', 'suit'])

class FrenchDeck:
    ranks = [str(n) for n in range(2, 11)] + list('JQKA')
    suits = 'spades diamonds clubs hearts'.split()

    def __init__(self):
        self._cards = [Card(rank, suit) for suit in self.suits
                                        for rank in self.ranks]

    def __len__(self):
        """
        Without this special function...

        >>> len(deck)
        Traceback (most recent call last):
            File "<stdin>", line 1, in <module>
        TypeError: object of type 'FrenchDeck' has no len()

        have to do...
        len(deck._cards) which is private and not guaranteed
        to have non-breaking changes
        """
        return len(self._cards)

    def __getitem__(self, position):
        """
        Without this special function...

        >>> deck[3]
        Traceback (most recent call last):
            File "<stdin>", line 1, in <module>
        TypeError: 'FrenchDeck' object is not subscriptable

        >>> Card(rank='K', suit='hearts') in deck
        Traceback (most recent call last):
            File "<stdin>", line 1, in <module>
        TypeError: argument of type 'FrenchDeck' is not iterable
        """
        return self._cards[position]

########################
# deck = FrenchDeck()

# manual_deck = [Card(1, 'spades'), Card(5, 'diamonds'), Card(8, 'hearts'), Card(3, 'clubs')]

## same behavior
# len(deck)
# len(manual_deck)

# deck[3]
# manual_deck[3]
########################

suit_values = dict(spades=3, hearts=2, diamonds=1, clubs=0)

def spades_high(card):
    """
    By implementing __len__ and __get_item__
    our custom class acts like a sequence.
    via composition, can use all the python standard lib.
    these delegate the work to a list object, deck._cards
    """
    rank_value = FrenchDeck.ranks.index(card.rank)
    return rank_value * len(suit_values) + suit_values[card.suit]

# usage
# for card in sorted(deck, key=spades_high):
#   print(card)
# recall:
#   first arg: the sequence to sort
#   key: fn to decide order
#   reverse: bool