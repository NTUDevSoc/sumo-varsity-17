
import io
import untangle
import xmltodict
import xml.etree.ElementTree


"""
read in file

@return startPos[x,y], endPos[x,y], islandPoints[[x,y],...nn]
"""
xmlFile = open("docsAndXML/testcases/sampleTestcase.xml")
e = xml.etree.ElementTree.parse('docsAndXML/testcases/sampleTestcase.xml').getroot()
print(e)
e.get("Point")

obj = untangle.parse('docsAndXML/testcases/sampleTestcase.xml')

print(obj.TestCase.StartPoint[0])

doc = xmltodict.parse(xmlFile.read())
print(doc)
print(doc['TestCase'])
doicskdmsa = {'fun':'done', 'foo':'bar'}
print(doicskdmsa)
