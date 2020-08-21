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
			self.deck.add_card(self.fac.create_spade(14))
		self.assertTrue(self.deck.get_count() == iterations)
	
	def test_remove_card(self):
		current_count = self.deck.get_count()
		ret = self.deck.remove_card()
		self.assertTrue(self.deck.get_count() == current_count-1)
		self.assertEqual(ret.get_value(), 14)
		self.assertEqual(ret.get_suit(), 'spade')

	def test_queue_pop(self):
		"""
		verify card removal is happening in FIFO order
		"""
		new_card = Card(5, 'heart')
		self.deck.add_card(new_card)
		ret = self.deck.remove_card()
		self.assertNotEqual(ret, new_card)

	def test_add_cards(self):
		"""
		test adding multiple cards in one transaction
		"""
		current_count = self.deck.get_count()
		cards = []

		for _ in range(10):
			cards.append(self.fac.create_heart(5))
		
		self.deck.add_cards(cards)
		self.assertEqual(self.deck.get_count(), current_count+10)