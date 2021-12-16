from utils import get_data

DEBUG = False

data = get_data(__file__, DEBUG)

data = [x.split(" | ") for x in data]

data = [[d[0].split(" "), d[1].split(" ")] for d in data]


def sol_1(data):
    count = 0
    for signals in data:
        valid = []
        for signal in signals[0]:
            if len(signal) in [2, 3, 4, 7]:
                valid.append(signal)

        for input in signals[1]:
            if len(input) in [2, 3, 4, 7]:
                for valid_signal in valid:
                    if set(input) == set(valid_signal):
                        count += 1

    return count


def sol_2(data):
    total = []
    answer = [
        {0, 1, 2, 4, 5, 6},
        {2, 5},
        {0, 2, 3, 4, 6},
        {0, 2, 3, 5, 6},
        {1, 2, 3, 5},
        {0, 1, 3, 5, 6},
        {0, 1, 3, 4, 5, 6},
        {0, 2, 5},
        {0, 1, 2, 3, 4, 5, 6},
        {0, 1, 2, 3, 5, 6},
    ]
    numbers = []
    for signals in data:

        display = ["X" for _ in range(7)]
        signals[0] = sorted(signals[0], key=len)

        # use 1 to get alpha at 2 and 5
        display[2] = signals[0][0][0]
        display[5] = signals[0][0][1]

        # use 7 to get alpha at 0
        display[0] = list(set(signals[0][1]) - set(signals[0][0]))[0]

        # use 2,3,5 to find alpha at 3 and 1

        display[3] = list(
            set(signals[0][3])
            & set(signals[0][4])
            & set(signals[0][5])
            & set(signals[0][2])
        )[0]

        display[1] = list(set(signals[0][2]) - set(display))[0]

        # confirm alpha at 2 and 5 using 0,1,3
        temp_sig = ""
        for t in [set(signals[0][3]), set(signals[0][4]), set(signals[0][5])]:
            if {display[0], display[1], display[3]} & t == {
                display[0],
                display[1],
                display[3],
            }:
                temp_sig = t

        if display[5] in temp_sig:
            pass
        else:
            display[2], display[5] = display[5], display[2]

        # use 0,6,9 to find alpha at 4
        display[6] = list(
            (set(signals[0][6]) & set(signals[0][7]) & set(signals[0][8]))
            - set(display)
        )[0]

        display[4] = list(set(signals[0][-1]) - set(display))[0]

        number = []
        for input in signals[1]:
            number.append(set(display.index(i) for i in input))

        numbers.append(number)

    for number in numbers:
        digit = ""
        for n in number:
            digit = digit + str(answer.index(n))

        total.append(int(digit))

    print(total)
    # print(display, number)

    return sum(total)


print(sol_2(data))
