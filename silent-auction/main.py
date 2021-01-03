import os
from art import logo

print(logo)

live_auction = True

auction_info = {}


def new_bid(person, amount):
    auction_info[person] = f"{amount}"


while live_auction:
    name = input('Please insert your name: \n')
    bid = int(input('Please place your bid: $'))
    new_bid(person=name, amount=bid)
    other_bids = input('Are there any other bidders? Type "yes" or "no"\n').lower()
    os.system('clear')
    if other_bids == 'no':
        live_auction = False
        highest_bidder = max(auction_info, key=auction_info.get)
        auction_values = auction_info.values()
        highest_value = max(auction_values)

        print(f"Congratulations {highest_bidder}, you won with a bid of ${highest_value}")
