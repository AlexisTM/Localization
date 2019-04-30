from .geometry import Point, Circle
from .methods import *

class Anchor:
    def __init__(self, ID, position):
        self.position = position
        self.ID = str(ID)

    def __str__(self):
        return 'Anchor ' + self.ID + ' @ ' + self.position.__str__()


class Target:
    def __init__(self, ID):
        self.position = None
        self.ID = str(ID)
        self.measures = []

    def __str__(self):
        if self.position is None:
            return 'Target ' + self.ID
        else:
            return 'Target ' + self.ID + ' @ Real position:' + self.position.__str__()

    def add_measure(self, a, d):
        self.measures.append((a, d))


class Project:
    def __init__(self, goal=[None, None, None]):
        self.anchors = {}
        self.targets = {}
        self.goal = goal

    def add_anchor(self, ID, position):
        try:
            self.anchors[ID]
            print(str(ID) + ':Anchor with same ID already exists')
            return
        except KeyError:
            a = Anchor(ID, Point(position))
            self.anchors[ID] = a
        return a

    def add_target(self, ID=None):
        try:
            self.targets[ID]
            print('Target with same ID already exists')
            return
        except:
            if ID:
                ID = str(ID)
            else:
                ID = 't' + str(len(self.targets))
            t = Target(ID)
            self.targets[ID] = t
        return t

    def solve(self, **kwargs):
        for target_id in self.targets.keys():
            target = self.targets[target_id]
            cA = []
            for tup in target.measures:
                landmark = tup[0]
                c = self.anchors[landmark].position
                d = tup[1]
                cA.append(Circle(c, d))
            target.position = lse(cA, goal=self.goal)
