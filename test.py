import multilateration

from multilateration import MODE_2D, MODE_3D, MODE_2D5

P=multilateration.Project(mode=MODE_2D)
P.add_anchor('anchore_A',(0,100,0))
P.add_anchor('anchore_B',(100,100,0))
P.add_anchor('anchore_C',(100,0,0))

t = P.add_target()
t.add_measure('anchore_A',100)
t.add_measure('anchore_B',50)
t.add_measure('anchore_C',50)
P.solve()

print(t.ID, str(t.loc))
