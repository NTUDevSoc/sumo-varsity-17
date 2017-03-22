import math

class Point:
    #Expects number
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def distanceTo(self, point):
        dist = math.sqrt(math.pow((point.x - self.x), 2) + math.pow((point.y - self.y), 2))
        return dist

    def angleBetween(self, point1, point2):
        p1Dist = self.distanceTo(point1)
        p2Dist = self.distanceTo(point2)
        betDist = point1.distanceTo(point2)
        try:
            ang = math.acos(((math.pow(p1Dist, 2)+math.pow(p2Dist,2))-math.pow(betDist,2))/(2*p1Dist*p2Dist))
        except:
            ang = 0
        return ang
