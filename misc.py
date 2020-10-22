from math import hypot


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __sub__(self, other):
        x_dist = self.x - other.x
        y_dist = self.y - other.y

        distance = hypot(x_dist, y_dist)
        return distance

    def __str__(self):
        return f'({self.x}, {self.y})'
