import io
import sys
import reading
try:
  from lxml import etree
  print("running with lxml.etree")
except ImportError:
  try:
    # Python 2.5
    import xml.etree.cElementTree as etree
    print("running with cElementTree on Python 2.5+")
  except ImportError:
    try:
      # Python 2.5
      import xml.etree.ElementTree as etree
      print("running with ElementTree on Python 2.5+")
    except ImportError:
      try:
        # normal cElementTree install
        import cElementTree as etree
        print("running with cElementTree")
      except ImportError:
        try:
          # normal ElementTree install
          import elementtree.ElementTree as etree
          print("running with ElementTree")
        except ImportError:
          print("Failed to import ElementTree from any known place")

def writeData(startPointData, endPointData, islandPointsData,
          routePointsData, filename):
    testCase = etree.Element("TestCase")
    startPoint = etree.SubElement(testCase, "StartPoint")
    startPoint.text = str(startPointData[0]) + " " + str(startPointData[1])
    endPoint = etree.SubElement(testCase, "EndPoint")
    endPoint.text = str(endPointData[0]) + " " + str(endPointData[1])
    islandPoints = etree.SubElement(testCase, "IslandPoints")
    #insert for loop which adds all the points of the island.
    for dataPoint in islandPointsData:
      xmlPoint = etree.SubElement(islandPoints, "Point")
      xmlPoint.text = str(dataPoint[0]) + " " + str(dataPoint[1])
    #insert for loop which adds all the points of the calculated solution.
    routePoints = etree.SubElement(testCase, "RoutePoints")
    for dataPoint in routePointsData:
      xmlPoint = etree.SubElement(routePoints, "Point")
      xmlPoint.text = str(dataPoint[0]) + " " + str(dataPoint[1])
    finalTree = etree.tostring(testCase, xml_declaration=True, pretty_print= True)
    print(finalTree)
    file = open(filename, 'wb')
    file.write(finalTree)
