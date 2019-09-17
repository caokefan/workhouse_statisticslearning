import numpy as np
import matplotlib.pyplot as plt

x = np.array([825, 215, 1070, 550, 480, 920, 1350, 325, 670, 1215])
y = np.array([3.5, 1.0, 4.0, 2.0, 1.0, 3.0, 4.5, 1.5, 3.0, 5.0])

# 1)
plt.scatter(x,y)
plt.savefig('scatter_figure.png')
# 3)
def least_square(x,y):
    sumx2 = sum(x ** 2)
    sumxy = sum(x * y)
    meanx = sum(x) / x.shape[0]
    meany = sum(y) / y.shape[0]
    n = x.shape[0]

    beta1 = (sumxy - n * meanx * meany) / (sumx2 - n * meanx ** 2)
    beta0 = meany - beta1 * meanx

    return beta0, beta1

beta0, beta1 = least_square(x, y)

# 2) 由图可以看出x与y大致呈线性关系
X = np.arange(100, 1500, 100)
Y = np.array([beta0 + beta1 * x for x in X])
plt.plot(X,Y)
plt.savefig("fit_figure.png")
plt.close()
# 4)
sigma2 = []
for valuey, valueY in zip(y,Y):
    sigma2.append((valueY - valuey) ** 2)
sumsigma2 = sum(sigma2)

# 6)
def SSR(Y,y):
    meany = sum(y) / y.shape[0]
    for i in Y:
        yield (i - meany) ** 2

def SST(y):
    meany = sum(y) / y.shape[0]
    for i in y:
        yield (i - meany) ** 2

r2 = sum(SSR(Y,y)) / sum(SST(y))

# 7)
St = sum(SST(y))
Sr = beta1 ** 2 * sum(SST(x))
Se = St - Sr
mSr = Sr / 1
mSe = Se / 8
F_ratio = mSr / mSe
# 10)
epsilon = np.array([yi - Yi for yi, Yi in zip(y,Y)])
plt.scatter(y,epsilon)
plt.savefig('epsilon_figure.png')
# 11)
x0 = 1000
predict_y = beta0 + beta1 * x0

with open('result.txt','w') as f:
    f.write("3) beta0 =%f,beta1 = %f\n" % (beta0,beta1))
    f.write("4) 回归标准误差：%f\n" % sumsigma2)
    f.write("6) x与y的决定系数：%f\n" % r2)
    f.write("7) F(1,8)= %f\n" % F_ratio)
    f.write("11) 需要的加班时间是：%f" % predict_y)
    f.close()