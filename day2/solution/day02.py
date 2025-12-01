"""
Advent of Code 2025 - Day 2
"""
from aoc_template import BaseSolution, parse_lines


class Solution(BaseSolution):
    """Solution for Day 2."""

    def parse_input(self, input_text: str):
        """Parse the input."""
        return parse_lines(input_text)

    def part1(self):
        """Solve part 1."""
        # TODO: Implement part 1
        pass

    def part2(self):
        """Solve part 2."""
        # TODO: Implement part 2
        pass


if __name__ == "__main__":
    from aoc_template import load_input

    # Load input (fetches from web or uses cached version)
    input_text = load_input(2025, 2)

    solution = Solution(input_text)
    print(f"Part 1: {solution.part1()}")
    print(f"Part 2: {solution.part2()}")
