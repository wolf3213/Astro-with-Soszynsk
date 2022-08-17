import math
from scipy.integrate import quad as integrate
import matplotlib.pyplot as plt
import numpy as np
def calk(f, a, b, dx):
    i = a
    s = 0
    while i <= b:
        s += f(i)*dx
        i += dx
    return s

def h(y,v,a):
    return math.exp(-y**2)/((v-y)**2+a**2)
def Hjer(v,a):
    return calk(lambda y:h(y,v,a),-10,10,0.01)*a/math.pi
def UnderINT1(v,a,c):
    return 1-math.exp(-c*Hjer(v,a))
def Wby2Lambda(a,vmx,c):#,dx):
   # return calk2(lambda x:UnderINT(x,a,C),0,vmx)
    x=integrate(lambda x: 1-math.exp(-c*Hjer(x,a)),0,vmx)#,dx)
    return x[0]


M=[]
indices=[]
indices2=[]
for i in np.arange(-1,4,0.05):
    if (i==0):
        print('nothing')
    else:
        indices.append(pow(10,i))
        indices2.append(i)
        #print(pow(10,i))
for i in indices:
    M.append(math.log10(Wby2Lambda(1,10000,i)))
    print(i)
plt.plot(indices2,M,color='b',label=r"$\alpha_0$=1")
print('2')
M.clear()
for i in indices:
    M.append(math.log10(Wby2Lambda(0.1,400,i)))
    print(i)
plt.plot(indices2,M,color='g',label=r"$\alpha_0$=0.1")
M.clear()
for i in indices:
    M.append(math.log10(Wby2Lambda(0.01,40,i)))
    print(i)
print('3')
plt.plot(indices2,M,color='r',label=r"$\alpha_0$=0.01")
M.clear()
for i in indices:
    M.append(math.log10(Wby2Lambda(0.001,40,i)))
    print(i)
print('3')
plt.plot(indices2,M,color='k',label=r"$\alpha_0$=0.001")
plt.legend()
plt.grid(b=True,which="major",color='#666666', linestyle='-',linewidth=0.2)
plt.show()
