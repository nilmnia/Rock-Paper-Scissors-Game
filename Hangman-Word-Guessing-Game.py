
import random

words = ["dragon", "vampire", "galaxy", "treasure",
         "zombie", "mermaid", "rainbow", "dinosaur"]

word = random.choice(words)
guessed_letters = []
attempts = 6

print("Welcome to Hangman!")
print("Guess the hidden word.")
print("You have 6 attempts.")

while attempts > 0:
    display_word = ""

    for letter in word:
        if letter in guessed_letters:
            display_word += letter + " "
        else:
            display_word += "_ "

    print("\nWord:", display_word)
    print("Attempts left:", attempts)

    if all(letter in guessed_letters for letter in word):
        print("\nCongratulations! You won!")
        break

    guess = input("Guess a letter: ").lower().strip()

    if len(guess) != 1 or not guess.isalpha():
        print("Please enter only one letter!")
        continue

    if guess in guessed_letters:
        print("You already guessed this letter!")
        continue

    guessed_letters.append(guess)

    if guess in word:
        print("Correct guess!")
    else:
        print("Wrong guess!")
        attempts -= 1

if attempts == 0:
    print("\nGame over!")
    print("The correct word was:", word)
