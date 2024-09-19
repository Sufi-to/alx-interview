#!/usr/bin/python3
"""Module for the making change function"""


def makeChange(coins, total):
    """Returns the min number of coins needed to reach the total"""
    if total <= 0:
        return 0
    lenArr = len(coins)
    temp = total

    i = lenArr - 1
    result = []
    while (i >= 0):
        while (total >= coins[i]):
            total -= coins[i]
            result.append(coins[i])
        i -= 1
    sumResult = sum(result)
    if temp == sumResult:
        return len(result)
    return -1
