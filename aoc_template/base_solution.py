from abc import ABC, abstractmethod
from pathlib import Path
from typing import Any


class BaseSolution(ABC):
    """Base class for Advent of Code solutions."""

    def __init__(self, input_text: str):
        """
        Initialize solution with input text.

        Args:
            input_text: Raw input text from puzzle
        """
        self.input_text = input_text.strip()
        self.data = self.parse_input(input_text)

    @abstractmethod
    def parse_input(self, input_text: str) -> Any:
        """
        Parse raw input text into a usable format.

        Args:
            input_text: Raw input text

        Returns:
            Parsed data structure
        """
        pass

    @abstractmethod
    def part1(self) -> Any:
        """
        Solve part 1 of the puzzle.

        Returns:
            Solution to part 1
        """
        pass

    @abstractmethod
    def part2(self) -> Any:
        """
        Solve part 2 of the puzzle.

        Returns:
            Solution to part 2
        """
        pass

    def solve(self) -> tuple[Any, Any]:
        """
        Solve both parts of the puzzle.

        Returns:
            Tuple of (part1_answer, part2_answer)
        """
        return self.part1(), self.part2()

    @classmethod
    def from_file(cls, filepath: str | Path) -> "BaseSolution":
        """
        Create solution instance from input file.

        Args:
            filepath: Path to input file

        Returns:
            Solution instance
        """
        return cls(Path(filepath).read_text())
