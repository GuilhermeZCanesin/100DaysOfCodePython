#DAY 11
import random
from art import logo

def blackjack():
	print(logo)
	deckDict = {
		'A': 11, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, '10': 10, 'J': 10, 'Q': 10, 'K': 10,
	}
	deck = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']
	dealer = []
	player = []
	
	def draw_card(chosen):
		"""Returns a random card from the deck"""
		chosen.append(deck[random.randint(0,12)])

	def first_round():
		draw_card(player)
		draw_card(dealer)
		draw_card(player)
		draw_card(dealer)
	
	def sum_cards(cards):
		finalSum1 = 0
		finalSum2 = 0
		for item in deckDict:
			for card in cards:
				if card == item and card == 'A':
					finalSum1 += 1
					finalSum2 += 11
				elif card == item:
					finalSum1 += deckDict[card]
					finalSum2 += deckDict[card]

		if finalSum1 == 21 or (finalSum1 < finalSum2 and finalSum2 > 21):
			return finalSum1
		else:
			return finalSum2

	def print_result(pSum, dSum, final):
		print("------------------------------------\n")
		print(f"Dealers hand: {dealer} = {dSum}")
		print(f"Your hand: {player} = {pSum}")
		print("\n------------------------------------")

		if final:
			if pSum > 21:
				print("You LOST!")
			elif dSum > 21:
				print("You WON!")
			elif dSum > pSum:
				print("You LOST!")
			elif dSum == pSum:
				print("It´s a TIE!")
			else:
				print("You WON!")

	def print_hands():
		print("------------------------------------\n")
		print(f"Dealers hand: ['*','{dealer[1]}']")
		print(f"Your hand: {player}")
		print("\n------------------------------------")
	
	print("Let´s begin!")
	first_round()
	print_hands()
	playing = True

	while playing:
		answer = input("Would you like another card? type 'hit' to stop type 'stop': ").upper()
		if answer == "HIT":
			draw_card(player)
			print_hands()
			if sum_cards(player) > 21:
				print("You scored more than 21! You lost!")
				print_result(sum_cards(player), sum_cards(dealer), True)
				playing = False
		elif answer == "STOP":
			print("Revealing dealers card!")
			if sum_cards(dealer) < 17:
				#print_result(sum_cards(player), sum_cards(dealer), False)
				print("Dealer cards sum inferior than 16 dealer draws a card!")
				draw_card(dealer)
			print_result(sum_cards(player), sum_cards(dealer), True)
			playing = False

again = True
while again:
	blackjack()
	print("\n------------------------------------")
	response = input("Would you like to play again? 'yes' or 'no': ").upper()
	if response == 'NO':
		again = False