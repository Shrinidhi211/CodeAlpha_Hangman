import random

# List of predefined words
words = ["python", "programming", "computer", "developer", "software"]

# Select a random word
word = random.choice(words)

# Store correctly guessed letters
guessed_letters = set()

# Number of incorrect guesses allowed
max_attempts = 6
incorrect_attempts = 0

print("=" * 40)
print("       WELCOME TO HANGMAN GAME")
print("=" * 40)

print("Guess the word one letter at a time.")
print(f"You have {max_attempts} incorrect guesses.")

while incorrect_attempts < max_attempts:

    # Display the current state of the word
    display_word = ""

    for letter in word:
        if letter in guessed_letters:
            display_word += letter + " "
        else:
            display_word += "_ "

    print("\nWord:", display_word)
    print("Incorrect guesses:", incorrect_attempts, "/", max_attempts)

    # Check whether the player has guessed the entire word
    if all(letter in guessed_letters for letter in word):
        print("\nCongratulations!")
        print("You guessed the word:", word)
        break

    # Take input from user
    guess = input("Enter a letter: ").lower().strip()

    # Validate input
    if len(guess) != 1 or not guess.isalpha():
        print("Please enter exactly one letter.")
        continue

    # Check whether the letter was already guessed
    if guess in guessed_letters:
        print("You already guessed that letter.")
        continue

    # Add the guess to the guessed letters
    guessed_letters.add(guess)

    # Check the guess
    if guess in word:
        print("Correct guess!")
    else:
        incorrect_attempts += 1
        print("Wrong guess!")

else:
    print("\nGame Over!")
    print("The correct word was:", word)