"""Day X: Advent of Code 2025."""

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent.parent))

from utils.array_functions import pad_2d_array, print_2d_array, transform_1d_to_2d


def traverse(inp, start_pos_x, start_pos_y) -> int:
    splits = 0
    next_pos_y = start_pos_y + 1
    next_char = inp[next_pos_y][start_pos_x]

    if next_char == "0":  # Base case
        return 0
    elif next_char == ".":  # Continue downwards, no split = no count
        inp[next_pos_y][start_pos_x] = "x"
        splits += traverse(inp, start_pos_x, next_pos_y)
    elif next_char == "^":  # Split happening!
        splits += 1
        splits += traverse(inp, start_pos_x - 1, next_pos_y)
        if inp[next_pos_y][start_pos_x + 1] != "x":
            splits += traverse(inp, start_pos_x + 1, next_pos_y)

    return splits


def part1(inp) -> int:
    start_x, start_y = 0, 1

    # locate starting coordinates, always in the first non-padded line
    for idx, ch in enumerate(inp[1]):
        if ch == "S":
            start_x = idx
            break

    return traverse(inp, start_x, start_y)


def main() -> None:
    """Main entry point for day X solution."""
    with open("full.txt", "r") as infile:
        lines = infile.read().strip().splitlines()
        lines = pad_2d_array(transform_1d_to_2d(lines), 1, "0")

    print(f"Part 1: {part1(lines)}")


if __name__ == "__main__":
    main()
