from matplotlib import pyplot as plt
import math

"""assume meteroite is a sphere"""

# acceleration due to gravity
acceleration = 9.81
# volume = 4/3*pi*r^3, density estimate 3 tonnes per cubic metre
# estimated radius 10 km

# set constants
DENSITY = 1.2 #kg/m^3
DRAG = 0.5
A = math.pi * 10000 **2

def calc_g(position: int):
    """g = GM/r^2"""
    # mass of the earth
    m_planet = 5.972 * 10**24
    # radius of the earth plus the distance
    r = (6371 * 1000) + position

    return 6.67 * 10**-11 * m_planet / r**2


def calc_mass(temp: int, t: int):
    """Using the Knudsen-Langmuir equation"""
    p_vap = 10**(12.509-20014/temp)

    return -4 * math.pi * 0.001**2*p_vap*math.sqrt(1.4*10**-8/2*math.pi*1.38 * 10**-23 * temp) * t

def calc_k(mass: int):
    return DRAG * DENSITY*A/(2*mass)

    



# 20 km/s 20 000 m /s
v = 200

# atmosphere thickness
THICKNESS = 10**5

epsilon = 0.01
time = 0
z = THICKNESS



v_t = plt.figure()
axes = v_t.add_subplot(111)
axes.set_ylabel("Position")
axes.set_xlabel("Time")

m_t = plt.figure()
axes2 = m_t.add_subplot(111)
axes2.set_ylabel("Mass")
axes2.set_xlabel("Time")

a, b, c, t = [], [], [], []

mass = 4/3 * math.pi* 10000**3
temp = 0

while z > 0:
    
    time += epsilon
    acceleration = calc_g(z)

    k = DRAG * DENSITY*A/(2*mass)
    #print(k)
    # update position
    z -= v*epsilon + 1/2 *(acceleration - k*v**2) * epsilon**2
    # update velocity
    v += (acceleration - k*v**2)*epsilon

    # melting point of iron is 1538 deg C
    if (temp < 1538):
        temp += DRAG * DENSITY * A/2 * v**2
    mass += calc_mass(temp, time)
    #print(calc_mass(temp, time))

    #print(z)
    # save variables
    a.append(z)
    b.append(v)
    c.append(mass)
    t.append(time)



axes.plot(t, a)
axes2.plot(t, c)
plt.show()
    
                            
