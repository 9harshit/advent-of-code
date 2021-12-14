from utils import get_data


def Diff(li1, li2):
    return list(set(li1) - set(li2))


DEBUG = False
data = get_data(__file__, DEBUG)

sequence = data[0].split(",")

tables = []
table = []

for row in range(2, len(data)):
    if data[row] == "":
        tables.append(table)
        table = []
    if data[row] != "":
        table.append(data[row].replace("  ", " ").split(",")[0].split(" "))

tables.append(table)

for table in range(len(tables)):
    for row in range(len(tables[table])):
        if "" in tables[table][row]:
            tables[table][row].remove("")


score = [[[0 for _ in range(5)], [0 for _ in range(5)]] for _ in range(len(tables))]
flag = [[], False, 999, []]


def sol_1():
    for number in sequence:
        for table in range(len(tables)):
            for row in range(len(tables[table])):
                if number in tables[table][row]:
                    score[table][0][row] += 1
                    score[table][1][tables[table][row].index(number)] += 1
                    if 5 in score[table][0] or 5 in score[table][1]:
                        flag[0] = table
                        flag[1] = True
                        flag[2] = number
            if flag[1]:
                break
        if flag[1]:
            break

    index_of_sequence = sequence.index(flag[2])

    sum_of_unmarked = 0
    for row in tables[flag[0]]:
        lst = Diff(row, sequence[: index_of_sequence + 1])
        lst = [int(x) for x in lst]
        sum_of_unmarked += sum(lst)

    return int(flag[2]) * sum_of_unmarked


def sol_2():
    total_table = len(tables)
    count = 0
    for number in sequence:
        for table in range(len(tables)):
            for row in range(len(tables[table])):
                if number in tables[table][row]:
                    score[table][0][row] += 1
                    score[table][1][tables[table][row].index(number)] += 1
                    if 5 in score[table][0] or 5 in score[table][1]:
                        if table not in flag[3]:
                            count += 1
                        flag[3].append(table)
                        if count == total_table:
                            count += 1
                            flag[0] = flag[3][-1]
                            flag[2] = number
                        if flag[0] == table:
                            flag[1] = True

            if flag[1]:
                break
        if flag[1]:
            break

    index_of_sequence = sequence.index(flag[2])

    sum_of_unmarked = 0
    for row in tables[flag[0]]:
        lst = Diff(row, sequence[: index_of_sequence + 1])
        lst = [int(x) for x in lst]
        sum_of_unmarked += sum(lst)

    return int(flag[2]) * sum_of_unmarked


# print(sol_1())
print(sol_2())
