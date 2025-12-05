"""Day X: Advent of Code 2025."""

import sys
from pathlib import Path


sys.path.insert(0, str(Path(__file__).parent.parent))


def fresh_range(fresh) -> tuple:
    ranges = []
    for id_range in fresh:
        start, stop = id_range.split("-")
        ranges.append((int(start), int(stop)))

    # Sort ranges based on the start value
    sorted_ranges = sorted(ranges, key=lambda x: int(x[0]))
    merged = [sorted_ranges[0]]

    for current in sorted_ranges[1:]:
        last_merged = merged[-1]
        # Check if there is an overlap or they are contiguous
        if int(current[0]) <= int(last_merged[1]) + 1:
            # Merge the ranges
            merged[-1] = (
                int(last_merged[0]),
                max(int(last_merged[1]), int(current[1])),
            )
        else:
            merged.append(current)

    return merged


def part2(fresh_map):
    cnt = 0
    for r in fresh_map:
        cnt += r[1] - r[0] + 1

    return cnt


def part1(fresh_map, available) -> int:
    cnt = 0

    for a in available:
        for r in fresh_map:
            if int(a) >= r[0] and int(a) <= r[1]:
                cnt += 1
                break

    return cnt


def main() -> None:
    """Main entry point for day X solution."""
    with open("full.txt", "r", encoding="utf-8") as file:
        data = file.read().strip().splitlines()
        split_idx = data.index("")
        fresh_ids, available_ids = data[:split_idx], data[split_idx + 1 :]

    fresh_map = fresh_range(fresh_ids)

    print(f"Part 1: {part1(fresh_map, available_ids)}")
    print(f"Part 2: {part2(fresh_map)}")


if __name__ == "__main__":
    main()
