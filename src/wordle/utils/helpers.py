def get_correct_letters(guess: str, word: str) -> list[str]:
    """Return the correct letters in the guess that are in the word. The letters are
    returned in sorted order.

    :param guess: The guess the player made.
    :type guess: str
    :param word: The secret word.
    :type word: str
    :return: The correct letters in the guess that are in the word.
    :rtype: list[str]
    """
    return sorted({letter for letter, correct in zip(guess, word) if letter == correct})


def get_incorrect_letters(guess: str, word: str) -> list[str]:
    """Return the incorrect letters in the guess that are not in the word. The letters
    are returned in sorted order.

    :param guess: The guess the player made.
    :type guess: str
    :param word: The secret word.
    :type word: str
    :return: The incorrect letters in the guess that are not in the word.
    :rtype: list[str]
    """
    return sorted(set(guess) - set(word))


def get_misplaced_letters(guess: str, word: str) -> list[str]:
    """Return the misplaced letters in the guess that are in the word. The letters are
    returned in sorted order.

    :param guess: The guess the player made.
    :type guess: str
    :param word: The secret word.
    :type word: str
    :return: The misplaced letters in the guess that are in the word.
    :rtype: list[str]
    """
    correct = get_correct_letters(guess, word)
    return sorted(set(guess) & set(word) - set(correct))
