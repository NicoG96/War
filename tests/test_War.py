import unittest
from War.War import War
from War.Player import Player
import random


class test_War(unittest.TestCase):
	@classmethod
	def setUpClass(cls):
		cls.game = War()

	def test_create_cards(self):
		card_set = set()
		cards = self.game.create_cards()
		# make sure each card is unique
		for card in cards:
			if card not in card_set:
				card_set.add(card)
		self.assertEqual(len(cards), 52)
		self.assertTrue(len(card_set) == 52)


	def test_split_cards(self):
		cards = self.game.create_cards()
		deck1, deck2 = self.game.split_cards(cards)
		self.assertEqual(len(deck1.get_cards()), len(deck2.get_cards()))
		
		for card in cards[:26]:
			self.assertTrue(card in deck1.get_cards())

		for card in cards[26:]:
			self.assertTrue(card in deck2.get_cards())

	def test_switch_player(self):
		p1 = Player()
		p2 = Player()

		ret1, ret2 = self.game.switch_player(p1, p2)

		self.assertEqual(ret1, p2)
		self.assertEqual(ret2, p1)