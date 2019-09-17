from spaceman import is_guess_in_word, get_guessed_word, switch_secret_word
# Test functions


def test_is_guess():
    """A test function for is_guess_in_word()."""
    assert not is_guess_in_word("l", "love"), "is_guess_in_word is working as planned."


def test_get_guessed():
    """A function to test get_guessed_word()."""
    assert get_guessed_word("pizza", ["p", "i", "z", "z", "a"]) == "igloo", "get_guessed_word is working as expected."


def test_switch():
    """A function to test switch_secret_word()."""
    assert len(switch_secret_word("games")) == 5, "switch secret word is not replacing words of same length."


if __name__ == '__main__':
    test_switch()
    # test_get_guessed()
    # test_is_guess()
