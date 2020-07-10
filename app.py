import itertools, random

def deal(cards , number_of_players):
	deck = shuffle_deck(cards)
	deal_to_players(deck,number_of_players)
	deal_to_table(deck)

def deal_to_players(deck,number_of_players):
	first_cards = [next(deck) for _ in range(number_of_players)]
	second_cards = [next(deck) for _ in range(number_of_players)]
	hands = zip(first_cards,second_cards)

	print()

	for i, (first_cards, second_cards) in enumerate(hands , start=1):
		print(f"Player {i} was dealt: {first_cards}, {second_cards}")


def deal_to_table(deck):
	next(deck)
	flop = ', '.join(str(next(deck)) for _ in range(3))
	print(f"The flop: {flop}")

	next(deck)
	print(f"The turn: {next(deck)}")

	next(deck)
	print(f"The river: {next(deck)}")
	print()

def get_players():
	while True:
		number_of_players = input("Enter number of players: ").strip()

		try:
			number_of_players = int(number_of_players)
		except ValueError:
			print("You must enter an integer:")
		else:
			if number_of_players in range (2,11):
				return number_of_players
			elif number_of_players <2:
				print("Need minimum 2 players.")
			else:
				print("You cannot have more than 10 players.")




def shuffle_deck(cards):
	deck = list(cards)
	random.shuffle(deck)
	return iter(deck)

ranks = (2,3,4,5,6,7,8,9,10,"Jack", "Queen", "king", "Ace")
suits = ("Clubs","Heart", "Diamond","Spades")
cards = list(itertools.product(ranks,suits))

deal(cards, get_players())


"""
cards= []
for rank in ranks:
	for suit in suits:
		cards.append((rank,suit))
print(len(cards))
random.shuffle(cards)
print("You got:")
for i in range(5):
	print(cards[i][0], "of", cards[i][1])
"""



