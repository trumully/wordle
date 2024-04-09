import pytest
from wordle.result import get_result


def test_get_result():
    title = "Wordle"
    guesses = ["grape", "peach", "melon", "fruit", "apple"]
    word = "apple"
    max_guesses = 5
    colors = {"correct": "🟩", "misplaced": "🟨", "incorrect": "⬛️"}

    result = get_result(title, guesses, word, max_guesses, colors)
    split_result = result.split("\n")

    assert isinstance(result, str)
    assert f"{title} ({len(guesses)}/{max_guesses})" in result
    assert split_result[1] == "⬛️⬛️🟨🟨🟩"
    assert split_result[2] == "🟨🟨🟨⬛️⬛️"
    assert split_result[3] == "⬛️🟨🟨⬛️⬛️"
    assert split_result[4] == "⬛️⬛️⬛️⬛️⬛️"
    assert split_result[5] == "🟩🟩🟩🟩🟩"


def test_get_result_no_guesses():
    title = "Wordle"
    guesses = []
    word = "apple"
    max_guesses = 5
    colors = {"correct": "🟩", "misplaced": "🟨", "incorrect": "⬛️"}

    with pytest.raises(ValueError):
        get_result(title, guesses, word, max_guesses, colors)
