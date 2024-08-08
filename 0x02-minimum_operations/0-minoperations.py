#!/usr/bin/python3
"""Module that shows how to find the minimum operations
needed to perform the task."""


def minOperations(n):
    """Returns the factorial of n which is the min operations needed."""
    num = 2
    res = 0
    while n > 1:
        while n % num == 0:
            res += num
            n /= num
        num += 1
    return res
