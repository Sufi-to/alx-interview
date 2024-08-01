#!/usr/bin/python3
"""Module for finding the locks."""


def canUnlockAll(boxes):
    """Returns a boolean of whether all the lockboxes can be unlocked."""
    keyLocks = set([0])
    keys_to_check = [0]

    while keys_to_check:
        current_key = keys_to_check.pop()
        for key in boxes[current_key]:
            if key not in keyLocks:
                keyLocks.add(key)
                if key < len(boxes):
                    keys_to_check.append(key)
    for i in range(len(boxes)):
        if i not in keyLocks:
            return False
    return True
