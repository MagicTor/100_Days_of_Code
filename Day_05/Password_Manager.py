# Password Generator Project
import math
import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v',
           'w', 'x', 'y', 'z']
letters += [letter.upper() for letter in letters]
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['`', '~', '!', '@', '#', '$', '%', '^', '&', '*', '+', '-', '_', '=', '(', ')', '{', '}', '[', ']', '\\',
           '/', '|', '.', ',', ':', ';', '<', '>', '?']

password_characters = letters + numbers + symbols

class password_generator:

    def __init__(self):
        self.password = self.generate_password()

        print(self.generate_password())

    def generate_password(self, pass_length=14):
        if pass_length > 2:
            nr_numbers = math.ceil(0.109 * pass_length)
            nr_symbols = math.ceil(0.326 * pass_length)
            nr_letters = pass_length - nr_numbers - nr_symbols
            password_list = [random.choice(numbers) for char in range(nr_numbers)]
            password_list += [random.choice(symbols) for char in range(nr_symbols)]
            password_list += [random.choice(letters) for char in range(nr_letters)]
            random.shuffle(password_list)
        else:
            password_list = [random.choice(password_characters) for char in range(pass_length)]

        return "".join(password_list)
