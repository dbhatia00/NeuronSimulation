import scipy.integrate as integrate
import scipy.special as special
import math

t = 500 *pow(10,-3) #s
wavelength = 2000 * pow(10,-9) #m
ua = 0.502 #cm^-1, optical absorbtion coeff
k = 0.6 #W m^-1 K^-1
p = 1000 #kg/m^-3
c = 4188 # J kg^-1 K^-1
pi = 3.14
P0 = 10 * pow(10,-3) #W
R = 93.41 * pow(10,-6)#m
z = 164.56 * pow(10,-6)#m

P = P0 * math.exp(-ua*z)
tc = pow(R,2) *c* p /(4*k)
constantBeforeIntegral = (2* ua * P) / (p*c*pi*pow(R,2))

insideIntegral =.083393742376

print("deltaT = ", insideIntegral*constantBeforeIntegral)
print(constantBeforeIntegral)
print(P)
print(tc)
print(R)
