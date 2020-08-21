from .Deck import Deck


class Player():
	def __init__(self, name="", deck=Deck()):
		self.name = name
		self.deck = deck

	def is_not_winner(self):
		return True if self.deck.get_count() != 52 else False

	def set_name(self, name):
		self.name = name

	def set_deck(self, deck):
		self.deck = deck