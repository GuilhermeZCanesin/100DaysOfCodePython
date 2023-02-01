#DAY 9
import os

logo = '''
                         ___________
                         \         /
                          )_______(
                          |"""""""|_.-._,.---------.,_.-._
                          |       | | |               | | ''-.
                          |       |_| |_             _| |_..-'
                          |_______| '-' `'---------'` '-'
                          )"""""""(
                         /_________\\
                       .-------------.
                      /_______________\\
'''

print(logo)
print("Blind auction - Lets begin!\n\n")

finished = False
bids = {}
highest_bidder = 0

def find_highest_bidder(bidding_record):
	highest_bid = 0
	winner = ""
	for bidder in bidding_record:
		bid_ammount = bidding_record[bidder]
		if bid_ammount > highest_bid:
			highest_bid = bid_ammount
			winner = bidder
	print(f"The winner is {winner} with a bid of ${highest_bid}")

while not finished:
	name = input("\n- What is your name? \n")
	bid = int(input("\n- What is your bid? \n $ "))
	bids[name] = bid
	next = (input("\n- Are there other to bid? YES or NO \n")).upper()
	if(next == "NO"):
		finished = True
		find_highest_bidder(bids)
	elif next == "YES":
		os.system('clear')
		