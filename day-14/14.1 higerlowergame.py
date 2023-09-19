# Higher Lower Game
import random

from art import logo, vs
from follower_data import data

# Print the game logo
print(logo)

# print first compare info
compare_a = random.choice(data)
print(f"Compare A: {compare_a['name']}, a {compare_a['description']}, from {compare_a['country']}.")

# Print vs logo
print(vs)

# print second compare info
compare_b = random.choice(data)
print(f"Compare B: {compare_b['name']}, a {compare_b['description']}, from {compare_b['country']}.")

# user input to compare between two
user_input = input("Who has more followers? Type 'A' or 'B': ")


# compare function
def compare_follower():
    if user_input.lower() == 'a' and (compare_a['follower_count'] > compare_b['follower_count']):
        return True
    elif user_input.lower() == 'b' and (compare_a['follower_count'] < compare_b['follower_count']):
        return True
    else:
        return False


keep_playing = True


def game():
    score = 0
    if compare_follower():
        score += 1
        print(f"You are right! Current score: {score}.")
        compare_a = compare_b
        compare_b = random.choice(data)
    else:
        print(f"You are wrong! Current score: {score}.")
        return
