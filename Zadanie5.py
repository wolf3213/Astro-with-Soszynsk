import math
import matplotlib.pyplot as plt
import numpy as np


#pierw.    Z   A  pot. jon.  g0  g1     x_i

#  H       1   1    13.54     2   1   0.7095
#  He      2   4    24.46     1   2   0.2774
#  O       8  16    13.55     9   4   0.0055
#  C       6  12    11.22     9   6   0.0021
#  Ne     10  20    21.47     1   6   0.0014
#  Fe     26  56     7.83    25  30   0.0011
#  N       7  14    14.48     4   9   0.00084
#  Si     14  28     8.15     9   6   0.00068
#  Mg     12  24     7.61     1   2   0.00059
#  S      16  32    10.36     9   4   0.00048

x=[0.7095,0.2774,0.0055,0.0021,0.00141,0.0011,0.00084,0.0068,0.00059,0.00048]
A=[1,4,16,12,20,56,14,18,24,32]
N_i=np.divide(x,A)
g0=[2,1,9,9,1,25,4,9,1,9]
g1=[1,2,4,6,6,30,9,6,2,4]
ch0=[13.54,24.46,13.55,11.22,21.47,7.83,14.48,8.15,7.16,10.36]
#N1byN0=[]#i+1 to i-ty pierwiastek
alfa_i=[]
PgbyPe=[]
indices=[]
LogP=[]
def sach(G1,G0,CHi,lP,T):
    return pow(10,-lP-CHi*5040/T+2.5*math.log10(T)-1.48+math.log10(2*G1/G0))
#for k in np.arange(-4,6,0.2):
   # LogP.append((pow(10,k)))

for t in np.arange(3000,11000,1000):
    for P in np.arange(-4,6,0.1):
        for i in np.arange(0,10):
            #N1byN0.append(sach(g1[i],g0[i],ch0[i],P,t))
            N1byN0=(sach(g1[i],g0[i],ch0[i],P,t))
            alfa_i.append(N1byN0/(1+N1byN0))
        E=sum(np.multiply(N_i,alfa_i))/sum(N_i)
        print(E)
        PgbyPe.append(math.log10(1/E+1))
        alfa_i.clear()
        indices.append(P)
    plt.plot(indices,PgbyPe,label=t)
    PgbyPe.clear()
    indices.clear()
plt.grid(b=True,which="major",color='#666666', linestyle='-',linewidth=0.2)
plt.legend()
plt.show()