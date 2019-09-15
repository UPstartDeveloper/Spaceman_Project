import random
import string  # Credit to https://stackoverflow.com/questions/16060899/alphabet-range-on-python
'''
Attempt at displaying image of a spaceman using ASCII art.
1. Image from here:
http://www.howmanyarethere.net/how-many-astronauts-walked-on-the-moon-surface/
2. Image generated from this online tool:
https://manytools.org/hacker-tools/convert-images-to-ascii-art/go
'''
from PIL import Image
image = Image.open('astronaut.png')


def generate_words_list():
    """
    A function that creates a list of words from words.txt.
    Input: words.txt file
    Output: list of words @words_list
    """
    f = open('words.txt', 'r')
    words_list = f.readlines()
    f.close()
    words_list = words_list[0].split(' ')
    return words_list


def load_word(words_list):
    """
    A function that chooses the word user needs to guess.
    Input: @param words_list a list of str objects
    Output: str object @secret_word
    """
    secret_word = random.choice(words_list)
    return secret_word

'''
def switch_secret_word(secret_word):
    """
     A function to switch the secret word for another (Sinister Spaceman).
     Input: @param secret_word a string the user has to guess.
     Output: another str object @new_secret the user must guess instead.
     Check words.txt for all words of same length as secret_word, then traverse
     that list for words with same letters,
     and in the same indices as guessed by user so far.
     """
    substitute_words = list()  # captures words of equal length to secret_word
    all_words = generate_words_list()

    # stores letters user has correct so far in secret_word
    guess_so_far = get_guessed_word(secret_word, letters_guessed)
    for word in all_words:
        if len(word) == len(secret_word):
            substitute_words.append(word)  # add all words of same length

    # get rid of spaces and underscores from get_guessed_word
    check_this_str = ""
    for letter in guess_so_far:
        if letter.isalpha():
            check_this_str += letter

    # delete words without same letters
    for word in substitute_words:
        for i in range(len(check_this_str)):
            if check_this_str[i].isalpha() and check_this_str[i] not in word:
                substitute_words.remove(word)
    new_secret = random.choice(substitute_words)

    return new_secret
'''

def is_word_guessed(secret_word, letters_guessed):
    """
     A function to check if all letters of the secret word have been guessed.
     Input: @param str object secret_word
            @param list object letters_guessed.
     Output: True if all letters of secret_word appear in letters_guessed,
     False otherwise.
     """
    for i in range(len(secret_word)):
        if not secret_word[i] in letters_guessed:
            return False
    return True


def get_guessed_word(secret_word, letters_guessed):
    """
    A function to return a str after each guess to represent user's progress.
    Input: @param str secret_word
           @param list letters_guessed
    Output: str object guess_so_far
    Looks for all letters in secret_word that appear in letters_guessed.
    Matches are shown.
    Letters in secret_word not found are represented by "_ ".
    """
    guess_so_far = ""
    for letter in secret_word:
        if letter in letters_guessed:
            guess_so_far += letter
        else:
            guess_so_far += "_ "
    return guess_so_far


def is_guess_in_word(guess, secret_word):
    """
    A function to check if the guessed letter is in the secret word.
    Input: @param str object guess
           @param str object secret_word
    Output: True or False.
    Checks to see if single letter entered by user appears in secret_word.
    """
    return (guess in secret_word)


def display_alpha(alphabet, guessed_letters):
    """
    A function to display letters of the alphabet not yet guessed.
    Input: @param list object alphabet
           @param list object guessed_letters
    Output: None.
    alphabet stores all 26 letters at start of the game.
    """

    # Remove letters from alphabet which appear in guessed_letters
    if not len(guessed_letters) == 0:
        for i in range(len(guessed_letters)):
            if guessed_letters[i] in alphabet:
                remove_letter = guessed_letters[i]
                alphabet.remove(remove_letter)

    # Display contents of alphabet to user.
    for letter in alphabet:
        print(letter, end="")
    print("")


def divide():
    """
    A function that prints a dashed line to divide the output into sections.
    Input: none.
    Output: none.
    """
    print("-------------------------------------")


def add_to_incorrect(letter, list_of_letters):
    """
    A function that builds a list of incorrect guesses.
    Input: @param str object letter, @param list object list_of_letters
    Output: none.
    """
    list_of_letters.append(letter)


def display_incorrect(list_of_incorrect):
    """
    A function that displays a list of incorrect guesses.
    Input: @param list object list_of_incorrect
    Output: none.
    """
    print("Here are the letters you guessed incorrectly:", end=" ")
    for letter in list_of_incorrect:
        print(letter, end="")
    print("")  # moves cursor to next line for formatting output


def spaceman(secret_word):
    """
    A function that controls the game of spaceman.
    Input: @param str object secret_word.
    Output: none.
    """
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

        # if the user enters a valid guess
        if user_guess not in letters_guessed:
            letters_guessed.append(user_guess)  # add the letter to letters_guessed

        # if the guess is correct and more letters need to be guessed
        if is_guess_in_word(user_guess, secret_word) and not is_word_guessed(secret_word, letters_guessed):
            print("Your guess appears in the word!")
            print(get_guessed_word(secret_word, letters_guessed))
            print(f"You have {guesses_left} incorrect guesses left.")
            print("These letters haven't been guessed yet: ", end="")
            display_alpha(alpha, letters_guessed)
            print("here")
            # secret_word = switch_secret_word(secret_word)  # switch the secret word
            # print("You have a new word to guess: {}".format(secret_word))  # *used for debugging switch_secret_word*
            # divide()
        # if the whole word has been guessed
        elif is_word_guessed(secret_word, letters_guessed):
            print("Your guess appears in the word!")
            print("You won!")
            display_incorrect(incorrect_guessed_letters)
        # if the guess is wrong, and the user is out of tries
        if not is_guess_in_word(user_guess, secret_word) and guesses_left == 1:
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


'''
Creating list of alphabetic letters.
Credit to https://stackoverflow.com/questions/16060899/alphabet-range-on-python
'''
secret_word = load_word(generate_words_list())
alpha = list(string.ascii_lowercase)
letters_guessed = list()

# Loops through game until user ready to quit.
control = "Yes"
while control == "Yes" or control == "yes":
    spaceman(secret_word)
    letters_guessed = []
    secret_word = load_word(generate_words_list())
    control = input("Would you like to play again? Enter 'Yes' or 'No': ")

'''
Main function used for debugging.
if __name__ == '__main__':
    spaceman()
'''
