import math
import art

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
            'v', 'w', 'x', 'y', 'z']


def caesar(start_text, shift_amount, cipher_direction):
    end_text = ''
    if cipher_direction == 'decode':
        shift_amount *= -1
    for char in start_text:
        if char in alphabet:
            index = alphabet.index(char) + shift_amount
            index = index % 26
            end_text += alphabet[index]
        else:
            end_text += char
    print(f"The {cipher_direction}d text is {end_text}\n")


# Welcome Screen
print(art.logo)

ans = 'yes'
while ans == 'yes':
    # Gathering input
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))

    caesar(text, shift, direction)
    ans = input("Would you like to run the program again:\n")