#!/usr/bin/python3
"""Module for removing the prime numbers in a list"""


def isWinner(x, nums):
    """Removes a prime number and its multiples for a given round
    and determines the winner
    """
    score = {"Maria": 0, "Ben": 0}
    for i in range(x):
        curr_num_primes = SieveOfEratosthenes(nums[i])
        if len(curr_num_primes) % 2 == 0:
            score['Ben'] += 1
        else:
            score['Maria'] += 1
    if score["Maria"] > score["Ben"]:
        return "Maria"
    elif score["Maria"] < score["Ben"]:
        return "Ben"
    else:
        return None


def SieveOfEratosthenes(n):
    prime = [True for i in range(n+1)]
    p = 2
    while (p * p <= n):

        if (prime[p] is True):
            for i in range(p * p, n+1, p):
                prime[i] = False
        p += 1

    primes = []
    for p in range(2, n+1):
        if prime[p]:
            primes.append(p)
    return primes
