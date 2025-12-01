"""CLI for managing Advent of Code solutions."""
import argparse
from pathlib import Path
import sys


SOLUTION_TEMPLATE = '''"""
Advent of Code {year} - Day {day}
"""
from aoc_template import BaseSolution, parse_lines


class Solution(BaseSolution):
    """Solution for Day {day}."""

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
    input_text = load_input({year}, {day})

    solution = Solution(input_text)
    print(f"Part 1: {{solution.part1()}}")
    print(f"Part 2: {{solution.part2()}}")
'''

TEST_TEMPLATE = '''"""Tests for Day {day} solution."""
import pytest
from solutions.day{day:02d} import Solution


@pytest.fixture
def example_input():
    """Example input for testing."""
    return """TODO: Add example input"""


@pytest.fixture
def solution(example_input):
    """Create solution instance with example input."""
    return Solution(example_input)


def test_parse_input(solution):
    """Test input parsing."""
    # TODO: Add parsing tests
    pass


def test_part1(solution):
    """Test part 1 solution."""
    # TODO: Add part 1 tests
    expected = None  # Replace with expected value
    # assert solution.part1() == expected


def test_part2(solution):
    """Test part 2 solution."""
    # TODO: Add part 2 tests
    expected = None  # Replace with expected value
    # assert solution.part2() == expected
'''


def create_day(day: int, year: int = 2025, force: bool = False) -> None:
    """
    Create solution and test files for a specific day.

    Args:
        day: Day number (1-25)
        year: Year of Advent of Code
        force: Overwrite existing files if True
    """
    if not 1 <= day <= 25:
        print(f"Error: Day must be between 1 and 25, got {day}", file=sys.stderr)
        sys.exit(1)

    # Create solutions directory if it doesn't exist
    solutions_dir = Path("solutions")
    tests_dir = Path("tests")
    solutions_dir.mkdir(exist_ok=True)
    tests_dir.mkdir(exist_ok=True)

    # File paths
    solution_file = solutions_dir / f"day{day:02d}.py"
    test_file = tests_dir / f"test_day{day:02d}.py"

    # Check if files already exist
    if solution_file.exists() and not force:
        print(f"Error: {solution_file} already exists. Use --force to overwrite.", file=sys.stderr)
        sys.exit(1)

    if test_file.exists() and not force:
        print(f"Error: {test_file} already exists. Use --force to overwrite.", file=sys.stderr)
        sys.exit(1)

    # Create solution file
    solution_content = SOLUTION_TEMPLATE.format(year=year, day=day)
    solution_file.write_text(solution_content)
    print(f"Created {solution_file}")

    # Create test file
    test_content = TEST_TEMPLATE.format(day=day)
    test_file.write_text(test_content)
    print(f"Created {test_file}")

    print(f"\nDay {day} setup complete!")
    print(f"\nNext steps:")
    print(f"1. Add your session cookie to .env: AOC_SESSION=your_session_cookie")
    print(f"2. Implement the solution in {solution_file}")
    print(f"3. Add tests in {test_file}")
    print(f"4. Run tests: uv run pytest {test_file}")
    print(f"5. Run solution: uv run python {solution_file}")


def main():
    """Main CLI entry point."""
    parser = argparse.ArgumentParser(
        description="Advent of Code template CLI",
        formatter_class=argparse.RawDescriptionHelpFormatter,
    )

    subparsers = parser.add_subparsers(dest="command", help="Available commands")

    # Create day command
    create_parser = subparsers.add_parser("create", help="Create a new day solution")
    create_parser.add_argument("day", type=int, help="Day number (1-25)")
    create_parser.add_argument("--year", type=int, default=2025, help="Year (default: 2025)")
    create_parser.add_argument("--force", action="store_true", help="Overwrite existing files")

    args = parser.parse_args()

    if args.command == "create":
        create_day(args.day, args.year, args.force)
    else:
        parser.print_help()


if __name__ == "__main__":
    main()
