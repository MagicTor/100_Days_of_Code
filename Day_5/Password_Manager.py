# Password Generator Project
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v',
           'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R',
           'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '@', '%', '&', '*', '+', '-', '(', ')', '{', '}', '[', ']', '\\', '/', '.', ',', '\'', ':', ';']

print("Welcome to the PyPassword Generator!")
nr_letters = int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))


password = []
while nr_numbers + nr_symbols + nr_letters > 0:  # Running the loop until there are no more characters in the password to choose from

    # Create a new list with all possible characters
    new_list = []
    if nr_letters > 0:
        new_list += letters
    if nr_numbers > 0:
        new_list += numbers
    if nr_symbols > 0:
        new_list += symbols

    # Get a random character from the new list
    password_character = random.choice(new_list)

    # Update the password
    password.append(password_character)

    # Shorten the password length by either 1 letter, symbol, or number
    if password_character in numbers:
        nr_numbers -= 1
    elif password_character in symbols:
        nr_symbols -= 1
    else:               # Else it will be in the letters list
        nr_letters -= 1

print("".join(password))