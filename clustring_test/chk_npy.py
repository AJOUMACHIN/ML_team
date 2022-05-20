import numpy as np

data = np.load("./sample_data.npy", allow_pickle=True)
print(np.shape(data))
np.savetxt('sample_data.csv', data)