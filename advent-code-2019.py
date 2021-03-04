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


data = [
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