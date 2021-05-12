import math
import scipy.integrate as integrate
import scipy.special as special
print("podaj temperature w[K]")
T=float(input())
print("podaj dolna granice[nm]")
a=float(input())
print("podaj górna granice[nm]")
b=float(input())
#a=400
#b=700
#T=310
d=6.62607015*299792458*pow(10,-2)/(a*T*1.380649)
c=6.62607015*299792458*pow(10,-2)/(b*T*1.380649)
result = integrate.quad(lambda x: x**2/(math.exp(x)-1),c,d)
result=result[0]
result=(result*T**3*2*3.1415*(1.380649)**3*10**17)/((2.998)**2*(6.62607015)**3)
print(result)