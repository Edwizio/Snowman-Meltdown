import random
from ascii_art import STAGES

# List of secret words
WORDS = ["python", "git", "github", "snowman", "meltdown"]


def get_random_word():
    """Selects a random word from the list."""
    return WORDS[random.randint(0, len(WORDS) - 1)]


def display_game_state(mistakes, secret_word, guessed_letters):
    """
    This function receives the basic states of the game as argument and update their values according to
    the current condition of the game loop.
    """
    # Ensure we don't go out of bounds
    stage_index = min(mistakes, len(STAGES) - 1)
    print(STAGES[stage_index])

    # Build display version of the word
    display_word = ""
    for letter in secret_word:
        if letter in guessed_letters:
            display_word += letter + " "
        else:
            display_word += "_ "
    print("Word: ", display_word)
    print("\n")



def play_game():
    """
    This function is the responsible for the execution of game logic based on the current states using the
    predefined methods display_game_state() and get_random_word().
    """

    secret_word = get_random_word()
    guessed_letters = []
    mistakes = 0
    max_mistakes = 4

    # Game loop
    while mistakes < max_mistakes:
        display_game_state(mistakes, secret_word, guessed_letters)

        # Check if player has won
        if set(secret_word).issubset(set(guessed_letters)):
            print("Congratulations! You saved the snowman!")
            return

        # Prompt for input
        guess = input("Guess a letter: ").lower()

        # Validate guess
        if not guess.isalpha() or len(guess) != 1:
            print("Please enter a single letter.")
            continue
        if guess in guessed_letters:
            print("You already guessed that letter.")
            continue

        # Update state
        guessed_letters.append(guess)
        if guess not in secret_word:
            mistakes += 1
            print("Guess Incorrect!")

    # Game over
    display_game_state(mistakes, secret_word, guessed_letters)
    print("The snowman melted! The word was:", secret_word)



