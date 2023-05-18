from typing import Union

import laspy
import numpy as np
from os import listdir, path

from utils import save_to_txt_file


def get_photos_center(photo_data):
    photos_dict = {}
    photos = photo_data['BlocksExchange']['Block']['Photogroups']['Photogroup']['Photo']
    for j in photos:
        photo_center = j['Pose']['Center']
        x = photo_center['x']
        y = photo_center['y']
        z = photo_center['z']
        image_file_name = j['ImagePath'][j['ImagePath'].rfind('/') + 1:]
        photos_dict[image_file_name] = {'x': x, 'y': y, 'z': z}
    return photos_dict


def get_las_files_names(las_files_path: str, return_data: Union[bool, int] = True) -> list:
    las_files = []
    for file_name in listdir(las_files_path):
        if path.isfile(path.join(las_files_path, file_name)) and file_name[-4:] == '.las':
            las_files.append(file_name)
    if return_data:
        return las_files
    elif type(return_data) == int:
        return las_files[return_data]


def __get_min_max_axis(arr: np.ndarray) -> dict:
    x_max = arr[:, 0].max()
    x_min = arr[:, 0].min()
    y_max = arr[:, 1].max()
    y_min = arr[:, 1].min()
    z_max = arr[:, 2].max()
    z_min = arr[:, 2].min()
    return {
        'x_max': x_max,
        'x_min': x_min,
        'y_max': y_max,
        'y_min': y_min,
        'z_max': z_max,
        'z_min': z_min
    }


def get_points_max_min_coords(
        las_files_names: list,
        las_files_path: str
) -> dict:
    points_max_min_coords = {}
    for las_file in las_files_names:
        las = laspy.read(f"{las_files_path}/{las_file}")
        xyz = las.xyz
        arr = np.array(xyz)
        min_max_value = __get_min_max_axis(arr)
        points_max_min_coords[las_file] = min_max_value
        print(f"{las_file} ended")
    return points_max_min_coords

# def get_points_max_min_value(las_files_names: list, las_files_path: str) -> list:
#     for las_file in las_files_names:
#         las_file_coordinate = []
#         las = laspy.read(f"{las_files_path}/{las_file}")
#         xyz = las.xyz
#         arr = np.array(xyz)
#         x_max = arr[:, 0].max()
#         x_min = arr[arr[:, 0].argsort()]
#         # z = arr[arr[:, 2].argsort()]
#         arr_sorted = arr.sort
#         points = {}
#         for i in arr:
#             xyz = i.tolist()
#             coordinate = (str(xyz[0]), str(xyz[1]), str(xyz[2]))
#             las_file_coordinate.append(coordinate)
#             # value = photos_center.get(coordinate)
#             # if value:
#             #     print(value)
#         print(f"{las_file} ended")
#         with open(f"{las_file}.txt", "w") as file:
#             file.write(str(las_file_coordinate))
