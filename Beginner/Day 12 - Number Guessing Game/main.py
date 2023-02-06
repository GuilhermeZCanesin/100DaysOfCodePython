#Number Guessing Game Objectives:

# Include an ASCII art logo.
# Allow the player to submit a guess for a number between 1 and 100.
# Check user's guess against actual answer. Print "Too high." or "Too low." depending on the user's answer. 
# If they got the answer correct, show the actual answer to the player.
# Track the number of turns remaining.
# If they run out of turns, provide feedback to the player. 
# Include two different difficulty levels (e.g., 10 guesses in easy mode, only 5 guesses in hard mode).

import random import randint

def set_difficulty(difficulty):
	if difficulty == 'easy':
		return 10
	elif difficulty == 'hard':
		return 5

playing = True
attempts = 0

print("Welcome to the number guessing game!")
print("I´m thinking about a number between 1 and 100.")

random_number = random.randint(1, 100)

difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ")
attempts = set_difficulty(difficulty)



print(f"You have {attempts} left to guess the number")

while playing:
	guess = int(input("Guess a number: "))
	
	if guess == random_number:
		print(f"You got it! The answer was {random_number}!")
		playing = False
		break
	elif guess > random_number:
		print("Too high!")
		attempts-=1
	elif guess < random_number:
		print("Too low!")
		attempts-=1
		
	if attempts == 0:
		print(f"Too bad, you did not guessed correctly! The answer was {random_number}")
		playing = False
	elif attempts == 1:
		print("This is your last attempt!")
	else:
		print(f"You have {attempts} left to guess the number")

