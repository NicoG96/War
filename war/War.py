from .CardFactory import CardFactory
from .Deck import Deck
from .Player import Player
import random


class War():
	_instance = None

	@staticmethod
	def get_instance():
		return War._instance

	def __init__(self):
		if War.get_instance() == None:
			self.factory = CardFactory()
			self.pot = Deck()
			self.player_1 = Player()
			self.player_2 = Player()
		else:
			raise Exception("Only one game permitted")

	def create_cards(self):
		cards = []
		# create 52-card deck, 13 for each suit
		for x in range(1, 14):
			cards.append(self.factory.create_spade(x)) 
			cards.append(self.factory.create_club(x)) 
			cards.append(self.factory.create_heart(x)) 
			cards.append(self.factory.create_diamond(x))
		return cards

	def split_cards(self, cards):
		return Deck(cards[:26]), Deck(cards[26:])

	def assign_decks(self, deck1, deck2):
		self.player_1.set_deck(deck1)
		self.player_2.set_deck(deck2)

	def switch_player(self, curr, prev):
		temp = prev
		prev = curr
		curr = temp
		return curr, prev

	def init_game(self):
		cards = self.create_cards()
		random.shuffle(cards)
		deck1, deck2 = self.split_cards(cards)
		self.assign_decks(deck1, deck2)
	
	def end_game(self):
		pass

	def start_game(self):
		self.init_game()
		
		# Get username
		print("Player 1, please enter your name: ")
		self.player_1.name = input()

		print("Player 2, please enter your name: (Press Enter if single-player mode) ")
		player2_name = input()
		self.player_2.name = player2_name if player2_name != "" else "Computer"

		whose_turn = random.randint(0, 1)
		current_player = None
		previous_player = None

		# randomly pick starting player
		if whose_turn:
			current_player = self.player_2
			previous_player = self.player_1
		else:
			current_player = self.player_1
			previous_player = self.player_2

		# start game
		while self.player_1.is_not_winner() and self.player_2.is_not_winner():
			# if player is going into the round with no cards, other player wins
			if self.player_1.deck.get_count() == 0 or self.player_2.deck.get_count() == 0:
				if self.player_1.deck.get_count() != 0:
					self.player_1.deck.add_cards(self.pot.get_cards())
					self.pot.clear_deck()
				elif self.player_2.deck.get_count() != 0:
					self.player_2.deck.add_cards(self.pot.get_cards())
					self.pot.clear_deck()
				break

			# remove card from player's deck & add to pot
			card1 = current_player.deck.remove_card()
			self.pot.add_card(card1)

			# switch players
			current_player, previous_player = self.switch_player(current_player, previous_player)

			card2 = current_player.deck.remove_card()
			self.pot.add_card(card2)

			for card in self.pot.get_cards():
				print(card.get_value())

			if card1.get_value() > card2.get_value():
				previous_player.deck.add_cards(self.pot.get_cards())
				self.pot.clear_deck()
			elif card2.get_value() > card1.get_value():
				current_player.deck.add_cards(self.pot.get_cards())
				self.pot.clear_deck()

			# war, each player contributes 1 card
			else:
				if current_player.deck.get_count() != 0:
					self.pot.add_card(current_player.deck.remove_card())
				# if the player doesn't have any more cards to play, other player wins
				else:
					previous_player.deck.add_cards(self.pot.get_cards())
					self.pot.clear_deck()
					break

				if previous_player.deck.get_count() != 0:
					self.pot.add_card(previous_player.deck.remove_card())
				else:
					current_player.deck.add_cards(self.pot.get_cards())
					self.pot.clear_deck()
					break

			current_player, previous_player = self.switch_player(current_player, previous_player)

		if self.player_1.is_not_winner():
			print("{} IS THE WINNER!".format(self.player_2.name))
		else:
			print("{} IS THE WINNER!".format(self.player_1.name))