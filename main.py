from matplotlib import pyplot as plt
import math

"""assume meteroite is a sphere"""

# acceleration due to gravity
acceleration = 9.81
# volume = 4/3*pi*r^3, density estimate 3 tonnes per cubic metre
# estimated radius 10 km

def calc_g(position: int):
    """g = GM/r^2"""
    # mass of the earth
    m_planet = 5.972 * 10**24
    # radius of the earth plus the distance
    r = (6371 * 1000) + position

    return 6.67 * 10**-11 * m_planet / r**2
    

# set constants
MASS = 4/3 * math.pi* 10000**3
DENSITY = 1.2 #kg/m^3
DRAG = 0.5
A = math.pi * 10000 **2

# 20 km/s 20 000 m /s
v = 200000

# atmosphere thickness
THICKNESS = 10**5

epsilon = 0.01
time = 0
z = THICKNESS

# constant used in multiple calculations
k = DRAG * DENSITY*A/(2*MASS)


v_t = plt.figure()
axes = v_t.add_subplot(111)
axes.set_ylabel("Position")
axes.set_xlabel("Time")

a, b, t = [], [], []

while z > 0:
    
    time += epsilon
    acceleration = calc_g(z)
    print(acceleration)

    # update position
    z -= v*epsilon + 1/2 *(acceleration - k*v**2) * epsilon**2
    # update velocity
    v += (acceleration - k*v**2)*epsilon

    # save variables
    a.append(z)
    b.append(v)
    t.append(time)



axes.plot(t, a)
plt.show()
    
                            
