from Tkinter import *

class TableRules(Frame):

	def __init__(self, master):
		Frame.__init__(self, master)
		self.grid()
		self.create_widgets()

	def create_widgets(self):
		self.insurance = IntVar()
		self.surrender = IntVar()
		self.das = IntVar()
		self.table_label = Label(self, text="Table Rules")
		self.table_label.grid(row=0, columnspan=3, sticky=W+E+N+S)
		self.insurance_button = Checkbutton(self, text="Insurance", variable=self.insurance)
		self.insurance_button.grid(row=1, column=0, sticky=W)
		self.blackjack_payout_label = Label(self, text="Blackjack Payout:")
		self.blackjack_payout_label.grid(row=1, column=1, sticky=W)
		self.blackjack_payout = Entry(self, width=5)
		self.blackjack_payout.insert(INSERT, "1.5")
		self.blackjack_payout.grid(row=1, column=2, sticky=W)
		self.surrender_button = Checkbutton(self, text="Surrender", variable=self.surrender)
		self.surrender_button.grid(row=2, column=0, sticky=W)
		self.players_label = Label(self, text="Number of Players:")
		self.players_label.grid(row=2, column=1)
		self.players = Entry(self, width=5)
		self.players.insert(INSERT, "1")
		self.players.grid(row=2, column=2, sticky=W)
		self.das_button = Checkbutton(self, text="Double After Split", variable=self.das)
		self.das_button.grid(row=3, column=0, sticky=W)
		self.decks_label = Label(self, text="Number of Decks:")
		self.decks_label.grid(row=3, column=1, sticky=W)
		self.decks = Entry(self, width=5)
		self.decks.insert(INSERT, "6")
		self.decks.grid(row=3, column=2, sticky=W)
