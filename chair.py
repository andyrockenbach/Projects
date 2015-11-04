from player import Player

class Chair(object):

	def __init__(self):
		self.player = Player()
		self.hands = []
		self.active = True
		self.splits = False

	def add_hand(self, hand):
		self.hands.append(hand)
			
	def check_splits(self):
		for hand in self.hands:
			if hand['active']:
				self.splits = True
				break
			else:
				self.splits = False

	def seat_player(self, player):
		self.player = player

	def split_hand(self, hand):
		new_hand = {
       		'hand': hand['hand'].split(),
       		'bet': hand['bet'],
       		'active': True
       		}
		self.hands.append(new_hand)
