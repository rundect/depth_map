import open3d as o3d
import numpy as np
import matplotlib.pyplot as plt

if __name__ == '__main__':
    # tum_data = o3d.data.SampleTUMRGBDImage(data_root='depth_map/A3D_Result_1.2/Scanner1/20230324134101635.las')
    readed_point_cloud = o3d.t.io.read_point_cloud(
        filename='depth_map/A3D_Result_1.2/Scanner1/20230324134621416.las',
        format='las'
    )
    print(readed_point_cloud)
    # depth = o3d.t.io.read_image(tum_data.depth_path)
    # intrinsic = o3d.core.Tensor(
    #     [[535.4, 0, 320.1],
    #      [0, 539.2, 247.6],
    #      [0, 0, 1]]
    # )

    # pcd = o3d.t.geometry.PointCloud.create_from_depth_image(
    #     depth,
    #     intrinsic,
    #     depth_scale=5000.0,
    #     depth_max=10.0)
    # o3d.visualization.draw([pcd])
    # depth_reproj = pcd.project_to_depth_image(
    #     640,
    #     480,
    #     intrinsic,
    #     depth_scale=5000.0,
    #     depth_max=10.0
    # )
    #
    # fig, axs = plt.subplots(1, 2)
    # axs[0].imshow(np.asarray(depth.to_legacy()))
    # axs[1].imshow(np.asarray(depth_reproj.to_legacy()))
    # plt.show()
