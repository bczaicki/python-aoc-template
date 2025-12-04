"""Tests for Day 3 solution."""
import pytest
import sys
from pathlib import Path

# Add parent directory to path to import solution
sys.path.insert(0, str(Path(__file__).parent.parent / "solution"))
from day03 import Solution


@pytest.fixture
def example_input():
    return """
    987654321111111
    811111111111119
    234234234234278
    818181911112111
"""


@pytest.fixture
def solution(example_input):
    """Create solution instance with example input."""
    return Solution(example_input)


def test_parse_input(solution):
    """Test input parsing."""
    assert len(solution.data) == 4
    assert int(solution.data[0][0]) == 9
    assert int(solution.data[0][-1]) == 1


def test_part1(solution):
    expected = 357
    actual = solution.part1()
    assert actual == expected


def test_part2(solution):
    expected = 3121910778619
    actual = solution.part2()
    assert actual == expected
