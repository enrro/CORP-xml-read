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


goalDirectory = "D:/Users/gdlebric/Downloads/"

folders = []
for f in os.listdir(goalDirectory):
    if not f == "desktop.ini":
        folders.append(f)



writer = csv.writer(open("report.csv", "w"), dialect='excel', lineterminator='\n')
header =["directory","name of file","Data Source","number of procedure","name of stored procedures","number of Queries"]
writer.writerow(header)
for directory in folders:
    filesList = (os.listdir(goalDirectory + "/" + directory))
    information = ["","","","","",""]

    for file in filesList:

        information[0] = directory
        tree = ET.parse(goalDirectory + directory + "/" + file)
        root = tree.getroot()
        uri = tag_uri_and_name(root)

        print(file + " DataSourceReference is")
        information[1] = file

        #iterate through the array to find the DataSoruce and find the attributes by name
        dataSourceName = ""
        for child in root.iter('{' + uri[0] + '}' + "DataSource"):
            dataSourceName = dataSourceName + " " + child.attrib['Name']
        information[2] = dataSourceName
        #iterate for procedures
        numberOfStoredProcedures = 0
        for child in root.iter('{' + uri[0] + '}' + "CommandType"):
            #print(child.text)
            numberOfStoredProcedures = numberOfStoredProcedures + 1

        # for child1 in root.iter('{' + uri[0] + '}' + "CommandText"):
        print("number of stop procedures = ", numberOfStoredProcedures)
        information[3] = numberOfStoredProcedures
        #iterate for queries
        numberOfQueries = 0
        nameOfStoredProcedures = ""
        for child in root.iter('{' + uri[0] + '}' + "CommandText"):
            if numberOfStoredProcedures > 0:
                nameOfStoredProcedures = nameOfStoredProcedures + " " + (child.text)
                numberOfStoredProcedures = numberOfStoredProcedures - 1
            else:
                numberOfQueries = numberOfQueries + 1

        information[4] = nameOfStoredProcedures
        print("number of queues ", numberOfQueries)
        information[5] = numberOfQueries
        print('\n')
        writer.writerow(information)
