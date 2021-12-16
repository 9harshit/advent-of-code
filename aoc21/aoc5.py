from collections import Counter

import numpy as np
from utils import get_data

DEBUG = False
coords = []

min_x, min_y = 9999, 9999
max_x, max_y = -9999, -9999

data = get_data(__file__, DEBUG)


def add_to_matrix(pts, matrix):
    pts = list(set(pts))
    matrix += pts
    return matrix


def get_points(matrix, line, diagonals=False):

    pts = []

    if (line[0][0] == line[1][0]) or (line[0][1] == line[1][1]):

        # create the points
        ys = np.linspace(line[0][1], line[1][1], max_y + max_x)

        xs = np.linspace(line[0][0], line[1][0], max_x + max_y)

        # print them
        for i in range(max_x + max_y):
            pts.append((int(xs[i]), int(ys[i])))

    elif abs(line[0][0] - line[1][0]) == abs(line[0][1] - line[1][1]) and diagonals:
        if line[0][0] > line[1][0]:
            line[0][0], line[0][1], line[1][0], line[1][1] = (
                line[1][0],
                line[1][1],
                line[0][0],
                line[0][1],
            )
        slope = (line[1][1] - line[0][1]) // (line[1][0] - line[0][0])
        for i, j in zip(
            range(line[0][0], line[1][0]),
            range(line[0][1], line[1][1], slope),
        ):
            pts.append((i, j))

    return add_to_matrix(pts, matrix)


def get_count_pts(matrix):
    d = Counter(matrix)

    count = 0
    for x in d.items():
        if x[1] >= 2:
            count += 1

    return count


for pts in data:
    start, end = pts.split(" -> ")
    start, end = start.split(","), end.split(",")
    start = [int(x) for x in start]
    end = [int(x) for x in end]
    coords.append([start, end])

    if min_x > int(start[0]) or min_x > int(end[0]):
        min_x = min(int(start[0]), int(end[0]))

    if min_y > int(start[1]) or min_y > int(end[1]):
        min_y = min(int(start[1]), int(end[1]))

    if max_x < int(start[0]) or max_x < int(end[0]):
        max_x = max(int(start[0]), int(end[0]))

    if max_y < int(start[1]) or max_y < int(end[1]):
        max_y = max(int(start[1]), int(end[1]))


def sol_1():
    matrix = []
    for line in coords:
        matrix = get_points(matrix, line, diagonals=False)

    return get_count_pts(matrix)


def sol_2():
    matrix = []
    for line in coords:
        matrix = get_points(matrix, line, diagonals=True)

    return get_count_pts(matrix)


print(sol_1())
print(sol_2())
