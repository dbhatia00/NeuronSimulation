import scipy.integrate as integrate
import matplotlib.pyplot as plt
import math

def integrand(x,tempC, lilR, bigR):
	#print(bigR, " ", lilR, " ", tempC, " ", x )
	c = ((1+2*(x/tempC)))
	
	expBit = (-2*pow(lilR,2)) / (pow(bigR, 2) * c)
	return (1/c)* math.exp(expBit)

t0 = [1] #s
wavelength = 1994 * pow(10,-9) #m
ua = 73.9 *100  #m^-1, optical absorbtion coeff
k = 0.6 #W m^-1 K^-1
p = 1000 #kg/m^-3
c = 4184 # J kg^-1 K^-1
pi = 3.14
P0 = [0 * pow(10,-3),5 * pow(10,-3),10 * pow(10,-3), 15 * pow(10,-3),20 * pow(10,-3)] #W // Array of power values
R = 25* pow(10,-6)#m
z = 117.55 * pow(10,-6)#m
r = 25 * pow(10,-6) #m

for t in t0:
	dt = []
	tc = pow(R,2) *c* p /(4*k)
	insideIntegral,error = integrate.quad(integrand, 0, t, args = (tc,r, R,))

	for powers in P0:
		P = powers * math.exp(-ua*z)
		
		constantBeforeIntegral = (2* ua * P) / (p*c*pi*pow(R,2))
		dt.append(insideIntegral*constantBeforeIntegral)
		#print("Integrand " , insideIntegral)
		#print("deltaT = ", insideIntegral*constantBeforeIntegral, "C when P = " , powers , "W")

	#print('Thermal time constant ' , tc)

	plt.plot(P0,dt)
	plt.xlabel('Laser Power (W)')
	plt.ylabel('Delta T (C)')
	plt.grid(True)

	slope = abs((dt[0] - dt[1]) / (P0[0] - P0[1])) * pow(10,-3)
	s = 'slope = ' + str(slope) + ' C/mW'
	plt.text(.00,max(dt)*.80,s)

	s = 'time = ' + str(t) + 's'
	plt.text(.0,max(dt)*.60,s)

	s = 'lambda = ' + str(wavelength*pow(10,9)) + 'nm'
	plt.text(.00,max(dt)*.40,s)

	plt.show()
