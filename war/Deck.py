class Deck():
	def __init__(self, cards=[]):
		self._cards = cards

	def add_card(self, card):
		self._cards.append(card)

	def add_cards(self, cards):
		self._cards.extend(cards)

	def remove_card(self):
		return self._cards.pop(0)

	def get_count(self):
		return len(self._cards)

	def get_cards(self):
		return self._cards

	def clear_deck(self):
		self._cards = []