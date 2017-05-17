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


    tree = ET.parse('../resources/' + file)
    root = tree.getroot()
    #print(root.tag)
    uri = tag_uri_and_name(root)




    print(file + " DataSourceReference is")


    #iterate through the array to find the DataSoruce and find the attributes by name
    for child in root.iter('{' + uri[0] + '}' + "DataSource"):
        print(child.attrib['Name'])

    numberOfStoredProcedures = 0
    for child in root.iter('{' + uri[0] + '}' + "CommandType"):
        #print(child.text)
        numberOfStoredProcedures = numberOfStoredProcedures + 1
    # for child1 in root.iter('{' + uri[0] + '}' + "CommandText"):
    print("number of stop procedures = ", numberOfStoredProcedures)

    numberOfQueries = 0
    for child in root.iter('{' + uri[0] + '}' + "CommandText"):
        if numberOfStoredProcedures > 0:
            print(child.text)
            numberOfStoredProcedures = numberOfStoredProcedures - 1
        else:
            numberOfQueries = numberOfQueries + 1




    print("number of queues ", numberOfQueries)

    print('\n')