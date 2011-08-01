import pyglet
from pyglet.window import key, mouse


class World(pyglet.window.Window):
    def __init__(self,sys,windowSize=500):
        super(World, self).__init__()
        self.sys = sys
        self.R = sys.R # max Radius used for scaling
        self.WindowBoxSize = windowSize
        self.width, self.height = windowSize, windowSize
        
        self.scale = self.WindowBoxSize/self.R
        # Origin will be center of screen
        # With screen width = twice the radius for scale
        
        self.points = []
        for i in range(0,self.sys.N*2):
            self.points.append(float(0))
        self.updateBodies()

        
        print "N: %i SCALE: %g" % (self.sys.N, self.scale)

        
        
        print "W: %i H: %i" % (self.width, self.height)

        self.label = pyglet.text.Label('Hello world',
                                  font_name='Times New Roman',
                                  font_size = 9,
                                  x=0,
                                  y=self.height,
                                  anchor_x='left',
                                  anchor_y='top')

        pyglet.clock.schedule_interval(self.updateLabel, 1/60.0)
    def on_draw(self):
        self.clear()
        pyglet.gl.glColor4f(0, 1, 1, 1.0)
        self.drawBodies()
        self.label.draw()
        
    def updateStats(self,newText):
        self.label.text = newText;
        
    def updateBodies(self):
        i=0
        for b in self.sys.bodies:
            self.points[i] = b.x * self.scale / 2 + self.WindowBoxSize / 2
            self.points[i+1] = b.y * self.scale / 2 + self.WindowBoxSize / 2
            i += 2

    def drawBodies(self): #R is max radius, used for scale
        pyglet.graphics.draw(self.sys.N,pyglet.gl.GL_POINTS,
                             ('v2f',self.points)
                             )


    
    def on_mouse_press(self,x,y,button,modifiers):
        if button == mouse.LEFT:
            print self.sys

    
    def on_key_press(self,symbol,modifiers):
        if symbol == key.A:
            print "Pausing"
            pyglet.clock.unschedule(self.update)
        if symbol == key.B:
            print "Unpausing"
            pyglet.clock.schedule_interval(self.update, 1/25.0)

    def update(self,dt):
        self.sys.step()
        self.updateBodies()

    def updateLabel(self,dt):
        self.updateStats("FPS: %.2f, " % pyglet.clock.get_fps() + \
                      "Steps: %5g, N: %i, O(n): %g, " % (self.sys.steps, self.sys.N, self.sys.accCount) + \
                      "System Time: %.3es" % self.sys.time
                         )
                         
    ##Shows all events
    ##window.push_handlers(pyglet.window.event.WindowEventLogger())


def drawPoint(x,y):
    pyglet.graphics.draw(1,pyglet.gl.GL_POINTS,
                         ('v2i',(x,y))
                         )


def drawBox(x,y,x2,y2):
    pyglet.graphics.draw_indexed(4,pyglet.gl.GL_LINES,
                                 [0,1, 1,2, 2,3, 3,0],
                         ('v2i',(x,y, x2,y, x2,y2, x,y2))
                         )
