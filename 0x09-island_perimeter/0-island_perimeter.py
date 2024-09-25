#!/usr/bin/python3
"""
island_perimeter
"""


def island_perimeter(grid):
    """
    Calculates the perimeter of the island described in the grid.

    Parameters:
    grid (list of list of int): A 2D list where 1
    represents land and 0 represents water.

    Returns:
    int: The perimeter of the island.
    """
    perimeter = 0
    rows = len(grid)
    cols = len(grid[0]) if rows > 0 else 0

    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == 1:
                perimeter += 4
                if r > 0 and grid[r-1][c] == 1:
                    perimeter -= 2
                if c > 0 and grid[r][c-1] == 1:
                    perimeter -= 2

    return perimeter
