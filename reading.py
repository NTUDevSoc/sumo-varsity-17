
import io
import untangle
import xmltodict
import xml.etree.ElementTree

obj = untangle.parse('docsAndXML/testcases/sampleTestcase.xml')



"""

"""
def readData(filename):
    dic = {}
    with open(filename) as fd:
        dic = xmltodict.parse(fd.read())
        #print(dic)

    start = dic['TestCase']['StartPoint']
    print(start)
    end =  dic['TestCase']['EndPoint']



readData('docsAndXML/testcases/sampleTestcase.xml')
