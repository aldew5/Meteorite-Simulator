from matplotlib import pyplot as plt
import math

"""
Assumptions
- Meteroite is a sphere
- Meteroite has uniform density
- All lost energy goes into heating the meteroid (not the air)


All units are SI
Meteorite is Taenite
"""


# acceleration due to gravity
acceleration = 9.81
# volume = 4/3*pi*r^3, density estimate 3 tonnes per cubic metre
# estimated radius 7.5 km

# set constants
THICKNESS = 480000
DENSITY = 8000 #kg/m^3
DRAG = 0.5


area = math.pi * 7500 **2
R = 7500 #m

def calc_radius(temp: int, r: float):
    """ri = ro - 0.3 * K/sigmaT^3"""
    if (temp == 0):
        return r
    # subtract the ablated section from the radius
    ri = r - 0.3 * 86/((5.67 * 10**-8) * temp**3)
    #print("TERM:DLKJF:", 0.3 * 86/((5.67 * 10**-8) * temp**3))
    #print("INNER", ri)
    return r - (r-ri)
    
def calc_g(position: int):
    """g = GM/r^2"""
    # mass of the earth
    m_planet = 5.972 * 10**24
    # radius of the earth plus the distance
    r = (6371 * 1000) + position

    return 6.67 * 10**-11 * m_planet / r**2


def calc_mass(temp: int, t: int):
    """Using the Knudsen-Langmuir equation to calculate mass loss due to ablation"""
    #print(temp)
    p_vap = 10**(12.509-20014/temp)

    return -4 * math.pi * 0.001**2*p_vap*math.sqrt(1.4*10**-8/2*math.pi*1.38 * 10**-23 * temp) * t

def calc_k(mass: int, area: float):
    
    return DRAG * DENSITY*area/(2*mass)

    



# 200 m /s
v = 200
epsilon = 0.1
time = 0
z = THICKNESS

# velocity-time graph
v_t = plt.figure()
axes = v_t.add_subplot(111)
axes.set_ylabel("Position")
axes.set_xlabel("Time")

# mass-time graph
m_t = plt.figure()
axes2 = m_t.add_subplot(111)
axes2.set_ylabel("Mass")
axes2.set_xlabel("Time")

a, b, c, t = [], [], [], []

# initial mass as a product of volume and density 
mass = 4/3 * math.pi* 10000**3
temp = 0

while z > 0:
    
    time += epsilon
    # update graviational acceleration
    acceleration = calc_g(z)


    # update the area
    radius = calc_radius(temp, R)
    area = math.pi * radius **2

    # udpate the constant k
    k = calc_k(mass, area)
    
    # update position
    #print("TERM 1", v*epsilon, "TERM 2: ", 1/2 *(acceleration - k*v**2) * epsilon**2)
    z -= (v*epsilon + (acceleration - k*v**2)/(4*mass) * epsilon**2)
    # update velocity
    v += (acceleration - (k*v**2)/mass)*epsilon
    #print("V",v)

    #print("V and Z", v, z)

    # melting point of iron is 1538 deg C
    # increase temperature until the melting point is reached
    if (temp < 1500):
        temp += DRAG * DENSITY * area/2 * v**2
    mass += calc_mass(temp, time)
   
    # save variables
    a.append(z)
    b.append(v)
    c.append(mass)
    t.append(time)

    #print('z:', z)



axes.plot(t, a)
axes2.plot(t, c)
plt.show()
    
                          
