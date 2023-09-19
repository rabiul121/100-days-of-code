import random

# from replit import clear

from art import logo, vs
from follower_data import data


def format_data(account):
    """Format the account data into printable format"""
    account_name = account['name']
    account_description = account['description']
    account_country = account['country']
    return f"{account_name}, a {account_description}, from {account_country}"


def check_answer(guess, a_followers, b_followers):
    """Use if statement to check if the user is correct and returns if they got it right."""
    if a_followers > b_followers:
        return guess == 'a'
    else:
        return guess == 'b'


print(logo)
score = 0
account_b = random.choice(data)

game_should_continue = True

while game_should_continue:
    # Generate a random account from tha game data
    account_a = account_b
    account_b = random.choice(data)

    while account_a == account_b:
        account_b = random.choice(data)

    print(f"Compare A: {format_data(account_a)}.")

    print(vs)

    print(f"Against B: {format_data(account_b)}.")

    guess = input("Who has more followers? Type 'A' or 'B': ").lower()

    a_followers_count = account_a["follower_count"]
    b_followers_count = account_b["follower_count"]
    is_correct = check_answer(guess, a_followers_count, b_followers_count)
    # clear()
    # print(logo)
    if is_correct:
        score += 1
        print(f"You're right! Current score: {score}.")
    else:
        game_should_continue = False
        print(f"Sorry, that's wrong. Final Score: {score}.")
