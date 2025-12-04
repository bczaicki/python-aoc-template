"""
Advent of Code 2025 - Day 3
"""
from pathlib import Path
from aoc_template import BaseSolution, parse_lines


class Solution(BaseSolution):
    """Solution for Day 3."""

    def parse_input(self, input_text: str):
        """Parse the input."""
        return parse_lines(input_text)

    def part1(self):
        total, highest, second_highest = 0, 0, 0
        for row in self.data:
            row_nums = [int(char) for char in row]
            highest = max(row_nums)

            # if max is at the end, can't be largest number
            hi_index = row_nums.index(highest)
            if hi_index == len(row_nums) - 1:
                last_popped = row_nums[0:len(row_nums) - 1]
                second_highest = highest
                highest = max(last_popped)
            else:
                # find first index of highest and then the following max from there
                next_index = hi_index + 1
                remaining_nums = row_nums[next_index:]
                second_highest = max(remaining_nums)
            num_added = highest * 10 + second_highest
            total += num_added
        return total








    def part2(self):
        # Pull the lowest 3 numbers out of the sequence


if __name__ == "__main__":
    solution = Solution.from_file(Path(__file__).parent / "input.txt")
    solution.display_description()
    print(f"Part 1: {solution.part1()}")
    print(f"Part 2: {solution.part2()}")
