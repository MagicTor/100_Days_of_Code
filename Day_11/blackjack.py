import art
import random

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

def declare_winner(user, comp):
    if user == 21:
        print("You got Black Jack. You win!")
    elif user > 21:
        print("You went over. You lose 😭")
    elif comp == 21:
        print("Lose, opponent has Blackjack 😱")
    elif comp > 21:
        print("Opponent went over. You win 😁")
    elif user == comp:
        print("Draw 🙃")
    elif user > comp:
        print("You win.")
    else:
        print("You lose 😤")

def computers_turn(hand):
    score = get_score(hand)
    while score < 17:
        hand.append(random.choice(cards))
        score = get_score(hand)
    return hand, score


def get_score(hand):
    if sum(hand) > 21:
        if 11 in hand:
            hand[hand.index(11)] = 1
    return sum(hand)


def play_game():
    print(art.logo)

    # Getting the first hands
    my_hand = [random.choice(cards), random.choice(cards)]
    computer_hand = [random.choice(cards)]

    my_score = get_score(my_hand)

    game_over = False
    while not game_over:
        print(f"Your cards: {my_hand}, current score: {my_score}")
        print(f"Computer's first card: {computer_hand}")

        if input("Type 'y' to get another card, type 'n' to pass: ") == 'y':
            my_hand.append(random.choice(cards))
            my_score = get_score(my_hand)
            if my_score > 21:
                game_over = True
        else:
            game_over = True

    computer_hand, computer_score = computers_turn(computer_hand)
    print(f"Your final hand: {my_hand}, final score: {my_score}")
    print(f"Computer's final hand: {computer_hand}, final score: {computer_score}")

    declare_winner(my_score, computer_score)


while input("Do you want to play a game of Blackjack? Type 'y' or 'n': ") == 'y':
    play_game()
