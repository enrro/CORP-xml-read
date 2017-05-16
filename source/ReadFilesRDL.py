import xml.etree.ElementTree as ET


tree = ET.parse('../resources/CMF Analyst Metrics Report.xml')
root = tree.getroot()

print(root.tag)
print(root.attrib)

for child in root:
    print(child.tag)

print("\n next \n")


print(root[1][0][0])
print(root[1][0][0].text)


#for child in root.iter():
#print(child.tag)
#print(child.attrib)
#if child.tag == "{http://schemas.microsoft.com/sqlserver/reporting/2010/01/reportdefinition}DataSources":
#print("reasd")
