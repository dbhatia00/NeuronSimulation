import scipy.integrate as integrate
import matplotlib.pyplot as plt
import math

def integrand(x,tempC, lilR, bigR):
	#print(bigR, " ", lilR, " ", tempC, " ", x )
	c = ((1+2*(x/tempC)))
	
	expBit = (-2*pow(lilR,2)) / (pow(bigR, 2) * c)
	return (1/c)* math.exp(expBit)

t0 = [0,.1,.2,.3,.4,.5,.6,.7,.8,.9,1] #s
wavelength = 1994 * pow(10,-9) #m
ua = 73.9 *100  #m^-1, optical absorbtion coeff
k = 0.6 #W m^-1 K^-1
p = 1000 #kg/m^-3
c = 4184 # J kg^-1 K^-1
pi = 3.14
P0 = [0.005, .00692, .01 ,.0132, .015, .02] #W // Array of power values
R = 25* pow(10,-6)#m
z = 117.55 * pow(10,-6)#m
r = 25.18 * pow(10,-6) #m

for P in P0:
	dt = []
	tc = pow(R,2) *c* p /(4*k)

	for t in t0:
		P1 = P * math.exp(-ua*z)
		insideIntegral,error = integrate.quad(integrand, 0, t, args = (tc,r, R,))
		constantBeforeIntegral = (2* ua * P1) / (p*c*pi*pow(R,2))
		dt.append(insideIntegral*constantBeforeIntegral)

	plt.plot(t0, dt, label = (str(P1)[0:7] + 'W'))
	plt.xlabel('Time from laser firing (s)')
	plt.ylabel('Delta T (C)')
	plt.title('Peak Temperature Change over Time; Power Alteration')
	plt.grid(True)

	#s = 'Power On Surface = ' + str(P1)[0:6] + 'W'
	#plt.text(.4,max(dt)*.3,s)

	#s = 'Optical Absorbtion Coeff = ' + str(u)[0:4] + 'm^-1'
	#plt.text(.4,max(dt)*.2,s)

	#s = 'lambda = ' + str(wavelength*pow(10,9))[0:4] + 'nm'
	#plt.text(.4,max(dt)*.1,s)

plt.legend()
plt.show()
