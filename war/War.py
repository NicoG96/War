from .CardFactory import CardFactory
from .Player import Player
from .Deck import Deck
import time
import random
from pyfiglet import Figlet
from termcolor import colored
from prettytable import PrettyTable


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
		for x in range(2, 15):
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

	def init_game(self):
		cards = self.create_cards()
		random.shuffle(cards)
		deck1, deck2 = self.split_cards(cards)
		self.assign_decks(deck1, deck2)

	def cli(self):
		print(colored("===============================", "cyan"))
		print(colored(Figlet(font="slant").renderText("W A R"), "cyan"), end="")
		print(colored("===============================", "cyan"))

	def start_game(self, is_interactive):
		self.init_game()
		self.cli()
		table = PrettyTable()
		
		# Get username
		print("Please enter your name: ", end="")
		self.player_1.name = input()
		self.player_2.name = "Computer"

		# start game
		while self.player_1.is_not_winner() and self.player_2.is_not_winner():
			p1_header = self.player_1.name + " (" + str(self.player_1.deck.get_count()-1) + ")"
			p2_header = self.player_2.name + " (" + str(self.player_2.deck.get_count()-1) + ")"
			table.field_names = [p1_header, p2_header]

			# update leaderboard. if in war, keep same stats
			if self.pot.get_count() == 0:
				table.clear_rows()
			# if player is going into the round with no cards, other player wins
			if self.player_1.deck.get_count() == 0 or self.player_2.deck.get_count() == 0:
				if self.player_1.deck.get_count() != 0:
					self.player_1.deck.add_cards(self.pot.get_cards())
					self.pot.clear_deck()
				elif self.player_2.deck.get_count() != 0:
					self.player_2.deck.add_cards(self.pot.get_cards())
					self.pot.clear_deck()
				break

			# game as usual, remove card from player's deck & add to pot
			if is_interactive:
				print("Press 'c' to draw a card")
				while input().lower() != 'c':
					continue
			card1 = self.player_1.deck.remove_card()
			self.pot.add_card(card1)

			# remove other player's
			if is_interactive:
				print("{} making their move...".format(self.player_2.name))
				time.sleep(1)
			card2 = self.player_2.deck.remove_card()
			self.pot.add_card(card2)

			# update gui
			table.add_row([
				card1.get_short_name() + " " + card1.get_symbol(), 
				card2.get_short_name() + " " + card2.get_symbol()])
			print(table)

			# slow down!
			time.sleep(1)

			# see who won the round
			if card1.get_value() > card2.get_value():
				self.player_1.deck.add_cards(self.pot.get_cards())
				self.pot.clear_deck()
				print("\n{} wins the pot!\n".format(self.player_1.name))
			elif card2.get_value() > card1.get_value():
				self.player_2.deck.add_cards(self.pot.get_cards())
				self.pot.clear_deck()
				print("\n{} wins the pot!\n".format(self.player_2.name))

			# war, each player contributes 1 card
			else:
				war_card1 = None
				war_card2 = None 

				# if the player doesn't have any more cards to play, other player wins
				# if they do have enough, then chip in
				if self.player_1.deck.get_count() != 0:
					war_card1 = self.player_1.deck.remove_card()
					self.pot.add_card(war_card1)

				else:
					self.player_2.deck.add_cards(self.pot.get_cards())
					self.pot.clear_deck()
					break

				if self.player_2.deck.get_count() != 0:
					war_card2 = self.player_2.deck.remove_card()
					self.pot.add_card(war_card2)
				else:
					self.player_1.deck.add_cards(self.pot.get_cards())
					self.pot.clear_deck()
					break

				# update gui with these war-round cards
				table.add_row([
					war_card1.get_short_name() + " " + war_card1.get_symbol(), 
					war_card2.get_short_name() + " " + war_card2.get_symbol()
				])
			if not is_interactive:
				time.sleep(2)

		if self.player_1.is_not_winner():
			print("{} won!".format(self.player_2.name))
		else:
			print("{} won!".format(self.player_1.name))