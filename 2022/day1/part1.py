#!/usr/bin/env python3

# Source: https://adventofcode.com/2022/day/1
def get_max_of_calories_by_elf(calories: str) -> int:
    r"""
    Usage Examples:
    >>> get_max_of_calories_by_elf('1000\n1000\n\n2000\n\n3000')
    3000
    >>> get_max_of_calories_by_elf('5000\n2000\n\n2000\n4000\n\n3000')
    7000
    """
    return max(
        [
            sum(map(int, group_of_calories.splitlines()))
            for group_of_calories in calories.split("\n\n")
        ]
    )


with open("./input.txt") as file:
    calories = file.read()
    print(get_max_of_calories_by_elf(calories))
