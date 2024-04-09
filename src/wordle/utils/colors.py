from enum import StrEnum


class Color(StrEnum):
    GREEN = "\33[32m"
    YELLOW = "\33[93m"
    WHITE = "\33[97m"
    END = "\33[0m"

    @classmethod
    def verify(cls, color: str) -> bool:
        return color in cls

    def colorize(self, text: str) -> str:
        """Return the text colorized with the specified color.

        :param text: The text to colorize.
        :type text: str
        :return: The text colorized with the specified color.
        :rtype: str
        """
        return f"{self}{text}{Color.END}"
