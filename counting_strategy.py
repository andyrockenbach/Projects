from Tkinter import *

class CountingStrategy(Frame):

	def __init__(self, master):
		Frame.__init__(self, master)
		self.grid()
		self.create_widgets()

	def create_widgets(self):
		self.count_label = Label(self, text="Counting Strategy")
		self.count_label.grid(row=0, columnspan=2, sticky=W+E+N+S)
		self.ace_label = Label(self, text="Ace:")
		self.ace_label.grid(row=1, column=0, sticky=W)
		self.ace_entry = Entry(self, width=5)
		self.ace_entry.insert(INSERT, "-1")
		self.ace_entry.grid(row=1, column=1)
		self.two_label = Label(self, text="Two:")
		self.two_label.grid(row=2, column=0, sticky=W)
		self.two_entry = Entry(self, width=5)
		self.two_entry.insert(INSERT, "1")
		self.two_entry.grid(row=2, column=1)
		self.three_label = Label(self, text="Three:")
		self.three_label.grid(row=3, column=0, sticky=W)
		self.three_entry = Entry(self, width=5)
		self.three_entry.insert(INSERT, "1")
		self.three_entry.grid(row=3, column=1)
		self.four_label = Label(self, text="Four:")
		self.four_label.grid(row=4, column=0, sticky=W)
		self.four_entry = Entry(self, width=5)
		self.four_entry.insert(INSERT, "1")
		self.four_entry.grid(row=4, column=1)
		self.five_label = Label(self, text="Five:")
		self.five_label.grid(row=5, column=0, sticky=W)
		self.five_entry = Entry(self, width=5)
		self.five_entry.insert(INSERT, "1")
		self.five_entry.grid(row=5, column=1)
		self.six_label = Label(self, text="Six:")
		self.six_label.grid(row=6, column=0, sticky=W)
		self.six_entry = Entry(self, width=5)
		self.six_entry.insert(INSERT, "1")
		self.six_entry.grid(row=6, column=1)
		self.seven_label = Label(self, text="Seven:")
		self.seven_label.grid(row=7, column=0, sticky=W)
		self.seven_entry = Entry(self, width=5)
		self.seven_entry.insert(INSERT, "0")
		self.seven_entry.grid(row=7, column=1)
		self.eight_label = Label(self, text="Eight:")
		self.eight_label.grid(row=8, column=0, sticky=W)
		self.eight_entry = Entry(self, width=5)
		self.eight_entry.insert(INSERT, "0")
		self.eight_entry.grid(row=8, column=1)
		self.nine_label = Label(self, text="Nine:")
		self.nine_label.grid(row=9, column=0, sticky=W)
		self.nine_entry = Entry(self, width=5)
		self.nine_entry.insert(INSERT, "0")
		self.nine_entry.grid(row=9, column=1)
		self.tens_label = Label(self, text="Tens(10,J,Q,K):")
		self.tens_label.grid(row=10, column=0, sticky=W)
		self.tens_entry = Entry(self, width=5)
		self.tens_entry.insert(INSERT, "-1")
		self.tens_entry.grid(row=10, column=1)