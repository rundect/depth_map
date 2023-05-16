import pandas as pd

PATH_TO_DATA_FILE = 'depth_map/A3D_Result_1.2/Scanner1/20230324134621416.las'
raw = pd.readers.las(PATH_TO_DATA_FILE, sep=" ", header=None).values

# labels = pd.read_csv(PATH_TO_LABEL_FILE, sep=’ ‘, header=None).values[:,0]
