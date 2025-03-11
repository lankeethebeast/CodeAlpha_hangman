import random


def choose_word():
    words = ["python", "java", "hangman", "programming", "developer"]
    return random.choice(words)


def display_word(word, guessed_letters):
    return " ".join([letter if letter in guessed_letters else "_" for letter in word])


def hangman():
    word = choose_word()
    guessed_letters = set()
    attempts = 6  # Maximum attempts

    print("Welcome to Hangman!")
    while attempts > 0:
        print("\n" + display_word(word, guessed_letters))
        guess = input("Guess a letter: ").lower()

        if guess in guessed_letters:
            print("You already guessed that letter.")
        elif guess in word:
            guessed_letters.add(guess)
            if set(word) == guessed_letters:
                print("\nYou won! The word was:", word)
                return
        else:
            attempts -= 1
            print(f"Wrong guess! Attempts left: {attempts}")

    print("\nGame over! The word was:", word)


if __name__ == "__main__":
    hangman()
