
import json
import xmltodict

PHOTO_INFO = 'A3D_Result_1.2/Block_1.xml'
SAVE_TO_JSON = 'Block_1.json'

with open(PHOTO_INFO) as xml_file:
    data_dict = xmltodict.parse(xml_file.read())

json_data = json.dumps(data_dict)

with open(SAVE_TO_JSON, "w") as json_file:
    json_file.write(json_data)
