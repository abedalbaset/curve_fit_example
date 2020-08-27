import matplotlib.pyplot as plt
from scipy.optimize import curve_fit
import scipy as sy
import pylab as plb

#data = plb.loadtxt('data.dat')

#x = data[:,0]
#y= data[:,1]

x = [1,2,3,4,5]
y= [1,4,9,16,25]

def func(x, a,b,d):
    # -*- coding: utf-8 -*-

    e1=a*x**b
    e2=d
    equation=e1+e2
    return equation

p0 = sy.array([1,1,1])
coeffs, matcov = curve_fit(func, x, y, p0)


print("coeffs ",coeffs)
print("matcov ",matcov)

arrinputs=[]
arroutputs=[]

for c in range(0,100):
    yaj = func(c, coeffs[0], coeffs[1], coeffs[2])
    arrinputs.append(c)
    arroutputs.append(yaj)

print("arrinputs ",arrinputs)
print("arroutputs ",arroutputs)
#markers_on = [12, 17, 18, 19]
plt.plot(arrinputs, arroutputs, '-bD', markevery=y)

#plt.plot(x,y,'x',x,'r-')
#plt.plot(arrinputs,arroutputs)
plt.show()
