#!/usr/bin/python3
"""Module for implementing a function that validates utf-8"""


def validUTF8(data):
    """Returns a boolean for whether the data is valid utf-8"""
    num_b = 0
    for byte in data:
        if num_b == 0:
            if byte >> 5 == 0b110:
                num_b = 1
            elif byte >> 4 == 0b1110:
                num_b = 2
            elif byte >> 3 == 0b11110:
                num_b = 3
            elif byte >> 7:
                return False
        else:
            if not (byte >> 6 == 0b10):
                return False
            num_b -= 1

    return num_b == 0
