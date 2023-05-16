import os
import numpy as np
import open3d as o3d
import laspy


FILE_TO_READ = '20230324134621416.las'
# FILE_TO_READ = '20230324134101635.las'
pc_path = 'A3D_Result_1.2/Scanner1'

pc1 = laspy.read(os.path.join(pc_path, FILE_TO_READ))
xyz = np.vstack((pc1.x, pc1.y, pc1.z)).transpose()
pcd = o3d.geometry.PointCloud()
pcd.points = o3d.utility.Vector3dVector(xyz)
pcd_1m = pcd.voxel_down_sample(voxel_size=1)
o3d.visualization.draw_geometries([pcd_1m])
