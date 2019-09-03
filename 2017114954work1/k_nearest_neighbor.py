from generate_one_handred_data import blue,orange
import numpy as np
import operator
import matplotlib.pyplot as plt

xy=np.concatenate((blue,orange),axis=0)
xy=np.hstack((np.ones([200,1]),xy))
z=np.append(np.zeros(100),np.ones(100))

def knn(inX,xy,z,k):
    datasize = xy.shape[0]
    diffmat = np.tile(inX, (datasize, 1)) - xy
    sqdiffmat = diffmat ** 2
    sqdistances = sqdiffmat.sum(axis=1)
    distances = sqdistances ** 0.5
    sorteddistindices = distances.argsort()
    classcount = {}
    for i in range(k):
        voteilabel = z[sorteddistindices[i]]
        classcount[voteilabel] = classcount.get(voteilabel, 0) + 1

    sortedclasscount = sorted(classcount.items(), key=operator.itemgetter(1), reverse=True)
    return sortedclasscount[0][0]

falserate=[]
for k in range(1,21):
    false = 0
    for i in range(200):
        if i < 100:
            if knn(xy[i], xy, z, k) > 0.5: false = false + 1
        else:
            if knn(xy[i], xy, z, k) < 0.5: false = false + 1
    falserate.append(false / 200)

plt.plot(np.linspace(1,20,20),np.array(falserate))
plt.savefig("k_fold_error_map.png")