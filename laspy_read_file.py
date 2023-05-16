import numpy as np
import laspy
# FILE_TO_READ = '20230324134621416.las'
FILE_TO_READ = '20230324134101635.las'


las = laspy.read(f'A3D_Result_1.2/Scanner1/{FILE_TO_READ}')
a = las.xyz.take(indices=0)
for dimension in las.point_format.dimensions:
    print(dimension.name)
# print(np.unique(las.classification))


# with laspy.open('A3D_Result_1.2/Scanner1/20230324134101635.las') as fh:
#     print('Points from Header:', fh.header.point_count)
#     las = fh.read()
#     print(las)
#     print('Points from data:', len(las.points))
#     ground_pts = las.classification == 2
#     bins, counts = np.unique(las.return_number[ground_pts], return_counts=True)
#     print('Ground Point Return Number distribution:')
#     for r, c in zip(bins, counts):
#         print('    {}:{}'.format(r, c))
