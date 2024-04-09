from wordle.game import Game
from wordle.utils.rules import default_rules
from wordle.logic import GameLogic
from wordle.handler import Handler
from wordle.result import get_result

# Ideally taking from a text file at random here.
your_secret_word = "sneak"

# Default rules for a regular game of Wordle.
logic = GameLogic(rules=default_rules(), secret_word=your_secret_word)
handler = Handler()
game = Game(logic, handler)
game.play()

# Get your result
result = get_result(
    logic.rules.title, logic.guesses, your_secret_word, logic.rules.max_guesses
)
print(result)
