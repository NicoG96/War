import unittest
from War.Deck import Deck
from War.Card import Card
import random


class test_Deck(unittest.TestCase):
	@classmethod
	def setUpClass(cls):
		cls.deck = Deck()
		cls.card = Card(1, 'spade')

	def test_add_card(self):
		iterations = random.randint(2, 10)

		for _ in range(iterations):
			self.deck.add_card(self.card)
		self.assertTrue(self.deck.get_count() == iterations)
	
	def test_remove_card(self):
		current_count = self.deck.get_count()
		ret = self.deck.remove_card()
		self.assertTrue(self.deck.get_count() == current_count-1)
		self.assertEqual(ret, self.card)

	def test_queue_pop(self):
		"""
		verify card removal is happening in FIFO order
		"""
		new_card = Card(5, 'heart')
		self.deck.add_card(new_card)
		ret = self.deck.remove_card()
		self.assertNotEqual(ret, new_card)