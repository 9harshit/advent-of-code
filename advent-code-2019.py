# 1

""" import math


def fuel(lst):
    answer = 0
    for i in lst:
        j = i // 3 - 2
        answer += j
    print(answer)


fuel(
    [
        83326,
        84939,
        135378,
        105431,
        119144,
        124375,
        138528,
        88896,
        98948,
        85072,
        112576,
        144497,
        112824,
        98892,
        81551,
        139462,
        73213,
        93261,
        130376,
        118425,
        132905,
        54627,
        134676,
        140435,
        131410,
        128441,
        96755,
        94866,
        89490,
        122118,
        106596,
        77531,
        84941,
        57494,
        97518,
        136224,
        69247,
        147209,
        92814,
        63436,
        79819,
        109335,
        85698,
        110103,
        79072,
        52282,
        73957,
        68668,
        105394,
        149663,
        91954,
        66479,
        55778,
        126377,
        75471,
        75662,
        71910,
        113031,
        133917,
        76043,
        65086,
        117882,
        134854,
        60690,
        67495,
        62434,
        67758,
        95329,
        123078,
        128541,
        108213,
        93543,
        147937,
        148262,
        56212,
        148586,
        73733,
        110763,
        149243,
        133232,
        95817,
        68261,
        123872,
        93764,
        147297,
        51555,
        110576,
        89485,
        109570,
        88052,
        132786,
        70585,
        105973,
        85898,
        149990,
        114463,
        147536,
        67786,
        139193,
        112322,
    ]
)
 """
# 1b


""" def fuel2(lst):
    if lst <= 0:
        return 0
    else:
        lst = lst // 3 - 2
        if lst >= 0:
            return lst + fuel2(lst)
        else:
            return fuel2(lst)


def fuel(lst):
    final = 0
    for i in lst:
        final += fuel2(i)

    print(final)


fuel(
    [
        83326,
        84939,
        135378,
        105431,
        119144,
        124375,
        138528,
        88896,
        98948,
        85072,
        112576,
        144497,
        112824,
        98892,
        81551,
        139462,
        73213,
        93261,
        130376,
        118425,
        132905,
        54627,
        134676,
        140435,
        131410,
        128441,
        96755,
        94866,
        89490,
        122118,
        106596,
        77531,
        84941,
        57494,
        97518,
        136224,
        69247,
        147209,
        92814,
        63436,
        79819,
        109335,
        85698,
        110103,
        79072,
        52282,
        73957,
        68668,
        105394,
        149663,
        91954,
        66479,
        55778,
        126377,
        75471,
        75662,
        71910,
        113031,
        133917,
        76043,
        65086,
        117882,
        134854,
        60690,
        67495,
        62434,
        67758,
        95329,
        123078,
        128541,
        108213,
        93543,
        147937,
        148262,
        56212,
        148586,
        73733,
        110763,
        149243,
        133232,
        95817,
        68261,
        123872,
        93764,
        147297,
        51555,
        110576,
        89485,
        109570,
        88052,
        132786,
        70585,
        105973,
        85898,
        149990,
        114463,
        147536,
        67786,
        139193,
        112322,
    ]
)
 """
# 2a
""" def alarm(lst):

    for i in range(0, len(lst), 4):
        if lst[i] not in [1, 2, 99]:
            return lst[0], lst
        if lst[i] == 99:
            return lst[0], lst
        if lst[i] == 1:
            lst[lst[i + 3]] = lst[lst[i + 1]] + lst[lst[i + 2]]
        if lst[i] == 2:
            lst[lst[i + 3]] = lst[lst[i + 1]] * lst[lst[i + 2]]


lst = [
    1,
    0,
    0,
    3,
    1,
    1,
    2,
    3,
    1,
    3,
    4,
    3,
    1,
    5,
    0,
    3,
    2,
    1,
    10,
    19,
    2,
    6,
    19,
    23,
    1,
    23,
    5,
    27,
    1,
    27,
    13,
    31,
    2,
    6,
    31,
    35,
    1,
    5,
    35,
    39,
    1,
    39,
    10,
    43,
    2,
    6,
    43,
    47,
    1,
    47,
    5,
    51,
    1,
    51,
    9,
    55,
    2,
    55,
    6,
    59,
    1,
    59,
    10,
    63,
    2,
    63,
    9,
    67,
    1,
    67,
    5,
    71,
    1,
    71,
    5,
    75,
    2,
    75,
    6,
    79,
    1,
    5,
    79,
    83,
    1,
    10,
    83,
    87,
    2,
    13,
    87,
    91,
    1,
    10,
    91,
    95,
    2,
    13,
    95,
    99,
    1,
    99,
    9,
    103,
    1,
    5,
    103,
    107,
    1,
    107,
    10,
    111,
    1,
    111,
    5,
    115,
    1,
    115,
    6,
    119,
    1,
    119,
    10,
    123,
    1,
    123,
    10,
    127,
    2,
    127,
    13,
    131,
    1,
    13,
    131,
    135,
    1,
    135,
    10,
    139,
    2,
    139,
    6,
    143,
    1,
    143,
    9,
    147,
    2,
    147,
    6,
    151,
    1,
    5,
    151,
    155,
    1,
    9,
    155,
    159,
    2,
    159,
    6,
    163,
    1,
    163,
    2,
    167,
    1,
    10,
    167,
    0,
    99,
    2,
    14,
    0,
    0,
]

# replace position 1 with the value 12 and replace position 2 with the value 2.

lst[1] = 12
lst[2] = 2
# alarm(lst)

# 2b


def alarm2(lst):
    for noun in range(0, 100):
        for verb in range(0, 100):
            data = lst.copy()
            data[1] = noun
            data[2] = verb

            answer, data = alarm(data)
            if answer == 19690720:
                print("found")
                return (100 * data[1]) + data[2]


print(alarm2(lst)) """


# 3a
""" def create_path_x(cor_set, current_cor, des_cor, x):
    while current_cor != des_cor:
        if current_cor < des_cor:
            current_cor += 1
        else:
            current_cor -= 1

        cor_set.add(tuple([x, current_cor]))

    return cor_set


def create_path_y(cor_set, current_cor, des_cor, y):
    while current_cor != des_cor:
        if current_cor < des_cor:
            current_cor += 1
        else:
            current_cor -= 1
        cor_set.add(tuple([current_cor, y]))

    return cor_set


def cor_finder(wire, cor, cor_set):
    dis = 0
    for i in wire:
        if i[0] == "R":
            dis = int(i[1:])
            current = cor[0]
            cor[0] += dis
            create_path_y(cor_set, current, cor[0], cor[1])
            cor_set.add(tuple(cor))

        if i[0] == "L":
            dis = int(i[1:])
            current = cor[0]
            cor[0] -= dis
            create_path_y(cor_set, current, cor[0], cor[1])
            cor_set.add(tuple(cor))

        if i[0] == "U":
            dis = int(i[1:])
            current = cor[1]
            cor[1] += dis
            create_path_x(cor_set, current, cor[1], cor[0])
            cor_set.add(tuple(cor))

        if i[0] == "D":
            dis = int(i[1:])
            current = cor[1]
            cor[1] -= dis
            create_path_x(cor_set, current, cor[1], cor[0])
            cor_set.add(tuple(cor))

    return cor, cor_set


def closer_wire_dis(wire1, wire2):

    cor1 = [0, 0]
    cor2 = [0, 0]
    cor_set1 = set()
    cor_set2 = set()

    cor1, cor_set1 = cor_finder(wire1, cor1, cor_set1)
    cor2, cor_set2 = cor_finder(wire2, cor2, cor_set2)

    intersection = cor_set1.intersection(cor_set2)
    distance = []
    for i in intersection:
        distance.append(abs(i[0]) + abs(i[1]))

    return min(distance), intersection


wire1 = "R995, U671, R852, U741, R347, U539, R324, U865, R839, U885, R924, D983, R865, D823, R457, U124, R807, U941, R900, U718, R896, D795, R714, D129, R465, U470, L625, U200, L707, U552, L447, D305, L351, D571, L346, D38, L609, U581, L98, D707, R535, D332, L23, D630, L66, U833, L699, D445, L981, D81, L627, U273, R226, D51, L177, D806, R459, D950, R627, U462, L382, D847, R335, D573, L902, D581, L375, D288, R26, U922, R710, D159, R481, U907, L852, U926, L905, D140, L581, U908, R158, D955, R349, U708, R196, D13, R628, D862, L899, U50, L56, D89, L506, U65, R664, D243, L701, D887, L552, U665, L674, U813, L433, U87, R951, D970, R914, D705, R79, U328, L107, D86, L307, U550, L872, U224, L595, D600, R442, D426, L139, U528, R680, U35, L951, D275, L78, U113, L509, U821, R150, U668, L981, U102, L632, D864, R636, D597, R385, U322, R464, U249, L286, D138, L993, U329, R874, D849, R6, D632, L751, U235, R817, D495, L152, D528, R872, D91, R973, D399, L14, D544, R20, U54, L793, U90, L756, D36, R668, D221, L286, D681, L901, U312, R290, D874, L155, U863, R35, D177, R900, D865, R250, D810, L448, D648, L358, U308, R986, D562, L112, D858, R77, D880, L12, U702, L987, D662, R771, U6, R643, U845, R54, U987, L994, D878, L934, U805, L85, D760, L775, D578, L557, U544, L522, U495, L678, D68, R615, U700, L415, U597, L964, D858, R504, U805, L392, U140, L721, D215, L842, U929, L30, U64, L748, D136, R274, D605, R863, U460, L354, U78, R705, D298, L456, U117, R308, D186, L707, D367, R824, U965, L162, D19, R950, D582, R911, D436, L165, U506, L186, D906, L69, U412, R810, U13, L350, U314, R192, U963, L143, D937, L685, D574, R434, D937, L365, U646, L741, U703, L66, U959, L103, U799, L480, U340, R981, U96, L675, U662, R536, U15, R171, U382, R396, D431, L922, D662, R365, D921, R915"

wire2 = "L999, D290, L462, D773, L687, D706, L785, D219, R102, U307, L466, D166, R11, D712, L675, D844, R834, U665, R18, D91, R576, U187, L832, D969, L856, U389, R275, D587, L153, U329, R833, U762, R487, U607, R232, D361, R301, D738, L121, D896, R729, D767, R596, U996, R856, D849, R748, D506, L949, U166, R194, D737, L946, D504, L908, D980, L249, U885, R930, D910, R860, D647, L985, U688, L695, U207, L182, D444, R809, D394, R441, U664, L721, U31, R690, U597, R694, U942, R878, U320, R874, U162, L840, U575, L602, U649, L337, D775, L316, D588, R603, D175, L299, D538, R117, U213, L542, D429, R969, D641, R946, D373, L406, D119, R58, D686, R460, U906, L303, D13, L209, D546, R33, D545, R806, U615, R416, D294, L932, D877, R270, U350, R40, U720, L248, D13, L120, D657, L787, U313, R93, U922, R330, D184, L595, D578, R144, D213, L827, U787, R41, D142, R340, D733, L547, U595, L49, U652, L819, D691, R871, D628, R117, U880, L140, U736, L776, U151, R781, U582, R438, D382, R747, D390, R956, U44, L205, U680, R775, D152, L8, D80, R730, U922, L348, U363, L44, D355, R556, D880, R734, U60, R102, U776, L822, D732, L332, D769, L272, D784, R908, U58, L252, U290, R478, D192, R638, U548, R169, D946, L749, D638, L962, U844, R458, D283, R354, U95, L271, U738, R764, U757, R862, U176, L699, D810, L319, U866, R585, U743, L483, D502, R904, D248, L792, D37, R679, U607, L439, U326, L105, U95, L486, D214, R981, U260, R801, U212, L718, U302, L644, D987, L73, U228, L576, U507, L231, D63, R871, U802, R282, D237, L277, U418, R116, U194, R829, U786, L982, D131, R630, U358, R939, D945, L958, D961, R889, U949, L469, D980, R25, D523, L830, U343, R780, U581, R562, U115, L569, D959, R738, U299, L719, U732, L444, D579, L13, U242, L953, U169, R812, D821, R961, D742, R814, D483, R479, D123, L745, D892, L534"
# wire1 = "R8,U5,L5,D3"
# wire2 = "U7,R6,D4,L4"
wire1 = wire1.strip().split(", ")
wire2 = wire2.strip().split(", ")

# intersection for 2b
min_dis, intersection = closer_wire_dis(wire1, wire2)


# 2b
def create_path_x_(current_cor, des_cor, x, intersection):
    step = 0
    while current_cor != des_cor:
        if (x, current_cor) == intersection:
            return step, True
        if current_cor < des_cor:
            current_cor += 1
        else:
            current_cor -= 1
        step += 1

    return step, False


def create_path_y_(current_cor, des_cor, y, intersection):
    step = 0
    while current_cor != des_cor:
        if (current_cor, y) == intersection:
            return step, True
        if current_cor < des_cor:
            current_cor += 1
        else:
            current_cor -= 1

        step += 1

    return step, False


def cor_finder_(wire, cor, intersection):
    dis = 0
    step = 0
    done = False
    for i in wire:
        if done:
            return step
        if i[0] == "R":
            dis = int(i[1:])
            current = cor[0]
            cor[0] += dis
            step_, done = create_path_y_(current, cor[0], cor[1], intersection)
            step += step_

        if i[0] == "L":
            dis = int(i[1:])
            current = cor[0]
            cor[0] -= dis
            step_, done = create_path_y_(current, cor[0], cor[1], intersection)
            step += step_
        if i[0] == "U":
            dis = int(i[1:])
            current = cor[1]
            cor[1] += dis
            step_, done = create_path_x_(current, cor[1], cor[0], intersection)
            step += step_

        if i[0] == "D":
            dis = int(i[1:])
            current = cor[1]
            cor[1] -= dis
            step_, done = create_path_x_(current, cor[1], cor[0], intersection)
            step += step_

    return step


def pathto_intersect(intersection, wire1, wire2):
    intersection = list(intersection)
    step = float("inf")
    for i in intersection:
        step1 = cor_finder_(wire1, [0, 0], i)
        step2 = cor_finder_(wire2, [0, 0], i)
        step = min(step, step1 + step2)

    return step


pathto_intersect(intersection, wire1, wire2)
 """

# 4a IMPORTANT
""" from itertools import groupby

bounds = (271973, 785961)

rules = [
    # Digits are never decreasing
    lambda s: all(int(s[i]) <= int(s[i + 1]) for i in range(len(s) - 1)),
    # Two adjacent digits are equal.
    lambda s: any(s[i] == s[i + 1] for i in range(len(s) - 1)),
    # Two adjacent digits don't form a larger group. 4B
    lambda s: any(len(list(v)) == 2 for _, v in groupby(s)),
]


def test(num, rules):
    return all(f(str(num)) for f in rules)


def solvea(bounds, rules):
    return sum(1 for i in range(bounds[0], bounds[1] + 1) if test(i, rules))


solvea(bounds, rules)
for i in range(bounds[0], bounds[1] + 1):
    for k, v in groupby(str(i)):
        print(k, ":", list(v))
    print("next")
 """
# other moethod

""" from collections import Counter


def part_1(bounds):
    for i in range(bounds[0], bounds[1] + 1):
        x = list(str(i))
        if x != sorted(x) or len(set(x)) == len(x):
            continue
        yield str(i)


def part_2(passwords):
    return sum(1 for x in passwords if 2 in Counter(x).values())


passwords = list(part_1(bounds))
print(len(passwords))
print(part_2(passwords))

for x in passwords:
    if 2 in Counter(x).values():
        print(Counter(x)) """


