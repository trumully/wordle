# Wordle

A small Wordle clone made in Python that can be run from the terminal.

## Table of Contents

- [Installation](#installation)
- [Usage](#usage)
- [License](#license)

## Installation
```shell
pip install poetry
poetry install
poetry build
```

## Usage
### Create a basic game:
```python
from wordle.game import Game
from wordle.utils.rules import default_rules
from wordle.logic import GameLogic
from wordle.handler import Handler

# Ideally taking from a text file at random here.
your_secret_word = "sneak"

# Default rules for a regular game of Wordle.
logic = GameLogic(rules=default_rules(), secret_word=your_secret_word)
handler = Handler()
game = Game(logic, handler)
game.play()
```
![Example 1](examples\example-1.png)
![Example 2](examples\example-2.png)
![Example 3](examples\example-3.png)
### Display game results like the real thing!
```python
from wordle.result import get_result

your_secret_word = "sneak"

logic = GameLogic(rules=default_rules(), secret_word=your_secret_word)
handler = Handler()
game = Game(logic, handler)
game.play()

# Get your result
result = get_result(logic.rules.title, logic.guesses, your_secret_word, logic.rules.max_guesses)
print(result)
```
![Example 4](examples\example-4.png)
## License

Check out the license [here](LICENSE).