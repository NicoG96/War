from War.Card import Card
import unittest
from War.Deck import Deck
from War.CardFactory import CardFactory
import random


class test_Deck(unittest.TestCase):
	@classmethod
	def setUpClass(cls):
		cls.deck = Deck()
		cls.fac = CardFactory()

	def test_add_card(self):
		iterations = random.randint(2, 10)

		for _ in range(iterations):
			self.deck.add_card(self.fac.create_spade(1))
		self.assertTrue(self.deck.get_count() == iterations)
	
	def test_remove_card(self):
		current_count = self.deck.get_count()
		ret = self.deck.remove_card()
		self.assertTrue(self.deck.get_count() == current_count-1)
		self.assertEqual(ret.get_value(), 1)
		self.assertEqual(ret.get_suit(), 'spade')

	def test_queue_pop(self):
		"""
		verify card removal is happening in FIFO order
		"""
		new_card = Card(5, 'heart')
		self.deck.add_card(new_card)
		ret = self.deck.remove_card()
		self.assertNotEqual(ret, new_card)