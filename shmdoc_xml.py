import xmltodict
from pprint import pprint
import pandas
import json

# How to convert a hierarchical file to a table?
# --> https://stackoverflow.com/questions/43693969/flatten-xml-into-pandas-dataframe-deeply-nested/43840952

# Convert the xml file to a nested dictionary
with open("das6380.xml") as fd:
    doc = json.dumps(xmltodict.parse(fd.read()))

data = json.loads(doc)
pprint(data)


# Flatten the nested dictionary
normalized = pandas.json_normalize(data)
normalized.to_csv("output.csv")

# Get a csv of the creators
test = normalized["resource.creators.creator"]
el = test[0]
norm = pandas.json_normalize(el)
norm.to_csv("creators.csv")

# pprint(normalized)
for element in normalized.iloc[:,-2]:
    for elementdeep in element:
        pprint(elementdeep)


