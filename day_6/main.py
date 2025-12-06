"""Day X: Advent of Code 2025."""

import math
import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent.parent))

from utils.array_functions import print_2d_array


def parse_data(input):
    # for Serban
    return [re.sub(r"\s+", "\t", i.strip()).split("\t") for i in input]


def calc(arr, op):
    rows = len(arr)
    atot = 0
    mtot = 1
    aud = []
    for x in range(len(arr[0])):
        subtot = ""
        for xidx in range(rows):
            if arr[xidx][x] != ".":
                subtot += arr[xidx][x]

        if op == "+":
            atot += int(subtot)
        else:
            mtot = mtot * int(subtot)
        aud.append(subtot)

    if mtot == 1:
        return atot
    return atot + mtot


def part_2(inp) -> int:
    total = 0
    max_idx = len(inp[0])
    rows = len(inp)
    record = False

    tmp = [[] for _ in range(rows - 1)]
    op = None
    for idx in range(max_idx):
        vals = [
            inp[i][idx] if inp[i][idx] != " " else "." for i in range(rows - 1)
        ]  # Ignore last row
        if not all(
            v == "." for v in vals
        ):  # True if any value is != '', character found
            if not record:  # First value in new set, record operator
                op = inp[-1][idx]
                record = True

            for j in range(rows - 1):
                tmp[j].append(vals[j])

        else:  # No characters found in row
            total += calc(tmp, op)
            tmp = [[] for _ in range(rows - 1)]
            op = None
            record = False

    total += calc(tmp, op)

    return total


def part_1(inp) -> int:
    total = 0

    for i in range(len(inp[0])):
        if inp[4][i] == "+":
            total += int(inp[0][i]) + int(inp[1][i]) + int(inp[2][i]) + int(inp[3][i])
        elif inp[4][i] == "*":
            total += int(inp[0][i]) * int(inp[1][i]) * int(inp[2][i]) * int(inp[3][i])

    return total


def main() -> None:
    """Main entry point for day X solution."""
    with open("full.txt", "r") as indata:
        d = indata.read().rstrip().splitlines()

    print(f"Part 1: {part_1(parse_data(d))}")
    print(f"Part 2: {part_2(d)}")


if __name__ == "__main__":
    main()
