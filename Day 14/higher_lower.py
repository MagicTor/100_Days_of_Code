from game_data import data
import art
import random


def is_correct(a, b):
    """Returns an updated score of the game based on the two current contestants"""
    guess = input("Who has more followers? Type 'A' or 'B': ").lower()
    if a > b:
        return guess == 'a'
    else:
        return guess == 'b'


def get_contestant(index=None):
    """Prints a random contestant from data and returns the follower_count"""
    if index == None:
        index = random.choice(data)
    print(index['name'] + ', a ' + index['description'] + ', from ' + index['country'])
    return index


index_A = random.choice(data)
score = 0
game_over = False
while not game_over:
    print(art.logo)

    print("Contestant A:", end=" ")
    get_contestant(index_A)
    print(art.vs)
    print("Contestant B:", end=" ")
    index_B = get_contestant()

    if is_correct(index_A['follower_count'], index_B['follower_count']):
        score += 1
        print(f"You're right! Current score: {score}.")
        index_A = index_B
    else:
        game_over = True
        print(f"Sorry, that's wrong. Final score: {score}")
