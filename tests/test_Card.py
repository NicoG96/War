import unittest
from War.CardFactory import CardFactory

class test_Card(unittest.TestCase):
	@classmethod
	def setUpClass(cls):
		cls.fac = CardFactory()
		cls.spade = cls.fac.create_spade(14)
		cls.club = cls.fac.create_club(14)
		cls.heart = cls.fac.create_heart(14)
		cls.diamond = cls.fac.create_diamond(14)

	def test_get_full_name(self):
		full_names = [
			"Ace",
			"Two",
			"Three",
			"Four",
			"Five",
			"Six",
			"Seven",
			"Eight",
			"Nine",
			"Ten",
			"Jack",
			"Queen",
			"King"
		]
		cards = [self.fac.create_club(card) for card in range(2, 15)]

		for card in cards:
			self.assertIn(card.get_full_name(), full_names)

	def test_get_short_name(self):
		ace = self.fac.create_spade(14)
		ten = self.fac.create_spade(10)
		jack = self.fac.create_spade(11)
		queen = self.fac.create_spade(12)
		king = self.fac.create_spade(13)

		self.assertEqual(ace.get_short_name(), 'A')
		self.assertEqual(ten.get_short_name(), '10')
		self.assertEqual(jack.get_short_name(), 'J')
		self.assertEqual(queen.get_short_name(), 'Q')
		self.assertEqual(king.get_short_name(), 'K')

	def test_get_symbol(self): 
		self.assertEqual(self.spade.get_symbol(), "♠")
		self.assertEqual(self.club.get_symbol(), "♣")
		self.assertEqual(self.heart.get_symbol(), "♥")
		self.assertEqual(self.diamond.get_symbol(), "♦")

	def test_get_color(self):
		self.assertEqual(self.spade.get_color(), 'black')
		self.assertEqual(self.club.get_color(), 'black')
		self.assertEqual(self.heart.get_color(), 'red')
		self.assertEqual(self.diamond.get_color(), 'red')