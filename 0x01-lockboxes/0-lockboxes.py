#!/usr/bin/python3

def canUnlockAll(boxes):
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
