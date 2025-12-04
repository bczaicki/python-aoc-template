"""CLI scripts for running solutions and tests."""
import sys
import subprocess
from pathlib import Path


def run_solution():
    """Run a specific day's solution: uv run solution 3"""
    if len(sys.argv) < 2:
        print("Usage: uv run solution <day>")
        sys.exit(1)

    day = sys.argv[1]
    solution_file = Path(f"day{day}/solution/day{day.zfill(2)}.py")

    if not solution_file.exists():
        print(f"Error: {solution_file} does not exist")
        sys.exit(1)

    subprocess.run([sys.executable, str(solution_file)])


def run_test():
    """Run tests with hot reloading: uv run test 3"""
    if len(sys.argv) < 2:
        print("Usage: uv run test <day>")
        sys.exit(1)

    day = sys.argv[1]
    test_path = f"day{day}/tests"

    if not Path(test_path).exists():
        print(f"Error: {test_path} does not exist")
        sys.exit(1)

    # Run pytest-watcher with clear screen
    subprocess.run(["ptw", test_path, "--clear", "--runner", "pytest", "--runner-args", "-v"])
