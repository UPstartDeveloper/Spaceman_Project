import random


def load_word():
    '''
    A function that reads a text file of words and randomly selects one to use
    as the secret word from the list.
    Returns:
           string: The secret word to be used in the spaceman guessing game
    '''
    f = open('words.txt', 'r')
    words_list = f.readlines()
    f.close()

    words_list = words_list[0].split(' ')
    secret_word = random.choice(words_list)
    return secret_word


# Checks if all the letters of the secret word have been guessed.
def is_word_guessed(secret_word, letters_guessed):
    for i in range(len(secret_word)):
        if not secret_word[i] in letters_guessed:
            return False
    return True


# Returns a string after each guess to represent user's progress
def get_guessed_word(secret_word, letters_guessed):
    guess_so_far = ""
    for i in range(len(letters_guessed)):
        if i > len(secret_word):
            return guess_so_far
        if is_guess_in_word(letters_guessed[i], secret_word):
            # decide if this index is the right place for the guessed letter
            if letters_guessed[i] == secret_word[i]:
                guess_so_far += letters_guessed[i] + " "
        else:
            guess_so_far += "_ "  # space reminds user of length of word
    return guess_so_far


def is_guess_in_word(guess, secret_word):
    # A function to check if the guessed letter is in the secret word
    return (guess in secret_word)


def spaceman(secret_word):
    '''
    A function that controls the game of spaceman. Will start spaceman in the command line.

    Args:
      secret_word (string): the secret word to guess.

    '''

    # TODO: show the player information about the game according to the project spec

    # TODO: Ask the player to guess one letter per round and check that it is only one letter

    # TODO: Check if the guessed letter is in the secret or not and give the player feedback

    # TODO: show the guessed word so far

    # TODO: check if the game has been won or lost
# These function calls that will start the game


secret_word = load_word()
spaceman(load_word())
