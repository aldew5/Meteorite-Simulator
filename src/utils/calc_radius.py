def calc_radius(temp: int, r):
    """ri = ro - 0.3 * K/sigmaT^3"""

    # nothing has ablated 
    if (temp == 0):
        return r

    ri = -1
    # calculate the inner radius
    if (temp > 1500):
        ri = r - 0.3 * 86* 10**8 /(5.67 * temp**3)

    # new radius
    if (ri < 0):
        return r
    
    return ri