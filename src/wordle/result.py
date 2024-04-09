from wordle.utils.helpers import (
    get_correct_letters,
    get_misplaced_letters,
    get_incorrect_letters,
)

BOXES: dict[str, str] = {
    "correct": "🟩",
    "misplaced": "🟨",
    "incorrect": "⬛️",
}


def get_result(
    title: str,
    guesses: list[str],
    word: str,
    max_guesses: int,
    colors: dict[str, str] = BOXES,
) -> str:
    """Return the result of the game. Correct, misplaced, and incorrect letters are
    represented by a colored box.

    Wordle (5/6)
    🟩🟩🟨⬛️⬛️
    🟩⬛️🟨⬛️⬛️
    🟨⬛️⬛️⬛️🟩
    🟩🟨⬛️⬛️🟨
    🟩🟩🟩🟩🟩

    In this example, green is for correct, yellow for misplaced, and black for
    incorrect.

    :param title: The title of the game.
    :type title: str
    :param guesses: The guesses in the game.
    :type guesses: list[str]
    :param word: The secret word in the game.
    :type word: str
    :param max_guesses: The maximum number of guesses in the game.
    :type max_guesses: int
    :param colors: The colors for the correct, misplaced, and incorrect letters.
                   Defaults to BOXES.
    :type colors: dict[str, str]
    :return: The result of the game.
    :rtype: str
    """
    if not guesses:
        raise ValueError("No guesses provided.")

    final = [f"{title} ({len(guesses)}/{max_guesses})"]

    for guess in guesses:
        result = ""
        colored = []

        letters = {
            "correct": get_correct_letters(guess, word),
            "misplaced": get_misplaced_letters(guess, word),
            "incorrect": get_incorrect_letters(guess, word),
        }
        for letter, secret in zip(guess, word):
            if letter in colored and letter != secret:
                result += colors["incorrect"]
            else:
                colored.append(letter)

                if letter in letters["correct"] and letter == secret:
                    result += colors["correct"]
                elif letter in letters["misplaced"]:
                    result += colors["misplaced"]
                else:
                    result += colors["incorrect"]

        final.append(result)

    return "\n".join(final)
