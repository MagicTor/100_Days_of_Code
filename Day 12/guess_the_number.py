import art
import random

EASY_LEVEL_TURNS = 10
HARD_LEVEL_TURNS = 5

def check_score(guess, number, turns):
    """Checks the guess with the answer, and returns the number of turns remaining."""
    if guess < number:
        print("Too low.\nGuess again.")
        return turns - 1
    elif guess > number:
        print("Too high.\nGuess again.")
        return turns - 1
    else:
        print("You got it!")

def set_difficulty():
    difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ")
    if difficulty == 'easy':
        return EASY_LEVEL_TURNS
    elif difficulty == 'hard':
        return HARD_LEVEL_TURNS

def game():
    print(art.logo)
    print("Welcome to the number guessing game!")
    print("I'm thinking of a number between 1 and 100.")

    number = random.randint(1, 100)
    print(f"Pssst, the correct answer is {number}")

    turns = set_difficulty()
    guess = None
    while turns > 0 and guess != number:
        print(f"You have {turns} attempts remaining to guess the number.")
        guess = int(input("Make a guess: "))
        turns = check_score(guess, number, turns)
    if turns == 0:
        print("You've run out of guesses, you lose.")
        return
game()