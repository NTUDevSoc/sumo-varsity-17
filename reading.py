
import io
import xml.etree.ElementTree


"""
read in file

@return startPos[x,y], endPos[x,y], islandPoints[[x,y],...nn]
"""
xmlFile = open("docsAndXML/testcases/sampleTestcase.xml")
e = xml.etree.ElementTree.parse('docsAndXML/testcases/sampleTestcase.xml').getroot()
print(e)
e.get("Point")
