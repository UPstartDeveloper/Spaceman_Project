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


# A function to check if the guessed letter is in the secret word.
def is_guess_in_word(guess, secret_word):
    return (guess in secret_word)


# A function that controls the game of spaceman.
def spaceman(secret_word):
    guesses_left = 7
    print("Welcome to Spaceman! \n" +
          "The secret word contains {} letters. \n".format(guesses_left) +
          "You have {} incorrect guesses, please enter one letter per round."
          .format(len(secret_word)))
    # while not guesses_left == 0:, commented so no infinite loop occurs
    print("-------------------------------------")


# These function calls will start the game
print(len("You have 7 incorrect guesses, please "))
secret_word = load_word()
spaceman(load_word())
