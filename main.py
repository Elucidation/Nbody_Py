from System import *

sys = System('solarsystem.txt',100000)

print sys

print "N : %d, R: %s" % (sys.N,sys.R)
for b in sys.bodies:
    b.pp()


from graphics import *
a = World(sys)



def updateLabel(dt):
    a.updateStats("FPS: %.2f, " % pyglet.clock.get_fps() + \
                  "Steps: %5g, N: %i, O(n): %g, " % (sys.steps, sys.N, sys.accCount) + \
                  "System Time: %.3es" % sys.time
                  )

def update(dt):
    sys.step()
    a.updateBodies()
    


pyglet.clock.schedule_interval(updateLabel, 1/60.0)
pyglet.clock.schedule_interval(update, 1/25.0)
pyglet.app.run()
