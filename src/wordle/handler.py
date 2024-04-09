from dataclasses import dataclass
import sys

from wordle.utils.colors import Color


@dataclass(frozen=True)
class Handler:
    """Handle input and output for the game."""

    def get_guess(self, *, prompt: str = "") -> str:
        """Get a guess from the user.

        :param max_length: The maximum length of the guess.
        :type max_length: int
        :return: The guess from the user.
        :rtype: str
        """
        return input(prompt)

    def display_text(self, text_to_display: str) -> None:
        """Display text in the terminal.

        :param text_to_display: The text to display.
        :type text_to_display: str
        """
        sys.stdout.write(f"{text_to_display}\n")

    def display_guess(
        self,
        guess: str,
        word: str,
        letters: dict[str, list[str]],
        colors: dict[str, Color],
    ) -> None:
        """Display the guess in the game. Correct, misplaced, and incorrect letters are
        colored their respective colors. If a letter is correct/misplaced, any duplicate
        letters that aren't also in the secret word are colored as incorrect.

        :param guess: The guess in the game.
        :type guess: str
        :param word: The secret word in the game.
        :type word: str
        :param letters: The correct, misplaced, and incorrect letters in the game.
        :type letters: dict[str, list[str]]
        :param colors: The colors for the correct, misplaced, and incorrect letters.
        :type colors: dict[str, Color]
        """
        result = []
        colored = []
        for letter, secret in zip(guess, word):
            if letter in colored and letter != secret:
                result.append(colors["incorrect"].colorize(letter))
            else:
                colored.append(letter)

                if letter in letters["correct"] and letter == secret:
                    result.append(colors["correct"].colorize(letter))
                elif letter in letters["misplaced"]:
                    result.append(colors["misplaced"].colorize(letter))
                else:
                    result.append(colors["incorrect"].colorize(letter))

        self.display_text("".join(result))

    def display_known_letters(self, letters: str) -> None:
        """Display the known letters in the game.

        :param letters: The known letters in the game.
        :type letters: str
        """
        self.display_text(f"Known letters: {letters}\n")

    def refresh_known_letters(self, line: int, letters: str) -> None:
        """Refresh the known letters in the game.

        :param letters: The known letters in the game.
        :type letters: str
        """
        self.replace_line(line, f"Known letters: {letters}")

    def clear_line(self, *, amount: int = 1) -> None:
        """Clear a line in the terminal.

        :param amount: The number of lines to track back to, defaults to 1
        :type amount: int, optional
        """
        sys.stdout.write(f"\x1b[{amount}A")
        sys.stdout.write("\x1b[2K")

    def replace_line(self, amount: int, text: str) -> None:
        """Replace a line in the terminal then return to the original position.

        :param amount: The number of lines to track back to.
        :type amount: int
        :param text: The text to replace the line with.
        :type text: str
        """
        self.clear_line(amount=amount)
        sys.stdout.write(f"{text}\n")
        sys.stdout.write(f"\x1b[{amount}B")
