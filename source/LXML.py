from lxml import etree
import csv

someiterable = ["hi"]
someiterable1 = [1,2,3,4,5]
import csv
writer = csv.writer(open("some.csv", "w"), dialect='excel', lineterminator='\n')
writer.writerow(someiterable)
writer.writerow(someiterable1)
