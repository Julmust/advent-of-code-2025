"""Day X: Advent of Code 2025."""

import sys
from pathlib import Path
from collections import Counter

from utils.array_functions import transform_1d_to_2d, pad_2d_array
from utils.read_input import read_input_file

sys.path.insert(0, str(Path(__file__).parent.parent))


def part1(inp, is_part_2=False) -> int:
    cnt = 0
    idx_x, idx_y = 1, 1  # Start at 1,1 since the array is padded
    height, width = len(inp), len(inp[0])
    # print(height, width)

    while True:
        if inp[idx_y][idx_x] == "x":  # End of row
            if idx_y == height - 1:  # End of list
                break
            idx_y += 1
            idx_x = 1
        if inp[idx_y][idx_x] != "@":  # Only check around @
            idx_x += 1
            continue

        # Extract 3x3 subarray around (idx_y, idx_x)
        start_x, stop_x = idx_x - 1, idx_x + 2
        start_y, stop_y = idx_y - 1, idx_y + 1
        subarr = (
            inp[start_y][start_x:stop_x]
            + inp[idx_y][start_x:stop_x]
            + inp[stop_y][start_x:stop_x]
        )

        tst = Counter(subarr)

        if tst["@"] <= 4:
            cnt += 1
            if is_part_2:
                inp[idx_y][idx_x] = "."

        idx_x += 1

    return cnt


def part2(inp) -> int:
    total = 0

    while True:
        subcount = part1(inp, True)
        total += subcount
        if subcount == 0:
            return total


def main() -> None:
    """Main entry point for day X solution."""
    d = read_input_file("full.txt")
    d = transform_1d_to_2d(d)
    d = pad_2d_array(d, 1, "x")

    # print(f"Part 1: {part1(d)}")
    print(f"Part 2: {part2(d)}")


if __name__ == "__main__":
    main()
