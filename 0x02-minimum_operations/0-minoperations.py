#!/usr/bin/env python3
"""minoperations"""


def minOperations(n):
    """
    Calculates the minimum number of operations needed to achieve exactly n 'H' characters in a text file,
    starting with a single 'H' and using only two operations: Copy All and Paste.

    Parameters:
    n (int): The target number of 'H' characters.

    Returns:
    int: The minimum number of operations needed, or 0 if n is less than or equal to 1.
    """
    if n <= 1:
        return 0

    operations = 0
    factor = 2

    while n > 1:
        while n % factor == 0:
            operations += factor
            n //= factor
        factor += 1

    return operations
