class Submarine:
    def __init__(self):
        self.x, self.y, self.aim = 0, 0, 0

    def forward(self, distance):
        self.x += distance

    def up(self, distance):
        self.y -= distance

    def down(self, distance):
        self.y += distance
