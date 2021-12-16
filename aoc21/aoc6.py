from utils import get_data

DEBUG = False

data = get_data(__file__, DEBUG)[0].split(",")
data = [int(x) for x in data]


def get_total_fish(data):

    original_fish = len(data)

    for day in range(256):
        for fish in range(len(data)):
            if data[fish] == 0:
                data.append(8)
                if fish < original_fish:
                    data[fish] = 6
                else:
                    data[fish] = 8
                original_fish += 1
            else:
                data[fish] -= 1

        # print("After  {} day: {}".format(day + 1, data))
    return len(data)

    # if day == 80:
    #     return 1


# print(get_total_fish(data))
"""
Not my solution, but it works.
days = [0] * 9
# Update the current numbers
for fish in data:
    days[fish] += 1
for i in range(256):
    # To make it cyclic: 0, 1, 2, 3, 4, 5, 6, 7, 8
    today = i % len(days)
    # Add new babies
    days[(today + 7) % len(days)] += days[today]
print(f"Total lanternfish after 256 days: {sum(days)}")

"""
