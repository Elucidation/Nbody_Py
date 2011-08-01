from System import *


sys = System('spiral.txt',100000)
#sys = System('dance10.txt',100000)
#sys = System('test1.txt',100000)
#sys = System('solarsystem.txt',100000)

print "N : %d, R: %s" % (sys.N,sys.R)
for b in sys.bodies:
    b.pp()


from graphics import *
a = World(sys)  

pyglet.app.run()
