from math import ceil, floor

from utils import get_data

DEBUG = False

data = get_data(__file__, DEBUG)[0].split(",")
data = [int(x) for x in data]


def sol_1(data):
    data.sort()
    mid = len(data) // 2
    position = (data[mid] + data[~mid]) / 2

    fuel = 0
    for pos in data:
        fuel += abs(position - pos)

    return fuel


def sol_2():
    fuel = {}
    positions = []
    positions.append(floor(sum(data) / len(data)))
    positions.append(ceil(sum(data) / len(data)))

    for position in positions:
        fuel[position] = 0
        for pos in data:
            if position in fuel:
                fuel[position] += abs(position - pos) * (abs(position - pos) + 1) / 2

    return min(fuel.values())


print(sol_2())
