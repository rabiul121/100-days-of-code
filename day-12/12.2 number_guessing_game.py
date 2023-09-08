# Guess a number
import random
from art import logo

print(logo)
answer = int(random.randint(0, 100))
print("Welcome to the Number Guessing Game!")
print("I am thinking of a number between 1 and 100.")
# print(f"Pssst, the correct answer is {answer}")

level = input("Chose a difficulty level, type 'easy' or 'hard': ")
if level == 'easy':
    attempt = 10
elif level == 'hard':
    attempt = 5
else:
    print("Wrong input! Try again.")


def game():
    remaining_attempt = attempt - 1
    for _ in range(attempt):
        guess = int(input("Make a guess: "))
        if guess == answer:
            print(f"You got it! The answer was {answer}.")
            break
        elif guess < answer:
            print("Too low.")
            print("Guess again!")
            if remaining_attempt == 0:
                print("You have run out of guess, you lose!")
            else:
                print(f"You have {remaining_attempt} attempts remaining to guess!")
        else:
            print("Too high.")
            if remaining_attempt == 0:
                print("You have run out of guess, you lose!")
            else:
                print(f"You have {remaining_attempt} attempts remaining to guess!")

        remaining_attempt -= 1


game()
