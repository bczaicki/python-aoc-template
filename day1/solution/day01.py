"""
Advent of Code - Day 1 Example
"""
from aoc_template import BaseSolution, parse_lines


class Solution(BaseSolution):
    """Example solution for Day 1."""

    def parse_input(self, input_text: str) -> list[str]:
        """Parse input into lines."""
        return parse_lines(input_text)

    def part1(self) -> int:
        """
        Solve part 1.

        Example: Count the number of lines in the input.
        """
        return len(self.data)

    def part2(self) -> int:
        """
        Solve part 2.

        Example: Count total characters across all lines.
        """
        return sum(len(line) for line in self.data)


if __name__ == "__main__":
    # Example usage with a test input
    test_input = """line 1
line 2
line 3"""

    solution = Solution(test_input)
    print(f"Part 1: {solution.part1()}")
    print(f"Part 2: {solution.part2()}")

    # To use with actual AoC input:
    # from aoc_template import load_input
    # input_text = load_input(2025, 1)
    # solution = Solution(input_text)
    # print(f"Part 1: {solution.part1()}")
    # print(f"Part 2: {solution.part2()}")
