import numpy as np
from scipy.optimize import minimize
from .geometry import Point, Circle
from time import time

from sys import version_info
if (version_info > (3, 0)):
    xrange = range


class Anchor(object):
    def __init__(self, ID, position, measure = None):
        self.position = position
        self.ID = str(ID)
        self.last_seen = time()
        self.measure = None

    @property
    def position(self):
        return self._position

    @position.setter
    def position(self, position):
        self._position = Point(position)

    def add_measure(self, data):
        self.measure = data
        self.last_seen = time()

    def valid(self, now = None):
        if now is None:
            now = time()
        if self.measure is None:
            print("No measure yet... " + str(self))
            return False
        if now - self.last_seen > 0.5:
            print("Last seen is too great! " + str(self.last_seen))
            return False
        return True

    def get(self):
        return Circle(self.position, self.measure)

    def __str__(self):
        return 'Anchor ' + self.ID + ' @ ' + self.position.__str__()


class Project(object):
    def __init__(self, goal=[None, None, None]):
        self.anchors = {}
        self.goal = goal
        self.last_result = Point(0,0,0)

    def add_anchor(self, ID, position):
        """Add a certain ID"""
        if ID in self.anchors:
            self.anchors[ID].position = position
        else:
            self.anchors[ID] = Anchor(ID, position)

    def add_measure_id(self, ID, measure):
        """Add a measurement for a certain anchor ID"""
        if ID in self.anchors:
            self.anchors[ID].add_measure(measure)
        else:
            print("anchor " + str(ID) + " does not exist yet")

    def add_measure(self, position, measure):
        """Distance measurement from an anchor position"""
        ID = str(position)

        if ID not in self.anchors:
            self.anchors[ID] = Anchor(ID, position, measure)
        else:
            self.anchors[ID] = measure

    def solve(self):
        cA = []
        for ID, anchor in self.anchors.items():
            if anchor.valid():
                cA.append(anchor.get())
        return self.lse(cA)

    def cost_function(self, x, c, r):
        e = 0
        # Force an axis
        # print x
        # # This force an axis value
        # for i, value in enumerate(goal):
        #     if value is not None:
        #         x[i] = value

        # current = [0,0,0]
        # for i, value in enumerate(goal):
        #     if value is not None:
        #         current[i] = value
        #     else:
        #         current[i] = x[i]

        for i in xrange(len(c)):
            e += (c[i].dist(x)- r[i]) ** 2
        return e

    def lse(self, cA):
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
        p0 = self.last_result  # Initialized Point
        for i in range(l):
            # p0 += Normalized distance * centers
            print(p0, W[i], c[i])
            p0 = p0 + W[i] * c[i]
            x0 = np.array([p0.x, p0.y, p0.z])
        print('LSE Geolocating...')
        # self.cost_function = the function to be minimized
        # x0 = the initial estimation that gets iterated
        # Extra arguments: 
        #   c = Point(), anchor positions
        #   r = all measurements
        for i, value in enumerate(self.goal):
            if value is not None:
                x0[i] = value

        result = minimize(self.cost_function, x0, args=(c, r), method='BFGS')
        ans = list(result.x)
        return Point(ans)

