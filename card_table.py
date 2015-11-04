from chair import Chair
from hand import Hand
from shoe import Shoe
from dealer import Dealer

class CardTable(object):

    def __init__(self):
        self.chairs = []
        self.shoe = Shoe(6)
        self.dealer = Dealer()
        self.insurance = True
        self.blackjack_payout = 1.5
        self.shoe_size = 6

    def ask_player(self, chair, hand, dealer_showing):
        decision = ""
        while decision is not "stay" and hand['hand'].is_busted() is False:
            decision = chair.player.decision(hand['hand'], dealer_showing)
            if decision is "split":
                chair.player.splits += 1
                chair.player.bankroll -= hand['bet']
                chair.split_hand(hand)
                hand['hand'].add_card(self.dealer.deal_card(self))
                chair.splits = True
            elif decision is "hit":
                hand['hand'].add_card(self.dealer.deal_card(self))
            elif decision is "double":
                chair.player.doubles += 1
                bet = hand['bet']
                chair.player.bankroll -= bet
                hand['bet'] = bet * 2
                hand['hand'].add_card(self.dealer.deal_card(self))
                decision = "stay"
        hand['active'] = False

    def play_round(self):
        if len(self.shoe.cards) < (self.shoe_size * 13):
            self.shoe = Shoe(self.shoe_size)
            for chair in self.chairs:
                chair.player.count = 0
        decks_left = len(self.shoe.cards) / 52
        self.dealer.hand = Hand()
        for chair in self.chairs:
            chair.hands = []
            chair.active = True
            chair.splits = False
            hand = Hand()
            chair.add_hand({
                'hand': hand,
                'bet': chair.player.make_bet(decks_left),
                'active': True
            })
        self.dealer.deal_round(self)
        if len(self.dealer.hand.cards) > 0:
            if self.dealer.hand.is_dealer_blackjack():
                for chair in self.chairs:
                    if chair.hands[0]['hand'].is_blackjack():
                        chair.player.blackjacks += 1
                        self.dealer.refund_player(chair.hands[0], chair)
                    chair.active = False
            elif self.dealer.showing() is 11:
                if self.insurance:
                    for chair in self.chairs:
                        if chair.player.insurance and chair.active:
                            chair.player.pay_insurance()
                if self.dealer.hand.is_blackjack():
                    for chair in self.chairs:
                        if chair.player.insurance:
                            if self.insurance:
                                self.dealer.refund_player(chair.hands[0], chair)
                        elif chair.hands[0]['hand'].is_blackjack():
                            chair.player.blackjacks += 1
                            self.dealer.refund_player(chair.hands[0], chair)
                        chair.active = False
                else:
                    self.resolve_chairs()
                    self.dealer.resolve_round(self)
            else:
                self.resolve_chairs()
                self.dealer.resolve_round(self)

    def resolve_chairs(self):
        for chair in self.chairs:
            if chair.hands[0]['hand'].is_blackjack():
                self.dealer.pay_player_blackjack(chair, self.blackjack_payout)
                chair.player.blackjacks += 1
                chair.active = False
            else:
                self.ask_player(chair, chair.hands[0], self.dealer.showing())
                while chair.splits:
                    for i in range(0, len(chair.hands)):
                        if chair.hands[i]['active']:
                            chair.hands[i]['hand'].add_card(self.dealer.deal_card(self))
                            self.ask_player(chair, chair.hands[i], self.dealer.showing())
                    chair.check_splits()
                for hand in chair.hands:
                    if hand['hand'].is_busted():
                        chair.active = False
                    else:
                        chair.active = True
                        break

    def seat_players(self, players):
        for player in players:
            chair = Chair()
            chair.seat_player(player)
            self.chairs.append(chair)

    def set_table_style(self, insurance, blackjack_payout, shoe_size):
        self.insurance = insurance
        self.blackjack_payout = blackjack_payout
        self.shoe_size = shoe_size
        self.shoe = Shoe(shoe_size)
