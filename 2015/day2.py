#!/usr/bin/env python3

# Source: https://adventofcode.com/2015/day/2

import os


def get_smallest_perimeter(length, width, height):
    p1 = length + length + width + width
    p2 = length + length + height + height
    p3 = width + width + height + height
    return min(p1, p2, p3)


with open(f"{os.getcwd()}/2015/inputs/day2_input.txt") as file:
    total_paper = 0
    total_ribbon = 0
    for dimensions in file:
        length, width, height = [int(value.strip()) for value in dimensions.split("x")]

        # calculating total paper
        m1 = length * width
        m2 = width * height
        m3 = height * length
        smallest_area = min(m1, m2, m3)
        total_paper += (2 * m1) + (2 * m2) + (2 * m3) + smallest_area

        # calculating total ribbon
        ribbon_to_wrap = get_smallest_perimeter(length, width, height)
        ribbon_to_bow = length * width * height
        total_ribbon += ribbon_to_wrap + ribbon_to_bow

    print(f"Total papaer needed: {total_paper}")
    print(f"Total ribbon needed: {total_ribbon}")
