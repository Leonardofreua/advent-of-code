#!/usr/bin/env python3

# Source: https://adventofcode.com/2015/day/6

import re
from collections import defaultdict
from enum import Enum
from typing import Generator

INSTRUCTION_PATTERN = "(turn on|turn off|toggle) (\\d+),(\\d+) through (\\d+),(\\d+)"


class InstructionType(Enum):
    TURN_ON = "turn on"
    TURN_OFF = "turn off"
    TOGGLE = "toggle"


def parse_instructions(instructions: list[str]) -> Generator:
    pattern = re.compile(INSTRUCTION_PATTERN)
    for instruction in instructions:
        match_result = re.match(pattern, instruction)
        if match_result:
            command = match_result.group(1)
            start_x = int(match_result.group(2))
            start_y = int(match_result.group(3))
            end_x = int(match_result.group(4))
            end_y = int(match_result.group(5))

        yield command, start_x, start_y, end_x, end_y


def find_coordinate_between_points(
    start_x: int, start_y: int, end_x: int, end_y: int
) -> Generator:
    for x_axis in range(end_x - start_x + 1):
        for y_axis in range(end_y - start_y + 1):
            coordinate = (start_x + x_axis, start_y + y_axis)
            yield coordinate


def count_status_of_lamps(lamps) -> int:
    return sum(lamp_status for lamp_status in lamps.values())


# PART 1
def lighting_up(instructions: list[str]) -> int:
    lamps = defaultdict(bool)

    def turn_on(coordinates: Generator) -> None:
        for position in coordinates:
            lamps[position] = True

    def turn_off(coordinates: Generator) -> None:
        for position in coordinates:
            lamps[position] = False

    def toggle(coordinates: Generator) -> None:
        for position in coordinates:
            lamps[position] = not lamps[position]

    for (command, start_x, start_y, end_x, end_y) in parse_instructions(instructions):
        coordinates = find_coordinate_between_points(start_x, start_y, end_x, end_y)
        if command == InstructionType.TURN_ON.value:
            turn_on(coordinates)
        elif command == InstructionType.TURN_OFF.value:
            turn_off(coordinates)
        elif command == InstructionType.TOGGLE.value:
            toggle(coordinates)

    return count_status_of_lamps(lamps)


# PART 2
def brightness_control(instructions: list[str]) -> int:
    lamps = defaultdict(int)

    def turn_on_brightness(coordinates: Generator) -> None:
        for position in coordinates:
            lamps[position] += 1

    def turn_off_brightness(coordinates: Generator) -> None:
        for position in coordinates:
            if lamps[position] > 0:
                lamps[position] -= 1

    def toggle_brightness(coordinates: Generator) -> None:
        for position in coordinates:
            lamps[position] += 2

    for (command, start_x, start_y, end_x, end_y) in parse_instructions(instructions):
        coordinates = find_coordinate_between_points(start_x, start_y, end_x, end_y)
        if command == InstructionType.TURN_ON.value:
            turn_on_brightness(coordinates)
        elif command == InstructionType.TURN_OFF.value:
            turn_off_brightness(coordinates)
        elif command == InstructionType.TOGGLE.value:
            toggle_brightness(coordinates)

    return count_status_of_lamps(lamps)


with open("./inputs/day6_input.txt") as file:
    lines = file.readlines()
    lights_on = lighting_up(lines)
    brightness_count = brightness_control(lines)
    print(f"{lights_on=}")
    print(f"{brightness_count=}")
