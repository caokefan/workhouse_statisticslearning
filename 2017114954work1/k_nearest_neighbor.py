from generate_one_handred_data import blue,orange
import numpy as np

xy=np.concatenate((blue,orange),axis=0)
xy=np.hstack((np.ones([200,1]),xy))
z=np.append(np.zeros(100),np.ones(100))

