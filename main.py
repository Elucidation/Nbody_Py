from Body import *

bodies = []
with open('solarsystem.txt','r') as f:
    print f

    N = int(f.readline())
    R = float(f.readline())
    print "N : %d, R: %s" % (N,R)
    for line in f.readlines():
        bodies.append(
            Body().loadFromString(line.strip()) 
            )        

for b in bodies:
    b.pp()
