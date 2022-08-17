import math
import scipy
import matplotlib.pyplot as plt
import numpy as np
def integrate(f, a, b, dx):
    i = a
    s = 0
    while i <= b:
        s += f(i)*dx
        i += dx
    return s

def h(y,v,a):
    return math.exp(-y**2)/((v-y)**2+a**2)
###v=1
    #a=1
    #return math.exp(-v**2)/((v-y)**2+a**2)
def Hjer(v,a):
    return integrate(lambda y:h(y,v,a),-10,10,0.001)*a/math.pi
def UnderINT(v,a,C):
    return 1-math.exp(-C*Hjer(v,a))
M=[]
indices=[]
for i in np.arange(-10,10,0.02):
    M.append(UnderINT(i,0.001,0.1))
    indices.append(i)
    print(i)
plt.plot(indices,M,color='r',label=r"$\alpha=1, C=0.1$")
M.clear()
indices.clear()
M=[]
indices=[]
for i in np.arange(-10,10,0.02):
    M.append(UnderINT(i,0.001,1))
    indices.append(i)
    print(i)
plt.plot(indices,M,color='y',label=r"$\alpha=1, C=1$")
M.clear()
indices.clear()
M=[]
indices=[]
for i in np.arange(-10,10,0.02):
    M.append(UnderINT(i,0.001,10))
    indices.append(i)
    print(i)
plt.plot(indices,M,color='k',label=r"$\alpha=1, C=10$")
M.clear()
indices.clear()
M=[]
indices=[]
for i in np.arange(-10,10,0.02):
    M.append(UnderINT(i,0.001,100))
    indices.append(i)
    print(i)
plt.plot(indices,M,color='g',label=r"$\alpha=1, C=100$")
M.clear()
indices.clear()
M.clear()
indices.clear()
M=[]
indices=[]
for i in np.arange(-10,10,0.02):
    M.append(UnderINT(i,0.01,1000))
    indices.append(i)
    print(i)
plt.plot(indices,M,color='b',label=r"$\alpha=1, C=1000$")
M.clear()
indices.clear()
plt.legend()
plt.show()