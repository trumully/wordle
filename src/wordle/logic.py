from dataclasses import dataclass, field

from wordle.utils import rules, colors, helpers


@dataclass
class GameLogic:
    """Handle the logic for the game Wordle."""

    rules: rules.Rules
    secret_word: str
    guesses: list[str] = field(default_factory=list)
    known_letters: list[str] = field(default_factory=list)

    def has_lost(self) -> bool:
        return len(self.guesses) >= self.max_guesses

    def has_won(self) -> bool:
        return self.secret_word in self.guesses

    def game_over(self) -> bool:
        return self.has_lost() or self.has_won()

    def get_correct_letters(self) -> list[str]:
        return helpers.get_correct_letters(self.secret_word, self.current_guess)

    def get_incorrect_letters(self) -> list[str]:
        return helpers.get_incorrect_letters(self.secret_word, self.current_guess)

    def get_misplaced_letters(self) -> list[str]:
        return helpers.get_misplaced_letters(self.secret_word, self.current_guess)

    def is_valid_word(self, word: str) -> bool:
        return len(word) == self.rules.word_length and word.isalpha()

    def update_known_letters(self) -> None:
        letters = self.get_correct_letters() + self.get_misplaced_letters()
        for letter in letters:
            if letter not in self.known_letters:
                self.known_letters.append(letter)

    @property
    def current_guess(self) -> str:
        return self.guesses[-1] if self.guesses else ""

    @property
    def title(self) -> str:
        return self.rules.title

    @property
    def max_guesses(self) -> int:
        return self.rules.max_guesses

    @property
    def colors(self) -> dict[str, colors.Color]:
        return self.rules.colors
