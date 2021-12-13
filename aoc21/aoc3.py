from collections import Counter

from utils import get_data

DEBUG = False
data = get_data(__file__, DEBUG)

len_of_signal = len(data[0])


def gamma_episoln(gamma, episoln, data):
    signal = "".join(data)
    for i in range(len_of_signal):
        wc = Counter(signal[i::len_of_signal])

        count_0 = wc["0"]
        count_1 = wc["1"]

        if count_0 > count_1:
            gamma += "0"
            episoln += "1"
        elif count_0 < count_1:
            gamma += "1"
            episoln += "0"
        else:
            gamma = "1"
            episoln = "0"

            return gamma, episoln

    return gamma, episoln


def get_gamma(gamma, o2_data):
    signal = "".join(o2_data)
    for i in range(len_of_signal):
        wc = Counter(signal[i::len_of_signal])

        count_0 = wc["0"]
        count_1 = wc["1"]

        if count_0 > count_1:
            gamma += "0"
        elif count_0 <= count_1:
            gamma += "1"

    return gamma


def get_episoln(episoln, co2_data):
    signal = "".join(co2_data)
    for i in range(len_of_signal):
        wc = Counter(signal[i::len_of_signal])

        count_0 = wc["0"]
        count_1 = wc["1"]

        if count_0 > count_1:
            episoln += "1"
        elif count_0 <= count_1:
            episoln += "0"
        else:
            episoln = "0"

            return episoln

    return episoln


def sol_1():

    gamma = ""
    episoln = ""

    gamma, episoln = gamma_episoln(gamma, episoln, data)

    return int(gamma, 2) * int(episoln, 2)


def sol_2():
    o2, co2 = "", ""

    o2_data = data.copy()
    co2_data = data.copy()

    for i in range(len(data[0])):
        gamma = get_gamma("", o2_data)
        episoln = get_episoln("", co2_data)

        if gamma == "1":
            for j in range(len(o2_data)):
                if o2_data[j][i] != gamma:
                    o2_data[j] = "9999"

            o2_data = [j for j in o2_data if j != "9999"]

        else:
            if len(o2_data) == 1:
                o2 = o2_data.pop(0)
                print("here")
            else:
                for j in range(len(o2_data)):
                    if o2_data[j][i] != gamma[i]:
                        o2_data[j] = "9999"

                o2_data = [j for j in o2_data if j != "9999"]

        if episoln == "0":
            for j in range(len(co2_data)):
                if co2_data[j][i] != episoln:
                    co2_data[j] = "9999"

            co2_data = [j for j in co2_data if j != "9999"]

        else:

            if len(co2_data) == 1:
                co2 = co2_data.pop(0)
            else:
                for j in range(len(co2_data)):
                    if co2_data[j][i] != episoln[i]:
                        co2_data[j] = "9999"

                co2_data = [j for j in co2_data if j != "9999"]

        if len(o2_data) == 1:
            o2 = o2_data.pop(0)

        if len(co2_data) == 1:
            co2 = co2_data.pop(0)

    return int(o2, 2) * int(co2, 2)


# print(sol_1())
print(sol_2())
