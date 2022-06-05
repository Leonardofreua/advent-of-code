#!/usr/bin/env python3

# Source: https://adventofcode.com/2015/day/3s


COORDINATES = {
    "^": (0, 1),
    "v": (0, -1),
    "<": (-1, 0),
    ">": (1, 0),
}
WIDTH = HEIGHT = 1000

x = y = 500
matrix = [[0 for _ in range(WIDTH)] for _ in range(HEIGHT)]
matrix[x][y] = 1

with open("./inputs/day3_input.txt") as file:
    for direction in file.read():
        x_coord, y_coord = COORDINATES[direction]

        x += x_coord
        y += y_coord

        matrix[x][y] += 1

count = 0
for paths in matrix:
    count += len(list(filter(lambda n: n >= 1, paths)))

print(f"Number of houses that received at least one present: {count}")
