from System import *

dt = 2500

sys = System('spiral.txt',dt)
#sys = System('dance10.txt',100000)
#sys = System('test1.txt',100000)
#sys = System('solarsystem.txt',100000)

print "N : %d, R: %s" % (sys.N,sys.R)
for b in sys.bodies:
    b.pp()


from graphics import *
a = World(sys,updateRate=1/1000.0) # Maxes out at roughly 300 somethin steps/sec
print "Refresh Rate: %g, Update Rate: %g" % (a.frameRate, a.updateRate)

pyglet.app.run()
