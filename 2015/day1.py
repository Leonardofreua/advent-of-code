#!/usr/bin/env python3

# Source: https://adventofcode.com/2015/day/1

DIRECTIONS = {")": -1, "(": 1}


with open("./inputs/day1_input.txt") as file:
    floor = 0
    position = 0
    for index, value in enumerate(file.read(), start=1):
        if value in DIRECTIONS:
            floor += DIRECTIONS[value]

        if floor == -1 and position == 0:
            position = index

print(f"Floor: {floor}")
print(f"Position of the first entry in the basement: {position}")
