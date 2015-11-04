from card import Card
import random

class Shoe(object):

    def __init__(self, num):
        self.cards = []
        for decks in range(num):
            for suit in range(4):
                for rank in range(0, 13):
                    card = Card(suit, rank)
                    self.cards.append(card)
        random.shuffle(self.cards)

    def get_next_card(self, i=-1):
        return self.cards.pop(i)
