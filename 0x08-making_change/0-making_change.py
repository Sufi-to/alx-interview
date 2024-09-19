#!/usr/bin/python3
"""Module for the making change function"""


def makeChange(coins, total):
    """Returns the min number of coins needed to reach the total"""
    if total <= 0:
        return 0
    lenArr = len(coins)
    temp = total
    sortedCoins = sorted(coins)

    i = lenArr - 1
    result = []
    while (i >= 0):
        while (total >= sortedCoins[i]):
            total -= sortedCoins[i]
            result.append(sortedCoins[i])
        i -= 1
    sumResult = sum(result)
    if temp == sumResult:
        return len(result)
    return -1
