import random
import string  # Credit to https://stackoverflow.com/questions/16060899/alphabet-range-on-python


def load_word():
    f = open('words.txt', 'r')
    words_list = f.readlines()
    f.close()
    # This function decides which word the user will guess.
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


# A function that controls the game of spaceman.
def spaceman(secret_word):
    guesses_left = 7
    print("Welcome to Spaceman! \n" +
          "The secret word contains {} letters. \n".format(len(secret_word)) +
          "You have {} incorrect guesses, please enter one letter per round."
          .format(guesses_left))
    while not is_word_guessed(secret_word, letters_guessed) and not guesses_left == 0:
        divide()
        user_guess = input("Enter a letter: ")
        while not len(user_guess) == 1:
            print("You may only guess one letter at a time.")
            divide()
            user_guess = input("Please enter a new letter as your guess: ")
        while user_guess in letters_guessed:
            print("You have already guessed that letter before.")
            divide()
            user_guess = input("Please enter a new letter as your guess: ")
        if user_guess not in letters_guessed:
            letters_guessed.append(user_guess)

        # if the guess appears in the word
        if is_guess_in_word(user_guess, secret_word):
            print("Your guess appears in the word!")
            # if the whole word has been guessed
            if is_word_guessed(secret_word, letters_guessed):
                print("You won!")
            else:
                print(get_guessed_word(secret_word, letters_guessed))
                print(f"You have {guesses_left} incorrect guesses left.")
                print("These letters haven't been guessed yet: ", end="")
                display_alpha(alpha, letters_guessed)
        # if the guess is wrong, and the user is out of tries
        elif not is_guess_in_word(user_guess, secret_word) and guesses_left == 1:
            guesses_left -= 1
            print("Sorry you didn't win, try again!")
            print(f"The word was: {secret_word}.")
        # if the guess is wrong, and user still has guesses guesses_left
        elif not is_guess_in_word(user_guess, secret_word):
            print("Sorry your guess is not in the word, try again.")
            guesses_left -= 1
            print(f"You have {guesses_left} incorrect guesses left.")
            print(get_guessed_word(secret_word, letters_guessed))
            print("These letters haven't been guessed yet: ", end="")
            display_alpha(alpha, letters_guessed)

# These function calls will start the game

alpha = list(string.ascii_lowercase)  # Credit to https://stackoverflow.com/questions/16060899/alphabet-range-on-python
secret_word = load_word()
letters_guessed = list()

control = "Yes"
while control == "Yes" or control == "yes":
    spaceman(secret_word)
    control = input("Would you like to play again? Enter 'Yes' or 'No': ")
