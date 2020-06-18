import scipy.integrate as integrate
import matplotlib.pyplot as plt
import math

def integrand(x, tempC, lilR, bigR):
	return (1/(1+2*(x/tempC))) * math.exp((-2*pow(lilR,2)) / (pow(bigR,2) * (1/(1+2*(x/tempC)))))

t = 500 *pow(10,-3) #s
wavelength = 1994 * pow(10,-9) #m
ua = 50 *100  #m^-1, optical absorbtion coeff
k = 0.6 #W m^-1 K^-1
p = 1000 #kg/m^-3
c = 4188 # J kg^-1 K^-1
pi = 3.14
P0 = [0 * pow(10,-3),5 * pow(10,-3),10 * pow(10,-3), 15 * pow(10,-3),20 * pow(10,-3)] #W // Array of power values
R = 93.41 * pow(10,-6)#m
z = 164.56 * pow(10,-6)#m
r = 25 * pow(10,-6) #m
dt = []
for powers in range(0,len(P0)):
	P = P0[powers] * math.exp(-ua*z)
	tc = pow(R,2) *c* p /(4*k)
	constantBeforeIntegral = (2* ua * P) / (p*c*pi*pow(R,2))
	
	insideIntegral = integrate.quad(integrand, 0, t, args = (tc,r, R))
	dt.append(insideIntegral[0]*constantBeforeIntegral)
	print("deltaT = ", insideIntegral[0]*constantBeforeIntegral, "C when P = " , P0[powers] , "W")

plt.plot(P0,dt)
plt.xlabel('Laser Power (W)')
plt.ylabel('Delta T (C)')
plt.grid(True)
slope = abs((dt[0] - dt[1]) / (P0[0] - P0[1])) * pow(10,-3)
s = 'slope = ' + str(slope) + ' C/mW'
plt.text(.0025,7,s)
plt.show()
