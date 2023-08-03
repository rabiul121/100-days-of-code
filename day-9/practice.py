from replit import clear

from blind_bid_art import logo

print(logo)
bids = {}


def find_winner(bidding_records):
    height_bid = 0
    winner = ""
    for bidder in bidding_records:
        if bidding_records[bidder] > height_bid:
            height_bid = bidding_records[bidder]
            winner = bidder
    print(f"The winner is {winner} with a bid amount ${height_bid}")


bidding_finished = False
while not bidding_finished:
    name = input("What is your name? ")
    bidding_amount = int(input("What is your bid amount? $"))
    bids[name] = bidding_amount
    should_continue = input("Is there any other bidder? Type 'yes' or 'no' \n")
    if should_continue == 'no':
        bidding_finished = True
        find_winner(bids)
    elif should_continue == 'yes':
        clear()
