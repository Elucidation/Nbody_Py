from System import *

sys = System('test1.txt',100000)

print sys

print "N : %d, R: %s" % (sys.N,sys.R)
for b in sys.bodies:
    b.pp()


from graphics import *
a = World(sys)  

pyglet.app.run()
