from generate_one_handred_data import blue,orange
import numpy as np
#import matplotlib.pyplot as plt

xy=np.concatenate((blue,orange),axis=0)
xy=np.hstack((np.ones([200,1]),xy))
z=np.append(np.zeros(100),np.ones(100))

xyMat=np.mat(xy)
zMat=np.mat(z).T
xyTxy=xyMat.T*xyMat
if np.linalg.det(xyTxy)==0:
    print("this matrix is singular,cannot do inverse")
else:
    w=xyTxy.I*(xyMat.T*zMat)
    print(w)
    false=0
    for i in range(200):
        if i<100:
            if np.dot(np.mat(w).T,xy[i])>0.5: false=false+1
        else:
            if np.dot(np.mat(w).T,xy[i])<0.5: false=false+1
    falserate=false/200
    print('误判率: {:.2%}'.format(falserate))