""" inp = [
    3,
    225,
    1,
    225,
    6,
    6,
    1100,
    1,
    238,
    225,
    104,
    0,
    1101,
    91,
    67,
    225,
    1102,
    67,
    36,
    225,
    1102,
    21,
    90,
    225,
    2,
    13,
    48,
    224,
    101,
    -819,
    224,
    224,
    4,
    224,
    1002,
    223,
    8,
    223,
    101,
    7,
    224,
    224,
    1,
    223,
    224,
    223,
    1101,
    62,
    9,
    225,
    1,
    139,
    22,
    224,
    101,
    -166,
    224,
    224,
    4,
    224,
    1002,
    223,
    8,
    223,
    101,
    3,
    224,
    224,
    1,
    223,
    224,
    223,
    102,
    41,
    195,
    224,
    101,
    -2870,
    224,
    224,
    4,
    224,
    1002,
    223,
    8,
    223,
    101,
    1,
    224,
    224,
    1,
    224,
    223,
    223,
    1101,
    46,
    60,
    224,
    101,
    -106,
    224,
    224,
    4,
    224,
    1002,
    223,
    8,
    223,
    1001,
    224,
    2,
    224,
    1,
    224,
    223,
    223,
    1001,
    191,
    32,
    224,
    101,
    -87,
    224,
    224,
    4,
    224,
    102,
    8,
    223,
    223,
    1001,
    224,
    1,
    224,
    1,
    223,
    224,
    223,
    1101,
    76,
    90,
    225,
    1101,
    15,
    58,
    225,
    1102,
    45,
    42,
    224,
    101,
    -1890,
    224,
    224,
    4,
    224,
    1002,
    223,
    8,
    223,
    1001,
    224,
    5,
    224,
    1,
    224,
    223,
    223,
    101,
    62,
    143,
    224,
    101,
    -77,
    224,
    224,
    4,
    224,
    1002,
    223,
    8,
    223,
    1001,
    224,
    4,
    224,
    1,
    224,
    223,
    223,
    1101,
    55,
    54,
    225,
    1102,
    70,
    58,
    225,
    1002,
    17,
    80,
    224,
    101,
    -5360,
    224,
    224,
    4,
    224,
    102,
    8,
    223,
    223,
    1001,
    224,
    3,
    224,
    1,
    223,
    224,
    223,
    4,
    223,
    99,
    0,
    0,
    0,
    677,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    1105,
    0,
    99999,
    1105,
    227,
    247,
    1105,
    1,
    99999,
    1005,
    227,
    99999,
    1005,
    0,
    256,
    1105,
    1,
    99999,
    1106,
    227,
    99999,
    1106,
    0,
    265,
    1105,
    1,
    99999,
    1006,
    0,
    99999,
    1006,
    227,
    274,
    1105,
    1,
    99999,
    1105,
    1,
    280,
    1105,
    1,
    99999,
    1,
    225,
    225,
    225,
    1101,
    294,
    0,
    0,
    105,
    1,
    0,
    1105,
    1,
    99999,
    1106,
    0,
    300,
    1105,
    1,
    99999,
    1,
    225,
    225,
    225,
    1101,
    314,
    0,
    0,
    106,
    0,
    0,
    1105,
    1,
    99999,
    1008,
    677,
    677,
    224,
    102,
    2,
    223,
    223,
    1005,
    224,
    329,
    1001,
    223,
    1,
    223,
    1108,
    677,
    226,
    224,
    1002,
    223,
    2,
    223,
    1006,
    224,
    344,
    101,
    1,
    223,
    223,
    107,
    677,
    226,
    224,
    1002,
    223,
    2,
    223,
    1006,
    224,
    359,
    101,
    1,
    223,
    223,
    108,
    677,
    677,
    224,
    1002,
    223,
    2,
    223,
    1006,
    224,
    374,
    1001,
    223,
    1,
    223,
    108,
    226,
    677,
    224,
    1002,
    223,
    2,
    223,
    1006,
    224,
    389,
    101,
    1,
    223,
    223,
    7,
    226,
    677,
    224,
    102,
    2,
    223,
    223,
    1006,
    224,
    404,
    1001,
    223,
    1,
    223,
    1108,
    677,
    677,
    224,
    1002,
    223,
    2,
    223,
    1005,
    224,
    419,
    101,
    1,
    223,
    223,
    1008,
    226,
    677,
    224,
    102,
    2,
    223,
    223,
    1006,
    224,
    434,
    101,
    1,
    223,
    223,
    107,
    226,
    226,
    224,
    102,
    2,
    223,
    223,
    1005,
    224,
    449,
    1001,
    223,
    1,
    223,
    1007,
    677,
    677,
    224,
    1002,
    223,
    2,
    223,
    1006,
    224,
    464,
    1001,
    223,
    1,
    223,
    1007,
    226,
    226,
    224,
    1002,
    223,
    2,
    223,
    1005,
    224,
    479,
    101,
    1,
    223,
    223,
    1008,
    226,
    226,
    224,
    102,
    2,
    223,
    223,
    1006,
    224,
    494,
    1001,
    223,
    1,
    223,
    8,
    226,
    226,
    224,
    102,
    2,
    223,
    223,
    1006,
    224,
    509,
    101,
    1,
    223,
    223,
    1107,
    677,
    677,
    224,
    102,
    2,
    223,
    223,
    1005,
    224,
    524,
    1001,
    223,
    1,
    223,
    1108,
    226,
    677,
    224,
    1002,
    223,
    2,
    223,
    1006,
    224,
    539,
    101,
    1,
    223,
    223,
    1107,
    677,
    226,
    224,
    1002,
    223,
    2,
    223,
    1006,
    224,
    554,
    101,
    1,
    223,
    223,
    1007,
    677,
    226,
    224,
    1002,
    223,
    2,
    223,
    1005,
    224,
    569,
    101,
    1,
    223,
    223,
    7,
    677,
    226,
    224,
    1002,
    223,
    2,
    223,
    1006,
    224,
    584,
    101,
    1,
    223,
    223,
    107,
    677,
    677,
    224,
    1002,
    223,
    2,
    223,
    1005,
    224,
    599,
    1001,
    223,
    1,
    223,
    8,
    226,
    677,
    224,
    1002,
    223,
    2,
    223,
    1005,
    224,
    614,
    101,
    1,
    223,
    223,
    7,
    677,
    677,
    224,
    1002,
    223,
    2,
    223,
    1006,
    224,
    629,
    1001,
    223,
    1,
    223,
    1107,
    226,
    677,
    224,
    1002,
    223,
    2,
    223,
    1006,
    224,
    644,
    101,
    1,
    223,
    223,
    108,
    226,
    226,
    224,
    102,
    2,
    223,
    223,
    1005,
    224,
    659,
    1001,
    223,
    1,
    223,
    8,
    677,
    226,
    224,
    1002,
    223,
    2,
    223,
    1005,
    224,
    674,
    101,
    1,
    223,
    223,
    4,
    223,
    99,
    226,
]

i = 0

# inp = [3, 12, 6, 12, 15, 1, 13, 14, 13, 4, 13, 99, -1, 0, 1, 9]


def getparam(mode, i, inp):
    if mode == 1:
        return int(inp[i])
    if mode == 0:
        return int(inp[inp[i]])


while inp[i] != 99:
    if inp[i] == 3:
        a = input("Enter System Id : ")
        inp[inp[i + 1]] = a
        i += 2

    elif inp[i] == 4:
        print("Output : ", inp[inp[i + 1]])
        i += 2

    elif inp[i] == 1:
        inp[inp[i + 3]] = int(inp[inp[i + 1]]) + int(inp[inp[i + 2]])
        i += 4

    elif inp[i] == 2:
        inp[inp[i + 3]] = int(inp[inp[i + 1]]) * int(inp[inp[i + 2]])
        i += 4"""

"""# else:
    code = str(inp[i])
    if len(code) == 4:
        de = int(code[2:])
        c = int(code[1])
        b = int(code[0])

    if len(code) == 3:
        de = int(code[1:])
        c = int(code[0])
        b = 0

    if len(code) == 2:
        de = int(code)
        c, b = 0, 0

    if len(code) == 1:
        de = int(code)
        c, b = 0, 0

    if 1 <= de <= 2:

        param1 = getparam(c, i + 1, inp)
        param2 = getparam(b, i + 2, inp)

        if de == 1:

            inp[inp[i + 3]] = param1 + param2
            i += 4

        if de == 2:
            inp[inp[i + 3]] = param1 * param2
            i += 4

    if 3 <= de <= 4:

        if de == 3:
            a = input("Enter System Id : ")
            inp[inp[i + 1]] = a
            i += 2

        if de == 4:
            param1 = getparam(c, i + 1, inp)
            print("Output : ", inp[inp[i + 1]])
            i += 2

    if 5 <= de <= 8:

        if de == 5:
            param1 = getparam(c, i + 1, inp)
            param2 = getparam(b, i + 2, inp)

            if param1 != 0:
                i = param2
            else:
                i += 3

        if de == 6:
            param1 = getparam(c, i + 1, inp)
            param2 = getparam(b, i + 2, inp)

            if param1 == 0:
                i = param2
            else:
                i += 3

        if de == 7:
            param1 = getparam(c, i + 1, inp)
            param2 = getparam(b, i + 2, inp)

            if param1 < param2:
                inp[inp[i + 3]] = 1
                i += 4

            else:
                inp[inp[i + 3]] = 0
                i += 4

        if de == 8:
            param1 = getparam(c, i + 1, inp)
            param2 = getparam(b, i + 2, inp)

            if param1 == param2:
                inp[inp[i + 3]] = 1
                i += 4

            else:
                inp[inp[i + 3]] = 0
                i += 4

 """
# 6a
""" class Planet:
    def __init__(self, name):
        self.name = name
        self.parent = None
        self.child = set()


class Galaxy:
    def __init__(self, orbit):
        self.galaxy_set = {}
        for orb in orbit:
            planet_name, moon_name = self.get_orbit_info(orb)

            if moon_name not in self.galaxy_set:
                moon = Planet(moon_name)
                self.galaxy_set[moon_name] = moon
            else:
                moon = self.galaxy_set[moon_name]

            if planet_name not in self.galaxy_set:
                planet = Planet(planet_name)
                self.galaxy_set[planet_name] = planet
            else:
                planet = self.galaxy_set[planet_name]

            moon.parent = planet
            planet.child.add(moon)

    def get_orbit_info(self, orb):
        list = orb.split(")")
        return list[0], list[1]

    def calculate_orbit(self):
        total_orbit = 0

        for planet in self.galaxy_set.values():
            while planet.parent:
                total_orbit += 1
                planet = planet.parent

        return total_orbit

    def find_santa(self):
        you = self.galaxy_set["YOU"]
        san = self.galaxy_set["SAN"]
        queue = [(you, [you])]

        while queue:
            (planet, path) = queue.pop(0)

            to_search = set()

            if planet.parent:
                to_search.add(planet.parent)

            for moon in planet.child:
                to_search.add(moon)

            to_search = to_search - set(path)

            for next_planet in to_search:

                if next_planet == san:
                    return len(path) - 2
                else:
                    queue.append((next_planet, path + [next_planet]))

        return 0


orbit = ""
planet_file = open("planet.txt", "r")

for i in planet_file:
    i = i.rstrip("\n")
    orbit = orbit + ", " + i


# orbit = "COM)B, B)C, C)D, D)E, E)F, B)G, G)H, D)I, E)J, J)K, K)L, K)YOU, I)SAN"
orbit = orbit.split(", ")
orbit = orbit[1:]
galaxy = Galaxy(orbit)
print(galaxy.calculate_orbit())
print(galaxy.find_santa())



 """

# 7a


""" data = [
    3,
    8,
    1001,
    8,
    10,
    8,
    105,
    1,
    0,
    0,
    21,
    34,
    51,
    64,
    73,
    98,
    179,
    260,
    341,
    422,
    99999,
    3,
    9,
    102,
    4,
    9,
    9,
    1001,
    9,
    4,
    9,
    4,
    9,
    99,
    3,
    9,
    1001,
    9,
    4,
    9,
    1002,
    9,
    3,
    9,
    1001,
    9,
    5,
    9,
    4,
    9,
    99,
    3,
    9,
    101,
    5,
    9,
    9,
    102,
    5,
    9,
    9,
    4,
    9,
    99,
    3,
    9,
    101,
    5,
    9,
    9,
    4,
    9,
    99,
    3,
    9,
    1002,
    9,
    5,
    9,
    1001,
    9,
    3,
    9,
    102,
    2,
    9,
    9,
    101,
    5,
    9,
    9,
    1002,
    9,
    2,
    9,
    4,
    9,
    99,
    3,
    9,
    1001,
    9,
    1,
    9,
    4,
    9,
    3,
    9,
    1002,
    9,
    2,
    9,
    4,
    9,
    3,
    9,
    1001,
    9,
    2,
    9,
    4,
    9,
    3,
    9,
    1001,
    9,
    2,
    9,
    4,
    9,
    3,
    9,
    102,
    2,
    9,
    9,
    4,
    9,
    3,
    9,
    102,
    2,
    9,
    9,
    4,
    9,
    3,
    9,
    101,
    1,
    9,
    9,
    4,
    9,
    3,
    9,
    101,
    1,
    9,
    9,
    4,
    9,
    3,
    9,
    102,
    2,
    9,
    9,
    4,
    9,
    3,
    9,
    101,
    2,
    9,
    9,
    4,
    9,
    99,
    3,
    9,
    101,
    1,
    9,
    9,
    4,
    9,
    3,
    9,
    1001,
    9,
    1,
    9,
    4,
    9,
    3,
    9,
    102,
    2,
    9,
    9,
    4,
    9,
    3,
    9,
    102,
    2,
    9,
    9,
    4,
    9,
    3,
    9,
    101,
    2,
    9,
    9,
    4,
    9,
    3,
    9,
    101,
    1,
    9,
    9,
    4,
    9,
    3,
    9,
    101,
    1,
    9,
    9,
    4,
    9,
    3,
    9,
    1002,
    9,
    2,
    9,
    4,
    9,
    3,
    9,
    1002,
    9,
    2,
    9,
    4,
    9,
    3,
    9,
    1001,
    9,
    2,
    9,
    4,
    9,
    99,
    3,
    9,
    101,
    2,
    9,
    9,
    4,
    9,
    3,
    9,
    102,
    2,
    9,
    9,
    4,
    9,
    3,
    9,
    1001,
    9,
    2,
    9,
    4,
    9,
    3,
    9,
    1001,
    9,
    2,
    9,
    4,
    9,
    3,
    9,
    1001,
    9,
    2,
    9,
    4,
    9,
    3,
    9,
    101,
    2,
    9,
    9,
    4,
    9,
    3,
    9,
    1001,
    9,
    1,
    9,
    4,
    9,
    3,
    9,
    102,
    2,
    9,
    9,
    4,
    9,
    3,
    9,
    102,
    2,
    9,
    9,
    4,
    9,
    3,
    9,
    101,
    2,
    9,
    9,
    4,
    9,
    99,
    3,
    9,
    1002,
    9,
    2,
    9,
    4,
    9,
    3,
    9,
    102,
    2,
    9,
    9,
    4,
    9,
    3,
    9,
    1001,
    9,
    2,
    9,
    4,
    9,
    3,
    9,
    1002,
    9,
    2,
    9,
    4,
    9,
    3,
    9,
    1001,
    9,
    2,
    9,
    4,
    9,
    3,
    9,
    1002,
    9,
    2,
    9,
    4,
    9,
    3,
    9,
    102,
    2,
    9,
    9,
    4,
    9,
    3,
    9,
    102,
    2,
    9,
    9,
    4,
    9,
    3,
    9,
    101,
    2,
    9,
    9,
    4,
    9,
    3,
    9,
    1001,
    9,
    2,
    9,
    4,
    9,
    99,
    3,
    9,
    1001,
    9,
    1,
    9,
    4,
    9,
    3,
    9,
    101,
    1,
    9,
    9,
    4,
    9,
    3,
    9,
    1002,
    9,
    2,
    9,
    4,
    9,
    3,
    9,
    1001,
    9,
    2,
    9,
    4,
    9,
    3,
    9,
    1001,
    9,
    1,
    9,
    4,
    9,
    3,
    9,
    101,
    1,
    9,
    9,
    4,
    9,
    3,
    9,
    102,
    2,
    9,
    9,
    4,
    9,
    3,
    9,
    1001,
    9,
    2,
    9,
    4,
    9,
    3,
    9,
    1002,
    9,
    2,
    9,
    4,
    9,
    3,
    9,
    1001,
    9,
    2,
    9,
    4,
    9,
    99,
]


# i = 0


def getparam(mode, i, inp):
    if mode == 1:
        return int(inp[i])
    if mode == 0:
        return int(inp[inp[i]])


max_thrust = 0
max_signal = 0
import itertools
 """

