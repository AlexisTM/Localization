#!/usr/bin/env python
# -*- coding: utf-8 -*-

from multilateration import Engine
from math import sqrt

engine = Engine(goal=[None, None, 2.0]) # To fix that the resulting height should be 2 meters
# P=multilateration.Project() # for 3D, simply do not set a goal
engine.add_anchor('anchor_A',(1,0,1))
engine.add_anchor('anchor_B',(-1,0,1))
engine.add_anchor('anchor_C',(1,1,1))

engine.add_measure_id('anchor_A',sqrt(2))
engine.add_measure_id('anchor_B',sqrt(2))
engine.add_measure_id('anchor_C',sqrt(3))
print(engine.solve())
