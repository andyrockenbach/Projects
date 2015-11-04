from card import Card

class Hand(object):
    
    def __init__(self):
        self.cards = []
        self.total = 0
        self.soft = False

    def __str__(self):
        res = []
        for card in self.cards:
            res.append(str(card))
        return '\n'.join(res)

    def add_card(self, card):
        self.cards.append(card)
        if card.rank is not 0:
            self.total += card.get_value()
            if self.soft:
                if self.total > 21:
                    self.soft = False
                    self.total -= 10
        else:
            if self.soft is False:
                self.soft = True
                self.total += 11
                if self.total > 21:
                    self.soft = False
                    self.total -= 10
            else:
                self.total += 1

    def is_blackjack(self):
        if len(self.cards) is 2 and self.total is 21:
            return True
        else:
            return False

    def is_busted(self):
        if self.total > 21:
            return True
        else:
            return False

    def is_dealer_blackjack(self):
        if self.total is 21 and self.cards[0].get_value() is 10:
            return True
        else:
            return False

    def is_pair(self):
        if len(self.cards) is 2:
            if self.cards[0].rank is self.cards[1].rank:
                return True
        else:
            return False

    def is_soft(self):
        return self.soft

    def split(self):
        hand = Hand()
        card = self.cards.pop(-1)
        hand.add_card(card)
        if card.rank is not 0:
            self.total -= card.get_value()
        else:
            self.total -= 1
        return hand
