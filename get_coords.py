from utils import read_json, save_xml_to_json, save_to_txt_file
from utils_las import get_las_files_names, get_photos_center, get_points_max_min_coords

LAS_FILES_PATH = 'A3D_Result_1.2/Scanner1'
PHOTO_INFO_JSON = 'Block_1.json'
PHOTO_INFO_XML = 'A3D_Result_1.2/Block_1.xml'

# save_xml_to_json(path_xml_file=PHOTO_INFO_XML, path_json_file=PHOTO_INFO_JSON)
las_files_names = get_las_files_names(LAS_FILES_PATH)
photo_data = read_json(PHOTO_INFO_JSON)
photos_center = get_photos_center(photo_data)
min_max_value = get_points_max_min_coords(las_files_names, LAS_FILES_PATH)


def save_coords(file_name: str, text: dict) -> None:
    save_to_txt_file(file_name, text)


save_coords('photos_center_coords', photos_center)
save_coords('points_coords', min_max_value)
