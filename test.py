import multilateration
from math import sqrt

P=multilateration.Project(goal=[None, None, 2.0])
# P=multilateration.Project()
P.add_anchor('anchor_A',(1,0,1))
P.add_anchor('anchor_B',(-1,0,1))
P.add_anchor('anchor_C',(1,1,1))

t = P.add_target()
t.add_measure('anchor_A',sqrt(2))
t.add_measure('anchor_B',sqrt(2))
t.add_measure('anchor_C',sqrt(3))
P.solve()

print(t.ID, str(t.position))
