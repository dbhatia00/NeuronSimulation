from neuron import h, gui
from matplotlib import pyplot
from matplotlib.pyplot import MultipleLocator
import mplcursors
import math

na = 0.075998  # Sodium conductance
k = 0.017005  # Potassium conductance
# Loop
for i in range(1):
    axon1 = h.Section()
    axon1.L = 10000
    axon1.diam = 25
    axon1.nseg = 200
    axon1.Ra = 5
    axon1.cm = 1
    axon1.insert('hh')   
    for seg in axon1:
        seg.hh.gnabar = na
        seg.hh.gkbar = k
        seg.hh.gl = 0.00014
        seg.hh.el = -65

    axon2 = h.Section()
    axon2.L = 10000
    axon2.diam = 25
    axon2.nseg = 200
    axon2.Ra = 5
    axon2.cm = 1
    axon2.insert('hh')
    for seg in axon2:
        seg.hh.gnabar = na
        seg.hh.gkbar = k
        seg.hh.gl = 0.00014
        seg.hh.el = -65

    i1 = h.IClamp(axon1(0.001))
    i1.delay = 100
    i1.dur = 1500
    i1.amp = 17.8

    i2 = h.IClamp(axon2(0.001))
    i2.delay = 100
    i2.dur = 1500
    i2.amp = 17.8

    t = h.Vector()
    v1 = h.Vector()
    v2 = h.Vector()
    t.record(h._ref_t)
    v1.record(axon1(0.55)._ref_v)
    v2.record(axon2(0.55)._ref_v)
    def turn_on():
        for time in range(196, 690):
                axon2(0.5475).hh.gl =  3.653*pow(10,-5)*(31.39 * math.exp((9.432*pow(10,-5)) * time) - (3.059*pow(10,6)) * math.exp(-.06376 * time))
                axon2(0.5525).hh.gl =  3.653*pow(10,-5)*(31.39 * math.exp((9.432*pow(10,-5)) * time) - (3.059*pow(10,6)) * math.exp(-.06376 * time))

    def turn_off():
        for time in range(690, 1700):
                axon2(0.5475).hh.gl = 6.81*pow(10,-6)*(6.742*pow(10,10) * math.exp(-.03253 * time) + (22.43) * math.exp(-5*pow(10,-5) * time))
                axon2(0.5525).hh.gl = 6.81*pow(10,-6)*(6.742*pow(10,10) * math.exp(-.03253 * time) + (22.43) * math.exp(-5*pow(10,-5) * time))

    h.finitialize(-65)
    h.CVode().event(200, turn_on)
    h.CVode().event(700, turn_off)
    h.continuerun(1700)

    # Define the derivative function simulate laser induced temp change in water 
    def difference(data_list):
        diff = list()
        for item in range(len(data_list) - 1):
            diff.append((data_list[item + 1] - data_list[item]) / 0.025)
        return diff

    ''' 
    # Phase Plot of the Action Potentials
    list_v1 = list(v1)
    list_v2 = list(v2)
    list_v3 = list_v1[66700:67600]  # Intercept a complete action potential
    list_v4 = list_v2[66500:69600]  # Intercept a complete action potential
    list_v5 = difference(list_v3)
    list_v6 = difference(list_v4)
    list_v7 = list_v1[66701:67600]  # Define the coordinate interval
    list_v8 = list_v2[66501:69600]  # Define the coordinate interval
    p1 = pyplot.plot(list_v7, list_v5, color='blue')
    p2 = pyplot.plot(list_v8, list_v6, color='red')
    pyplot.legend(p1 + p2, ['IR off', 'IR on'])
    pyplot.xlabel('Membrane potential (mV)')
    pyplot.ylabel('dv/dt (V/s)')
    pyplot.show()
    ''' 

    # Partial enlargement
    p1 = pyplot.plot(t, v1, color='blue')
    p2 = pyplot.plot(t, v2, color='red')
    pyplot.legend(p1 + p2, ['IR off', 'IR on'])
    pyplot.xlabel('Time (ms)')
    pyplot.ylabel('Membrane potential (mV)')
    pyplot.xlim(0, 2000)  # Define the coordinate interval
    mplcursors.cursor()  # Data cursor
    # Set coordinate scale
    x_major_locator = MultipleLocator(100)
    ax = pyplot.gca()
    ax.xaxis.set_major_locator(x_major_locator)
    pyplot.show()

    '''
    # Calculate the maximum attenuation of action potentials' amplitude under infrared radiation
    list_v1 = list(v1)
    amp1 = max(list_v1[28000:28400])
    list_v2 = list(v2)
    amp2 = max(list_v2[28000:28400])
    print(amp1, end=' ')
    print(amp2, end=' ')
    print(amp1 - amp2)
    '''

    '''
    # Export simulation data to a file saved in '.txt' format
    file1 = open('v1.txt', 'w')
    for j in list_v1:
        file1.write(str(j))
        file1.write('\n')
    file1.close()
    file2 = open('v2.txt', 'w')
    for j in list_v2:
        file2.write(str(j))
        file2.write('\n')
    file2.close()
    '''