# signal = [9, 8, 7, 6, 5]
# for signal in itertools.permutations(range(5, 10), 5):
# input_to_passed = 0
# signal_activate = 1
# i = 0

# for s in signal:
#     i = 0
#     inp = data.copy()
#     signal_activate = 1
#     while inp[i] != 99:

#         # else:
#         code = inp[i].__str__()
#         if len(code) == 4:
#             de = int(code[2:])
#             c = int(code[1])
#             b = int(code[0])

#         if len(code) == 3:
#             de = int(code[1:])
#             c = int(code[0])
#             b = 0

#         if len(code) == 2:
#             de = int(code)
#             c, b = 0, 0

#         if len(code) == 1:
#             de = int(code)
#             c, b = 0, 0

#         if 1 <= de <= 2:

#             param1 = getparam(c, i + 1, inp)
#             param2 = getparam(b, i + 2, inp)

#             if de == 1:

#                 inp[inp[i + 3]] = param1 + param2
#                 i += 4

#             if de == 2:
#                 inp[inp[i + 3]] = param1 * param2
#                 i += 4

#         if 3 <= de <= 4:

#             if de == 3:
#                 if signal_activate != 1:
#                     a = input_to_passed
#                 else:
#                     a = s
#                     # a = input("Enter System Id : ")
#                 print(a)
#                 signal_activate += 1
#                 inp[inp[i + 1]] = a
#                 i += 2

#             if de == 4:
#                 param1 = getparam(c, i + 1, inp)
#                 print("Output : ", inp[inp[i + 1]])

#                 input_to_passed = int(inp[inp[i + 1]])
#                 i += 2

#         if 5 <= de <= 8:

#             if de == 5:
#                 param1 = getparam(c, i + 1, inp)
#                 param2 = getparam(b, i + 2, inp)

#                 if param1 != 0:
#                     i = param2
#                 else:
#                     i += 3

#             if de == 6:
#                 param1 = getparam(c, i + 1, inp)
#                 param2 = getparam(b, i + 2, inp)

#                 if param1 == 0:
#                     i = param2
#                 else:
#                     i += 3

#             if de == 7:
#                 param1 = getparam(c, i + 1, inp)
#                 param2 = getparam(b, i + 2, inp)

#                 if param1 < param2:
#                     inp[inp[i + 3]] = 1
#                     i += 4

#                 else:
#                     inp[inp[i + 3]] = 0
#                     i += 4

#             if de == 8:
#                 param1 = getparam(c, i + 1, inp)
#                 param2 = getparam(b, i + 2, inp)

#                 if param1 == param2:
#                     inp[inp[i + 3]] = 1
#                     i += 4

#                 else:
#                     inp[inp[i + 3]] = 0
#                     i += 4

# if max_thrust < input_to_passed:
#     max_thrust = input_to_passed
#     max_signal = signal


# 7b


""" def amplifier(input_to_passed, s, inp, i, signal_activate):

    while inp[i] != 99:

        # else:
        code = inp[i].__str__()
        if len(code) == 4:
            de = int(code[2:])
            c = int(code[1])
            b = int(code[0])

        if len(code) == 3:
            de = int(code[1:])
            c = int(code[0])
            b = 0

        if len(code) == 2:
            de = int(code)
            c, b = 0, 0

        if len(code) == 1:
            de = int(code)
            c, b = 0, 0

        if 1 <= de <= 2:

            param1 = getparam(c, i + 1, inp)
            param2 = getparam(b, i + 2, inp)

            if de == 1:

                inp[inp[i + 3]] = param1 + param2
                i += 4

            if de == 2:
                inp[inp[i + 3]] = param1 * param2
                i += 4

        if 3 <= de <= 4:

            if de == 3:
                if signal_activate != 1:
                    a = input_to_passed
                else:
                    a = s
                    # a = input("Enter System Id : ")
                print(a)
                signal_activate += 1
                inp[inp[i + 1]] = a
                i += 2

            if de == 4:
                param1 = getparam(c, i + 1, inp)
                print("Output : ", inp[inp[i + 1]])

                input_to_passed = int(inp[inp[i + 1]])
                i += 2
                return input_to_passed, False, inp, i, signal_activate

        if 5 <= de <= 8:

            if de == 5:
                param1 = getparam(c, i + 1, inp)
                param2 = getparam(b, i + 2, inp)

                if param1 != 0:
                    i = param2
                else:
                    i += 3

            if de == 6:
                param1 = getparam(c, i + 1, inp)
                param2 = getparam(b, i + 2, inp)

                if param1 == 0:
                    i = param2
                else:
                    i += 3

            if de == 7:
                param1 = getparam(c, i + 1, inp)
                param2 = getparam(b, i + 2, inp)

                if param1 < param2:
                    inp[inp[i + 3]] = 1
                    i += 4

                else:
                    inp[inp[i + 3]] = 0
                    i += 4

            if de == 8:
                param1 = getparam(c, i + 1, inp)
                param2 = getparam(b, i + 2, inp)

                if param1 == param2:
                    inp[inp[i + 3]] = 1
                    i += 4

                else:
                    inp[inp[i + 3]] = 0
                    i += 4

    return input_to_passed, True, inp, i, signal_activate


max_thrust = 0
max_signal = 0
# signal = [9, 7, 8, 5, 6]

for signal in itertools.permutations(range(5, 10), 5):
    doneE = False
    input_to_passed = 0

    iA, iB, iC, iD, iE = 0, 0, 0, 0, 0
    inpA, inpB, inpC, inpD, inpE = (
        data.copy(),
        data.copy(),
        data.copy(),
        data.copy(),
        data.copy(),
    )

    (
        signal_activateA,
        signal_activateB,
        signal_activateC,
        signal_activateD,
        signal_activateE,
    ) = (1, 1, 1, 1, 1)

    while not doneE:
        input_to_passed, doneA, inpA, iA, signal_activateA = amplifier(
            input_to_passed, signal[0], inpA, iA, signal_activateA
        )

        input_to_passed, doneB, inpB, iB, signal_activateB = amplifier(
            input_to_passed, signal[1], inpB, iB, signal_activateB
        )

        input_to_passed, doneC, inpC, iC, signal_activateC = amplifier(
            input_to_passed, signal[2], inpC, iC, signal_activateC
        )

        input_to_passed, doneD, inpD, iD, signal_activateD = amplifier(
            input_to_passed, signal[3], inpD, iD, signal_activateD
        )

        input_to_passed, doneE, inpE, iE, signal_activateE = amplifier(
            input_to_passed, signal[4], inpE, iE, signal_activateE
        )
    if max_thrust < input_to_passed:
        max_thrust = input_to_passed
        max_signal = signal
 """
""" 

image = "112222222222222212222122220212222222202222222222222122222222202100222222120222101222222122222222221222220102222222222020222222212221222222222222221222102222222222222212222222220222222222202222222222222122222222222100222222120222121222222122222222221222221002222222222222222222202221222222222222222222022222222222222212222222220222222222202222222222222222222222222201222222120222010222222022222222221222220012222222222021222222212222222222222222221222112222222222222222222022222212222222222222222222222022222222202000222222021222021222222222222222221222220202222222222222222222202221222222222222222222212222222222222202222222222222222222222222222222222222222222212021222222021222001222222222222222222222222122222222222222222222222221222222222222221222222222222222222202222122222222222222202222212222222122222202212110222222222222220222222022222222220222221012222222222020222222222221222222222222220222022222222222222202222222221222222222222222212222202122222202202012222222222222220222222122222222222222222122222222222220222222222222222222222212220222112222222222222222222122221212222222222222202222212222222222222111222222121222121222222122222222220222222100222222222221222222212221222222222222221222022222222222222212222022222212222222212222202222222222222212122011222222222222002222222122222222222222220012222222222021222222222220222222222222220222022222222222220212222022222202222222202222212222201122222202222212222222222222102222222222222222222222222212222222222222222222212220222222222202221222002222222222222222222022220212222222212222212222220122222212022201222222121222100222222122222222220222222122222222222122222222202222222222222212222222002222222222222222222122222212222222222222222222222222222222102110222222221222101222222222222222220222221212222222222021222222202222222222222222221222202220222222220212222222222222222222212222202222211022222202022221222222222222001222222122222222021222220012222222222122222222212221222222222222222222212222222222221202222022221222222222222222212222200222222212012101222222021222200222222022222222120222222210222222222021222222212222222222222222220222002222222222221212222222220212222222202222222222212222222222202202222222221222100222222022222222220222222000222222222121222222212220222222222212221222112220222222221222222222222222222222212222212222222122222212122212212222221222010222222022222222022222222002222222222120222222202222222222222202222222222222222222221222222022221222222222212222202222212122222222122201212222120222101222222222222222222222221212222222222120222222222220222222222202220222022221222222222212222122220222222222212222212222212022222202222012222222120222000222222222222222121222222221222022222220222222222222222222222202221222002221222222222222222122222212222222202222012222211222222212112111212222122222020222222022222222022222221011222122222220222222212221222220222211221222112222222222221222222122221222222222222222102222211222222212002101202222020222111222222222022222122222222022222222222122222222222222222220222220222222202222222222220222222122221212222222202222222222222022222222202200222221021222220222221222122222122222221011222022222222222222202220222220222201222222112222222222221202222122222222222222222222012222210122222212012000202222121222011222221022220222020222220002222122222222222222222220222222222202020222002220222222222222222122221022222222202222222222220122222212102201222221022222221222221022022222222222220100202222222220222222202220222221202201221222022221222222220222222022220002222222202222202222210222222202022101202222220222120222221220021222021222221000212122222220222222212222222220222211122222002222222222220202222222221212222222222222102222221222222212002001202222021222011222220021121222222222220201212122222021222222212220222222222221220220022220222222221212222122222222222222222222102222222022222202112000222021022222011222222121220222121222220101222022222122222222212221222222212212122222022220222222121222222222220202222222222222012222210222222212222120222220221222222222221121121222220222220022212222222222222222222220222220202220020222202221212222020222222222221022222222212222112222202022222212212021202222021222202222220122221222120222220020112122222022222222200222222222222210120222022222202222021212222022222002202222222222222222221122222202112201212221020222200220221020120222022222220012212022222120222222212222222222212211122222012222212222020222222122221002212222212222102222222222222210002010212221221222211222221220121222222222220211102122222022222222220221222221222220122221222221212222022202222122222122222222202222012222211022222202222110222121122222112221221222222222121222220202122022222022222222220220222222212200020221202220222222221202222222220202222222222222022222211122222222222120212022221222120222222221120222122222222100222022222021222222201222222220222220220222022222212222120211222122220222212222202222222222202222222212212221202221221222021221220021220222022222222002112122222021222222211220222221222200122222212021202222122200222122220022202222202222222222211222222200122122212122220222112221220122122222120222222222102022222122202222220221222221202202220222102222212222022200222112220222212222212222212222220022222212012020202121120222212221222020220222120222221101122222222022212222210220222221202211222220022021202222222220222120222222202222202222012222210222222210212021212021120222102220222222220222120222221000122122222220202222222020222222212222021222112022212222221202222021222102220222212222022222221022222222202102212021121222101222222120021222122222222212122122222021202222210022222222222212220222112021202222122201222101222212202222202222102222211022222210012010212120222222121221222121021222022222222002112022222222212202200222222222222210222220012121212222120202222012221102212222201222212222212122222220122101212221222222212222222020222222122222221122212022222121212222211221222222222220120222222220222222120221222200221112211222212222112222211122222220222010222121220222211220220120021222022222220021222222222020212212210221222221202222122222012220202222221211222212220202211222201222112222212122222202112222222121122222220222222120120222021222222001212122222021212212200121222221212200022222222020202222020222222100220112221222200222022222221222222200012010212221120222200222222220121222221222222211022222222222202222221122222221212210221220222120212222121200222100220202211222200222022122212122222222122100212121120122212221221021122222020222222102202222222022202222210121222220212200220222122221222222222200222110222012201222222222002022211122222211222001222021022122101220220221120222021222222200112122222020212212210020222220222212122221222220202222020212222010221122202222220222022222220022222221122221212120021122222221222220020222021222220010012222222022202212221121222220222201122220212221212222020211122202220112200222201222112022201222222202102022212021020122021222220222221222021222221000102022222120212222220021222221222222121220102022202222020202222000220002211222221222002022220022222201022112222122121222102220221120121222120222221201212122222222212202220022222222221200022222222222222222022212122211221112222222222222012022222222222220122120212122021022202220222220220222122222222210212122222122212222212021222200220201021222202120222222022221222212220222210222212222202122211222222212002001202022222022200220220222120222021222221222002122222122212222221221222221201211221221012220222221220200122212212102210222210222212122221122222212122101212122022022211221221122122222222222222200012102222020212212221221222202210211221221022021202220022220222101202222211222221222002122211222222202122100212221122022001220222122221222121222221020212002222122222212202222222201222210221220001221212221022221222201211222211222202222122222211222222222122202212121121122010220221222121222021222220201012212222220212212211220222211212202220222221022202222220220122101202022221222221222122222201022222200002202212220021222000222222021220222102222222202202102222120222212211222222201211210021222211120222221021221122120220222220222210222012222201022222221202121222020122122201220021120221222211222220122212122222220212222201221222210200211220222111020212221222211122000220002210222212222202002201222222201222202222222020222011221021120222222211222221120002222222022202222210222222201210201122220001222222221020202122020202022212222201202002012202222222200002101212122121222012220022022120222120222220110102002222122212202211022222220210200220221222121222222220212122020212112220222221212102102212022222210212221202122221022021220021021221222010222222011102222222221202212212020222222202201221221211222202221020201022120202102201222210212202222212122222201222011212121222122201222120220220222121222221210002112222220222202222022222211212221121222101121222222120200222202201012222222201212002012210222222221002111202021221122000222220020121222020222220122202022222020222212211121122211222222220222020220202221120221222111212022221222201212112122222022222221022100222122122122222222122022220222222222220002202212222222212202221222022210221222022220212121222222022222122201222122212222202202212202221122222211102112202222020022002222121221022022200220221020011202222121212212200121122200210202222222111220222220222200022112212002211222200222122202211022222212120211222221220022020220022221021222011222221120011002222021212212222222222210220221121221020222212221022220122000202102201222221212002122212122222001012121202122222022001222220022121022201222020200212112222020202222210021122212212210221222000221222221222202022122200222200222221222222212220222222200000012212120021122210222020120221222202221021000022102222220212112201122022222202201022222211222212222221222122221212112222222220212112212212022222112212011222122220122120222221220022022110221020111000112222120202222202021022221202200022220000220222220222221122122222002222222212212022112221122222201112210212220122222212222020222112222022221122122010222222120222012220121122211212200122220212222202220020202022210212022210222201222222122222022222011002011202120222122211221221222211102101221121202220102222122212212221222122210200202220221010122210220020201022020212122202222212202222212222222222001022201212022020222102220021122201221011221222212010002222220202002200021222201210221121220110221210221020211222012202102201222200212102212222122222212221001202021022122211222020122111221110220021212222012222221212212210020222212201200122221200222211222120212122122201222210222202222222002202222222222001222222121221022020222221022121021110220122211000122222121222011211022222221221111020222011120220220020221022020222212212222222212002212200022222221002221212220021022021222220022222000200222020100202002222200212002200220022220202201220222222021222220221210122101222102220222202212212102201122222002020012222022222202012221221222122121120221021112221212212001222000211220022222212002121220010121212220220201222020220012212222210222102022221022222221101021212021021122122222121222222101101222120110110112212010102111220222222202212011020222212222111222221210122020221212220222211202110022221222222102011120212120020102120221222222111121220222120011112002202010122212222220222201200112021200112121120220020201022110200002202222211222200022220122222200220111212021122012012221221222000211012221021201122212222022022012212022022200202012222212201022210221220211022102210112212222220222200012201222222011120101212022121022002220122121212122002221122101110202212110112012210122022201212210112212110121221222021212022200201102200222211202200022220222222000210201202020021010002222020021201101220220122201220202222102102021212120122211201001112212020122110221022220122122220012212222211202200212212022222022202222222121221202122221220222011000012222221212020212202222212202200221022201221111000200000220002220200210122221222012202222211212000202222222222021201101202122122020222220120221112200121210020210101122212201012021210221122200211102212200012020200220220222022111212202211222222222222212202122222111202022222222121021111220220120001220120222021211200002222000022000202221222210210220101220102021110220112200221122210212212222220222012112220122222112020110222220121121211202020022111000100211022112020212212121102022212222122202222220201212002022012222002202020010222212212202202202222212212022222010210101202122020002101222022122202022121222120220100102212120012020220020222201201000211211120120112222202212222021021112220202202202120022212022222021111220202222022222121201022120201010212211122121202002212121222222222022022202221021010201111201200220112201122220010222210222202222102012222222222112020002222020121220221221021221211212021202121021100022212020212210212122122201220120000211202201121222101222220202122002210222210202221222202222222221210001212022120221222211020022022001002220220222000012202021002020200222022210221011220200101202012220220202221201020122220222222202202112220222222102121221212122021100121210020122112201210220021120012002202101002002220220222212201022100221122220011210011222021020201022211222200212121112200022022002210100212222022122000200021120110212011200220001020202212022122122202220222211002022220200122020122200001212021200110202212222212212001212222022222000200101222010221210201211021022111100001221120221201212212222202211220121022221001121111221222212011200110202120121001202200212222202212202212122022100010012222211121110001202022222120022020221222002202002222011102212200220022210111202010210122212200211000102021001010202220222202202100222220122022100112200212211122012202011020220102021210202020221000222202020212201210022122202012211212211010011200211002020122110021022202202222222211112211222222000102010222222221112210211122122022112122222020001002212222101102221201021222210201010220221011022102202110221221022010222222222221212022102221222022120111002202210022121121100221121221000120212022212121112212220112010212222222211020222010202112201010212110001220102211222220222210202210112221122212201222200212112221120220212020221201100210210120111020112212100112201211020122222020211220200002101012201211122221022201012201202212222102112221022102021100112212201021102002011222120220200200202022110012122202000212202220221122211020011012210022000121200121200122202011212220212212212222222202022022000220022212102221100111101221120002111210000122201220212202100002202202022022201110201021222110120202222000012021211021122212221220202201022201122122001201022212210220121002000020121212020022021221222111012202210102211201121022210002120001220212020012210020222021120121222220221201222102002202222022000201001222122220222210010222022102200120202220002201102212001112012210200022220101122102202111121121210100220221020012212200210212202111212201022012201010020202201020202110002122220211200202212021001110022202001022022220201122212012010111210101002020222011112222111210122200220012220220002210222222001012120222112121012001112021121202212121112121012112112212210002010210222222202111200210211202121012002102000101211111010100120221012202200121110120121110120020121100021222100011001001200112000212100001000010102120220120002000122100001220102"

# image = "0222112222120000"
row, col = 25, 6

elements_in_layer = row * col

layers = [
    image[i : i + elements_in_layer] for i in range(0, len(image), elements_in_layer)
]

min_count_zero = float("inf")
layer_check = layers[0]


for layer in layers:
    count_zero = layer.count("0")
    if count_zero < min_count_zero:
        min_count_zero = count_zero
        layer_check = layer

# print(layer_check)

final_answer = layer_check.count("1") * layer_check.count("2")

# 8B


index = [i for i in range(len(layers[0]))]
final_image = [0] * len(layers[0])

# # while index:
# for layer in layers:
#     if not index:
#         break
#     else:
#         for i in index:
#             if layer[i] != "2":
#                 final_image[i] = layer[i]
#                 index.remove(i)


for i in index:
    for layer in layers:
        if layer[i] != "2":
            final_image[i] = layer[i]
            break

str1 = "".join(str(s) for s in final_image)

rows = 0

for i in range(len(str1)):
    if str1[i] != "0":
        print("█", end="")
    # if final_image[i] == "0":
    #     print(" ", end="")
    else:
        print(" ", end="")

    rows += 1
    if rows == row:
        print("")
        rows = 0
 """

