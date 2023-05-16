import numpy as np
import laspy
import json
from os import listdir, path


LAS_FILES_PATH = 'A3D_Result_1.2/Scanner1'
PHOTO_INFO = 'Block_1.json'


with open(f"{PHOTO_INFO}") as json_data:
    photo_data = json.loads(json_data.read())


def get_photos_info(photo_data):
    photos_dict = {}
    photos = photo_data['BlocksExchange']['Block']['Photogroups']['Photogroup']['Photo']
    for j in photos:
        photo_center = j['Pose']['Center']
        x = photo_center['x']
        y = photo_center['y']
        z = photo_center['z']
        photos_dict[(x, y, z)] = {'x': x, 'y': y, 'z': z, 'ImagePath': j['ImagePath']}
    return photos_dict


def get_las_files_names(las_files_path: str) -> list:
    las_files = []
    for file_name in listdir(las_files_path):
        if path.isfile(path.join(las_files_path, file_name)) and file_name[-4:] == '.las':
            las_files.append(file_name)
    return las_files


las_files_names = get_las_files_names(LAS_FILES_PATH)
photos_center = get_photos_info(photo_data)


for las_file in las_files_names:
    las_file_coordinate = []
    las = laspy.read(f"{LAS_FILES_PATH}/{las_file}")
    xyz = las.xyz
    arr = np.array(xyz)
    points = {}
    for i in arr:
        xyz = i.tolist()
        coordinate = (str(xyz[0]), str(xyz[1]), str(xyz[2]))
        las_file_coordinate.append(coordinate)
        # value = photos_center.get(coordinate)
        # if value:
        #     print(value)
    print(f"{las_file} ended")
    with open(f"{las_file}.txt", "w") as file:
        file.write(str(las_file_coordinate))


print('END')
