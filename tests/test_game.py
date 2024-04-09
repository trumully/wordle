import pytest
from unittest.mock import Mock, PropertyMock

from wordle.game import Game
from wordle.logic import GameLogic
from wordle.handler import Handler


@pytest.fixture
def logic():
    return Mock(spec=GameLogic)


@pytest.fixture
def handler():
    return Mock(spec=Handler)


@pytest.fixture
def game(logic, handler):
    return Game(logic, handler)


def test_game_initialization(logic, handler, game):
    assert game.logic == logic
    assert game.handler == handler


def test_get_guess(logic, handler, game):
    logic.is_valid_word.return_value = True
    handler.get_guess.return_value = "apple"

    assert game.get_guess() == "apple"


def test_add_guess(logic, handler, game):
    type(logic).guesses = PropertyMock(return_value=[])
    game.add_guess = Mock(side_effect=lambda guess: logic.guesses.append(guess))

    game.add_guess("apple")

    assert "apple" in logic.guesses


def test_known_letters(logic, game):
    logic.known_letters = ["a", "p", "p", "l", "e"]

    assert game.known_letters() == "a, p, p, l, e"


def test_has_lost(logic, game):
    logic.has_lost.return_value = False

    assert game.has_lost() is False


def test_has_won(logic, game):
    logic.has_won.return_value = True

    assert game.has_won() is True


def test_game_over(logic, game):
    logic.game_over.return_value = False

    assert game.game_over() is False
