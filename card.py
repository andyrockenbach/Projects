class Card(object):

    suit_names = ["Clubs", "Diamonds", "Hearts", "Spades"]
    rank_names = ["Ace", "Two", "Three", "Four", "Five", "Six", "Seven", 
              "Eight", "Nine", "Ten", "Jack", "Queen", "King"]

    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank

    def __str__(self):
        return "%s of %s" % (Card.rank_names[self.rank],
                             Card.suit_names[self.suit])

    def get_value(self):
    	if self.rank is 10:
            return 10
        elif self.rank is 11:
            return 10
        elif self.rank is 12:
            return 10
        elif self.rank is 0:
            return 11
        else:
            num = self.rank + 1
            return num
