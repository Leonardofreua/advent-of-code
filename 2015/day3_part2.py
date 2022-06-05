#!/usr/bin/env python3

# Source: https://adventofcode.com/2015/day/3s


COORDINATES = {
    "^": (0, 1),
    "v": (0, -1),
    "<": (-1, 0),
    ">": (1, 0),
}
WIDTH = HEIGHT = 1000

x_santa = y_santa = x_robo = y_robo = 500
matrix = [[0 for _ in range(WIDTH)] for _ in range(HEIGHT)]
matrix[x_santa][y_santa] = 2

with open("./inputs/day3_input.txt") as file:
    for index, direction in enumerate(file.read()):
        x_coord, y_coord = COORDINATES[direction]

        if (index % 2) == 0:
            x_santa += x_coord
            y_santa += y_coord
            matrix[x_santa][y_santa] += 1
        else:
            x_robo += x_coord
            y_robo += y_coord
            matrix[x_robo][y_robo] += 1

count = 0
for paths in matrix:
    count += len(list(filter(lambda n: n >= 1, paths)))

print(f"Number of houses that received at least one present: {count}")
