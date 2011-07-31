from Body import *

bodies = []
with open('solarsystem.txt','r') as f:
    print f

    N = int(f.readline())
    R = float(f.readline())
    for line in f.readlines():
        bodies.append(
            Body().loadFromString(line.strip()) 
            )        

print "N : %d, R: %s" % (N,R)
for b in bodies:
    b.pp()



from graphics import *
a = World(bodies,R)
a.go()
