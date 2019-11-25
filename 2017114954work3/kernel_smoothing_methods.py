import numpy as np
import matplotlib.pyplot as plt

X = np.random.uniform(0,1,100)
epsilon = np.random.normal(0,1/3,100)
Y = np.sin(4 * X) + epsilon

plt.plot(np.arange(0,1,0.01),np.sin(4 * np.arange(0,1,0.01)))
plt.scatter(X,Y)

XY = np.vstack((X,Y))

def knn(x,k,XY):
    xdis = [(x-i)**2 for i in XY[0]]
    xdissortedindex = np.array(xdis).argsort()
    sumy = 0
    for i in range(k):
        sumy += XY[1][xdissortedindex[i]]
    yknn = sumy / k
    return yknn

xknn = np.arange(0,1,0.001)
yknn = [knn(i,30,XY) for i in xknn]
yknn = np.array(yknn)
#plt.plot(xknn,yknn)
#plt.savefig('knn.png')

def EpanechnikovQuadraticKernel(x0,x):
    t = abs(x-x0)/0.2
    if abs(t) <= 1:
        return 3/4 *(1 - t**2)
    else:
        return 0

def NadarayaWatson(x0,N,XY):
    xdis = [(x0 - i) ** 2 for i in XY[0]]
    xdissortedindex = np.array(xdis).argsort()
    sumy = 0
    sumkernel = 0
    for i in range(N):
        sumy += EpanechnikovQuadraticKernel(x0,XY[0][xdissortedindex[i]])*XY[1][xdissortedindex[i]]
        sumkernel += EpanechnikovQuadraticKernel(x0,XY[0][xdissortedindex[i]])
    return sumy / sumkernel

xNW = np.arange(0,1,0.001)
yNW = [NadarayaWatson(i,30,XY) for i in xNW]
yNW = np.array(yNW)
#plt.plot(xNW,yNW)
#plt.savefig('NadarayaWatson.png')

def adaptivekernel(x0,x,xk):
    t = abs(x - x0) / abs(x0-xk)
    if abs(t) <= 1:
        return 3 / 4 * (1 - t ** 2)
    else:
        return 0

def adaptive(x0,N,XY):
    xdis = [(x0 - i) ** 2 for i in XY[0]]
    xdissortedindex = np.array(xdis).argsort()
    sumy = 0
    sumkernel = 0
    for i in range(N):
        sumy += adaptivekernel(x0,XY[0][xdissortedindex[i]],XY[0][xdissortedindex[N-1]]) * XY[1][xdissortedindex[i]]
        sumkernel += adaptivekernel(x0,XY[0][xdissortedindex[i]],XY[0][xdissortedindex[N-1]])
    return sumy / sumkernel

xAD = np.arange(0,1,0.001)
yAD = [adaptive(i,30,XY) for i in xAD]
yAD = np.array(yAD)
plt.plot(xAD,yAD)
plt.savefig('widthfunction.png')