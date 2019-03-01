import numpy as np
from .geometry import Point
from scipy.optimize import minimize
from .constants import MODE_2D, MODE_3D, MODE_2D5

def norm(A, B, mode=MODE_2D):
    if mode == MODE_2D:
        return ((A[0] - B[0]) ** 2 + (A[1] - B[1]) ** 2) ** .5
    elif mode == MODE_3D:
        return ((A[0] - B[0]) ** 2 + (A[1] - B[1]) ** 2 + (A[2] - B[2]) ** 2) ** .5
    else:
        raise Exception('Unknown')

def sum_error(x, c, r, mode):
    l = len(c)
    e = 0
    for i in range(l):
        e = e + (norm(x, c[i].std(), mode=mode) - r[i]) ** 2
    return e

def lse(cA, mode=MODE_2D, cons=True):
    l = len(cA)
    r = [w.r for w in cA]
    c = [w.c for w in cA]
    S = sum(r)
    W = [(S - w) / ((l - 1) * S) for w in r]
    p0 = Point(0, 0, 0)  # Initialized Point
    for i in range(l):
        p0 = p0 + W[i] * c[i]
    if mode == MODE_2D:
        x0 = np.array([p0.x, p0.y])
    elif mode == MODE_3D:
        x0 = np.array([p0.x, p0.y, p0.z])
    else:
        raise Exception('Mode not supported:' + mode)
    print('LSE Geolocating...')
    res = minimize(sum_error, x0, args=(c, r, mode), method='BFGS')
    ans = res.x
    return Point(ans)
