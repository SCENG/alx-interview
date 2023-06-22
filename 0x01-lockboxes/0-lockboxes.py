#!/usr/bin/python3
"""Solves the lock boxes puzzle """



def canUnlockAll(boxes):
    """Check if all boxes can be opened
    Args:
        boxes (list): List which contain all the boxes with the keys
    Returns:
        bool: True if all boxes can be opened, otherwise, False
    """

    n = len(boxes)
    visited = [False] * n
    visited[0] = True

    stack = [0]  # Start with the first box

    while stack:
        box = stack.pop()

        # Check each key in the current box
        for key in boxes[box]:
            if key < n and not visited[key]:
                visited[key] = True
                stack.append(key)

    return all(visited)

