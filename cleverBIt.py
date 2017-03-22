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
            pList.append(Point.Point(i[0], i[1]))

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

            currentNode = nextNode

        return length

    def solve(self):
        islandStart = self.findClosest(self.start)
        islandEnd = self.findClosest(self.end)
        cwLength = self.calculateRouteLength(islandStart, islandEnd, True)
        acwLength = self.calculateRouteLength(islandStart, islandEnd, False)
        if (cwLength < acwLength):
            return cwLength
        else:
            return acwLength




"""

Entry point system
"""
if __name__ == '__main__':
    #Grab the data
    data = reading.readData('docsAndXML/testcases/sampleTestcase.xml')
    #print(data)
    #Create a point
    startPos = data['start']
    endPos = data['end']
    islandPoints = data['island']

    #Create some points
    startPnt = Point.Point(startPos[0],startPos[1])
    #print(startPnt)
    endPnt = Point.Point(endPos[0],endPos[1])
    #print(endPos)
    print(islandPoints)

    #print(islandPoints[0])
    #create a cleveBit class
