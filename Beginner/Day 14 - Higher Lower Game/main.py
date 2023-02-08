#DAY 14
import os
from random import choice, randint
from art import logo, vs
from gamedata import data


def initial_load():
	position = randint(0,len(data)-1)
	return position

def call_new_compare(selected):
	position = choice([i for i in range(0,len(data)-1) if i not in [selected]])
	return position

def compare_followers(a_item, b_item):
	if a_item.get('follower_count') >= b_item.get('follower_count'):
		return 'A'
	elif b_item.get('follower_count') >= a_item.get('follower_count'):
		return 'B'


a_position = initial_load()
b_position = call_new_compare(a_position)
itemA = data[a_position]
itemB = data[b_position]
counter = 0
playing = True

while playing:
	print(logo)
	if counter > 0:
		print(f"You got {counter} correct!")
		
	print(f"Compare A: {itemA.get('name')}, {itemA.get('description')}, from {itemA.get('country')}")
	print(vs)
	print(f"Compare B: {itemB.get('name')}, {itemB.get('description')}, from {itemB.get('country')}")
	answer = input("Who has more followers? Type 'A' or 'B': ")
	if compare_followers(itemA, itemB) == answer:
		if answer == 'A':
			itemB = data[call_new_compare(a_position)]
		elif answer == 'B':
			a_position = b_position
			b_position = call_new_compare(a_position)
			itemA = itemB
			itemB = data[b_position]
		counter+=1
		os.system('clear')
	else:
		print(f"Too bad! You missed! You only got {counter} correct! Bye!")
		playing = False