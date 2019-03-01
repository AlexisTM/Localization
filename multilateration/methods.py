import numpy as np
from .geometry import Point
from scipy.optimize import minimize
from .constants import MODE_2D, MODE_3D, MODE_2D5
from math import sqrt

def cost_function(x, c, r):
    e = 0
    for i in xrange(len(c)):
        e += (c[i].dist(x)- r[i]) ** 2
    return e

def lse(cA):
    # cA is a cicle array [Circle(), Circle()] representing measurements
    # l = number of circles
    l = len(cA)
    # r = radiuses of the circles (distance measured)
    r = [w.r for w in cA]
    # c = Point(), center of the circles (anchor position)
    c = [w.c for w in cA]
    # S = the sum of all radiuses
    S = sum(r)
    # W = Normalized 1/distances [(Sum - distance) / (Nmeasures-1)*Sum] 
    W = [(S - w) / ((l - 1) * S) for w in r]
    p0 = Point(0, 0, 0)  # Initialized Point
    for i in range(l):
        # p0 += Normalized distance * centers
        p0 = p0 + W[i] * c[i]
        x0 = np.array([p0.x, p0.y, p0.z])
    print('LSE Geolocating...')
    # cost_function = the function to be minimized
    # x0 = the initial estimation that gets iterated
    # Extra arguments: 
    #   c = Point(), anchor positions
    #   r = all measurements
    result = minimize(cost_function, x0, args=(c, r), method='BFGS')
    ans = list(result.x)
    return Point(ans)
