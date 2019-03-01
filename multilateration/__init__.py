from .geometry import Point, Circle
from .methods import *

class Anchor:
    def __init__(self, ID, loc):
        self.loc = loc
        self.ID = str(ID)

    def __str__(self):
        return 'Anchor ' + self.ID + ' @ ' + self.loc.__str__()


class Target:
    def __init__(self, ID):
        self.loc = None
        self.ID = str(ID)
        self.measures = []

    def __str__(self):
        if self.loc is None:
            return 'Target ' + self.ID
        else:
            return 'Target ' + self.ID + ' @ Real Location:' + self.loc.__str__()

    def add_measure(self, a, d):
        self.measures.append((a, d))


class Project:
    def __init__(self, goal=[None, None, None]):
        self.AnchorDic = {}
        self.TargetDic = {}
        self.goal = goal

    def add_anchor(self, ID, loc):
        try:
            self.AnchorDic[ID]
            print(str(ID) + ':Anchor with same ID already exists')
            return
        except KeyError:
            a = Anchor(ID, Point(loc))
            self.AnchorDic[ID] = a
        return a

    def add_target(self, ID=None):
        try:
            self.TargetDic[ID]
            print('Target with same ID already exists')
            return
        except:
            if ID:
                ID = str(ID)
            else:
                ID = 't' + str(len(self.TargetDic))
            t = Target(ID)
            self.TargetDic[ID] = t
        return t

    def solve(self, **kwargs):
        for tID in self.TargetDic.keys():
            tar = self.TargetDic[tID]
            cA = []
            for tup in tar.measures:
                landmark = tup[0]
                c = self.AnchorDic[landmark].loc
                d = tup[1]
                cA.append(Circle(c, d))
            tar.loc = lse(cA, goal=self.goal)