# 9
""" inp = [
    1102,
    34463338,
    34463338,
    63,
    1007,
    63,
    34463338,
    63,
    1005,
    63,
    53,
    1102,
    1,
    3,
    1000,
    109,
    988,
    209,
    12,
    9,
    1000,
    209,
    6,
    209,
    3,
    203,
    0,
    1008,
    1000,
    1,
    63,
    1005,
    63,
    65,
    1008,
    1000,
    2,
    63,
    1005,
    63,
    904,
    1008,
    1000,
    0,
    63,
    1005,
    63,
    58,
    4,
    25,
    104,
    0,
    99,
    4,
    0,
    104,
    0,
    99,
    4,
    17,
    104,
    0,
    99,
    0,
    0,
    1101,
    0,
    493,
    1024,
    1102,
    1,
    38,
    1015,
    1101,
    20,
    0,
    1011,
    1101,
    0,
    509,
    1026,
    1101,
    0,
    32,
    1018,
    1101,
    0,
    333,
    1022,
    1102,
    1,
    0,
    1020,
    1101,
    326,
    0,
    1023,
    1101,
    0,
    33,
    1010,
    1101,
    21,
    0,
    1016,
    1101,
    25,
    0,
    1004,
    1102,
    28,
    1,
    1008,
    1102,
    1,
    506,
    1027,
    1102,
    488,
    1,
    1025,
    1101,
    0,
    27,
    1013,
    1101,
    1,
    0,
    1021,
    1101,
    0,
    34,
    1019,
    1101,
    607,
    0,
    1028,
    1102,
    1,
    23,
    1003,
    1102,
    26,
    1,
    1007,
    1102,
    29,
    1,
    1009,
    1101,
    31,
    0,
    1000,
    1102,
    37,
    1,
    1012,
    1101,
    30,
    0,
    1005,
    1101,
    602,
    0,
    1029,
    1101,
    36,
    0,
    1002,
    1102,
    1,
    22,
    1001,
    1102,
    1,
    35,
    1014,
    1102,
    24,
    1,
    1006,
    1102,
    39,
    1,
    1017,
    109,
    4,
    21102,
    40,
    1,
    6,
    1008,
    1010,
    40,
    63,
    1005,
    63,
    203,
    4,
    187,
    1106,
    0,
    207,
    1001,
    64,
    1,
    64,
    1002,
    64,
    2,
    64,
    109,
    13,
    1206,
    3,
    221,
    4,
    213,
    1106,
    0,
    225,
    1001,
    64,
    1,
    64,
    1002,
    64,
    2,
    64,
    109,
    -5,
    1208,
    -9,
    22,
    63,
    1005,
    63,
    241,
    1106,
    0,
    247,
    4,
    231,
    1001,
    64,
    1,
    64,
    1002,
    64,
    2,
    64,
    109,
    -5,
    21107,
    41,
    40,
    3,
    1005,
    1010,
    263,
    1106,
    0,
    269,
    4,
    253,
    1001,
    64,
    1,
    64,
    1002,
    64,
    2,
    64,
    109,
    -1,
    1202,
    3,
    1,
    63,
    1008,
    63,
    29,
    63,
    1005,
    63,
    295,
    4,
    275,
    1001,
    64,
    1,
    64,
    1106,
    0,
    295,
    1002,
    64,
    2,
    64,
    109,
    16,
    21108,
    42,
    42,
    -8,
    1005,
    1014,
    313,
    4,
    301,
    1105,
    1,
    317,
    1001,
    64,
    1,
    64,
    1002,
    64,
    2,
    64,
    109,
    -4,
    2105,
    1,
    5,
    1001,
    64,
    1,
    64,
    1105,
    1,
    335,
    4,
    323,
    1002,
    64,
    2,
    64,
    109,
    -5,
    1207,
    -4,
    28,
    63,
    1005,
    63,
    355,
    1001,
    64,
    1,
    64,
    1105,
    1,
    357,
    4,
    341,
    1002,
    64,
    2,
    64,
    109,
    2,
    21102,
    43,
    1,
    -1,
    1008,
    1014,
    45,
    63,
    1005,
    63,
    377,
    1106,
    0,
    383,
    4,
    363,
    1001,
    64,
    1,
    64,
    1002,
    64,
    2,
    64,
    109,
    -10,
    1208,
    -3,
    36,
    63,
    1005,
    63,
    401,
    4,
    389,
    1106,
    0,
    405,
    1001,
    64,
    1,
    64,
    1002,
    64,
    2,
    64,
    109,
    6,
    21107,
    44,
    45,
    1,
    1005,
    1012,
    423,
    4,
    411,
    1105,
    1,
    427,
    1001,
    64,
    1,
    64,
    1002,
    64,
    2,
    64,
    109,
    4,
    21101,
    45,
    0,
    3,
    1008,
    1018,
    45,
    63,
    1005,
    63,
    453,
    4,
    433,
    1001,
    64,
    1,
    64,
    1105,
    1,
    453,
    1002,
    64,
    2,
    64,
    109,
    -23,
    2101,
    0,
    10,
    63,
    1008,
    63,
    36,
    63,
    1005,
    63,
    475,
    4,
    459,
    1106,
    0,
    479,
    1001,
    64,
    1,
    64,
    1002,
    64,
    2,
    64,
    109,
    26,
    2105,
    1,
    6,
    4,
    485,
    1105,
    1,
    497,
    1001,
    64,
    1,
    64,
    1002,
    64,
    2,
    64,
    109,
    4,
    2106,
    0,
    5,
    1105,
    1,
    515,
    4,
    503,
    1001,
    64,
    1,
    64,
    1002,
    64,
    2,
    64,
    109,
    -25,
    1201,
    10,
    0,
    63,
    1008,
    63,
    26,
    63,
    1005,
    63,
    537,
    4,
    521,
    1105,
    1,
    541,
    1001,
    64,
    1,
    64,
    1002,
    64,
    2,
    64,
    109,
    18,
    21101,
    46,
    0,
    -1,
    1008,
    1014,
    43,
    63,
    1005,
    63,
    565,
    1001,
    64,
    1,
    64,
    1106,
    0,
    567,
    4,
    547,
    1002,
    64,
    2,
    64,
    109,
    -6,
    1201,
    -4,
    0,
    63,
    1008,
    63,
    33,
    63,
    1005,
    63,
    587,
    1105,
    1,
    593,
    4,
    573,
    1001,
    64,
    1,
    64,
    1002,
    64,
    2,
    64,
    109,
    22,
    2106,
    0,
    -3,
    4,
    599,
    1105,
    1,
    611,
    1001,
    64,
    1,
    64,
    1002,
    64,
    2,
    64,
    109,
    -28,
    2102,
    1,
    -2,
    63,
    1008,
    63,
    22,
    63,
    1005,
    63,
    633,
    4,
    617,
    1105,
    1,
    637,
    1001,
    64,
    1,
    64,
    1002,
    64,
    2,
    64,
    109,
    -1,
    21108,
    47,
    44,
    9,
    1005,
    1011,
    653,
    1105,
    1,
    659,
    4,
    643,
    1001,
    64,
    1,
    64,
    1002,
    64,
    2,
    64,
    109,
    10,
    2107,
    24,
    -8,
    63,
    1005,
    63,
    681,
    4,
    665,
    1001,
    64,
    1,
    64,
    1105,
    1,
    681,
    1002,
    64,
    2,
    64,
    109,
    -11,
    2107,
    31,
    4,
    63,
    1005,
    63,
    697,
    1106,
    0,
    703,
    4,
    687,
    1001,
    64,
    1,
    64,
    1002,
    64,
    2,
    64,
    109,
    8,
    2101,
    0,
    -8,
    63,
    1008,
    63,
    23,
    63,
    1005,
    63,
    727,
    1001,
    64,
    1,
    64,
    1105,
    1,
    729,
    4,
    709,
    1002,
    64,
    2,
    64,
    109,
    -16,
    2108,
    21,
    10,
    63,
    1005,
    63,
    749,
    1001,
    64,
    1,
    64,
    1106,
    0,
    751,
    4,
    735,
    1002,
    64,
    2,
    64,
    109,
    17,
    2108,
    36,
    -8,
    63,
    1005,
    63,
    769,
    4,
    757,
    1105,
    1,
    773,
    1001,
    64,
    1,
    64,
    1002,
    64,
    2,
    64,
    109,
    -10,
    1207,
    1,
    23,
    63,
    1005,
    63,
    791,
    4,
    779,
    1105,
    1,
    795,
    1001,
    64,
    1,
    64,
    1002,
    64,
    2,
    64,
    109,
    -3,
    2102,
    1,
    6,
    63,
    1008,
    63,
    22,
    63,
    1005,
    63,
    815,
    1106,
    0,
    821,
    4,
    801,
    1001,
    64,
    1,
    64,
    1002,
    64,
    2,
    64,
    109,
    16,
    1205,
    7,
    837,
    1001,
    64,
    1,
    64,
    1105,
    1,
    839,
    4,
    827,
    1002,
    64,
    2,
    64,
    109,
    -5,
    1202,
    0,
    1,
    63,
    1008,
    63,
    30,
    63,
    1005,
    63,
    863,
    1001,
    64,
    1,
    64,
    1106,
    0,
    865,
    4,
    845,
    1002,
    64,
    2,
    64,
    109,
    4,
    1205,
    9,
    883,
    4,
    871,
    1001,
    64,
    1,
    64,
    1106,
    0,
    883,
    1002,
    64,
    2,
    64,
    109,
    16,
    1206,
    -7,
    899,
    1001,
    64,
    1,
    64,
    1106,
    0,
    901,
    4,
    889,
    4,
    64,
    99,
    21102,
    1,
    27,
    1,
    21101,
    915,
    0,
    0,
    1105,
    1,
    922,
    21201,
    1,
    47633,
    1,
    204,
    1,
    99,
    109,
    3,
    1207,
    -2,
    3,
    63,
    1005,
    63,
    964,
    21201,
    -2,
    -1,
    1,
    21102,
    942,
    1,
    0,
    1105,
    1,
    922,
    22102,
    1,
    1,
    -1,
    21201,
    -2,
    -3,
    1,
    21101,
    957,
    0,
    0,
    1106,
    0,
    922,
    22201,
    1,
    -1,
    -2,
    1105,
    1,
    968,
    22101,
    0,
    -2,
    -2,
    109,
    -3,
    2106,
    0,
    0,
]

# inp = [104, 1125899906842624, 99]

input_extnd = {}

for key, i in enumerate(inp):
    input_extnd[key] = i

extend_mem_index = 0


def getparam(mode, i, input_extnd, base):

    global extend_mem_index
    if extend_mem_index >= len(inp):
        extend_mem_index = 0

    if mode == 1:

        if i not in input_extnd:
            input_extnd[i] = input_extnd[extend_mem_index]
            extend_mem_index += 1
        return int(input_extnd[i])

    if mode == 0:
        if input_extnd[i] not in input_extnd:
            input_extnd[input_extnd[i]] = input_extnd[extend_mem_index]
            extend_mem_index += 1

        return int(input_extnd[input_extnd[i]])

    if mode == 2:

        if input_extnd[i] + base not in input_extnd:
            input_extnd[input_extnd[i] + base] = input_extnd[extend_mem_index]
            extend_mem_index += 1

        return int(input_extnd[input_extnd[i] + base])


base = 0
i = 0

while input_extnd[i] != 99:

    code = str(input_extnd[i])

    if len(code) == 5:
        de = int(code[3:])
        c = int(code[2])
        b = int(code[1])
        a = int(code[0])

    if len(code) == 4:
        de = int(code[2:])
        c = int(code[1])
        b = int(code[0])
        a = 0

    if len(code) == 3:
        de = int(code[1:])
        c = int(code[0])
        a, b = 0, 0

    if len(code) == 2:
        de = int(code)
        a, c, b = 0, 0, 0

    if len(code) == 1:
        de = int(code)
        a, c, b = 0, 0, 0

    param1 = getparam(c, i + 1, input_extnd, base)

    if de not in [3, 4, 9]:
        param2 = getparam(b, i + 2, input_extnd, base)

    if 1 <= de <= 2:

        if de == 1:

            if a == 2:
                input_extnd[input_extnd[i + 3] + base] = param1 + param2
            else:
                input_extnd[input_extnd[i + 3]] = param1 + param2

        if de == 2:
            if a == 2:
                input_extnd[input_extnd[i + 3] + base] = param1 * param2
            else:

                input_extnd[input_extnd[i + 3]] = param1 * param2

        i += 4

    if 3 <= de <= 4 or de == 9:

        if de == 3:

            a = input("Enter System Id : ")
            if c == 2:
                input_extnd[base + input_extnd[i + 1]] = int(a)
            else:
                input_extnd[input_extnd[i + 1]] = int(a)

        if de == 4:
            print("Output : ", param1)
            if param1 == 99:
                break

        if de == 9:
            base += param1

        i += 2

    if 5 <= de <= 8:

        if de == 5:

            if param1 != 0:
                i = param2
            else:
                i += 3

        if de == 6:

            if param1 == 0:
                i = param2
            else:
                i += 3

        if de == 7:

            if param1 < param2:
                if a == 2:
                    input_extnd[input_extnd[i + 3] + base] = 1
                else:
                    input_extnd[input_extnd[i + 3]] = 1
                i += 4

            else:
                if a == 2:
                    input_extnd[input_extnd[i + 3] + base] = 0
                else:
                    input_extnd[input_extnd[i + 3]] = 0
                i += 4

        if de == 8:

            if param1 == param2: 2
            
                if a == 2:
                    input_extnd[input_extnd[i + 3] + base] = 1

                else:
                    input_extnd[input_extnd[i + 3]] = 1
                i += 4

            else:
                if a == 2:
                    input_extnd[input_extnd[i + 3] + base] = 0

                else:
                    input_extnd[input_extnd[i + 3]] = 0
                i += 4
 """
