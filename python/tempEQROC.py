import matplotlib.pyplot as plt

dt = [0,1.98119461758,2.26499613135,2.43134,2.549466]
t = [0,.25,.5,.75,1]

plt.scatter(t,dt)
plt.xlabel('Time (s)')
plt.ylabel('Temperature change over power (C/mW)')
plt.grid(True)
plt.show()
