# Guess a number game
import random

from art import logo
answer = int(random.randint(0, 100))
print("Welcome to the Number Guessing Game!")
print("I am thinking of a number between 1 and 100.")

print(logo)


def set_level():
    level = input("Chose a difficulty level, type 'easy' or 'hard': ")
    if level == 'easy':
        return 10
    elif level == 'hard':
        return 5


attempt = set_level()


def check_remaining_attempts():
    if attempt > 1:
        print("Guess again!")
    else:
        print("You have run out of guess, you lose!")


def game():
    global attempt
    for _ in range(attempt):
        print(f"You have {attempt} attempts remaining to guess!")
        guess = int(input("Make a guess: "))
        if guess == answer:
            print(f"You got it! The answer was {answer}.")
            return
        elif guess < answer:
            print("Too low.")
            check_remaining_attempts()

        elif guess > answer:
            print("Too high.")
            check_remaining_attempts()

        attempt -= 1


game()