# 10a
""" from collections import OrderedDict

input_file = open("input10.txt")

input = []
for i in input_file:
    input.append(i.replace("\n", ""))

row = len(input)
col = len(input[0])
cor_asteroid = OrderedDict()
los = {}
slope_seen = set()

index = 0
for i in range(row):
    for j in range(col):
        if input[i][j] == "#":
            k = str((j, i))
            cor_asteroid[index] = (j, i)
            los[k] = 0
            index += 1

slope_from_base = set()
max_asteroid = float("-inf")
max_slope_all = set()
slope_all = OrderedDict()


for i in cor_asteroid.values():
    for j in cor_asteroid.values():
        if i == j:
            continue
        else:

            x = j[0] - i[0]
            y = j[1] - i[1]
            if j[0] > i[0]:
                direction = "L"
            else:
                direction = "R"

            if j[1] > i[1]:
                direction = direction + "D"
            else:
                direction = direction + "U"

            if x == 0 and "U" in direction:
                slope = "undefined"
            elif x == 0 and "D" in direction:
                slope = "-undefined"
            else:
                slope = y / x

            if (slope, direction) not in slope_seen:
                slope_seen.add((slope, direction))
                k = str(i)
                los[k] += 1

            l = str(j)
            slope_all[l] = slope, direction

    if los[str(i)] > max_asteroid:
        base_asteroid = i

        slope_from_base.clear()
        max_slope_all.clear()

        slope_from_base = slope_seen.copy()
        max_slope_all = slope_all.copy()
        max_asteroid = los[str(i)]

    slope_seen.clear()


# 10b
import math

laser_cor = base_asteroid
# print(max_slope_all)
# print(slope_from_base)


all_angle_from_base = {}
angle_from_base = set()
run = 0

for i in slope_from_base:
    if i[0] == "undefined" and "U" in i[1]:
        angle_from_base.add(-90)
        run += 1

    elif i[0] == "-undefined" and "D" in i[1]:
        angle_from_base.add(90)
        run += 1
    elif i[1] not in ["LD", "LU"]:
        angle_from_base.add(180 + math.degrees(math.atan(i[0])))
        run += 1
    else:
        angle_from_base.add(math.degrees(math.atan(i[0])))
        run += 1


# print(angle_from_base)

for i in max_slope_all:
    if max_slope_all[i][0] == "undefined":
        all_angle_from_base[i] = -90
    elif max_slope_all[i][0] == "-undefined":
        all_angle_from_base[i] = 90
    elif max_slope_all[i][1] not in ["LD", "LU"]:
        all_angle_from_base[i] = 180 + math.degrees(math.atan(max_slope_all[i][0]))
    else:
        all_angle_from_base[i] = math.degrees(math.atan(max_slope_all[i][0]))

angle_from_base = sorted(angle_from_base)

sorted_angle = [
    (angle, point)
    for angle, point in sorted(
        all_angle_from_base.items(),
        key=lambda all_angle_from_base: all_angle_from_base[1],
    )
]
destroyed = 0

def string_to_set(x):
    value1 = ""
    value2 = ""

    index = 0

    for i in x[1:]:
        if i != ",":
            value1 = value1 + i
            index += 1
        else:
            break

    for i in range(index + 2, len(x) - 1):
        value2 = value2 + x[i]
    return (int(value1), int(value2))


sorted_angle.remove((str(laser_cor), 0))

while sorted_angle:
    for i in angle_from_base:

        targets_top = [x for x in sorted_angle if x[1] == i]
        target = None

        min_dis = float("inf")
        for x in targets_top:

            x = string_to_set(x[0])
            dis = math.dist(x, base_asteroid)
            if dis < min_dis:
                target = x
                min_dis = dis

        if target != laser_cor and target:
            destroyed += 1
            print("Destroyed at:", destroyed, "Asteroid : ", str(target), i)
            sorted_angle.remove((str(target), i))

        if destroyed == 200:
            print("200th : ", target) """

""" inp = [
    3,
    8,
    1005,
    8,
    329,
    1106,
    0,
    11,
    0,
    0,
    0,
    104,
    1,
    104,
    0,
    3,
    8,
    102,
    -1,
    8,
    10,
    1001,
    10,
    1,
    10,
    4,
    10,
    1008,
    8,
    0,
    10,
    4,
    10,
    1002,
    8,
    1,
    29,
    2,
    1102,
    1,
    10,
    1,
    1009,
    16,
    10,
    2,
    4,
    4,
    10,
    1,
    9,
    5,
    10,
    3,
    8,
    1002,
    8,
    -1,
    10,
    101,
    1,
    10,
    10,
    4,
    10,
    108,
    0,
    8,
    10,
    4,
    10,
    101,
    0,
    8,
    66,
    2,
    106,
    7,
    10,
    1006,
    0,
    49,
    3,
    8,
    1002,
    8,
    -1,
    10,
    101,
    1,
    10,
    10,
    4,
    10,
    108,
    1,
    8,
    10,
    4,
    10,
    1002,
    8,
    1,
    95,
    1006,
    0,
    93,
    3,
    8,
    102,
    -1,
    8,
    10,
    1001,
    10,
    1,
    10,
    4,
    10,
    108,
    1,
    8,
    10,
    4,
    10,
    102,
    1,
    8,
    120,
    1006,
    0,
    61,
    2,
    1108,
    19,
    10,
    2,
    1003,
    2,
    10,
    1006,
    0,
    99,
    3,
    8,
    1002,
    8,
    -1,
    10,
    1001,
    10,
    1,
    10,
    4,
    10,
    1008,
    8,
    0,
    10,
    4,
    10,
    101,
    0,
    8,
    157,
    3,
    8,
    102,
    -1,
    8,
    10,
    1001,
    10,
    1,
    10,
    4,
    10,
    1008,
    8,
    1,
    10,
    4,
    10,
    1001,
    8,
    0,
    179,
    2,
    1108,
    11,
    10,
    1,
    1102,
    19,
    10,
    3,
    8,
    102,
    -1,
    8,
    10,
    1001,
    10,
    1,
    10,
    4,
    10,
    1008,
    8,
    1,
    10,
    4,
    10,
    101,
    0,
    8,
    209,
    2,
    108,
    20,
    10,
    3,
    8,
    1002,
    8,
    -1,
    10,
    101,
    1,
    10,
    10,
    4,
    10,
    108,
    1,
    8,
    10,
    4,
    10,
    101,
    0,
    8,
    234,
    3,
    8,
    102,
    -1,
    8,
    10,
    101,
    1,
    10,
    10,
    4,
    10,
    108,
    0,
    8,
    10,
    4,
    10,
    1002,
    8,
    1,
    256,
    2,
    1102,
    1,
    10,
    1006,
    0,
    69,
    2,
    108,
    6,
    10,
    2,
    4,
    13,
    10,
    3,
    8,
    102,
    -1,
    8,
    10,
    101,
    1,
    10,
    10,
    4,
    10,
    1008,
    8,
    0,
    10,
    4,
    10,
    1002,
    8,
    1,
    294,
    1,
    1107,
    9,
    10,
    1006,
    0,
    87,
    2,
    1006,
    8,
    10,
    2,
    1001,
    16,
    10,
    101,
    1,
    9,
    9,
    1007,
    9,
    997,
    10,
    1005,
    10,
    15,
    99,
    109,
    651,
    104,
    0,
    104,
    1,
    21101,
    387395195796,
    0,
    1,
    21101,
    346,
    0,
    0,
    1105,
    1,
    450,
    21101,
    0,
    48210129704,
    1,
    21101,
    0,
    357,
    0,
    1105,
    1,
    450,
    3,
    10,
    104,
    0,
    104,
    1,
    3,
    10,
    104,
    0,
    104,
    0,
    3,
    10,
    104,
    0,
    104,
    1,
    3,
    10,
    104,
    0,
    104,
    1,
    3,
    10,
    104,
    0,
    104,
    0,
    3,
    10,
    104,
    0,
    104,
    1,
    21101,
    0,
    46413147328,
    1,
    21102,
    404,
    1,
    0,
    1106,
    0,
    450,
    21102,
    179355823323,
    1,
    1,
    21101,
    415,
    0,
    0,
    1105,
    1,
    450,
    3,
    10,
    104,
    0,
    104,
    0,
    3,
    10,
    104,
    0,
    104,
    0,
    21102,
    1,
    838345843476,
    1,
    21101,
    0,
    438,
    0,
    1105,
    1,
    450,
    21101,
    709475709716,
    0,
    1,
    21101,
    449,
    0,
    0,
    1105,
    1,
    450,
    99,
    109,
    2,
    22102,
    1,
    -1,
    1,
    21102,
    40,
    1,
    2,
    21101,
    0,
    481,
    3,
    21101,
    0,
    471,
    0,
    1105,
    1,
    514,
    109,
    -2,
    2105,
    1,
    0,
    0,
    1,
    0,
    0,
    1,
    109,
    2,
    3,
    10,
    204,
    -1,
    1001,
    476,
    477,
    492,
    4,
    0,
    1001,
    476,
    1,
    476,
    108,
    4,
    476,
    10,
    1006,
    10,
    508,
    1101,
    0,
    0,
    476,
    109,
    -2,
    2106,
    0,
    0,
    0,
    109,
    4,
    2101,
    0,
    -1,
    513,
    1207,
    -3,
    0,
    10,
    1006,
    10,
    531,
    21101,
    0,
    0,
    -3,
    21201,
    -3,
    0,
    1,
    21201,
    -2,
    0,
    2,
    21101,
    1,
    0,
    3,
    21101,
    550,
    0,
    0,
    1105,
    1,
    555,
    109,
    -4,
    2106,
    0,
    0,
    109,
    5,
    1207,
    -3,
    1,
    10,
    1006,
    10,
    578,
    2207,
    -4,
    -2,
    10,
    1006,
    10,
    578,
    21201,
    -4,
    0,
    -4,
    1105,
    1,
    646,
    22101,
    0,
    -4,
    1,
    21201,
    -3,
    -1,
    2,
    21202,
    -2,
    2,
    3,
    21101,
    597,
    0,
    0,
    1105,
    1,
    555,
    22102,
    1,
    1,
    -4,
    21101,
    0,
    1,
    -1,
    2207,
    -4,
    -2,
    10,
    1006,
    10,
    616,
    21101,
    0,
    0,
    -1,
    22202,
    -2,
    -1,
    -2,
    2107,
    0,
    -3,
    10,
    1006,
    10,
    638,
    22102,
    1,
    -1,
    1,
    21101,
    638,
    0,
    0,
    106,
    0,
    513,
    21202,
    -2,
    -1,
    -2,
    22201,
    -4,
    -2,
    -4,
    109,
    -5,
    2106,
    0,
    0,
]

from collections import OrderedDict

panel_painted = OrderedDict()
robot_face_direction = "UP"

position = (0, 0)

min_x, min_y, max_x, max_y = 0, 0, 0, 0

input_extnd = {}

for key, i in enumerate(inp):
    input_extnd[key] = i

extend_mem_index = 0
get_param = 0
panel_painted = {(0, 0): 1}


def getparam(mode, i, input_extnd, base):

    global extend_mem_index
    if extend_mem_index >= len(inp):
        extend_mem_index = 0

    if mode == 1:

        if i not in input_extnd:
            input_extnd[i] = input_extnd[extend_mem_index]
            extend_mem_index += 1
        return int(input_extnd[i])

    if mode == 0:
        if input_extnd[i] not in input_extnd:
            input_extnd[input_extnd[i]] = input_extnd[extend_mem_index]
            extend_mem_index += 1

        return int(input_extnd[input_extnd[i]])

    if mode == 2:

        if input_extnd[i] + base not in input_extnd:
            input_extnd[input_extnd[i] + base] = input_extnd[extend_mem_index]
            extend_mem_index += 1

        return int(input_extnd[input_extnd[i] + base])


base = 0
i = 0


def change_position(position, robot_face_direction, change_direction_to):

    if robot_face_direction == "UP":
        if change_direction_to == 0:
            new_robot_face_direction = "LEFT"
        else:
            new_robot_face_direction = "RIGHT"

    if robot_face_direction == "DOWN":
        if change_direction_to == 0:
            new_robot_face_direction = "RIGHT"
        else:
            new_robot_face_direction = "LEFT"

    if robot_face_direction == "LEFT":
        if change_direction_to == 0:
            new_robot_face_direction = "DOWN"
        else:
            new_robot_face_direction = "UP"

    if robot_face_direction == "RIGHT":
        if change_direction_to == 0:
            new_robot_face_direction = "UP"
        else:
            new_robot_face_direction = "DOWN"

    if new_robot_face_direction == "UP":
        new_position = (position[0], position[1] + 1)

    elif new_robot_face_direction == "DOWN":
        new_position = (position[0], position[1] - 1)

    elif new_robot_face_direction == "LEFT":
        new_position = (position[0] - 1, position[1])

    else:
        new_position = (position[0] + 1, position[1])

    return new_position, new_robot_face_direction


run = 0
while input_extnd[i] != 99:

    code = str(input_extnd[i])

    if len(code) == 5:
        de = int(code[3:])
        c = int(code[2])
        b = int(code[1])
        a = int(code[0])

    if len(code) == 4:
        de = int(code[2:])
        c = int(code[1])
        b = int(code[0])
        a = 0

    if len(code) == 3:
        de = int(code[1:])
        c = int(code[0])
        a, b = 0, 0

    if len(code) == 2:
        de = int(code)
        a, c, b = 0, 0, 0

    if len(code) == 1:
        de = int(code)
        a, c, b = 0, 0, 0

    param1 = getparam(c, i + 1, input_extnd, base)

    if de not in [3, 4, 9]:
        param2 = getparam(b, i + 2, input_extnd, base)

    if 1 <= de <= 2:

        if de == 1:

            if a == 2:
                input_extnd[input_extnd[i + 3] + base] = param1 + param2
            else:
                input_extnd[input_extnd[i + 3]] = param1 + param2

        if de == 2:
            if a == 2:
                input_extnd[input_extnd[i + 3] + base] = param1 * param2
            else:

                input_extnd[input_extnd[i + 3]] = param1 * param2

        i += 4

    if 3 <= de <= 4 or de == 9:

        if de == 3:

            # a = input("Enter System Id : ")
            if position not in panel_painted:
                panel_painted[position] = 0

            a = panel_painted[position]

            if c == 2:
                input_extnd[base + input_extnd[i + 1]] = int(a)
            else:
                input_extnd[input_extnd[i + 1]] = int(a)

        if de == 4:
            get_param += 1

            if get_param == 2:
                # print("Direction : ", param1)
                position, robot_face_direction = change_position(
                    position, robot_face_direction, param1
                )
                get_param = 0

                min_x = min(min_x, position[0])
                min_y = min(min_y, position[1])
                max_x = max(max_x, position[0])
                max_y = max(max_y, position[1])

            else:
                # print("Color : ", param1)
                panel_painted[position] = param1

            if param1 == 99:
                break

        if de == 9:
            base += param1

        i += 2

    if 5 <= de <= 8:

        if de == 5:

            if param1 != 0:
                i = param2
            else:
                i += 3

        if de == 6:

            if param1 == 0:
                i = param2
            else:
                i += 3

        if de == 7:

            if param1 < param2:
                if a == 2:
                    input_extnd[input_extnd[i + 3] + base] = 1
                else:
                    input_extnd[input_extnd[i + 3]] = 1
                i += 4

            else:
                if a == 2:
                    input_extnd[input_extnd[i + 3] + base] = 0
                else:
                    input_extnd[input_extnd[i + 3]] = 0
                i += 4

        if de == 8:

            if param1 == param2:
                if a == 2:
                    input_extnd[input_extnd[i + 3] + base] = 1

                else:
                    input_extnd[input_extnd[i + 3]] = 1
                i += 4

            else:
                if a == 2:
                    input_extnd[input_extnd[i + 3] + base] = 0

                else:
                    input_extnd[input_extnd[i + 3]] = 0
                i += 4

    run += 1

for j in range(max_y, min_y - 1, -1):
    for i in range(min_x, max_x + 1):
        if (i, j) not in panel_painted:
            print(" ", end="")
        else:
            if panel_painted[((i, j))] == 0:
                print(" ", end="")
            else:
                print("1", end="")

    print() """

