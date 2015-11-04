from Tkinter import *
from card_table import CardTable
from counting_strategy import CountingStrategy
from dealer import Dealer
from player import Player
from player_strategy import PlayerStrategy
from table_rules import TableRules
import datetime

class Blackjack(Frame):

	def __init__(self, master):
		Frame.__init__(self, master)
		self.grid()
		self.create_widgets()

	def create_widgets(self):
		self.blackjack_title = Label(self, text="Learn to count cards!")
		self.blackjack_title.grid(row=0, columnspan=2, sticky=W+E+N+S)
		self.bankroll = Label(self, text="Average Bankroll:")
		self.bankroll.grid(row=1, columnspan=2, sticky=W+E+N+S)
		self.bankrupt = Label(self, text="Bankrupt:")
		self.bankrupt.grid(row=2, columnspan=2, sticky=W+E+N+S)
		self.rules = TableRules(self)
		self.rules.grid(row=3, columnspan=2)
		self.count = CountingStrategy(self)
		self.count.grid(row=4, column=0)
		self.player_strategy = PlayerStrategy(self)
		self.player_strategy.grid(row=4, column=1, stick=N)
		self.run_button = Button(self, text="Run Simulation", command=self.run_simulation)
		self.run_button.grid(row=5, columnspan=2, sticky=E)		

	def run_simulation(self):
		print datetime.datetime.now().time()
		players = []
		if int(self.rules.players.get()) > 1:
			extra = int(self.rules.players.get()) - 1
			for _ in range(extra):
				player = Player()
				players.append(player)
		player = Player()
		player.set_player_style(int(self.count.ace_entry.get()), int(self.count.two_entry.get()), int(self.count.three_entry.get()), int(self.count.four_entry.get()), int(self.count.five_entry.get()), int(self.count.six_entry.get()), int(self.count.seven_entry.get()), int(self.count.eight_entry.get()), int(self.count.nine_entry.get()), int(self.count.tens_entry.get()), int(self.player_strategy.bankroll_entry.get()), int(self.player_strategy.min_bet_entry.get()), int(self.player_strategy.max_bet_entry.get()), int(self.player_strategy.count_bet_entry.get()), int(self.player_strategy.bet_inc_entry.get()), False)
		players.append(player)
		card_table = CardTable()
		card_table.set_table_style(self.rules.insurance.get(), float(self.rules.blackjack_payout.get()), int(self.rules.decks.get()))
		card_table.seat_players(players)
		bankroll = 0
		bankrupt = 0
		for num in range(10000):
			for _ in range(int(self.player_strategy.session_entry.get())*100):
				card_table.play_round()
			if card_table.chairs[-1].player.bankroll < 1:
				bankrupt += 1
			bankroll += card_table.chairs[-1].player.bankroll
			for chair in card_table.chairs:
				chair.player.bankroll = 5000
			card_table.chairs[-1].player.bankroll = int(self.player_strategy.bankroll_entry.get())
			card_table.shoe.cards = []
		num_bankrupt = float(bankrupt) / float(100)
		self.bankrupt["text"] = 'Bankrupt: %.2f%%' % num_bankrupt
		bankroll = bankroll / 10000
		self.bankroll["text"] = "Average Bankroll: $ %.2f" % bankroll
		print datetime.datetime.now().time()
		
root = Tk()
root.title("Blackjack")
root.geometry("328x525")
root.configure(background="#e9eaed")

app = Blackjack(root)

root.mainloop()
