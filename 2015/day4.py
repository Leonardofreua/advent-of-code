#!/usr/bin/env python3

# Source: https://adventofcode.com/2015/day/4

import hashlib

SECRET_KEY = "yzbqklnj"
BLOCKS = 10000000


def find_answer_by_five_zeros():
    for index in range(BLOCKS):
        hashex = hashlib.md5(f"{SECRET_KEY}{index}".encode()).hexdigest()
        if hashex[:5] == "00000":
            return index
    return None


def find_answer_by_six_zeros():
    for index in range(BLOCKS):
        hashex = hashlib.md5(f"{SECRET_KEY}{index}".encode()).hexdigest()
        if hashex[:6] == "000000":
            return index
    return None


print(
    f"Mined block! Hash starting with at least FIVE ZEROS => {find_answer_by_five_zeros()}"
)
print(
    f"Mined block! Hash starting with at least SIX ZEROS => {find_answer_by_six_zeros()}"
)
