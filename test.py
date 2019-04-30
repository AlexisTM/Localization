import multilateration
from math import sqrt

P=multilateration.Project(goal=[None, None, 2.0]) # To fix that the resulting height should be 2 meters
# P=multilateration.Project() # for 3D, simply do not set a goal
P.add_anchor('anchor_A',(1,0,1))
P.add_anchor('anchor_B',(-1,0,1))
P.add_anchor('anchor_C',(1,1,1))

P.add_measure_id('anchor_A',sqrt(2))
P.add_measure_id('anchor_B',sqrt(2))
P.add_measure_id('anchor_C',sqrt(3))
print(P.solve())
