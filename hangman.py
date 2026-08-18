import random
words = ["python", "programming", "computer", "developer", "software"]
word = random.choice(words)
guessed_letters = set()
max_attempts = 6
incorrect_attempts = 0

print("=" * 40)
print("       WELCOME TO HANGMAN GAME")
print("=" * 40)

print("Guess the word one letter at a time.")
print(f"You have {max_attempts} incorrect guesses.")

while incorrect_attempts < max_attempts:
    display_word = ""

    for letter in word:
        if letter in guessed_letters:
            display_word += letter + " "
        else:
            display_word += "_ "

    print("\nWord:", display_word)
    print("Incorrect guesses:", incorrect_attempts, "/", max_attempts)

    if all(letter in guessed_letters for letter in word):
        print("\nCongratulations!")
        print("You guessed the word:", word)
        break

    guess = input("Enter a letter: ").lower().strip()

    if len(guess) != 1 or not guess.isalpha():
        print("Please enter exactly one letter.")
        continue

    if guess in guessed_letters:
        print("You already guessed that letter.")
        continue

    guessed_letters.add(guess)

   
    if guess in word:
        print("Correct guess!")
    else:
        incorrect_attempts += 1
        print("Wrong guess!")

else:
    print("\nGame Over!")
    print("The correct word was:", word)
