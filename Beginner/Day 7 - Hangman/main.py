#DAY 7
import random
import hangman_art
from hangman_words import word_list

word = random.choice(word_list)
word_length = len(word)
guesses = []

mistakes = 6
word_final = []
letters = []

for letter in word:
		letters+="_"
		word_final+=letter

print(hangman_art.logo);
print(hangman_art.stages[mistakes]);
print(f"\n{' '.join(letters)}")

while letters != word_final and mistakes != 0:
	
	guess = input("\nGuess a letter: ").lower()
	if guess not in word:
		guesses+=guess
		mistakes-=1
		print("\nWrong! Lost 1 life!")
	elif guess in guesses:
		print("\nLetter already guessed!")
	else:
		for position in range(word_length):
			letter = word[position]
			if letter == guess:
				guesses+=guess + ""
				letters[position] = letter

	print(hangman_art.stages[mistakes]);
	print(f"\nGuesses: {' '.join(guesses)}" )
	print(f"\n{' '.join(letters)}")

if letters == word_final:
	print("\nYou win!")
else:
	print("\nYou lost!")
	print("\nThe correct word was: " + word)
	
	