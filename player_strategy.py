from Tkinter import *

class PlayerStrategy(Frame):

	def __init__(self, master):
		Frame.__init__(self, master)
		self.grid()
		self.create_widgets()

	def create_widgets(self):
		self.player_label = Label(self, text="Player Strategy")
		self.player_label.grid(row=0, columnspan=2, sticky=W+E+N+S)
		self.bankroll = Label(self, text="Bankroll:")
		self.bankroll.grid(row=1, column=0, sticky=W)
		self.bankroll_entry = Entry(self, width=5)
		self.bankroll_entry.insert(INSERT, "5000")
		self.bankroll_entry.grid(row=1, column=1)
		self.min_bet = Label(self, text="Minimum Bet:")
		self.min_bet.grid(row=2, column=0, sticky=W)
		self.min_bet_entry = Entry(self, width=5)
		self.min_bet_entry.insert(INSERT, "25")
		self.min_bet_entry.grid(row=2, column=1)
		self.max_bet = Label(self, text="Maximum Bet:")
		self.max_bet.grid(row=3, column=0, sticky=W)
		self.max_bet_entry = Entry(self, width=5)
		self.max_bet_entry.insert(INSERT, "400")
		self.max_bet_entry.grid(row=3, column=1)
		self.count_bet = Label(self, text="Count Bet:")
		self.count_bet.grid(row=4, column=0, sticky=W)
		self.count_bet_entry = Entry(self, width=5)
		self.count_bet_entry.insert(INSERT, "2")
		self.count_bet_entry.grid(row=4, column=1)
		self.bet_inc = Label(self, text="Bet Increase:")
		self.bet_inc.grid(row=5, column=0, sticky=W)
		self.bet_inc_entry = Entry(self, width=5)
		self.bet_inc_entry.insert(INSERT, "2")
		self.bet_inc_entry.grid(row=5, column=1)
		
