import json
from typing import Any

import xmltodict


def save_xml_to_json(path_xml_file: str, path_json_file: str) -> None:
    with open(path_xml_file) as xml_file:
        data_dict = xmltodict.parse(xml_file.read())

    json_data = json.dumps(data_dict)

    with open(path_json_file, "w") as json_file:
        json_file.write(json_data)


def read_json(path_json_file: str) -> dict:
    with open(f"{path_json_file}") as json_data:
        dict = json.loads(json_data.read())
        return dict


def save_to_txt_file(file_name: str, text: Any) -> None:
    with open(f"{file_name}.txt", "w") as file:
        file.write(str(text))
