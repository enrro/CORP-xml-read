import xml.etree.ElementTree as ET


tree = ET.parse('../resources/CMF Analyst Metrics Report.xml')
root = tree.getroot()
print(root.tag, root.attrib)
#for child in root.iter():
    #print(child.tag)
    #print(child.attrib)
    #if child.tag == "{http://schemas.microsoft.com/sqlserver/reporting/2010/01/reportdefinition}DataSources":
        #print("reasd")

