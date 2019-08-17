from matplotlib import pyplot as plt
import numpy as np
from PIL import Image, ImageTk

'''
Izhikevich Neural Model:
Izhikevich developed a simple, semiempirical model of cortical neurons. 
The properties of each neuron are controlled by 4 parameters, plus a constant current input.There are two state variables:
v is the membrane potential potential and u is the membrane recovery variable.

dv/dt = 0.04v^2 + 5v + 140 - u + I
du/dt = a(bv - u)

if v = 30mv,
then v <- c, u <- u + d
'''

# the init value of membrane potential (mV)
v_init = -87
# the interval between v(k) and v(k+1) (ms)
h = 0.1

'''
LTS:(0.02, 0.25, -65, 2)
TC:(0.02, 0.25, -65, 0.05)
RS:(0.02, 0.2, -65, 8)
IB:(0.02, 0.2, -55, 4)
CH:(0.02, 0.2, -50, 2)
RZ:(0.1, 0.26, -65, 2)
FS:(0.1, 0.2, -65, 2)
'''

# a, b, c, d
parameters = (0.02, 0.25, -65, 0.05)

a = parameters[0]
b = parameters[1]
c = parameters[2]
d = parameters[3]

v = v_init
u = -20
I = 0.15

data_v = list()
data_u = list()
scale = 1000

for i in range(scale):
    u += a*(b*v - u)*h
    v += (0.04*v**2 + 5*v + 140 - u + I)*h
    if v >= 30:
        v = c
        u += d 
    data_v.append(v)
    data_u.append(u)

data_x = np.arange(0, scale/10, 0.1)
print(data_v)
# plt.title("LTS Neuron Simulation Demo")
plt.title("TC Neuron Simulation Demo")
# plt.title("RS Neuron Simulation Demo")
# plt.title("IB Neuron Simulation Demo")
# plt.title("CH Neuron Simulation Demo")
# plt.title("RZ Neuron Simulation Demo")
# plt.title("FS Neuron Simulation Demo")
plt.xlabel("t/ms")
plt.plot(data_x, data_v)
plt.plot(data_x, data_u)
plt.show()

