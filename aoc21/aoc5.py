from math import ceil

import numpy as np
from utils import get_data

DEBUG = False

data = get_data(__file__, DEBUG)

coords = []

min_x, min_y = 999, 999
max_x, max_y = -999, -999


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

matrix = []
for line in coords:
    if (line[0][0] == line[1][0]) or (line[0][1] == line[1][1]):

        pts = []

        # create the points
        ys = np.linspace(line[0][1], line[1][1], max_x)

        xs = np.linspace(line[0][0], line[1][0], max_y)

        # print them
        for i in range(len(xs)):

            pts.append((int(xs[i]), int(ys[i])))

        pts = list(set(pts))
        matrix += pts

from collections import Counter

d = Counter(matrix)

count = 0
for x in d.items():
    if x[1] >= 2:
        count += 1

print(count, max_x, max_y)
