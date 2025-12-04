"""
Advent of Code 2025 - Day 2
"""
from pathlib import Path
from aoc_template import BaseSolution, parse_lines


class Solution(BaseSolution):
    """Solution for Day 2."""

    def parse_input(self, input_text: str):
        """Parse the input."""
        return parse_lines(input_text)[0].split(',')

    def _generate_repeating_halves(self, beg, end):
        """Generate even-length numbers where first half equals second half."""
        results = []
        min_digits = len(str(beg))
        max_digits = len(str(end))

        for num_digits in range(min_digits, max_digits + 1):
            # Only even-length numbers
            if num_digits % 2 != 0:
                continue

            half_len = num_digits // 2
            # Generate all possible halves
            start = 10 ** (half_len - 1) if half_len > 1 else 1
            stop = 10 ** half_len

            for half in range(start, stop):
                # Repeat the half (not reverse it)
                repeated = int(str(half) * 2)
                if beg <= repeated <= end:
                    results.append(repeated)

        return results

    def _generate_repeating_patterns(self, beg, end):
        """Generate numbers with repeating patterns in range [beg, end]."""
        results = set()
        min_digits = len(str(beg))
        max_digits = len(str(end))

        for num_digits in range(min_digits, max_digits + 1):
            # Try each pattern length that divides num_digits
            for pattern_len in range(1, num_digits):
                if num_digits % pattern_len != 0:
                    continue

                # Generate all patterns of this length
                start = 10 ** (pattern_len - 1) if pattern_len > 1 else 1
                stop = 10 ** pattern_len

                for pattern in range(start, stop):
                    # Repeat pattern to create number
                    pattern_str = str(pattern)
                    repeated = int(pattern_str * (num_digits // pattern_len))
                    if beg <= repeated <= end:
                        results.add(repeated)

        return results

    def part1(self):
        """Solve part 1."""
        total = 0
        for num_range in self.data:
            values = num_range.split('-')
            beg, end = int(values[0]), int(values[1])
            repeating_halves = self._generate_repeating_halves(beg, end)
            total += sum(repeating_halves)
        return total


    def part2(self):
        """Solve part 2."""
        all_nums = set()
        for num_range in self.data:
            values = num_range.split('-')
            beg, end = int(values[0]), int(values[1])
            repeating = self._generate_repeating_patterns(beg, end)
            all_nums.update(repeating)
        return sum(all_nums)
                



if __name__ == "__main__":
    solution = Solution.from_file(Path(__file__).parent / "input.txt")
    solution.display_description()
    print(f"Part 1: {solution.part1()}")
    print(f"Part 2: {solution.part2()}")
