from .CardFactory import CardFactory
from .Deck import Deck
import random


class War():
	_instance = None

	@staticmethod
	def get_instance():
		return War._instance

	def __init__(self):
		if War.get_instance() == None:
			self.factory = CardFactory()
			self.deck = Deck()
		else:
			raise Exception("Only one game permitted")

	def init_game(self):
		# create 52-card deck, 13 for each suit
		for x in range(1, 14):
			self.deck.add_card(self.factory.create_spade(x)) 
			self.deck.add_card(self.factory.create_club(x)) 
			self.deck.add_card(self.factory.create_heart(x)) 
			self.deck.add_card(self.factory.create_diamond(x))
		random.shuffle(self.deck.get_cards())

	def start_game(self):
		self.init_game()
