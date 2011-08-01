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

a.setupEvents()

def update(dt):
    bodies[0].y += 1e8
    a.updateBodies(bodies)

pyglet.clock.schedule_interval(update, 0.1)

pyglet.app.run()
