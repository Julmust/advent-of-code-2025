"""Day X: Advent of Code 2025."""

import sys
from pathlib import Path


sys.path.insert(0, str(Path(__file__).parent.parent))


def add_ints(a, b):
    return int(str(a) + str(b))


def part_1(banks) -> int:
    total = 0

    for bank in banks:
        pos1, pos2 = int(bank[0]), int(bank[1])
        curr_max = add_ints(pos1, pos2)

        for battery in bank[2:]:
            joltage = int(battery)
            if add_ints(pos2, joltage) > curr_max:
                pos1, pos2 = pos2, joltage
                curr_max = add_ints(pos1, pos2)
            elif joltage > pos2:
                pos2 = joltage
                curr_max = add_ints(pos1, pos2)

        print(curr_max)
        total += curr_max
    return total


def main() -> None:
    """Main entry point for day X solution."""
    with open("full.txt", "r") as infile:
        data = infile.read().strip()
        data = data.split("\n")

    print(f"Part 1: {part_1(data)}")


if __name__ == "__main__":
    main()
