import toml
from pathlib import Path

TOML_PATH: Path = Path("pyproject.toml")

__name__ = "wordle"
__version__ = toml.load(TOML_PATH)["tool"]["poetry"]["version"]
__author__ = toml.load(TOML_PATH)["tool"]["poetry"]["authors"][0]
