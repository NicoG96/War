from CardFactory import CardFactory
from Deck import Deck


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
		pass

	def start_game(self):
		self.init_game()
