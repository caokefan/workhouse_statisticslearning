import numpy as np
import matplotlib.pyplot as plt

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
    subscript=int(10*i)-1
    blue.append([np.random.normal(nblue[0][subscript],0.2),np.random.normal(nblue[1][subscript],0.2)])
    orange.append([np.random.normal(norange[0][subscript],0.2),np.random.normal(norange[1][subscript],0.2)])

blue=np.array(blue)
orange=np.array(orange)
plt.figure(1)
plt.scatter(blue[:,0],blue[:,1])
plt.scatter(orange[:,0],orange[:,1])
plt.savefig('scatter_figure.png')
plt.close(1)