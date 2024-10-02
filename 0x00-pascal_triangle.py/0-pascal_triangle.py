#!/usr/bin/env python3
""" python algorithm for a pascal triangle """


def pascal_triangle(n):
    """ function return n number
        of the pascal triangle
    """

    if n <= 0 or n is None:
        return []
    if n == 1:
        return [[1]]

    count = 0
    pascal = [[1]]
    while (count < n-1):
        pascal[count].insert(0, 0)
        # inserting 0 beginning for a simpler approach
        pascal[count].append(0)
        # inserting 0 at ending for a simpler approach
        pas = []
        for i in range(len(pascal[count])-1):
            # iterate over the value of each list
            pas.append(pascal[count][i] + pascal[count][i+1])
            # adds the previous index to the next
        pascal.append(pas)
        pascal[count] = pascal[count][1:-1]
        # removes the initial zeros at beginning and end
        count += 1
    return pascal
