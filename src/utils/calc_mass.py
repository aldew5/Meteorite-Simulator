import math

def calc_mass(temp: int, t: int, r_o: int):
    """Using the Knudsen-Langmuir equation to calculate mass loss due to ablation"""
    #print(temp)
    p_vap = 10**(12.509-20014/temp)

    return -4 * math.pi * r_o**2*p_vap*math.sqrt(1.4*10**-8/2*math.pi*1.38 * 10**-23 * temp) * t
