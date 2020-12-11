import scipy.integrate as integrate
import matplotlib.pyplot as plt
import math

def integrand(x,tempC, lilR, bigR):
	#print(bigR, " ", lilR, " ", tempC, " ", x )
	c = ((1+2*(x/tempC)))
	
	expBit = (-2*pow(lilR,2)) / (pow(bigR, 2) * c)
	return (1/c)* math.exp(expBit)

t0 = [0,.25,.5,.75,1] #s
wavelength = 1994 * pow(10,-9) #m
ua = 73.9 *100  #m^-1, optical absorbtion coeff
k = 0.6 #W m^-1 K^-1
p = 1000 #kg/m^-3
c = 4184 # J kg^-1 K^-1
pi = 3.14
P0 = .0029 #W 
R = 25* pow(10,-6)#m
z = 117.55 * pow(10,-6)#m
r = 25 * pow(10,-6) #m
dt = []
tc = pow(R,2) *c* p /(4*k)

for t in t0:	
	insideIntegral,error = integrate.quad(integrand, 0, t, args = (tc,r, R,))
	P = P0 * math.exp(-ua*z)
	constantBeforeIntegral = (2* ua * P0) / (p*c*pi*pow(R,2))
	dt.append(insideIntegral*constantBeforeIntegral)

plt.scatter(t0,dt)
plt.xlabel('Time (s)')
plt.ylabel('Delta T (C)')
plt.grid(True)

s = 'Power = ' + str(P0) + 'W'
plt.text(.0,max(dt)*.60,s)

s = 'lambda = ' + str(wavelength*pow(10,9)) + 'nm'
plt.text(.00,max(dt)*.40,s)

plt.show()
