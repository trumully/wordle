from dataclasses import dataclass

from wordle.utils.colors import Color


@dataclass(frozen=True, kw_only=True)
class Rules:
    """The rules for the game Wordle."""

    title: str
    max_guesses: int
    word_length: int
    colors: dict[str, Color]


def default_rules() -> Rules:
    """The default rules for the game Wordle. In a regular game of Wordle, the player
    has 6 guesses to guess the secret word.

    :return: The default rules for the game Wordle.
    :rtype: Rules
    """
    colors = {
        "correct": Color.GREEN,
        "misplaced": Color.YELLOW,
        "incorrect": Color.WHITE,
    }
    return Rules(title="Wordle", max_guesses=6, word_length=5, colors=colors)
