from dataclasses import dataclass

from wordle.logic import GameLogic
from wordle.handler import Handler


@dataclass
class Game:
    """A game of Wordle."""

    logic: GameLogic
    handler: Handler

    def get_guess(self, *, prompt: str = "") -> str:
        """Get a valid guess from the user.

        :param prompt: The text the user is prompted with, defaults to ""
        :type prompt: str, optional
        :return: The valid guess from the user.
        :rtype: str
        """
        while not (
            self.logic.is_valid_word(guess := self.handler.get_guess(prompt=prompt))
        ):
            self.handler.replace_line(1, f"Invalid guess: {guess}")
        return guess

    def add_guess(self, guess: str) -> None:
        self.logic.guesses.append(guess)

    def play(self) -> None:
        """Play a game of Wordle."""
        self.handler.display_text(f"Welcome to {self.title}!")
        self.handler.display_known_letters(self.known_letters())
        while not self.game_over():
            guess = self.get_guess()
            self.add_guess(guess)
            self.logic.update_known_letters()
            self.handler.refresh_known_letters(
                2 + len(self.logic.guesses), self.known_letters()
            )
            self.display_guess()
        self.display_guess()

    def display_guess(self) -> None:
        """Display the current guess."""
        self.handler.clear_line()
        self.handler.display_guess(
            self.current_guess,
            self.logic.secret_word,
            {
                "correct": self.get_correct_letters(),
                "misplaced": self.get_misplaced_letters(),
                "incorrect": self.get_incorrect_letters(),
            },
            self.logic.colors,
        )

    def known_letters(self) -> str:
        """Return the known letters in the game."""
        return ", ".join(letters for letters in self.logic.known_letters)

    def has_lost(self) -> bool:
        return self.logic.has_lost()

    def has_won(self) -> bool:
        return self.logic.has_won()

    def game_over(self) -> bool:
        return self.logic.game_over()

    def get_correct_letters(self) -> list[str]:
        return self.logic.get_correct_letters()

    def get_incorrect_letters(self) -> list[str]:
        return self.logic.get_incorrect_letters()

    def get_misplaced_letters(self) -> list[str]:
        return self.logic.get_misplaced_letters()

    @property
    def current_guess(self) -> str:
        return self.logic.current_guess

    @property
    def title(self) -> str:
        return self.logic.title

    @property
    def max_guesses(self) -> int:
        return self.logic.max_guesses
