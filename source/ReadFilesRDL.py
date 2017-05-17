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

writer = csv.writer(open("some.csv", "w"), dialect='excel', lineterminator='\n')
filesList = (os.listdir("../resources/"))
header =["name of file","number of stored procedures","number of procedure","name of stored procedures","number of queue"]
writer.writerow(header)
information = ["","","","",""]

for file in filesList:


    tree = ET.parse('../resources/' + file)
    root = tree.getroot()
    uri = tag_uri_and_name(root)

    print(file + " DataSourceReference is")
    information[0] = file

    #iterate through the array to find the DataSoruce and find the attributes by name
    for child in root.iter('{' + uri[0] + '}' + "DataSource"):
        information[1] =(child.attrib['Name'])
    #iterate for procedures
    numberOfStoredProcedures = 0
    for child in root.iter('{' + uri[0] + '}' + "CommandType"):
        #print(child.text)
        numberOfStoredProcedures = numberOfStoredProcedures + 1
    # for child1 in root.iter('{' + uri[0] + '}' + "CommandText"):
    print("number of stop procedures = ", numberOfStoredProcedures)
    information[2] = numberOfStoredProcedures
    #iterate for queries
    numberOfQueries = 0
    nameOfStoredProcedures = ""
    for child in root.iter('{' + uri[0] + '}' + "CommandText"):
        if numberOfStoredProcedures > 0:
            nameOfStoredProcedures = nameOfStoredProcedures + " " + (child.text)
            numberOfStoredProcedures = numberOfStoredProcedures - 1
        else:
            numberOfQueries = numberOfQueries + 1

    information[3] = nameOfStoredProcedures
    print("number of queues ", numberOfQueries)
    information[4] = numberOfQueries
    print('\n')
    writer.writerow(information)