from hand import Hand

class Dealer(object):

	def __init__(self):
		self.hand = Hand()

	def deal_card(self, card_table):
		card = card_table.shoe.get_next_card()
		for chair in card_table.chairs:
			chair.player.observe_card(card)
		return card

	def deal_round(self, card_table):
		for _ in range(2):
			for chair in card_table.chairs:
				if chair.hands[0]['bet'] is not "bankrupt":
					chair.hands[0]['hand'].add_card(self.deal_card(card_table))
				else:
					chair.active = False
			for chair in card_table.chairs:
				if chair.active:
					self.hand.add_card(self.deal_card(card_table))
					break

	def hit_dealer(self, card_table):
		while self.hand.is_soft():
			if self.hand.total < 18:
				self.hand.add_card(self.deal_card(card_table))
			else:
				break
		while self.hand.total < 17:
			self.hand.add_card(self.deal_card(card_table))

	def pay_player(self, hand, chair):
		chair.player.bankroll += hand['bet'] * 2

	def pay_player_blackjack(self, chair, blackjack_payout):
		bet = chair.hands[0]['bet'] + chair.hands[0]['bet'] * blackjack_payout
		chair.player.bankroll += bet

	def refund_player(self, hand, chair):
		chair.player.bankroll += hand['bet']

	def resolve_round(self, card_table):
		for chair in card_table.chairs:
			if chair.active:
				self.hit_dealer(card_table)
				break
		for chair in card_table.chairs:
			if chair.active:
				if self.hand.is_busted():
					for hand in chair.hands:
						if hand['hand'].is_busted() is False:
							self.pay_player(hand, chair)
				else:
					for hand in chair.hands:
						if self.hand.total < hand['hand'].total:
							self.pay_player(hand, chair)
						elif self.hand.total is hand['hand'].total:
							self.refund_player(hand, chair)

	def showing(self):
		return self.hand.cards[0].get_value()