""" ### 12A
io = {"x": 8, "y": 0, "z": 8, "velocity": {"x": 0, "y": 0, "z": 0}}
europa = {"x": 0, "y": -5, "z": -10, "velocity": {"x": 0, "y": 0, "z": 0}}
ganymede = {"x": 16, "y": 10, "z": -5, "velocity": {"x": 0, "y": 0, "z": 0}}
callisto = {"x": 19, "y": -10, "z": -7, "velocity": {"x": 0, "y": 0, "z": 0}}


# io = {"x": -1, "y": 0, "z": 2, "velocity": {"x": 0, "y": 0, "z": 0}}
# europa = {"x": 2, "y": -10, "z": -7, "velocity": {"x": 0, "y": 0, "z": 0}}
# ganymede = {"x": 4, "y": -8, "z": 8, "velocity": {"x": 0, "y": 0, "z": 0}}
# callisto = {"x": 3, "y": 5, "z": -1, "velocity": {"x": 0, "y": 0, "z": 0}}


def change_in_velocity(a, b, c, d):
    for com in [b, c, d]:

        for key in ["x", "y", "z"]:

            if a[key] == com[key]:
                pass

            elif a[key] > com[key]:
                a["velocity"][key] -= 1

            else:
                a["velocity"][key] += 1

    return a


def change_in_position(moons):

    for moon in moons:
        for key in ["x", "y", "z"]:
            moon[key] += moon["velocity"][key]

    return moons


def total_energy(moons):

    total_energy = 0
    for moon in moons:
        pot = 0
        kit = 0
        for key in ["x", "y", "z"]:
            pot += abs(moon[key])
            kit += abs(moon["velocity"][key])

        total_energy += pot * kit

    print(total_energy)


# for _ in range(1000):

#     io_new = change_in_velocity(io, europa, ganymede, callisto)
#     europa_new = change_in_velocity(europa, io, ganymede, callisto)
#     ganymede_new = change_in_velocity(ganymede, io, europa, callisto)
#     callisto_new = change_in_velocity(callisto, io, europa, ganymede)

#     io_new, europa_new, ganymede_new, callisto_new = change_in_position(
#         [io_new, europa_new, ganymede_new, callisto_new]
#     )


# total_energy([io, europa, ganymede, callisto])

# 12b
def change_in_velocity2(a, b, c, d, key):
    for com in [b, c, d]:
        if a[key] == com[key]:
            pass

        elif a[key] > com[key]:
            a["velocity"][key] -= 1

        else:
            a["velocity"][key] += 1

    return a


def change_in_position2(moons, key):

    for moon in moons:
        for key in [key]:
            moon[key] += moon["velocity"][key]

    return moons


io_init = {"x": 8, "y": 0, "z": 8, "velocity": {"x": 0, "y": 0, "z": 0}}
europa_init = {"x": 0, "y": -5, "z": -10, "velocity": {"x": 0, "y": 0, "z": 0}}
ganymede_init = {"x": 16, "y": 10, "z": -5, "velocity": {"x": 0, "y": 0, "z": 0}}
callisto_init = {"x": 19, "y": -10, "z": -7, "velocity": {"x": 0, "y": 0, "z": 0}}

io_init = {"x": -8, "y": -10, "z": 0, "velocity": {"x": 0, "y": 0, "z": 0}}
europa_init = {"x": 5, "y": 5, "z": 10, "velocity": {"x": 0, "y": 0, "z": 0}}
ganymede_init = {"x": 2, "y": -7, "z": 3, "velocity": {"x": 0, "y": 0, "z": 0}}
callisto_init = {"x": 9, "y": -8, "z": -3, "velocity": {"x": 0, "y": 0, "z": 0}}

io_init = {"x": -1, "y": 0, "z": 2, "velocity": {"x": 0, "y": 0, "z": 0}}
europa_init = {"x": 2, "y": -10, "z": -7, "velocity": {"x": 0, "y": 0, "z": 0}}
ganymede_init = {"x": 4, "y": -8, "z": 8, "velocity": {"x": 0, "y": 0, "z": 0}}
callisto_init = {"x": 3, "y": 5, "z": -1, "velocity": {"x": 0, "y": 0, "z": 0}}

steps_moon = []
i = 0

from math import gcd

# for moon_init in [io_init, europa_init, ganymede_init, callisto_init]:

#     steps = []

#     for key in ["x", "y", "z"]:

#         step = 0

# io = {"x": 8, "y": 0, "z": 8, "velocity": {"x": 0, "y": 0, "z": 0}}
# europa = {"x": 0, "y": -5, "z": -10, "velocity": {"x": 0, "y": 0, "z": 0}}
# ganymede = {"x": 16, "y": 10, "z": -5, "velocity": {"x": 0, "y": 0, "z": 0}}
# callisto = {"x": 19, "y": -10, "z": -7, "velocity": {"x": 0, "y": 0, "z": 0}}

# io = {"x": -8, "y": -10, "z": 0, "velocity": {"x": 0, "y": 0, "z": 0}}
# europa = {"x": 5, "y": 5, "z": 10, "velocity": {"x": 0, "y": 0, "z": 0}}
# ganymede = {"x": 2, "y": -7, "z": 3, "velocity": {"x": 0, "y": 0, "z": 0}}
# callisto = {"x": 9, "y": -8, "z": -3, "velocity": {"x": 0, "y": 0, "z": 0}}

# io_init = {"x": -1, "y": 0, "z": 2, "velocity": {"x": 0, "y": 0, "z": 0}}
# europa_init = {"x": 2, "y": -10, "z": -7, "velocity": {"x": 0, "y": 0, "z": 0}}
# ganymede_init = {"x": 4, "y": -8, "z": 8, "velocity": {"x": 0, "y": 0, "z": 0}}
# callisto_init = {"x": 3, "y": 5, "z": -1, "velocity": {"x": 0, "y": 0, "z": 0}}

#         while True:

#             step += 1
#             # io_copy = io.copy()
#             # europa_copy = europa.copy()
#             # ganymede_copy = ganymede.copy()
#             # callisto_copy = callisto.copy()

#             io_new = change_in_velocity2(io, europa, ganymede, callisto, key)
#             europa_new = change_in_velocity2(europa, io, ganymede, callisto, key)
#             ganymede_new = change_in_velocity2(ganymede, io, europa, callisto, key)
#             callisto_new = change_in_velocity2(callisto, io, europa, ganymede, key)

#             io_new, europa_new, ganymede_new, callisto_new = change_in_position2(
#                 [io_new, europa_new, ganymede_new, callisto_new], key
#             )

#             if i == 0:
#                 moon = io_new
#                 # moon_prev = io_copy

#             elif i == 1:
#                 moon = europa_new
#                 # moon_prev = europa_copy

#             elif i == 2:
#                 moon = ganymede_new
#                 # moon_prev = ganymede_copy

#             else:
#                 moon = callisto_new
#                 # moon_prev = callisto_copy

#             if moon[key] == moon_init[key] and moon["velocity"][key] == 0:
#                 print(moon)

#             if len(steps) < 4:
#                 steps.append(step)
#             else:
#                 break

#     steps_moon.append(steps)
#     i += 1


# lcm_list = []

# for x in steps_moon:
#     a = x  # will work for an int array of any length
#     lcm = a[0]
#     for i in a[1:]:
#         lcm = lcm * i // gcd(lcm, i)

#     lcm_list.append(lcm)


io_init = {"x": -8, "y": -10, "z": 0, "velocity": {"x": 0, "y": 0, "z": 0}}
europa_init = {"x": 5, "y": 5, "z": 10, "velocity": {"x": 0, "y": 0, "z": 0}}
ganymede_init = {"x": 2, "y": -7, "z": 3, "velocity": {"x": 0, "y": 0, "z": 0}}
callisto_init = {"x": 9, "y": -8, "z": -3, "velocity": {"x": 0, "y": 0, "z": 0}}


j = 0
i = 0

for moon_init in [io_init, europa_init, ganymede_init, callisto_init]:

    io = {"x": -8, "y": -10, "z": 0, "velocity": {"x": 0, "y": 0, "z": 0}}
    europa = {"x": 5, "y": 5, "z": 10, "velocity": {"x": 0, "y": 0, "z": 0}}
    ganymede = {"x": 2, "y": -7, "z": 3, "velocity": {"x": 0, "y": 0, "z": 0}}
    callisto = {"x": 9, "y": -8, "z": -3, "velocity": {"x": 0, "y": 0, "z": 0}}

    step = 0
    j = 0
    x, y, z = None, None, None

    moon_new = moon_init

    while True:

        if j == 3:
            break

        else:
            step += 1

            io_new = change_in_velocity(io, europa, ganymede, callisto)
            # europa_new = change_in_velocity(europa, io, ganymede, callisto)
            # ganymede_new = change_in_velocity(ganymede, io, europa, callisto)
            # callisto_new = change_in_velocity(callisto, io, europa, ganymede)

            io_new, europa_new, ganymede_new, callisto_new = change_in_position(
                [io_new, europa_new, ganymede_new, callisto_new]
            )

            if i == 0:
                moon = io_new
                # moon_prev = io_copy

            elif i == 1:
                moon = europa_new
                # moon_prev = europa_copy

            elif i == 2:
                moon = ganymede_new
                # moon_prev = ganymede_copy

            else:
                moon = callisto_new
                # moon_prev = callisto_copy

            if moon["x"] == moon_init["x"] and moon["velocity"]["x"] == 0 and x == None:

                x = step
                j += 1

            if moon["y"] == moon_init["y"] and moon["velocity"]["y"] == 0 and y == None:

                y = step
                j += 1

            if moon["z"] == moon_init["z"] and moon["velocity"]["z"] == 0 and z == None:

                z = step
                j += 1

            # io_new = change_in_velocity(io, europa, ganymede, callisto)
            europa_new = change_in_velocity(europa, io, ganymede, callisto)
            # ganymede_new = change_in_velocity(ganymede, io, europa, callisto)
            # callisto_new = change_in_velocity(callisto, io, europa, ganymede)

            io_new, europa_new, ganymede_new, callisto_new = change_in_position(
                [io_new, europa_new, ganymede_new, callisto_new]
            )

            if i == 0:
                moon = io_new
                # moon_prev = io_copy

            elif i == 1:
                moon = europa_new
                # moon_prev = europa_copy

            elif i == 2:
                moon = ganymede_new
                # moon_prev = ganymede_copy

            else:
                moon = callisto_new
                # moon_prev = callisto_copy

            if moon["x"] == moon_init["x"] and moon["velocity"]["x"] == 0 and x == None:

                x = step
                j += 1

            if moon["y"] == moon_init["y"] and moon["velocity"]["y"] == 0 and y == None:

                y = step
                j += 1

            if moon["z"] == moon_init["z"] and moon["velocity"]["z"] == 0 and z == None:

                z = step
                j += 1

            # io_new = change_in_velocity(io, europa, ganymede, callisto)
            # europa_new = change_in_velocity(europa, io, ganymede, callisto)
            ganymede_new = change_in_velocity(ganymede, io, europa, callisto)
            # callisto_new = change_in_velocity(callisto, io, europa, ganymede)

            io_new, europa_new, ganymede_new, callisto_new = change_in_position(
                [io_new, europa_new, ganymede_new, callisto_new]
            )

            if i == 0:
                moon = io_new
                # moon_prev = io_copy

            elif i == 1:
                moon = europa_new
                # moon_prev = europa_copy

            elif i == 2:
                moon = ganymede_new
                # moon_prev = ganymede_copy

            else:
                moon = callisto_new
                # moon_prev = callisto_copy

            if moon["x"] == moon_init["x"] and moon["velocity"]["x"] == 0 and x == None:

                x = step
                j += 1

            if moon["y"] == moon_init["y"] and moon["velocity"]["y"] == 0 and y == None:

                y = step
                j += 1

            if moon["z"] == moon_init["z"] and moon["velocity"]["z"] == 0 and z == None:

                z = step
                j += 1

            # io_new = change_in_velocity(io, europa, ganymede, callisto)
            # europa_new = change_in_velocity(europa, io, ganymede, callisto)
            # ganymede_new = change_in_velocity(ganymede, io, europa, callisto)
            callisto_new = change_in_velocity(callisto, io, europa, ganymede)

            io_new, europa_new, ganymede_new, callisto_new = change_in_position(
                [io_new, europa_new, ganymede_new, callisto_new]
            )

            if i == 0:
                moon = io_new
                # moon_prev = io_copy

            elif i == 1:
                moon = europa_new
                # moon_prev = europa_copy

            elif i == 2:
                moon = ganymede_new
                # moon_prev = ganymede_copy

            else:
                moon = callisto_new
                # moon_prev = callisto_copy

            if moon["x"] == moon_init["x"] and moon["velocity"]["x"] == 0 and x == None:

                x = step
                j += 1

            if moon["y"] == moon_init["y"] and moon["velocity"]["y"] == 0 and y == None:

                y = step
                j += 1

            if moon["z"] == moon_init["z"] and moon["velocity"]["z"] == 0 and z == None:

                z = step
                j += 1

    steps_moon = steps_moon + [x // 2, y // 2, z // 2]

    if len(steps_moon) == 12:
        break

    i += 1

a = steps_moon  # will work for an int array of any length
lcm = a[0]
for i in a[1:]:
    lcm = lcm * i // gcd(lcm, i)

print(lcm)
 """

