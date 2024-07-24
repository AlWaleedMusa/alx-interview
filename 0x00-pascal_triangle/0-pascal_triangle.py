#!/usr/bin/python3


def pascal_triangle(n):
    """return a list of lists of ints representing the pascal triangle"""

    if n <= 0:
        return []
    else:
        triangle = [[1]]
        for i in range(1, n):
            row = [1]
            for j in range(1, i):
                row.append(triangle[i - 1][j - 1] + triangle[i - 1][j])
            row.append(1)
            triangle.append(row)
        return triangle
