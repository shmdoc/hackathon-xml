import xmltodict
import pprint
import pandas

# How to convert a hierarchical file to a table?
# --> https://stackoverflow.com/questions/43693969/flatten-xml-into-pandas-dataframe-deeply-nested/43840952

# Convert the xml file to a nested dictionary
with open("das6380.xml") as fd:
    doc = xmltodict.parse(fd.read())

print(doc['resource'].type)

# Flatten the nested dictionary
normalized = pandas.json_normalize(doc)
for element in normalized.iloc[:,-2]:
    for elementdeep in element:
        print(elementdeep)
            

