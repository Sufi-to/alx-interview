#!/usr/bin/python3
"""Module for implementing a function that validates utf-8"""


def validUTF8(data):
    """Returns a boolean for whether the data is valid utf-8"""
    num_b = 0
    for bite in data:
        if num_b == 0:
            if bite >> 5 == 0b110:
                num_b = 1
            elif bite >> 4 == 0b1110:
                num_b = 2
            elif bite >> 3 == 0b11110:
                num_b = 3
            elif bite >> 7:
                return False
        else:
            check1 = 1 << 7
            check2 = 1 << 6
            if not (bite & check1 and not (bite & check2)):
                return False
            num_b -= 1
        if num_b < 0:
            return False
    return num_b == 0