# 13a

inp = [
    2,
    380,
    379,
    385,
    1008,
    2823,
    432584,
    381,
    1005,
    381,
    12,
    99,
    109,
    2824,
    1101,
    0,
    0,
    383,
    1101,
    0,
    0,
    382,
    20102,
    1,
    382,
    1,
    20102,
    1,
    383,
    2,
    21102,
    1,
    37,
    0,
    1105,
    1,
    578,
    4,
    382,
    4,
    383,
    204,
    1,
    1001,
    382,
    1,
    382,
    1007,
    382,
    42,
    381,
    1005,
    381,
    22,
    1001,
    383,
    1,
    383,
    1007,
    383,
    26,
    381,
    1005,
    381,
    18,
    1006,
    385,
    69,
    99,
    104,
    -1,
    104,
    0,
    4,
    386,
    3,
    384,
    1007,
    384,
    0,
    381,
    1005,
    381,
    94,
    107,
    0,
    384,
    381,
    1005,
    381,
    108,
    1105,
    1,
    161,
    107,
    1,
    392,
    381,
    1006,
    381,
    161,
    1101,
    -1,
    0,
    384,
    1105,
    1,
    119,
    1007,
    392,
    40,
    381,
    1006,
    381,
    161,
    1101,
    0,
    1,
    384,
    21002,
    392,
    1,
    1,
    21102,
    24,
    1,
    2,
    21102,
    0,
    1,
    3,
    21102,
    138,
    1,
    0,
    1105,
    1,
    549,
    1,
    392,
    384,
    392,
    20102,
    1,
    392,
    1,
    21101,
    0,
    24,
    2,
    21101,
    0,
    3,
    3,
    21101,
    161,
    0,
    0,
    1105,
    1,
    549,
    1101,
    0,
    0,
    384,
    20001,
    388,
    390,
    1,
    20101,
    0,
    389,
    2,
    21101,
    0,
    180,
    0,
    1106,
    0,
    578,
    1206,
    1,
    213,
    1208,
    1,
    2,
    381,
    1006,
    381,
    205,
    20001,
    388,
    390,
    1,
    21002,
    389,
    1,
    2,
    21101,
    0,
    205,
    0,
    1106,
    0,
    393,
    1002,
    390,
    -1,
    390,
    1101,
    1,
    0,
    384,
    20102,
    1,
    388,
    1,
    20001,
    389,
    391,
    2,
    21102,
    1,
    228,
    0,
    1105,
    1,
    578,
    1206,
    1,
    261,
    1208,
    1,
    2,
    381,
    1006,
    381,
    253,
    21001,
    388,
    0,
    1,
    20001,
    389,
    391,
    2,
    21101,
    253,
    0,
    0,
    1106,
    0,
    393,
    1002,
    391,
    -1,
    391,
    1102,
    1,
    1,
    384,
    1005,
    384,
    161,
    20001,
    388,
    390,
    1,
    20001,
    389,
    391,
    2,
    21102,
    1,
    279,
    0,
    1105,
    1,
    578,
    1206,
    1,
    316,
    1208,
    1,
    2,
    381,
    1006,
    381,
    304,
    20001,
    388,
    390,
    1,
    20001,
    389,
    391,
    2,
    21102,
    1,
    304,
    0,
    1106,
    0,
    393,
    1002,
    390,
    -1,
    390,
    1002,
    391,
    -1,
    391,
    1102,
    1,
    1,
    384,
    1005,
    384,
    161,
    21001,
    388,
    0,
    1,
    21002,
    389,
    1,
    2,
    21101,
    0,
    0,
    3,
    21101,
    0,
    338,
    0,
    1106,
    0,
    549,
    1,
    388,
    390,
    388,
    1,
    389,
    391,
    389,
    21002,
    388,
    1,
    1,
    20102,
    1,
    389,
    2,
    21101,
    4,
    0,
    3,
    21102,
    1,
    365,
    0,
    1106,
    0,
    549,
    1007,
    389,
    25,
    381,
    1005,
    381,
    75,
    104,
    -1,
    104,
    0,
    104,
    0,
    99,
    0,
    1,
    0,
    0,
    0,
    0,
    0,
    0,
    380,
    19,
    21,
    1,
    1,
    21,
    109,
    3,
    22102,
    1,
    -2,
    1,
    21201,
    -1,
    0,
    2,
    21102,
    1,
    0,
    3,
    21101,
    0,
    414,
    0,
    1105,
    1,
    549,
    21201,
    -2,
    0,
    1,
    21202,
    -1,
    1,
    2,
    21102,
    1,
    429,
    0,
    1105,
    1,
    601,
    1202,
    1,
    1,
    435,
    1,
    386,
    0,
    386,
    104,
    -1,
    104,
    0,
    4,
    386,
    1001,
    387,
    -1,
    387,
    1005,
    387,
    451,
    99,
    109,
    -3,
    2105,
    1,
    0,
    109,
    8,
    22202,
    -7,
    -6,
    -3,
    22201,
    -3,
    -5,
    -3,
    21202,
    -4,
    64,
    -2,
    2207,
    -3,
    -2,
    381,
    1005,
    381,
    492,
    21202,
    -2,
    -1,
    -1,
    22201,
    -3,
    -1,
    -3,
    2207,
    -3,
    -2,
    381,
    1006,
    381,
    481,
    21202,
    -4,
    8,
    -2,
    2207,
    -3,
    -2,
    381,
    1005,
    381,
    518,
    21202,
    -2,
    -1,
    -1,
    22201,
    -3,
    -1,
    -3,
    2207,
    -3,
    -2,
    381,
    1006,
    381,
    507,
    2207,
    -3,
    -4,
    381,
    1005,
    381,
    540,
    21202,
    -4,
    -1,
    -1,
    22201,
    -3,
    -1,
    -3,
    2207,
    -3,
    -4,
    381,
    1006,
    381,
    529,
    22102,
    1,
    -3,
    -7,
    109,
    -8,
    2105,
    1,
    0,
    109,
    4,
    1202,
    -2,
    42,
    566,
    201,
    -3,
    566,
    566,
    101,
    639,
    566,
    566,
    2102,
    1,
    -1,
    0,
    204,
    -3,
    204,
    -2,
    204,
    -1,
    109,
    -4,
    2105,
    1,
    0,
    109,
    3,
    1202,
    -1,
    42,
    594,
    201,
    -2,
    594,
    594,
    101,
    639,
    594,
    594,
    20102,
    1,
    0,
    -2,
    109,
    -3,
    2105,
    1,
    0,
    109,
    3,
    22102,
    26,
    -2,
    1,
    22201,
    1,
    -1,
    1,
    21101,
    557,
    0,
    2,
    21102,
    671,
    1,
    3,
    21101,
    0,
    1092,
    4,
    21101,
    630,
    0,
    0,
    1105,
    1,
    456,
    21201,
    1,
    1731,
    -2,
    109,
    -3,
    2106,
    0,
    0,
    1,
    1,
    1,
    1,
    1,
    1,
    1,
    1,
    1,
    1,
    1,
    1,
    1,
    1,
    1,
    1,
    1,
    1,
    1,
    1,
    1,
    1,
    1,
    1,
    1,
    1,
    1,
    1,
    1,
    1,
    1,
    1,
    1,
    1,
    1,
    1,
    1,
    1,
    1,
    1,
    1,
    1,
    1,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    1,
    1,
    0,
    0,
    2,
    2,
    0,
    0,
    2,
    0,
    0,
    0,
    0,
    0,
    2,
    2,
    2,
    0,
    2,
    2,
    2,
    0,
    0,
    2,
    0,
    0,
    0,
    0,
    0,
    2,
    0,
    2,
    0,
    0,
    2,
    2,
    0,
    2,
    2,
    2,
    0,
    0,
    1,
    1,
    0,
    0,
    2,
    2,
    2,
    0,
    0,
    2,
    0,
    2,
    2,
    2,
    2,
    0,
    0,
    2,
    2,
    0,
    2,
    2,
    2,
    2,
    0,
    0,
    0,
    0,
    2,
    0,
    2,
    0,
    2,
    2,
    2,
    2,
    0,
    2,
    0,
    0,
    0,
    0,
    1,
    1,
    0,
    0,
    2,
    2,
    2,
    2,
    0,
    2,
    0,
    2,
    2,
    2,
    0,
    2,
    0,
    0,
    0,
    2,
    0,
    0,
    2,
    2,
    2,
    2,
    2,
    0,
    2,
    0,
    0,
    0,
    2,
    2,
    0,
    0,
    2,
    2,
    2,
    2,
    2,
    0,
    1,
    1,
    0,
    0,
    2,
    2,
    0,
    0,
    0,
    2,
    0,
    2,
    2,
    2,
    2,
    0,
    0,
    0,
    2,
    0,
    0,
    2,
    2,
    2,
    0,
    0,
    2,
    0,
    0,
    0,
    2,
    2,
    2,
    0,
    2,
    0,
    0,
    0,
    2,
    0,
    2,
    0,
    1,
    1,
    0,
    2,
    0,
    0,
    2,
    2,
    2,
    0,
    2,
    2,
    0,
    2,
    0,
    2,
    0,
    0,
    2,
    0,
    0,
    2,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    2,
    2,
    0,
    2,
    2,
    0,
    0,
    2,
    2,
    2,
    2,
    2,
    0,
    1,
    1,
    0,
    2,
    0,
    2,
    2,
    2,
    2,
    0,
    2,
    0,
    2,
    0,
    2,
    2,
    0,
    2,
    0,
    2,
    0,
    2,
    2,
    2,
    2,
    0,
    0,
    0,
    2,
    2,
    2,
    2,
    2,
    0,
    0,
    2,
    0,
    0,
    0,
    2,
    0,
    0,
    1,
    1,
    0,
    2,
    0,
    2,
    2,
    2,
    2,
    0,
    2,
    2,
    0,
    2,
    2,
    2,
    2,
    2,
    0,
    2,
    2,
    2,
    2,
    0,
    2,
    2,
    0,
    2,
    0,
    2,
    2,
    2,
    0,
    2,
    2,
    2,
    0,
    2,
    0,
    0,
    0,
    0,
    1,
    1,
    0,
    2,
    0,
    2,
    2,
    2,
    2,
    2,
    2,
    2,
    2,
    0,
    0,
    2,
    0,
    0,
    2,
    2,
    2,
    2,
    2,
    0,
    0,
    0,
    2,
    0,
    2,
    0,
    2,
    2,
    0,
    2,
    2,
    0,
    0,
    0,
    2,
    2,
    2,
    0,
    1,
    1,
    0,
    2,
    0,
    0,
    0,
    0,
    2,
    0,
    0,
    2,
    0,
    2,
    0,
    2,
    0,
    0,
    2,
    2,
    2,
    2,
    2,
    0,
    2,
    0,
    0,
    2,
    0,
    2,
    0,
    2,
    2,
    0,
    0,
    2,
    2,
    0,
    0,
    2,
    0,
    0,
    1,
    1,
    0,
    0,
    2,
    0,
    0,
    0,
    2,
    2,
    0,
    0,
    0,
    0,
    2,
    2,
    0,
    0,
    0,
    2,
    2,
    0,
    2,
    0,
    0,
    2,
    2,
    0,
    2,
    2,
    0,
    0,
    2,
    0,
    2,
    2,
    2,
    0,
    0,
    2,
    2,
    0,
    1,
    1,
    0,
    2,
    2,
    2,
    0,
    0,
    2,
    0,
    2,
    2,
    0,
    0,
    2,
    2,
    2,
    2,
    2,
    0,
    2,
    2,
    0,
    2,
    2,
    2,
    2,
    2,
    0,
    2,
    0,
    0,
    2,
    0,
    2,
    0,
    2,
    0,
    2,
    2,
    2,
    0,
    1,
    1,
    0,
    0,
    2,
    0,
    2,
    0,
    0,
    0,
    0,
    2,
    2,
    2,
    2,
    0,
    0,
    0,
    0,
    0,
    2,
    2,
    0,
    2,
    2,
    0,
    2,
    0,
    2,
    2,
    2,
    2,
    0,
    0,
    0,
    0,
    2,
    2,
    0,
    2,
    2,
    0,
    1,
    1,
    0,
    0,
    0,
    2,
    0,
    2,
    2,
    2,
    2,
    2,
    2,
    0,
    2,
    2,
    0,
    0,
    0,
    2,
    0,
    2,
    2,
    0,
    2,
    2,
    2,
    2,
    0,
    2,
    0,
    2,
    0,
    0,
    2,
    0,
    0,
    2,
    2,
    2,
    2,
    0,
    1,
    1,
    0,
    0,
    0,
    2,
    2,
    0,
    2,
    2,
    0,
    2,
    2,
    0,
    0,
    2,
    0,
    2,
    0,
    0,
    2,
    0,
    2,
    0,
    0,
    2,
    0,
    0,
    2,
    0,
    2,
    2,
    2,
    0,
    2,
    2,
    2,
    2,
    0,
    0,
    2,
    0,
    1,
    1,
    0,
    0,
    0,
    2,
    2,
    0,
    2,
    2,
    2,
    0,
    2,
    2,
    0,
    0,
    2,
    0,
    0,
    2,
    2,
    2,
    0,
    0,
    0,
    2,
    0,
    0,
    2,
    0,
    2,
    0,
    0,
    2,
    0,
    2,
    2,
    2,
    0,
    0,
    0,
    0,
    1,
    1,
    0,
    0,
    2,
    0,
    2,
    0,
    2,
    0,
    0,
    2,
    2,
    2,
    0,
    2,
    2,
    2,
    2,
    0,
    2,
    2,
    0,
    2,
    2,
    0,
    0,
    0,
    0,
    2,
    0,
    0,
    2,
    2,
    2,
    0,
    0,
    0,
    2,
    2,
    2,
    0,
    1,
    1,
    0,
    2,
    2,
    0,
    2,
    2,
    0,
    0,
    0,
    0,
    0,
    2,
    2,
    2,
    0,
    2,
    2,
    2,
    0,
    2,
    2,
    0,
    0,
    2,
    2,
    0,
    2,
    0,
    2,
    0,
    2,
    0,
    2,
    0,
    0,
    0,
    2,
    2,
    2,
    0,
    1,
    1,
    0,
    2,
    2,
    0,
    2,
    2,
    2,
    2,
    0,
    2,
    2,
    2,
    2,
    2,
    2,
    2,
    2,
    2,
    2,
    0,
    2,
    0,
    2,
    2,
    0,
    0,
    2,
    2,
    0,
    2,
    0,
    2,
    2,
    2,
    2,
    0,
    0,
    2,
    0,
    0,
    1,
    1,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    1,
    1,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    4,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    1,
    1,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    1,
    1,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    1,
    1,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    3,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    1,
    1,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    1,
    26,
    39,
    93,
    24,
    77,
    14,
    80,
    83,
    52,
    91,
    93,
    34,
    84,
    34,
    71,
    69,
    88,
    90,
    9,
    41,
    47,
    38,
    55,
    55,
    97,
    48,
    94,
    51,
    98,
    36,
    7,
    89,
    44,
    29,
    22,
    82,
    9,
    40,
    55,
    30,
    48,
    6,
    30,
    71,
    85,
    16,
    56,
    22,
    20,
    34,
    83,
    79,
    18,
    54,
    97,
    37,
    1,
    18,
    41,
    60,
    62,
    10,
    90,
    5,
    66,
    35,
    59,
    62,
    46,
    39,
    95,
    95,
    75,
    30,
    47,
    81,
    92,
    86,
    41,
    23,
    4,
    60,
    17,
    68,
    1,
    38,
    93,
    38,
    63,
    57,
    19,
    91,
    76,
    36,
    17,
    39,
    33,
    15,
    10,
    38,
    55,
    89,
    90,
    80,
    33,
    41,
    68,
    68,
    88,
    42,
    31,
    24,
    50,
    74,
    41,
    58,
    69,
    57,
    13,
    97,
    83,
    92,
    25,
    23,
    27,
    13,
    50,
    92,
    41,
    82,
    23,
    31,
    11,
    53,
    10,
    10,
    49,
    53,
    50,
    73,
    58,
    12,
    84,
    58,
    10,
    95,
    1,
    28,
    76,
    2,
    53,
    86,
    66,
    98,
    20,
    88,
    30,
    39,
    21,
    47,
    31,
    30,
    78,
    28,
    74,
    63,
    90,
    91,
    88,
    78,
    10,
    64,
    52,
    91,
    18,
    65,
    20,
    16,
    90,
    76,
    2,
    22,
    18,
    43,
    90,
    5,
    59,
    62,
    60,
    71,
    41,
    66,
    64,
    39,
    32,
    90,
    10,
    61,
    52,
    71,
    46,
    61,
    18,
    53,
    82,
    80,
    53,
    39,
    70,
    71,
    81,
    48,
    17,
    26,
    14,
    19,
    69,
    16,
    68,
    39,
    39,
    86,
    31,
    34,
    4,
    11,
    81,
    32,
    55,
    54,
    12,
    93,
    34,
    49,
    50,
    2,
    64,
    61,
    44,
    89,
    13,
    45,
    64,
    45,
    87,
    92,
    16,
    81,
    83,
    18,
    4,
    96,
    43,
    88,
    74,
    27,
    16,
    78,
    10,
    12,
    31,
    38,
    28,
    84,
    50,
    28,
    75,
    74,
    39,
    42,
    43,
    41,
    16,
    5,
    76,
    95,
    88,
    49,
    22,
    43,
    13,
    95,
    66,
    68,
    32,
    79,
    66,
    26,
    82,
    43,
    25,
    79,
    10,
    2,
    77,
    22,
    19,
    81,
    4,
    92,
    42,
    54,
    67,
    62,
    18,
    9,
    69,
    69,
    24,
    69,
    87,
    6,
    53,
    56,
    22,
    20,
    98,
    85,
    3,
    79,
    35,
    4,
    32,
    96,
    25,
    69,
    59,
    23,
    14,
    92,
    19,
    34,
    73,
    42,
    44,
    45,
    7,
    85,
    8,
    31,
    55,
    68,
    84,
    59,
    4,
    18,
    65,
    19,
    61,
    37,
    72,
    29,
    46,
    67,
    64,
    40,
    46,
    82,
    8,
    50,
    57,
    8,
    59,
    83,
    47,
    22,
    16,
    1,
    58,
    41,
    93,
    56,
    60,
    17,
    95,
    24,
    63,
    48,
    47,
    89,
    23,
    12,
    37,
    82,
    19,
    9,
    74,
    30,
    15,
    65,
    1,
    86,
    88,
    93,
    75,
    73,
    11,
    80,
    88,
    36,
    49,
    62,
    57,
    59,
    75,
    43,
    91,
    47,
    93,
    98,
    65,
    30,
    90,
    50,
    93,
    81,
    58,
    43,
    84,
    58,
    24,
    33,
    17,
    83,
    48,
    45,
    91,
    60,
    40,
    87,
    75,
    94,
    26,
    95,
    81,
    93,
    62,
    68,
    73,
    71,
    77,
    56,
    89,
    49,
    26,
    56,
    26,
    4,
    26,
    63,
    16,
    64,
    77,
    33,
    16,
    93,
    21,
    68,
    63,
    55,
    15,
    65,
    23,
    14,
    45,
    35,
    22,
    3,
    78,
    50,
    83,
    45,
    96,
    69,
    79,
    7,
    20,
    6,
    75,
    64,
    8,
    7,
    71,
    85,
    16,
    68,
    27,
    50,
    88,
    31,
    34,
    50,
    32,
    83,
    48,
    1,
    35,
    50,
    90,
    10,
    59,
    19,
    80,
    61,
    83,
    34,
    59,
    25,
    7,
    41,
    48,
    56,
    10,
    64,
    23,
    14,
    85,
    70,
    77,
    73,
    91,
    17,
    36,
    60,
    2,
    1,
    77,
    89,
    39,
    84,
    89,
    76,
    55,
    77,
    51,
    24,
    43,
    2,
    31,
    50,
    46,
    50,
    62,
    22,
    48,
    86,
    38,
    19,
    13,
    2,
    96,
    80,
    74,
    82,
    54,
    84,
    49,
    7,
    4,
    1,
    86,
    33,
    50,
    7,
    37,
    51,
    4,
    54,
    37,
    91,
    11,
    12,
    29,
    77,
    78,
    55,
    98,
    15,
    34,
    82,
    7,
    28,
    41,
    16,
    42,
    73,
    44,
    62,
    70,
    61,
    20,
    76,
    24,
    95,
    78,
    40,
    44,
    24,
    25,
    29,
    85,
    83,
    39,
    48,
    5,
    64,
    43,
    81,
    12,
    8,
    84,
    37,
    47,
    80,
    62,
    53,
    32,
    29,
    87,
    7,
    8,
    41,
    1,
    72,
    9,
    38,
    58,
    64,
    31,
    6,
    23,
    15,
    31,
    3,
    53,
    56,
    34,
    35,
    30,
    57,
    75,
    13,
    56,
    36,
    7,
    87,
    88,
    22,
    91,
    60,
    64,
    10,
    45,
    91,
    43,
    83,
    50,
    23,
    79,
    87,
    4,
    80,
    51,
    11,
    3,
    60,
    56,
    86,
    19,
    83,
    76,
    75,
    43,
    44,
    35,
    75,
    25,
    97,
    40,
    20,
    11,
    51,
    31,
    1,
    23,
    89,
    35,
    41,
    68,
    33,
    93,
    9,
    74,
    80,
    81,
    58,
    13,
    13,
    22,
    80,
    54,
    21,
    93,
    19,
    40,
    25,
    46,
    85,
    75,
    62,
    15,
    54,
    90,
    12,
    10,
    31,
    49,
    89,
    51,
    13,
    57,
    92,
    3,
    17,
    28,
    84,
    36,
    90,
    21,
    12,
    86,
    44,
    87,
    66,
    58,
    24,
    83,
    55,
    13,
    91,
    21,
    70,
    91,
    50,
    94,
    77,
    90,
    35,
    6,
    72,
    79,
    95,
    20,
    2,
    45,
    50,
    77,
    15,
    3,
    97,
    73,
    94,
    54,
    12,
    64,
    30,
    9,
    26,
    45,
    84,
    34,
    95,
    57,
    15,
    88,
    33,
    47,
    62,
    69,
    62,
    89,
    29,
    60,
    34,
    47,
    13,
    86,
    66,
    86,
    75,
    5,
    29,
    50,
    19,
    65,
    70,
    81,
    51,
    62,
    43,
    21,
    61,
    87,
    39,
    19,
    49,
    48,
    7,
    23,
    62,
    52,
    2,
    17,
    31,
    54,
    97,
    98,
    83,
    76,
    98,
    4,
    30,
    31,
    56,
    11,
    89,
    7,
    75,
    46,
    13,
    62,
    32,
    70,
    83,
    29,
    23,
    53,
    40,
    90,
    28,
    45,
    64,
    9,
    35,
    52,
    39,
    77,
    71,
    24,
    40,
    69,
    66,
    59,
    98,
    53,
    15,
    57,
    83,
    50,
    65,
    75,
    26,
    1,
    83,
    17,
    73,
    75,
    34,
    72,
    11,
    66,
    18,
    50,
    77,
    8,
    26,
    80,
    61,
    33,
    84,
    12,
    52,
    13,
    7,
    30,
    26,
    61,
    23,
    10,
    88,
    3,
    80,
    80,
    49,
    29,
    40,
    90,
    65,
    25,
    89,
    55,
    42,
    13,
    98,
    23,
    3,
    19,
    46,
    5,
    94,
    5,
    19,
    72,
    63,
    2,
    20,
    36,
    26,
    20,
    4,
    51,
    77,
    93,
    2,
    25,
    86,
    12,
    7,
    56,
    12,
    61,
    85,
    53,
    12,
    15,
    10,
    13,
    13,
    50,
    73,
    34,
    86,
    59,
    94,
    40,
    36,
    9,
    95,
    74,
    55,
    13,
    19,
    71,
    60,
    63,
    74,
    26,
    24,
    10,
    5,
    21,
    86,
    93,
    62,
    62,
    34,
    47,
    85,
    26,
    94,
    60,
    25,
    9,
    93,
    57,
    57,
    97,
    80,
    6,
    80,
    48,
    22,
    11,
    77,
    50,
    9,
    20,
    23,
    21,
    15,
    33,
    49,
    8,
    76,
    94,
    2,
    61,
    88,
    10,
    24,
    56,
    47,
    43,
    48,
    39,
    12,
    52,
    66,
    19,
    68,
    35,
    26,
    46,
    93,
    27,
    51,
    72,
    98,
    58,
    1,
    24,
    5,
    5,
    9,
    51,
    61,
    3,
    42,
    76,
    98,
    83,
    90,
    49,
    94,
    74,
    79,
    73,
    4,
    46,
    55,
    62,
    16,
    19,
    35,
    51,
    19,
    39,
    64,
    87,
    2,
    95,
    65,
    66,
    26,
    81,
    67,
    35,
    54,
    51,
    70,
    10,
    63,
    76,
    51,
    82,
    67,
    48,
    78,
    15,
    19,
    27,
    37,
    24,
    63,
    97,
    55,
    97,
    7,
    49,
    72,
    7,
    76,
    25,
    82,
    84,
    56,
    94,
    47,
    48,
    44,
    91,
    10,
    432584,
]

