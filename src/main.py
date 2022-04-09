from matplotlib import pyplot as plt
import math
from utils.calc_gravity import calc_g
from utils.calc_radius import calc_radius
from utils.calc_mass import calc_mass

"""
Assumptions
- Meteorite is a sphere
- Meteroite has uniform density
- All lost energy goes into heating the meteoroid (not the air)

All units are SI
Meteorite is Taenite
"""

# parameters to vary
initial_radius = 8000 #m
epsilon = 0.015

# acceleration due to gravity
acceleration = 9.81
# volume = 4/3*pi*r^3, density estimate 3 tonnes per cubic metre
# estimated radius 7.5 km

# set constants
THICKNESS = 480000
DENSITY = 8385 #kg/m^3
DRAG = 0.5

area = math.pi * 7417.5 **2

def calc_k(mass: int, area: float):
    #print("K", DRAG, DENSITY, area, 2 * mass)
    return DRAG * DENSITY*area/(2*mass)


# 200 m /s
v = 1
time = 0
z = THICKNESS

# velocity-time graph
ke_t = plt.figure()
axes = ke_t.add_subplot(111)
axes.set_ylabel("Radius (m)")
axes.set_xlabel("Time (s)")

# mass-time graph
m_t = plt.figure()
axes2 = m_t.add_subplot(111)
axes2.set_ylabel("Mass (kg)")
axes2.set_xlabel("Time (s)")

a, b, c, t = [], [], [], []

# initial mass as a product of volume and density 
mass = 4/3 * math.pi* initial_radius**3
temp = 0

radius = initial_radius
count = 0

while z > 0:
    time += epsilon
    count += epsilon
    # update graviational acceleration
    acceleration = calc_g(z)

    # update the area and radius
    if (count >= 0.1):
        radius = calc_radius(temp, radius)
        count = 0
        
    area = math.pi * radius **2

    # udpate the constant k
    k = calc_k(mass, area)
    
    # update position
    z -= (v*epsilon + (acceleration - k*v**2)/(4*mass) * epsilon**2)
    delta_z = v*epsilon + (acceleration - k*v**2)/(4*mass) * epsilon**2
    # update velocity
    v += (acceleration - (k*v**2)/mass)*epsilon

    # melting point of taeunite is 1500 deg C
    # increase temperature until the melting point is reached
    if (temp < 2863):
        temp += DRAG * DENSITY * area/2 * delta_z* v**2/(450*mass)
    
    mass += calc_mass(temp, time, radius)

    # save variables
    a.append(radius)
    b.append(v)
    c.append(mass)
    t.append(time)

axes.plot(t, a)
axes2.plot(t, c)
plt.show()
    
                          
