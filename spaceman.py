import random
from PIL import Image
import string  # Credit to https://stackoverflow.com/questions/16060899/alphabet-range-on-python
'''
Attempt at displaying image of a spaceman using ASCII art.
1. Image from here:
http://www.howmanyarethere.net/how-many-astronauts-walked-on-the-moon-surface/
2. Image generated from this online tool:
https://manytools.org/hacker-tools/convert-images-to-ascii-art/go
'''
image = Image.open('astronaut.png')


# A function that creates a list of words from words.txt.
def generate_words_list():
    f = open('words.txt', 'r')
    words_list = f.readlines()
    f.close()
    words_list = words_list[0].split(' ')
    return words_list


# A function that chooses the word user needs to guess.
def load_word(words_list):
    secret_word = random.choice(words_list)
    return secret_word


# A function to switch the secret word for another (Sinister Spaceman).
def switch_secret_word(secret_word):
    new_secret = ""  # return value
    same_len = list()  # captures words of equal length to secret_word
    all_words = generate_words_list()
    for word in all_words:
        if len(word) == len(secret_word):
            


# Checks if all the letters of the secret word have been guessed.
def is_word_guessed(secret_word, letters_guessed):
    for i in range(len(secret_word)):
        if not secret_word[i] in letters_guessed:
            return False
    return True


# Returns a string after each guess to represent user's progress
def get_guessed_word(secret_word, letters_guessed):
    guess_so_far = ""
    for letter in secret_word:
        if letter in letters_guessed:
            guess_so_far += letter
        else:
            guess_so_far += "_ "
    return guess_so_far


# A function to check if the guessed letter is in the secret word.
def is_guess_in_word(guess, secret_word):
    return (guess in secret_word)


# A function to display letters of the alphabet not yet guessed.
def display_alpha(alphabet, guessed_letters):
    if not len(guessed_letters) == 0:
        for i in range(len(guessed_letters)):
            if guessed_letters[i] in alphabet:
                remove_letter = guessed_letters[i]
                alphabet.remove(remove_letter)

    for letter in alphabet:
        print(letter, end="")
    print("")


# A function that prints a dashed line to divide the output into sections.
def divide():
    print("-------------------------------------")


# A function that builds a list of incorrect guesses.
def add_to_incorrect(letter, list_of_letters):
    list_of_letters.append(letter)


# A function that displays a list of incorrect guesses.
def display_incorrect(list_of_incorrect):
    print("Here are the letters you guessed incorrectly:", end=" ")
    for letter in list_of_incorrect:
        print(letter, end="")
    print("")  # moves cursor to next line for formatting output


# A function that controls the game of spaceman.
def spaceman(secret_word):
    guesses_left = len(secret_word)
    incorrect_guessed_letters = list()
    print("Welcome to Spaceman! \n" +
          "The secret word contains {} letters. \n".format(len(secret_word)) +
          "You have {} incorrect guesses, please enter one letter per round."
          .format(guesses_left))
    # Enters a loop to prompt user for guesses
    while not is_word_guessed(secret_word, letters_guessed) and not guesses_left == 0:
        divide()
        user_guess = input("Enter a letter: ")
        # if the guess is longer than one letter:
        while not len(user_guess) == 1:
            print("You may only guess one letter at a time.")
            divide()
            user_guess = input("Please enter a single letter as your guess: ")
        # if the letter has already been guessed before
        while user_guess in letters_guessed:
            print("You have already guessed that letter before.")
            divide()
            print("These letters haven't been guessed yet: ", end="")
            display_alpha(alpha, letters_guessed)
            user_guess = input("Please enter a new letter as your guess: ")
        # if the user enters a valid guess, add to guessed letters
        if user_guess not in letters_guessed:
            letters_guessed.append(user_guess)

        # if the guess appears in the word
        if is_guess_in_word(user_guess, secret_word):
            print("Your guess appears in the word!")
            # if the whole word has been guessed
            if is_word_guessed(secret_word, letters_guessed):
                print("You won!")
                display_incorrect(incorrect_guessed_letters)
            else:  # more letters need to be guessed
                print(get_guessed_word(secret_word, letters_guessed))
                print(f"You have {guesses_left} incorrect guesses left.")
                print("These letters haven't been guessed yet: ", end="")
                display_alpha(alpha, letters_guessed)
        # if the guess is wrong, and the user is out of tries
        elif not is_guess_in_word(user_guess, secret_word) and guesses_left == 1:
            add_to_incorrect(user_guess, incorrect_guessed_letters)
            guesses_left -= 1
            print("Sorry you didn't win, try again!")
            print(f"The word was: {secret_word}.")
            print("Here is your Spaceman (opens in a new window): ")
            image.show()
            divide()
        # if the guess is wrong, and user still has guesses guesses_left
        elif not is_guess_in_word(user_guess, secret_word):
            add_to_incorrect(user_guess, incorrect_guessed_letters)
            print("Sorry your guess is not in the word, try again.")
            guesses_left -= 1
            print(f"You have {guesses_left} incorrect guesses left.")
            print(get_guessed_word(secret_word, letters_guessed))
            print("These letters haven't been guessed yet: ", end="")
            display_alpha(alpha, letters_guessed)


# These function calls will start the game
'''
Creating list of alphabetic letters.
Credit to https://stackoverflow.com/questions/16060899/alphabet-range-on-python
'''
secret_word = load_word(generate_words_list())
alpha = list(string.ascii_lowercase)
letters_guessed = list()

control = "Yes"
while control == "Yes" or control == "yes":
    spaceman(secret_word)
    letters_guessed = []
    secret_word = load_word(generate_words_list())
    control = input("Would you like to play again? Enter 'Yes' or 'No': ")
    image.close()
