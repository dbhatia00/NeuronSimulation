import scipy.integrate as integrate
import matplotlib.pyplot as plt
import math
import numpy
from sklearn.metrics import mean_absolute_error

def integrand(x,tempC, lilR, bigR):
	#print(bigR, " ", lilR, " ", tempC, " ", x )
	c = ((1+2*(x/tempC)))
	
	expBit = (-2*pow(lilR,2)) / (pow(bigR, 2) * c)
	return (1/c)* math.exp(expBit)

def MAPE(a, f):
	error = 0
	for i in range(1,len(a)):
		error = error + (abs(a[i] - f[i])/(a[i]))
	return error/len(f)

t0 = numpy.linspace(0, .5, 100) #s
wavelength = 1994 * pow(10,-9) #m
ua = 107.8 *100  #m^-1, optical absorbtion coeff - OPTIMAL VAL = 107 CM^-1
#U0 = numpy.linspace(10*100, 120*100, 10)
k = 0.6 #W m^-1 K^-1
p = 1000 #kg/m^-3 - density of saline
c = 4184 # J kg^-1 K^-1
pi = 3.14
#P0 = [0.005, .00692, .01 ,.0132, .015, .02] #W // Array of power values
#P0 = numpy.linspace(.0045, .0060, 10) #OPTIMAL INITIAL POWER = 483 mW
P = .00483
#z = 117.55 * pow(10,-6)#m
Z0 = numpy.linspace(100 * pow(10,-6), 175 * pow(10,-6), 10)
r = 25 * pow(10,-6) #m - radius of fiber core, radius at beam waist

divAngle = ((wavelength / 1000) / (pi * r / 1000)) / 1000 #Half angle divergence of the 



time = numpy.linspace(200,700, 100)
actualy = []


for t in time: #experimental data
	actualy.append(31.39 * math.exp(9.432 * math.pow(10,-5) * t) - 3.059 * math.pow(10,6) * math.exp(-0.06376 * t))

base = actualy[0]
dy = []

for ay in actualy: #calculate the delta of experimental data
	dy.append(ay-base)

plt.plot(numpy.linspace(0,.5, 100), dy, label = 'EXPERIMENTAL')



for z in Z0: #approximations over target variable
	dt = []
	R =  r + z*math.tan(divAngle) #m - radius at axial distance
	tc = pow(R,2) *c* p /(4*k)	
	for t in t0:
		P1 = P * math.exp(-ua*z)
		insideIntegral,error = integrate.quad(integrand, 0, t, args = (tc,r, R,))
		constantBeforeIntegral = (2* ua * P1) / (p*c*pi*pow(R,2))
		dt.append(insideIntegral*constantBeforeIntegral)


	plt.plot(t0, dt, label = (str(z * pow(10,6))[0:7] + 'um' + ', error = ' + str(MAPE(dy,dt) * 100)[0:5]) + '%')

#set up grid
plt.xlabel('Time from laser firing (s)')
plt.ylabel('Delta T (C)')
plt.title('Peak Temperature Change over Time; Z Distance Alteration')
plt.grid(True)
plt.legend(title = 'Surface Power')
plt.show()
