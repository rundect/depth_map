import os
import numpy as np
import laspy
import xml.etree.ElementTree as ET

LAS_FILE = '20230324134621416.las'
LAS_FILES_PATH = 'A3D_Result_1.2/Scanner1'
PHOTO_INFO = 'A3D_Result_1.2/Block_1.xml'

root_node = ET.parse(PHOTO_INFO)
level = 'Name'
root_node_findall = root_node.findall(level)
for item in root_node.find('Center'):

    # empty news dictionary
    news = {}

    # iterate child elements of item
    for child in item:

        # special checking for namespace object content:media
        if child.tag == '{http://search.yahoo.com/mrss/}content':
            news['media'] = child.attrib['url']
        else:
            news[child.tag] = child.text.encode('utf8')




# for event, element in ET.iterparse(PHOTO_INFO):
#     print(event, element.tag)

# for tag in root_node.find(level):
#     print(tag)
#     value = tag.get(attribute)
#     if value is not None:
#         print(value)


# las = laspy.read(f"{LAS_FILES_PATH}/{LAS_FILE}")
# xyz = las.xyz
# arr = np.array(xyz)
# for i in arr:
#     print(i[1])
