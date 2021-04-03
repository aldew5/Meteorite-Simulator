from matplotlib import pyplot as plt
import math

"""assume meteroite is a sphere"""

ACCELERATION = 9.81
# volume = 4/3*pi*r^3, density estimate 3 tonnes per cubic metre
# estimated radius 10 km

MASS = 4/3 * math.pi* 10000**3
DENSITY = 1.2 #kg/m^3
DRAG = 0.5
A = math.pi * 10000 **2

# 20 km/s 20 000 m /s
v = 200000

THICKNESS = 10**5

epsilon = 0.01
time = 0
z = 0

k = DRAG * DENSITY*A/(2*MASS)

print(k)

v_t = plt.figure()
axes = v_t.add_subplot(111)
axes.set_ylabel("Position")
axes.set_xlabel("Time")

a, b, t = [], [], []

while z < THICKNESS:
    
    time += epsilon
    #print(z, v)
    z += v*epsilon + 1/2 *(ACCELERATION - k*v**2) * epsilon**2
    v += (ACCELERATION - k*v**2)*epsilon
    #print(z, v)

    a.append(z)
    b.append(v)
    t.append(time)



axes.plot(t, a)
plt.show()
    
                            
