#DAY 4
import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

outcomes = [rock, paper, scissors]

my_play = int(input("What do you choose? Type 0 for Rock, 1 for Paper, 2 for Scissors.\nYou: "))

if my_play >= 0 and my_play <= 2:	
	print(outcomes[my_play])	

	computer_play = random.randint(0,2)
	print(f"Oponent: {computer_play}")
	print(outcomes[computer_play])	

	if (computer_play == 0 and my_play == 2) or (computer_play == 2 and my_play == 0):
		print("Rock crushes Scissors!")
		if my_play == 0:
			print("You win!")
		else:
			print("You lose!")
	elif (computer_play == 1 and my_play == 0) or (computer_play == 0 and my_play == 1):
		print("Paper covers Rock!")
		if my_play == 1:
			print("You win!")
		else:
			print("You lose!")
	elif (computer_play == 2 and my_play == 1) or (computer_play == 1 and my_play == 2):
		print("Scissors cuts Paper!")
		if my_play == 2:
			print("You win!")
		else:
			print("You lose!")
	elif computer_play == my_play:
			print("It´s a tie!")
else:
	print("Wrong input! You lost!")