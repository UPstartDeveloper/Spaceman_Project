import spaceman
# Test functions


def test_is_guess():
    """A test function for is_guess_in_word()."""
    result = spaceman.is_guess_in_word("l", "love")
    assert result


def test_get_guessed():
    """A function to test get_guessed_word()."""
    result = spaceman.get_guessed_word("pizza", ["z", "p", "i", "a"])
    assert result == "pizza", "get_guessed_word is not working as expected."


def test_switch_len():
    """A function to test switch_secret_word().
    This test checks to make sure the new word is the same
    length as the input word."""
    new_word = spaceman.switch_secret_word("games")
    assert len(new_word) == len("games"), "switched word is not same length."


def test_divide():
    """A function to test switch_secret_word().
    This test checks to make sure the new word has similar spelling
    to the first secret word."""
    result_str = spaceman.divide()
    assert not len(result_str) == 38, "Divider line is not correct length."
