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

        total += curr_max
    return total


def find_highest(bank, to_find):
    split_pos = to_find - 1

    # Is this how I would want to do it? No. Does it work? Yes
    if not split_pos:
        find_high_in_bank = bank
        high, high_idx = 0, 0
        for idx, battery in enumerate(find_high_in_bank):
            if int(battery) > high:
                high, high_idx = int(battery), idx
        return str(high)

    # figure out the highest number, excluding the last 11
    # this will be our starting point
    find_high_in_bank = bank[:-split_pos]
    high, high_idx = 0, 0
    for idx, battery in enumerate(find_high_in_bank):
        if int(battery) > high:
            high, high_idx = int(battery), idx

    # remove everything before and including the highest number
    bank = bank[high_idx + 1 :]

    return str(high) + find_highest(bank, to_find - 1)


def part_2(banks):
    total = 0

    for bank in banks:
        res = find_highest(bank, 12)
        total += int(res)

    return total


def main() -> None:
    """Main entry point for day X solution."""
    with open("full.txt", "r") as infile:
        data = infile.read().strip()
        data = data.split("\n")

    print(f"Part 1: {part_1(data)}")
    print(f"Part 2: {part_2(data)}")


if __name__ == "__main__":
    main()
