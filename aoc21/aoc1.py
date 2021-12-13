from utils import get_data

DEBUG = False

data = get_data(__file__, DEBUG)


def sol_1():
    count = 0

    for i in range(1, len(lines)):
        if int(lines[i]) > int(lines[i - 1]):
            count += 1

        return count


def sol_2():
    count = 0
    for i in range(0, len(lines) - 3):
        if int(lines[i]) + int(lines[i + 1]) + int(lines[i + 2]) < int(
            lines[i + 1]
        ) + int(lines[i + 2]) + int(lines[i + 3]):
            count += 1

    return count


print(sol_2())
