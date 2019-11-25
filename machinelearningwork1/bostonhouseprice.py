import numpy as np

blue=[]
orange=[]
#step1
nblue=np.array([np.random.normal(1,1,10),np.random.normal(0,1,10)])
norange=np.array([np.random.normal(0,1,10),np.random.normal(1,1,10)])
#step2:
#step2-1
s=np.random.uniform(0,1,100)
#step2-2,2-3
for i in s:
    index=int(10*i)-1
    blue.append([np.random.normal(nblue[0][index],0.2),np.random.normal(nblue[1][index],0.2)])
    orange.append([np.random.normal(norange[0][index],0.2),np.random.normal(norange[1][index],0.2)])

blue=np.array(blue)
orange=np.array(orange)
print(blue)
print(orange)

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
    np.savetxt("data.txt",w)
    false=0
    for i in range(200):
        if i<100:
            if np.dot(np.mat(w).T,xy[i])>0.5: false=false+1
        else:
            if np.dot(np.mat(w).T,xy[i])<0.5: false=false+1
    falserate=false/200
    file = open('data.txt', 'a')
    file.write('误判率: {:.2%}'.format(falserate))
    file.close()
    print('误判率: {:.2%}'.format(falserate))