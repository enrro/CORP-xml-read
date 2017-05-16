import xml.etree.ElementTree as ET
import os
import csv


def tag_uri_and_name(elem):
    if elem.tag[0] == "{":
        uri, ignore, tag = elem.tag[1:].partition("}")
    else:
        uri = None
        tag = elem.tag
    return uri, tag


filesList = (os.listdir("../resources/"))

for file in filesList:
    print(file)

    tree = ET.parse('../resources/' + file)
    root = tree.getroot()
    print(root.tag)
    uri = tag_uri_and_name(root)

    for child in root:
        print(child.tag)

    #
    # print("\n next \n")
    #
    #
    # print(root[1][0][0])
    # print(root[1][0][0].text)

    print("\n The DataSourceReference is \n")


    #iterate through the array to find the DataSoruce and find the attributes by name
    for child in root.iter('{' + uri[0] + '}' + "DataSource"):
        #print(child.tag)
        #print(child.attrib)
        print(child.attrib['Name'])
        print("\n")

        #print(child.text)
        # if child.tag == "{http://schemas.microsoft.com/sqlserver/reporting/2010/01/reportdefinition}DataSources":
        #     print("reasd")