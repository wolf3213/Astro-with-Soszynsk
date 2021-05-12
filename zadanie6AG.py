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
M=[]
indices=[]
for i in np.arange(-10,10,0.02):
    M.append(Hjer(i,1))
    indices.append(i)
plt.plot(indices,M,color='r',label=r"$\alpha=1$")
M.clear()
indices.clear()
print('1')
for i in np.arange(-10,10,0.02):
    M.append(Hjer(i,0.1))
    indices.append(i)
print('2')
plt.plot(indices,M,color='g',label=r"$\alpha=0.1$")
M.clear()
indices.clear()
for i in np.arange(-10,10,0.02):
    M.append(Hjer(i,0.01))
    indices.append(i)
print('3')
plt.plot(indices,M,color='y',label=r"$\alpha=0.01$")
M.clear()
indices.clear()
for i in np.arange(-10,10,0.02):
    M.append(Hjer(i,0.001))
    indices.append(i)
print('4')
plt.plot(indices,M,color='k',label=r"$\alpha=0.001$")
plt.legend()
plt.grid(b=True,which="major",color='#666666', linestyle='-',linewidth=0.2)



plt.show()