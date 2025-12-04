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
        total = 0
        TARGET_LEN = 12

        for row in self.data:
            digits = row.strip()
            n = len(digits)
            k = n - TARGET_LEN  # number of digits to remove

            stack = []
            for ch in digits:
                # While we can still remove digits and the last digit is smaller than current,
                # pop it to make the number larger.
                while k > 0 and stack and stack[-1] < ch:
                    stack.pop()
                    k -= 1
                stack.append(ch)

            # If we still have digits to remove, remove them from the end
            if k > 0:
                stack = stack[:-k]

            # Now stack should have exactly TARGET_LEN digits
            best_number = int("".join(stack))
            total += best_number

        return total


if __name__ == "__main__":
    solution = Solution.from_file(Path(__file__).parent / "input.txt")
    solution.display_description()
    print(f"Part 1: {solution.part1()}")
    print(f"Part 2: {solution.part2()}")
