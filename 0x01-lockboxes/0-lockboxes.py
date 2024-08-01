#!/usr/bin/python3
"""Module for finding the locks."""


def canUnlockAll(boxes):
    """Returns a boolean of whether all the lockboxes can be unlocked."""
    keyLocks = set()
    for i in range(1, len(boxes)):
        if i in boxes[i-1]:
            for j in boxes[i-1]:
                keyLocks.add(j)
            for x in boxes[i]:
                keyLocks.add(x)
    for y in range(len(boxes)):
        for i in boxes:
            if boxes.index(i) in keyLocks:
                for j in i:
                    keyLocks.add(j)
    setKeys = set(keyLocks)
    for i in range(1, len(boxes)-1):
        if i not in setKeys:
            return False
    return True
