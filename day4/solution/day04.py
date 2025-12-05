"""
Advent of Code 2025 - Day 4
"""
from pathlib import Path
from aoc_template import BaseSolution, parse_lines, neighbors_8, parse_grid


class Solution(BaseSolution):
    """Solution for Day 4."""

    def parse_input(self, input_text: str):
        return parse_grid(input_text)

    def valid_neighbor(self, neighbor, row_len, col_len):
        return (neighbor[0] >= 0 and 
                neighbor[0] > row_len and
                neighbor[1] >= 0 and
                neighbor[1] > col_len
        )

    def filter_invalid_neighbors(self, neighborsList, row_len, col_len):
        return [neighbor for neighbor in neighborsList if self.valid_neighbor(neighbor, row_len, col_len)]


    def part1(self):
        total = 0
        grid = self.data
        ROLL_VALUE = '@'
        for r_index, row in enumerate(grid):
            for c_index, col in enumerate(row):
                if grid[r_index][c_index] != ROLL_VALUE:
                    continue
                neighborsList = neighbors_8(r_index, c_index)
                row_len = len(grid) 
                col_len = len(row)
                neighbors = self.filter_invalid_neighbors(
                        neighborsList,
                        row_len,
                        col_len
                )
                rolls = list(filter(lambda neighbor: ROLL_VALUE in neighbor, neighbors))
                rolls_len = len(rolls)
                if rolls_len < 4:
                    total += 1
        return total
                             



    def part2(self):
        """Solve part 2."""
        # TODO: Implement part 2
        pass


if __name__ == "__main__":
    solution = Solution.from_file(Path(__file__).parent / "input.txt")
    solution.display_description()
    print(f"Part 1: {solution.part1()}")
    print(f"Part 2: {solution.part2()}")
