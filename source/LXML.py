from lxml import etree

#tree = etree.parse('../resources/CMF Analyst Metrics Report.rdl')

root = tree.getroot()
#print(root.tag)
#print(len(root))

tag = etree.QName(root)
print(print(tag.localname))
print(tag.namespace)
print(tag.text)
print(root.find(".//DataSourceName").tag)
#parser = etree.XMLParser(target = EchoTarget())

#print(etree.tostring(tree.getroot()))

