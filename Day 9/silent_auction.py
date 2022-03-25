from replit import clear
import art

def get_winner(record):
    highest_bid = 0
    winner = ''
    for bidder in record:
        if record[bidder] > highest_bid:
            highest_bid = record[bidder]
            winner = bidder
    return winner

print(art.logo)
print("Welcome to the secret auction program.")

auction = {}
more_bidders = 'yes'
while more_bidders == 'yes':
    name = input("What is your name?: ")
    bid = float(input("What's your bid?: $"))

    auction[name] = bid

    more_bidders = input("Are there any other bidders? Type 'yes or 'no'.\n")
    if more_bidders == 'yes':
        clear()

winner = get_winner(auction)

print(f"The winner is {winner} with a bid of ${auction[winner]}")