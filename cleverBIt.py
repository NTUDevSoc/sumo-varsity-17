import reading
import Point

class Problem:
    #Start and End are point objects repesenting the ships
    #island = list [[x,y],..]
    def __init__(self, start, end, island):
        self.start = start
        self.end = end
        self.island = self.createPoints(island)

    #creates point objects
    def createPoints(self, island):
        pList = []
        for i in island:
            pList.append(Point.Point(float(i[0]), float(i[1])))

        return pList

    def findClosest(self, tarPoint):
        closest = 0
        for i in range(0, len(self.island)):
            if (self.island[i].distanceTo(tarPoint) < self.island[closest].distanceTo(tarPoint)):
                closest = i
        return closest

    def calculateRouteLength(self, start, end, clockwise):
        currentNode = start
        length = 0
        route = [self.island[start]]
        while (currentNode != end):
            if clockwise:
                if (currentNode == len(self.island)-1):
                    nextNode = 0
                else:
                    nextNode = currentNode+1
            else:
                if (currentNode == 0):
                    nextNode = len(self.island)-1
                else:
                    nextNode = currentNode-1

            length += self.island[currentNode].distanceTo(self.island[nextNode])
            route.append(self.island[nextNode])

            currentNode = nextNode

        route.insert(0, self.start)
        route.append(self.end)
        return length, route

    def smooth(self):
        smoothedIsland = [self.start]
        returning = False
        while returning != True:
            nextCandidate = self.end
            for i in self.island:
                ang = smoothedIsland[-1].angleBetween(self.end, i)
                if ((ang > smoothedIsland[-1].angleBetween(self.end, nextCandidate)) & (ang > 0 )):
                    nextCandidate = i
            if i == self.end:
                returning = True
            smoothedIsland.append(i)

        while returning == True:
            nextCandidate = self.start
            for i in self.island:
                ang = smoothedIsland[-1].angleBetween(self.start, i)
                if ((ang > smoothedIsland[-1].angleBetween(self.start, nextCandidate)) & (ang > 0)):
                    nextCandidate = i
            if i == self.start:
                returning = False
            else:
                smoothedIsland.append(i)

        self.island = smoothedIsland

    def solve(self):
        islandStart = self.findClosest(self.start)
        islandEnd = self.findClosest(self.end)
        cwLength, cwRoute = self.calculateRouteLength(islandStart, islandEnd, True)
        acwLength, acwRoute = self.calculateRouteLength(islandStart, islandEnd, False)
        if (cwLength < acwLength):
            return cwRoute
        else:
            return acwRoute


if __name__ == '__main__':
    #Grab the data
    data = reading.readData('docsAndXML/testcases/sampleTestcase.xml')
    #print(data)
    #Create a point
    startPos = data['start']
    endPos = data['end']
    islandPoints = data['island']

    #Create some points
    startPnt = Point.Point(float(startPos[0]),float(startPos[1]))
    #print(startPnt)
    endPnt = Point.Point(float(endPos[0]),float(endPos[1]))
    #print(endPos)
    #print(islandPoints)


    #print(islandPoints[0])
    #create a cleveBit class
    solver = Problem(startPnt,endPnt,islandPoints)
    solver.smooth()
    solution = solver.solve()
    print(solution)
    for pnt in solution:
        print("First go: ", "x:", pnt.x,"y:",pnt.y)
