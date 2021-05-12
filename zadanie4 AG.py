import math
import scipy.integrate as integrate
import matplotlib.pyplot as plt
import numpy as np
#pierwiastek bor
def sach(Gi,gi,ci,lP,T):
    return -lP-ci*5040/T+2.5*math.log10(T)-1.48+math.log10(2*Gi/gi)
def N1byN0(lP,T):
    return 10**(sach(g1,g0,c0,lP,T))
def N2byN1(lP,T):
    return 10**(sach(g2,g1,c1,lP,T))
def N3byN2(lP,T):
    return 10**(sach(g3,g2,c2,lP,T))
def N4byN3(lP,T):
    return 10**(sach(g4,g3,c3,lP,T))
def sum(lP,T):
    return (1+N1byN0(lP,T)+N2byN1(lP,T)*N1byN0(lP,T)+N3byN2(lP,T)*N2byN1(lP,T)*N1byN0(lP,T)+N4byN3(lP,T)*N3byN2(lP,T)*N2byN1(lP,T)*N1byN0(lP,T))
def N0byN(lP,T):
    return 1/ sum(lP, T)
def N1byN(lP,T):
    return N1byN0(lP,T)/sum(lP,T)
def N2byN(lP,T):
    return N2byN1(lP, T)*N1byN0(lP,T) / sum(lP, T)
def N3byN(lP,T):
    return N3byN2(lP,T)*N1byN0(lP,T)*N2byN1(lP,T)/sum(lP,T)
def N4byN(lP,T):
    return 1-N3byN(lP,T)-N2byN(lP,T)-N1byN(lP,T)-N0byN(lP,T)

g0=6
g1=1
g2=2
g3=1
g4=2
c0=8.3
c1=25.15
c2=37.92
c3=259.30
c4=340.13
M=[]
N=[]
indices = []
indices2 = []
for i in np.arange(1,100000,10):
    M.append(N0byN(1,i))
    indices.append(i)
plt.plot(indices,M,color='b',label=r"$\alpha_0$")
M.clear()
indices.clear()
for i in np.arange(1,100000,10):
    M.append(N1byN(1,i))
    indices.append(i)
plt.plot(indices,M,color='r',label=r"$\alpha_1$")
M.clear()
indices.clear()
for i in np.arange(1,100000,10):
    M.append(N2byN(1,i))
    indices.append(i)
plt.plot(indices,M,color='g',label=r"$\alpha_2$")
M.clear()
indices.clear()
for i in np.arange(1,100000,10):
    M.append(N3byN(1,i))
    indices.append(i)
plt.plot(indices,M,color='y',label=r"$\alpha_3$")
M.clear()
indices.clear()
for i in np.arange(1,100000,10):
    M.append(N4byN(1,i))
    indices.append(i)
plt.plot(indices,M,color='k',label=r"$\alpha_4$")








plt.grid(b=True,which="major",color='#666666', linestyle='-',linewidth=0.2)
plt.xlabel('T',fontsize=16)
plt.ylabel(r"$\alpha_j$",fontsize=16)
plt.title(r'Rysunek dla $\log{P_{e}}=1$')
plt.legend()
plt.show()