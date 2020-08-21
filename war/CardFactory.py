from .Card import Card


class CardFactory():
	_instance = None

	@staticmethod
	def get_instance():
		return CardFactory._instance
	
	def __init__(self):
		if CardFactory.get_instance() == None:
			CardFactory._instance = self
		else:
			raise Exception("Only one factory permitted")

	def create_spade(self, value):
		return Card(value, 'spade')

	def create_club(self, value):
		return Card(value, 'club')

	def create_heart(self, value):
		return Card(value, 'heart')

	def create_diamond(self, value):
		return Card(value, 'diamond')