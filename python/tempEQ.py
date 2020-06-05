import scipy.integrate as integrate
import scipy.special as special
import math

t = 500 #ms
wavelength = 2000 #nm
ua = 0.502 #cm^-1, optical absorbtion coeff
k = 0.6 #W m^-1 K^-1
p = 1000 #kg/m^-3
c = 4188 # J kg^-1 K^-1
pi = 3.14
P0 = 10 #mW
R = 93.41 # um
z = 164.56 #um

P = P0 * math.exp(-ua*z)
tc = pow(R,2) *c* p /(4*k)
constantBeforeIntegral = (2* ua * P) / (p*c*pi*pow(R,2))

integralBit = 
