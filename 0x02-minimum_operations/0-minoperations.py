#!/usr/bin/python3
""" Module for 0-minoperations"""


def minOperations(n: int) -> int:
    """
    Calculates the fewest number of operations
    needed to result in exactly n H characters.

    Args:
        n (int): The target number of H characters.

    Returns:
        int: The minimum number of operations required.

    """
    if n <= 1:
        return 0

    operations, divisor = 0, 2

    while n > 1:
        if n % divisor == 0:
            n //= divisor
            operations += divisor
        else:
            divisor += 1

    return operations
