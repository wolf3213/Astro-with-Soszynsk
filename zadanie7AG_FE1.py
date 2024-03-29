import math
import scipy.integrate as integrate
from scipy.optimize import minimize
import matplotlib.pyplot as plt
import numpy as np
import random
import time
from scipy.optimize import curve_fit
   #5243.78   4.257  -1.150   82   63   78   97   92  104   99   81   84   98
   #5288.53   3.695  -1.508   81   64   81   97   92  102   99   85   83   98
   #5294.55   3.640  -2.860   36   16   30   48   41   57   52   32   34   49
   #5326.15   3.570  -2.071   65   39   61   85   78   97   84   66   65   85
   #5373.71   4.474  -0.737   76   58   76   94   92   98   96   80   80   91
   #5379.57   3.680  -1.514   84   67   84  103   99  113  104   84   86  105
   #5386.34a   4.155  -1.719   53   33   50   69   65   76   72   50   53   67
   #5417.04   4.416  -1.424   52   30   48   70   66   74   71   54   52   68
   #5473.90   4.155  -0.749   95   81   96  117  116  120  119  107  103  114
   #5539.29   3.642  -2.660   42   21   40   55   54   67   64   41   43   58
   #5543.94   4.218  -1.103   79   63   81   94   97  102   99   83   82   95
   #5546.51a   4.372  -1.310   67   50   68   90   89   99   92   77   73   89
   #5560.22   4.435  -1.051   67   50   67   81   80   88   80   70   71   82
   #5618.64   4.209  -1.275   67   48   65   83   81   86   84   69   71   81
   #5619.59   4.387  -1.510   55   31   49   73   65   83   76   52   53   72
   #5633.95   4.992  -0.333   76   58   76   95   94   99   97   82   80   91
   #5638.26   4.221  -0.755   94   77   95  115  111  123  117   97   99  114
   #5661.35   4.280  -1.756   44   21   38   60   55   70   63   43   43   58
   #5662.52   4.178  -0.573  109   91  107  127  126  136  131  113  113  126
   #5679.03   4.652  -0.727   71   51   70   88   87   91   88   74   74   85
   #5680.24   4.187  -2.379   25   11   22   39   34   47   43   25   26   38
   #5705.47   4.300  -1.355   58   35   56   74   69   80   77   56   60   73
   #5731.77   4.257  -1.130   79   57   74   99   92  103   96   79   81   94
   #5741.86   4.257  -1.672   51   29   47   73   64   74   69   52   52   66
   #5752.04  4.549  -0.944   69   51   68   88   83   89   87   72   73   84
   #5775.09   4.221  -1.297   79   61   78   98   91  102   97   83   81   95
   #5778.46   2.588  -3.430   62   34   58   76   69   88   88   55   59   81
   #5784.66   3.400  -2.530   58  ...   49   73   65   82   77   49   51   70
   #5806.72   4.608  -0.845   68   50   68   90   88   94   90   73   73   85
   #5809.22a   3.884  -1.583   81   53   75   99   94  109  106   75   81   99
   #5811.92   4.143  -2.374   25   11   24   36   33   42   39   21   25   35
   #5855.08a   4.610  -1.478   37   18   34   56   50   60   53   41   41   52
   #5862.35   4.549  -0.343   97   79   98  122  116  122  117  103  104  112
   #5905.68   4.652  -0.763   74   51   69   91   86   94   89   73   75   86
   #5909.98   3.210  -2.587   72   44   69  101   90  102   97   78   74   91
   #5916.25   2.454  -2.834   99   73   95  109  106  131  123   92   99  118
   #5927.80   4.652  -1.090   56   38   54   73   71   72   74   58   60   70
   #6027.06   4.076  -1.089   88   68   85  111  103  111  107   96   92  105
   #6056.01   4.733  -0.443   82   66   83  103  101  105  102   88   87   99
   #6082.72   2.220  -3.573   78   52   76   91   84  108  104   70   76   98
   #6120.24   0.915  -5.970   43   14   33   47   37   72   69   25   33   62
   #6151.62   2.180  -3.330   93   71   92  104  102  120  121   85   94  116
def mymodel(x,a,b):
    return a*x+b

lmb=[5243.78,5288.53,5294.55,5326.15,5373.71,5379.57,5386.34,5417.04,5473.90,5539.29,5543.94,5546.51,5560.22,5618.64,5619.59,5633.95,5638.26,5661.35,5662.52,5679.03,5680.24,5705.47,5731.77,5741.86,5752.04,5775.09,5778.46,5784.66,5806.72,5809.22,5811.92,5855.08,5862.35,5905.68,5909.98,5916.25,5927.80,6027.06,6056.01,6082.72,6120.24,6151.62]
print(len(lmb))
Chi_d=[4.257,3.695,3.640,3.570,4.474,3.680,4.155,4.416,4.155,3.642,4.218,4.372,4.435,4.209,4.387,4.992,4.221,4.280,4.178,4.652,4.187,4.300,4.257,4.257,4.549,4.221,2.588,3.400,4.608,3.884,4.143,4.610,4.549,4.652,3.210,2.454,4.652,4.076,4.733,2.220,0.915,2.180]
print(len(Chi_d))
lgdf=[-1.150,-1.508,-2.860,-2.071,-0.737,-1.514,-1.719,-1.424,-0.749,-2.660, -1.103,-1.310,-1.051, -1.275, -1.510, -0.333,-0.755,-1.756,-0.573,-0.727,-2.379,-1.355,-1.130, -1.672, -0.944,-1.297,-3.430,-2.530, -0.845,-1.583,-2.374,-1.478,-0.343,-0.763,-2.587,-2.834,-1.090,-1.089,-0.443,-3.573,-5.970,-3.33   ]
print(len(lgdf))
W=[ 82,81,36,65,76,84,53,52,95,42,79,67,67,67,55,76,94,44,109,71,25,58,79,51,69,79,62,58,68,81,25,37,97,74,72,99,56,88,82,78,43,93]
print(len(W))
gdf=[]
for x in lgdf:
    gdf.append(10**x)
gdflmb=np.multiply(gdf,lmb)
Wbyl=np.divide(W,lmb)
loggflmb=np.log10(gdflmb)
logWbyl=np.log10(Wbyl)
plt.plot(Chi_d,logWbyl-loggflmb,'bo')
Y=np.array(logWbyl-loggflmb)
X=np.array(Chi_d)
popt, pcov = curve_fit(mymodel, X,Y)
print('a wynosi:' )
a=popt[0]
print(a)
print('b wynosi')
b=popt[1]
print(b)
plt.plot(X,mymodel(X,*popt))
plt.show()
S_x=sum(X)
X2=[]
for i in X:
   X2.append(i**2)
S_xx=sum(X2)
delta=42*S_xx-(S_x)**2
k=[]
for i in np.arange(0,41):
    k.append((Y[i]-a*X[i]-b)**2)
sigma_y2=sum(k)
print('sigma_a kwadrat wynosi:')
sigma_a2=sigma_y2/40*42/delta
print(sigma_a2)
print('theta wynosi')
print(-a)
print('tw wynosi')
print(5040/-a)
print('sigma_tw wynosi')
print(5040/a**2*math.sqrt(sigma_a2))