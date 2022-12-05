#!/usr/bin/env python3

# Source: https://adventofcode.com/2022/day/1


def sum_calories_per_elf(calories: str) -> list[int]:
    r"""
    Usage Examples:
    >>> sum_calories_per_elf('1000\n1000\n\n2000\n\n3000')
    [2000, 2000, 3000]
    >>> sum_calories_per_elf('5000\n2000\n\n2000\n4000\n\n3000')
    [7000, 6000, 3000]
    """
    return [
        sum(map(int, group_of_calories.splitlines()))
        for group_of_calories in calories.split("\n\n")
    ]


def get_top_three_calories_per_elf(calories_per_elf: list[int]) -> int:
    """
    Usage Examples:
    >>> get_top_three_calories_per_elf([55, 45, 11, 23, 12, 99])
    199
    >>> get_top_three_calories_per_elf([110, 1, 7, 88, 678, 44, 876, 345])
    1899
    """
    return sum(sorted(calories_per_elf, reverse=True)[:3])


with open("./input.txt") as file:
    calories = file.read()
    calories_per_elf = sum_calories_per_elf(calories)

    print(f"(Part 1) Elf carrying the most Calories: {max(calories_per_elf)}")
    print(
        f"(Part 2) Total Calories carried by the TOṔ THREE Elves: {get_top_three_calories_per_elf(calories_per_elf)}"
    )
