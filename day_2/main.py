"""Day X: Advent of Code 2025."""

import sys
from pathlib import Path


sys.path.insert(0, str(Path(__file__).parent.parent))


def part_1(inp) -> int:
    total = 0
    for id_range in inp:
        for i in range(id_range[0], id_range[1] + 1):
            stringified = str(i)
            num_len = len(stringified)

            if num_len % 2:  # Odd length numbers cannot be repeating
                continue

            h1, h2 = stringified[: (num_len // 2)], stringified[(num_len // 2) :]
            if h1 == h2:
                total += i

    return total


def main() -> None:
    """Main entry point for day X solution."""
    with open("full.txt", "r") as file:
        data = file.read().split(",")

    data = [d.split("-") for d in data]
    data = [list(map(int, i)) for i in data]

    print(f"Part 1: {part_1(data)}")


if __name__ == "__main__":
    main()
