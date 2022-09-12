#!/usr/bin/env python3

# Source: https://adventofcode.com/2015/day/5

VOWELS = "aeiou"
UNWANTED_STRINGS = ["ab", "cd", "pq", "xy"]


def has_at_least_three_vowels(string: str) -> bool:
    result = [char for char in string if char in VOWELS]
    return len(result) >= 3


def contains_at_least_one_letter_equal_side_by_side(string: str) -> bool:
    for index in range(1, len(string)):
        if string[index] == string[index - 1]:
            return True
    return False


def has_not_unwanted_string(string: str) -> bool:
    return not any(value for value in UNWANTED_STRINGS if value in string)


with open("./inputs/day5_input.txt") as file:
    nice_strings = 0
    for line in file:
        string = line.strip()
        if (
            has_at_least_three_vowels(string)
            and contains_at_least_one_letter_equal_side_by_side(string)
            and has_not_unwanted_string(string)
        ):
            nice_strings += 1

    print(f"Total Nice strings: {nice_strings}")
