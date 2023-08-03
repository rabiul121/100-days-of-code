from replit import clear

from blind_bid_art import logo

print(logo)
bids = {}
bids_finished = False


def find_winner(bidding_record):
    highest_bid = 0
    winner = ""
    for bidder in bidding_record:
        bid_amount = bidding_record[bidder]
        if bid_amount > highest_bid:
            highest_bid = bid_amount
            winner = bidder
    print(f"The winner is {winner} with a bid of ${highest_bid}.")


while not bids_finished:
    name = input("What is your name?: ")
    amount = int(input("What's your bid?: $"))
    bids[name] = amount
    should_continue = input("Are there any other bidders? Type 'yes' or 'no' \n")
    if should_continue == "no":
        bids_finished = True
        find_winner(bids)
    elif should_continue == "yes":
        clear()