from collections import OrderedDict
import curses


elements = {0: " ", 1: "|", 2: "▄", 3: "_", 4: "O"}


min_x, min_y, max_x, max_y = 0, 0, 0, 0

input_extnd = {}

inp[0] = 2

for key, i in enumerate(inp):
    input_extnd[key] = i

extend_mem_index = 0
get_param = 0


def getparam(mode, i, input_extnd, base):

    global extend_mem_index
    if extend_mem_index >= len(inp):
        extend_mem_index = 0

    if mode == 1:

        if i not in input_extnd:
            input_extnd[i] = input_extnd[extend_mem_index]
            extend_mem_index += 1
        return int(input_extnd[i])

    if mode == 0:
        if input_extnd[i] not in input_extnd:
            input_extnd[input_extnd[i]] = input_extnd[extend_mem_index]
            extend_mem_index += 1

        return int(input_extnd[input_extnd[i]])

    if mode == 2:

        if input_extnd[i] + base not in input_extnd:
            input_extnd[input_extnd[i] + base] = input_extnd[extend_mem_index]
            extend_mem_index += 1

        return int(input_extnd[input_extnd[i] + base])


base = 0
i = 0
game = {}
score = 0
run = 0
game_input = []

pos_ball = (0, 0)
pos_paddle = (0, 0)

import time
import curses


def display_game(game, score):

    stdscr = curses.initscr()
    curses.curs_set(0)

    for i in game:
        stdscr.addstr(i[0], i[1], str(game[i]))

    stdscr.addstr(0, i[1] + 1, "SCORE : " + str(score))

    stdscr.refresh()


def count_block(game):
    answer = 0
    for i in game:
        if game[i] == elements[2]:
            answer += 1
    return answer


stdscr = curses.initscr()
curses.curs_set(0)

while input_extnd[i] != 99:

    code = str(input_extnd[i])

    if len(code) == 5:
        de = int(code[3:])
        c = int(code[2])
        b = int(code[1])
        a = int(code[0])

    if len(code) == 4:
        de = int(code[2:])
        c = int(code[1])
        b = int(code[0])
        a = 0

    if len(code) == 3:
        de = int(code[1:])
        c = int(code[0])
        a, b = 0, 0

    if len(code) == 2:
        de = int(code)
        a, c, b = 0, 0, 0

    if len(code) == 1:
        de = int(code)
        a, c, b = 0, 0, 0

    param1 = getparam(c, i + 1, input_extnd, base)

    if de not in [3, 4, 9]:
        param2 = getparam(b, i + 2, input_extnd, base)

    if 1 <= de <= 2:

        if de == 1:

            if a == 2:
                input_extnd[input_extnd[i + 3] + base] = param1 + param2
            else:
                input_extnd[input_extnd[i + 3]] = param1 + param2

        if de == 2:
            if a == 2:
                input_extnd[input_extnd[i + 3] + base] = param1 * param2
            else:

                input_extnd[input_extnd[i + 3]] = param1 * param2

        i += 4

    if 3 <= de <= 4 or de == 9:

        if de == 3:
            # for col in range(min_y, max_y):
            #     for row in range(max_x, min_x - 1, -1):
            #         if str((row, col)) not in game:
            #             print(" ", end="")
            #         else:
            #             print(game[str((row, col))], end="")

            #     print()

            # print()
            # a = input("Enter System Id : ")
            # display_game(game, score)
            if pos_ball[1] > pos_paddle[1]:
                joystick = 1
            elif pos_ball[1] < pos_paddle[1]:
                joystick = -1
            else:
                joystick = 0

            if c == 2:
                input_extnd[base + input_extnd[i + 1]] = int(joystick)
            else:
                input_extnd[input_extnd[i + 1]] = int(joystick)

        if de == 4:

            game_input.append(param1)

            if len(game_input) == 3:
                x = game_input[0]
                y = game_input[1]
                e = game_input[2]

                pos = int(y), int(x)

                if int(e) == 3:
                    pos_paddle = pos
                if int(e) == 4:
                    pos_ball = pos

                if int(x) == -1 and int(y) == 0:
                    score = int(e)
                else:
                    game[pos] = elements[int(e)]

                    game_input = []

                    min_x = min(min_x, x)
                    max_x = max(max_x, x)
                    min_y = min(min_y, y)
                    max_y = max(max_y, y)
                    stdscr.addstr(y, x, game[pos])
                    stdscr.refresh()

                game_input = []

            # xc, yc = 0, 0

            # game.append(param1)
            # if param1 == 99:
            #     break

        if de == 9:
            base += param1

        i += 2

    if 5 <= de <= 8:

        if de == 5:

            if param1 != 0:
                i = param2
            else:
                i += 3

        if de == 6:

            if param1 == 0:
                i = param2
            else:
                i += 3

        if de == 7:

            if param1 < param2:
                if a == 2:
                    input_extnd[input_extnd[i + 3] + base] = 1
                else:
                    input_extnd[input_extnd[i + 3]] = 1
                i += 4

            else:
                if a == 2:
                    input_extnd[input_extnd[i + 3] + base] = 0
                else:
                    input_extnd[input_extnd[i + 3]] = 0
                i += 4

        if de == 8:

            if param1 == param2:
                if a == 2:
                    input_extnd[input_extnd[i + 3] + base] = 1

                else:
                    input_extnd[input_extnd[i + 3]] = 1
                i += 4

            else:
                if a == 2:
                    input_extnd[input_extnd[i + 3] + base] = 0

                else:
                    input_extnd[input_extnd[i + 3]] = 0
                i += 4

    run += 1

print(count_block(game))
print(score)