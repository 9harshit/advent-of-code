from utils import get_data

DEBUG = True

data = get_data(__file__, DEBUG)
lst = data.copy()
data = []
for x in lst:
    tmp = []
    for i in x:
        tmp.append(int(i))
    data.append(tmp)


def sol_1(data):
    low_point = []
    basin_location = []
    for i in range(len(data)):
        for j in range(len(data[i])):
            if data[i][j] == 0:
                low_point.append(data[i][j])
                basin_location.append((i, j))
                continue

            if data[i][j] == 9:
                continue

            if i == 0:
                if j == 0:
                    if data[i][j] < data[i][j + 1] and data[i][j] < data[i + 1][j]:
                        low_point.append(data[i][j])
                        basin_location.append((i, j))
                elif j == len(data[i]) - 1:
                    if data[i][j] < data[i][j - 1] and data[i][j] < data[i + 1][j]:
                        low_point.append(data[i][j])
                        basin_location.append((i, j))
                else:
                    if (
                        data[i][j] < data[i + 1][j]
                        and data[i][j] < data[i][j - 1]
                        and data[i][j] < data[i][j + 1]
                    ):
                        low_point.append(data[i][j])
                        basin_location.append((i, j))
                continue

            if i == len(data) - 1:
                if j == 0:
                    if data[i][j] < data[i][j + 1] and data[i][j] < data[i - 1][j]:
                        low_point.append(data[i][j])
                        basin_location.append((i, j))
                elif j == len(data[i]) - 1:
                    if data[i][j] < data[i][j - 1] and data[i][j] < data[i - 1][j]:
                        low_point.append(data[i][j])
                        basin_location.append((i, j))
                else:
                    if (
                        data[i][j] < data[i][j + 1]
                        and data[i][j] < data[i - 1][j]
                        and data[i][j] < data[i][j - 1]
                    ):
                        low_point.append(data[i][j])
                        basin_location.append((i, j))
                continue

            if j == 0:
                if (
                    data[i][j] < data[i][j + 1]
                    and data[i][j] < data[i - 1][j]
                    and data[i][j] < data[i + 1][j]
                ):
                    low_point.append(data[i][j])
                    basin_location.append((i, j))
                continue

            if j == len(data[i]) - 1:
                if (
                    data[i][j] < data[i][j - 1]
                    and data[i][j] < data[i - 1][j]
                    and data[i][j] < data[i + 1][j]
                ):
                    low_point.append(data[i][j])
                    basin_location.append((i, j))
                continue

            else:
                if (
                    data[i][j] < data[i][j + 1]
                    and data[i][j] < data[i + 1][j]
                    and data[i][j] < data[i][j - 1]
                    and data[i][j] < data[i - 1][j]
                ):
                    low_point.append(data[i][j])
                    basin_location.append((i, j))

    return int(sum(low_point) + (1 * len(low_point))), basin_location


def sol_2(data):
    _, basin_location = sol_1(data)
    for x, y in basin_location:
        


# print(sol_1(data))
print(sol_2(data))
