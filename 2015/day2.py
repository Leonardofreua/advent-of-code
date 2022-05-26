#!/usr/bin/env python3

# Source: https://adventofcode.com/2015/day/2

import os

with open(f"{os.getcwd()}/2015/inputs/day2_input.txt") as file:
    total_paper = 0
    for dimensions in file:
        length, width, height = [int(value.strip()) for value in dimensions.split("x")]
        m1 = length * width
        m2 = width * height
        m3 = height * length
        smallest_area = min(m1, m2, m3)
        total_paper += (2 * m1) + (2 * m2) + (2 * m3) + smallest_area

    print(f"Total papaer needed: {total_paper}")
