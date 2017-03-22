import reading


class Problem:
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

    def solve(self):
        islandStart = self.findClosest(self.start)
        islandEnd = self.findClosest(self.end)



"""

Entry point system
"""


#Grab the data
startPos,endPos,islandPoints = reading.readData('docsAndXML/testcases/sampleTestcase.xml')
