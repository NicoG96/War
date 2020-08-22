import enum

class CardEnum(enum.Enum):
	Two = 2
	Three = 3
	Four = 4
	Five = 5
	Six = 6
	Seven = 7
	Eight = 8
	Nine = 9
	Ten = 10
	Jack = 11
	Queen = 12
	King = 13
	Ace = 14

class Card():
	def __init__(self, value, suit):
		self._enum = CardEnum(value)
		self._suit = suit

	def get_value(self):
		return self._enum.value

	def get_full_name(self):
		return self._enum.name

	def get_short_name(self):
		if self._enum.value == 11:
			return 'J'
		elif self._enum.value == 12:
			return 'Q'
		elif self._enum.value == 13:
			return 'K'
		elif self._enum.value == 14:
			return 'A'
		else:
			return str(self._enum.value)
	
	def get_suit(self):
		return self._suit

	def get_symbol(self):
		if self._suit == "spade":
			return "♠"
		elif self._suit == "club":
			return "♣" 
		elif self._suit == "heart":
			return "♥" 
		else:
			return "♦"

	def get_color(self):
		return 'black' if self._suit == 'spade' or self._suit == 'club' else 'red'
