import random
import hangman_art
import hangman_words

# Welcome Message
print(hangman_art.logo)
print("Welcome to the game and good luck!\n")

chosen_word = random.choice(hangman_words.word_list)
display = ['_' for i in range(len(chosen_word))]
lives = 6
letters_guessed = []

for word in hangman_words.word_list:
    if 'ani' in word:
        print(word)

while '_' in display and lives > 0:
    guess = input("Guess a letter: ").lower()

    # Inform the user on their guesses
    letters_guessed.append(guess)
    print("You have guessed", letters_guessed)

    if guess in chosen_word:
        for i in range(len(chosen_word)):
            if chosen_word[i] == guess:
                display[i] = guess
    else:
        lives -= 1
        print(f"You guessed '{guess}', that's not in the word. You lose a life.")

    print(display)
    print(hangman_art.stages[lives])

if lives > 0:
    print("You survived!")
else:
    print("You didn't survive and now you're meat for the pigs")