import unittest
import random
from War.CardFactory import CardFactory


class test_CardFactory(unittest.TestCase):
	@classmethod
	def setUpClass(cls):
		cls.fac = CardFactory()

	def test_create_spade(self):
		card = self.fac.create_spade(14)
		self.assertEqual(card.get_suit(), 'spade')

	def test_create_club(self):
		card = self.fac.create_club(14)
		self.assertEqual(card.get_suit(), 'club')

	def test_create_heart(self):
		card = self.fac.create_heart(14)
		self.assertEqual(card.get_suit(), 'heart')

	def test_create_diamond(self):
		card = self.fac.create_diamond(14)
		self.assertEqual(card.get_suit(), 'diamond')
		
	def test_value(self):
		for _ in range(100):
			value = random.randint(2, 14)
			card = self.fac.create_spade(value)
			self.assertEqual(card.get_value(), value)