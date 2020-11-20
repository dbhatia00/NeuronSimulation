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
		diff = (abs(a[i] - f[i])/(a[i]))
		error = error + diff
	return error/len(a)

t0 = numpy.linspace(0, 1, 100) #s
wavelength = 1994 * pow(10,-9) #m
ua = 73.9 *100  #m^-1, optical absorbtion coeff
#U0 = numpy.linspace(10*100, 57*100, 4)
k = 0.6 #W m^-1 K^-1
p = 1000 #kg/m^-3
c = 4184 # J kg^-1 K^-1
pi = 3.14
#P0 = [0.005, .00692, .01 ,.0132, .015, .02] #W // Array of power values
P0 = numpy.linspace(.001, .01, 5)
#P = .00692
R = 25* pow(10,-6)#m
z = 117.55 * pow(10,-6)#m
#Z0 = numpy.linspace(1 * pow(10,-6), 200 * pow(10,-6), 10)
r = 25.18 * pow(10,-6) #m


time = numpy.linspace(200,700, 100)
actualy = []


for t in time:
	actualy.append(31.39 * math.exp(9.432 * math.pow(10,-5) * t) - 3.059 * math.pow(10,6) * math.exp(-0.06376 * t))

base = actualy[0]
dy = []
for ay in actualy:
	dy.append(ay-base)

plt.plot(numpy.linspace(0,1, 100), dy, label = 'EXPERIMENTAL')



for P in P0:
	dt = []
	tc = pow(R,2) *c* p /(4*k)

	for t in t0:
		P1 = P * math.exp(-ua*z)
		insideIntegral,error = integrate.quad(integrand, 0, t, args = (tc,r, R,))
		constantBeforeIntegral = (2* ua * P1) / (p*c*pi*pow(R,2))
		dt.append(insideIntegral*constantBeforeIntegral)


	plt.plot(t0, dt, label = (str(P1)[0:7] + 'W' + ', error = ' + str(MAPE(actualy,dt) * 100)[0:5]) + '%')


plt.xlabel('Time from laser firing (s)')
plt.ylabel('Delta T (C)')
plt.title('Peak Temperature Change over Time; Initial Power Alteration')
plt.grid(True)
plt.legend(title = 'Surface Power')
plt.show()
