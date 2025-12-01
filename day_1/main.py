"""Day X: Advent of Code 2025."""

import sys
from pathlib import Path


sys.path.insert(0, str(Path(__file__).parent.parent))


def part_1(move_list) -> int:
    position, cnt = 150, 0

    for move in move_list:
        if move[0] == "L":
            position -= move[1]
        elif move[0] == "R":
            position += move[1]
        if position % 100 == 0:
            cnt += 1

    return cnt


def part_2(move_list) -> int:
    position, cnt = 50, 0

    for move in move_list:
        zeroes, rotations = divmod(move[1], 100)
        cnt += zeroes

        if move[0] == "R":
            if position + rotations >= 100:
                cnt += 1
            position = (position + rotations) % 100
        else:  # move[0] == "L":
            if position and position - rotations <= 0:
                cnt += 1
            position = (position - rotations) % 100

    return cnt


def main() -> None:
    with open("full.txt", "r") as inp:
        data = inp.read().strip()
    lst = data.split("\n")
    move_list = [[i[:1], int(i[1:])] for i in lst]

    print("Part 1:", part_1(move_list))
    print("Part 2:", part_2(move_list))


if __name__ == "__main__":
    main()
