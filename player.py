class Player(object):

    def __init__(self):
        self.bankroll = 5000
        self.count_strategy = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        self.min_bet = 25
        self.max_bet = 400
        self.current_bet = 25
        self.bet_inc = 2
        self.count = 0
        self.count_to_increase_bet = 2
        self.insurance = False
        self.splits = 0
        self.doubles = 0
        self.blackjacks = 0

    def decision(self, hand, dealer_showing):
        if hand.is_pair():
            if hand.cards[0].rank is 1 and dealer_showing in range(4,8):
                return "split"
            elif hand.cards[0].rank is 2 and dealer_showing in range(4, 8):
                return "split"
            elif hand.cards[0].rank is 5 and dealer_showing in range(3, 7):
                return "split"
            elif hand.cards[0].rank is 6 and dealer_showing < 8:
                return "split"
            elif hand.cards[0].rank is 0 or hand.cards[0].rank is 8:
                return "split"
        if hand.is_soft():
            if (hand.total < 15 and dealer_showing in range(5, 7)) or (hand.total < 17 and dealer_showing in range(4, 7)) or (hand.total < 19 and dealer_showing in range(3, 7)):
                if len(hand.cards) is 2:
                    return "double"
                else:
                    return "hit"
            elif hand.total < 18:
                return "hit"
            else:
                return "stay"
        elif (hand.total is 9 and dealer_showing in range(3, 7)) or (hand.total is 10 and dealer_showing < 10) or hand.total is 11:
            if len(hand.cards) is 2:
                return "double"
            else:
                return "hit"
        elif hand.total < 12:
            return "hit"
        elif dealer_showing > 6 and hand.total < 17:
            return "hit"
        elif dealer_showing < 4 and hand.total is 12:
            return "hit"
        else:
            return "stay"

    def make_bet(self, decks_left):
        true_count = self.count / decks_left
        if self.bankroll > 0:
            if int(true_count) > self.count_to_increase_bet:
                if self.current_bet < self.max_bet:
                    bet = self.current_bet * self.bet_inc
                    self.current_bet = bet
                    if self.current_bet < self.bankroll:
                        self.bankroll -= self.current_bet
                        return self.current_bet
                    else:
                        self.current_bet = self.bankroll
                        self.bankroll = 0
                        return self.current_bet
                else:
                    if self.current_bet < self.bankroll:
                        self.bankroll -= self.current_bet
                        return self.current_bet
                    else:
                        self.current_bet = self.bankroll
                        self.bankroll = 0
                        return self.current_bet
            else:
                self.current_bet = self.min_bet
                if self.current_bet < self.bankroll:
                    self.bankroll -= self.current_bet
                    return self.current_bet
                else:
                    self.current_bet = self.bankroll
                    self.bankroll = 0
                    return self.current_bet
        else:
            return "bankrupt"
        print self.current_bet

    def observe_card(self, card):
        self.count += self.count_strategy[card.rank]

    def pay_insurance(self):
        self.bankroll -= (self.current_bet / 2)

    def set_player_style(self, ace, two, three, four, five, six, seven, eight, nine, ten, bankroll, min_bet, max_bet, count_to_increase_bet, incr, insurance):
        self.bankroll = bankroll
        self.min_bet = min_bet
        self.max_bet = max_bet
        self.current_bet = min_bet
        self.bet_inc = incr
        self.insurance = insurance
        self.count_strategy = [ace, two, three, four, five, six, seven, eight, nine, ten, ten, ten, ten]
        self.count_to_increase_bet = count_to_increase_bet
