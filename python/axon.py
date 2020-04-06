from neuron import h, gui
from matplotlib import pyplot
from matplotlib.pyplot import MultipleLocator
import mplcursors

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

    i1 = h.IClamp(axon1(0.5))
    i1.delay = 100
    i1.dur = 1500
    i1.amp = 20

    i2 = h.IClamp(axon2(0.5))
    i2.delay = 100
    i2.dur = 1500
    i2.amp = 20

    t = h.Vector()
    v1 = h.Vector()
    v2 = h.Vector()
    t.record(h._ref_t)
    v1.record(axon1(0.53)._ref_v)
    v2.record(axon2(0.53)._ref_v)

    def turn_on():
        axon2(0.4975).hh.gl = 0.001225
        axon2(0.5025).hh.gl = 0.001225

    def turn_off():
        axon2(0.4975).hh.gl = 0.00014
        axon2(0.5025).hh.gl = 0.00014

    h.finitialize(-65)
    h.CVode().event(200, turn_on)
    h.CVode().event(700, turn_off)
    h.continuerun(1400)

    # Define the derivative function
    def difference(data_list):
        diff = list()
        for item in range(len(data_list) - 1):
            diff.append((data_list[item + 1] - data_list[item]) / 0.025)
        return diff

    
    # Phase Plot of the Action Potentials
    list_v1 = list(v1)
    list_v2 = list(v2)
    list_v3 = list_v1[27644:28744]  # Intercept a complete action potential
    list_v4 = list_v2[27450:28600]  # Intercept a complete action potential
    list_v5 = difference(list_v3)
    list_v6 = difference(list_v4)
    list_v7 = list_v1[27645:28744]  # Define the coordinate interval
    list_v8 = list_v2[27451:28600]  # Define the coordinate interval
    p1 = pyplot.plot(list_v7, list_v5, color='blue')
    p2 = pyplot.plot(list_v8, list_v6, color='red')
    pyplot.legend(p1 + p2, ['IR off', 'IR on'])
    pyplot.xlabel('Membrane potential (mV)')
    pyplot.ylabel('dv/dt (V/s)')
    pyplot.show()
    

    # Partial enlargement
    p1 = pyplot.plot(t, v1, color='blue')
    p2 = pyplot.plot(t, v2, color='red')
    pyplot.legend(p1 + p2, ['IR off', 'IR on'])
    pyplot.xlabel('Time (ms)')
    pyplot.ylabel('Membrane potential (mV)')
    pyplot.xlim(274, 288)  # Define the coordinate interval
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
