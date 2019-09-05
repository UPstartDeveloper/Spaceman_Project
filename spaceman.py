import random
import string  # Credit to https://stackoverflow.com/questions/16060899/alphabet-range-on-python


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


# A function to display letters of the alphabet not yet guessed.
def display_alpha(alphabet, guessed_letters):
    if not len(guessed_letters) == 0:
        '''
        for letter in alphabet:
            if letter in guessed_letters:
                alphabet.pop(letter)
        '''
        for i in range(len(guessed_letters)):
            if guessed_letters[i] in alphabet:
                remove_letter = guessed_letters[i]
                alphabet.remove(remove_letter)

    for letter in alphabet:
        print(letter, end="")
    print("")


# A function that controls the game of spaceman.
def spaceman(secret_word):
    guesses_left = 7
    print("Welcome to Spaceman! \n" +
          "The secret word contains {} letters. \n".format(len(secret_word)) +
          "You have {} incorrect guesses, please enter one letter per round."
          .format(guesses_left))
    while not (is_word_guessed(secret_word, letters_guessed) and guesses_left == 0):
        print("-------------------------------------")
        user_guess = input("Enter a letter: ")
        if user_guess not in letters_guessed:
            letters_guessed.append(user_guess)

        if is_guess_in_word(user_guess, secret_word):
            print("Your guess appears in the word!")
        else:
            print("Sorry your guess is not in the word, try again.")
            guesses_left -= 1
        if not guesses_left == 0:
            print(f"You have {guesses_left} incorrect guesses left.")
            print(get_guessed_word(secret_word, letters_guessed))
            display_alpha(alpha, letters_guessed)
        if is_word_guessed(secret_word, letters_guessed):
            print("You won!")
        if guesses_left == 0:
            print("Sorry you didn't win, try again!")
            print(f"The word was: {secret_word}.")


# These function calls will start the game
# print(len("You have 7 incorrect guesses, please "))
alpha = list(string.ascii_lowercase)  # Credit to https://stackoverflow.com/questions/16060899/alphabet-range-on-python
secret_word = load_word()
letters_guessed = list()
spaceman(secret_word)
