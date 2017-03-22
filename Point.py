import math

class Point
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def distanceTo(self, point):
        dist = math.sqrt(math.pow((point.x - self.x), 2) + math.pow((point.y - self.y), 2))
        return dist