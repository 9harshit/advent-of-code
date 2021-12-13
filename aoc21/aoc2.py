from utils import Submarine, get_data

DEBUG = False


data = get_data(__file__[-7:-3], DEBUG)


def sol_1():
    submarine = Submarine()

    for move in data:
        direction = move.split(" ")[0]
        distance = int(move.split(" ")[1])

        if direction == "forward":
            submarine.forward(distance)
        elif direction == "up":
            submarine.up(distance)
        elif direction == "down":
            submarine.down(distance)

    return submarine.x * submarine.y


def sol_2():
    class Submarine1(Submarine):
        def __init__(self):
            super().__init__()

        def forward(self, distance):
            self.x += distance
            self.y += self.aim * distance

        def up(self, distance):
            self.aim -= distance

        def down(self, distance):
            self.aim += distance

    submarine = Submarine1()

    for move in data:
        direction = move.split(" ")[0]
        distance = int(move.split(" ")[1])

        if direction == "forward":
            submarine.forward(distance)
        elif direction == "up":
            submarine.up(distance)
        elif direction == "down":
            submarine.down(distance)

    return submarine.x * submarine.y


print(sol_2())
