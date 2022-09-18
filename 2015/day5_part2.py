#!/usr/bin/env python3

# Source: https://adventofcode.com/2015/day/5


def has_pairs_appers_at_least_twice(string: str) -> bool:
    return any(
        [
            (string.count(string[index : index + 2]) >= 2)
            for index in range(len(string) - 2)
        ]
    )


def has_one_letter_between_same_letter(string: str) -> bool:
    for index in range(len(string) - 2):
        if string[index] == string[index + 2]:
            return True
    return False


with open("./inputs/day5_input.txt") as file:
    nice_strings = 0
    for line in file:
        string = line.strip()
        if has_one_letter_between_same_letter(
            string
        ) and has_pairs_appers_at_least_twice(string):
            nice_strings += 1
    print(f"Total Nice strings: {nice_strings}")
