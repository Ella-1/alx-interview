#!/usr/bin/python3
"""
Pascal Triangle
"""


def pascal_triangle(n):
    """Create a function def pascal_triangle(n): that returns a list of lists
    of integers representing the Pascal’s triangle of n
    """
    result = []
    for count in range(n):
        n = []
        for element in range(count + 1):
            n.append(combination(count, element))
        result.append(n)
    return result
