from .Card import Card


class CardFactory():
	def create_spade(self, value):
		return Card(value, 'spade')

	def create_club(self, value):
		return Card(value, 'club')

	def create_heart(self, value):
		return Card(value, 'heart')

	def create_diamond(self, value):
		return Card(value, 'diamond')