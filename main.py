from System import *

sys = System('solarsystem.txt',10000)

print sys

print "N : %d, R: %s" % (sys.N,sys.R)
for b in sys.bodies:
    b.pp()


from graphics import *
a = World(sys.bodies,sys.R)



def updateLabel(dt):
    a.updateStats("FPS: %.2f \n" % pyglet.clock.get_fps() + \
                  "Steps: %5g   #CompsPerStep: %g \n" % (sys.steps, sys.accCount) + \
                  "System Time: %.0fs" % sys.time
                  )

def update(dt):
    sys.step()
    a.updateBodies(sys.bodies)
    

pyglet.clock.schedule_interval(updateLabel, 1/60.0)
pyglet.clock.schedule_interval(update, 1/25.0)
pyglet.app.run()
