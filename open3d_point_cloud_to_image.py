import os
import numpy as np
import open3d as o3d
import laspy
from matplotlib import pyplot as plt
from PIL import Image

pc_path = '.'
pc_fn = '20230324134621416.las'
pc1 = laspy.read(os.path.join(pc_path, pc_fn))
xyz = np.vstack((pc1.x, pc1.y, pc1.z)).transpose()
pcd = o3d.geometry.PointCloud()
vis = o3d.visualization.Visualizer()

vis.create_window('pcl', 640, 480, 50, 50, True)
vis.add_geometry(pcd)

vis = o3d.visualization.Visualizer()
vis.create_window(visible=True)
vis.add_geometry(pcd)

depth = vis.capture_depth_float_buffer(False)

image = vis.capture_screen_float_buffer(False)
plt.imshow(np.asarray(depth))
o3d.io.write_image("./test_depth.png", depth)

# plt.imsave("./test_depth.png",
#            np.asarray(out_depth))  # , dpi = 1)
#
# img = Image.open('./test_depth.png').convert('LA')
# img.save('./greyscale.png')
