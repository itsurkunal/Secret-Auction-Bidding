from replit import clear
from art import logo

print(logo)

bids = {}
bidding_finished = False


def find_highest_bidder(bid_record):
  highest_bid = 0
  winner = ""
  for bidder in bid_record:
    bid_amount = bid_record[bidder]
    if bid_amount > highest_bid:
      highest_bid = bid_amount
      winner = bidder
  print(f"The winner is {winner} with a bid of ${highest_bid}.")


print("Welcome to the secret Auction Program!")

while not bidding_finished:
  name = input("What is your name?: ")
  price = int(input("What is your bid?: $"))
  bids[name] = price
  should_continue = input("Do you want to continue type yes or no. ").lower()
  if should_continue == "no":
    bidding_finished = True
    find_highest_bidder(bids)
  elif should_continue == "yes":
    clear()
  else:
    bidding_finished = True
    find_highest_bidder(bids)
