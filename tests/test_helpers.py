import pytest

from wordle.utils.helpers import get_misplaced_letters


def test_get_misplaced_letters():
    guess = "apple"
    word = "peach"
    result = get_misplaced_letters(guess, word)
    assert isinstance(result, list)
    assert sorted(result) == sorted(["p", "a", "e"])


def test_get_misplaced_letters_no_misplaced():
    guess = "grape"
    word = "apple"
    result = get_misplaced_letters(guess, word)
    assert isinstance(result, list)
    assert result == sorted(["a", "p"])


def test_get_misplaced_letters_all_misplaced():
    guess = "peach"
    word = "apple"
    result = get_misplaced_letters(guess, word)
    assert isinstance(result, list)
    assert sorted(result) == sorted(["p", "a", "e"])


@pytest.mark.parametrize(
    "guess, word, expected",
    [
        ("", "apple", []),
        ("apple", "", []),
        ("", "", []),
    ],
)
def test_get_misplaced_letters_empty_strings(guess, word, expected):
    result = get_misplaced_letters(guess, word)
    assert isinstance(result, list)
    assert result == expected
