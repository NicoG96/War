from Deck import Deck


class Player():
	def __init__(self, name, deck=Deck(), is_turn=False):
		self.name = name
		self.cards = deck
		self.is_turn = is_turn

	def check_if_winner(self):
		return True if self.cards == 52 else False