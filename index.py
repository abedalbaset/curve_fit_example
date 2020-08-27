import matplotlib.pyplot as plt
from scipy.optimize import curve_fit
import scipy as sy
import pylab as plb

#data = plb.loadtxt('data.dat')

#x = data[:,0]
#y= data[:,1]

x = [1,2,3,4,5]
y= [1,4,9,16,25]

def func(x, a, b, c):
  return a*x**b +c*x

p0 = sy.array([0.1,0.1,0.1])
coeffs, matcov = curve_fit(func, x, y, p0)


print("coeffs ",coeffs)
print("matcov ",matcov)


#yaj = func(x, coeffs[0], coeffs[1], coeffs[2])
#plt.plot(x,y,'x',x,yaj,'r-')
#plt.show()
