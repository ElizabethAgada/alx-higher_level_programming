#!/usr/bin/python3
"""Defining a Pascal's triangle function."""


def pascal_triangle(n):
    """Representing Pascal's Triangle of size n.

    Returns list of lists of integers representing d triangle.
    """
    if n <= 0:
        return []

    triangles = [[1]]
    while len(triangles) != n:
        tri = triangles[-1]
        tmp = [1]
        for q in range(len(tri) - 1):
            tmp.append(tri[q] + tri[q + 1])
        tmp.append(1)
        triangles.append(tmp)
    return triangles
