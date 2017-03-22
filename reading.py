
import io
import untangle
import xmltodict
import xml.etree.ElementTree

obj = untangle.parse('docsAndXML/testcases/sampleTestcase.xml')



"""
@param filename with xml pleassee

@return start[x,y], end[x,y], islandPoints=[[x,y],...,n]
"""
def readData(filename):
    dic = {}
    with open(filename) as fd:
        dic = xmltodict.parse(fd.read())
        #print(dic)

    start = dic['TestCase']['StartPoint']
    startPos =  start.split(" ")

    end =  dic['TestCase']['EndPoint']
    endPos = end.split(" ")

    #Gathering the
    points = dic['TestCase']['IslandPoints']['Point']

    islandPoints = []
    for i in points:
        islandPoints.append(i.split(" "))

    return {'start': startPos,'end':endPos,'island':islandPoints}


    #return {'str':startPos, 'end': endPos, 'island':islandPoints}




#data = readData('docsAndXML/testcases/sampleTestcase.xml')
#print(data)
