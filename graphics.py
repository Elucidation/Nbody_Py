import pyglet
from pyglet.window import key, mouse


class World(pyglet.window.Window):
    def __init__(self,bodies,R,windowSize=500):
        super(World, self).__init__()
        self.bodies = bodies
        self.R = R # max Radius used for scaling
        self.WindowBoxSize = windowSize
        
        self.scale = self.WindowBoxSize/self.R
        # Origin will be center of screen
        # With screen width = twice the radius for scale

        self.updateBodies(bodies)
        print "N: %i SCALE: %g" % (self.N, self.scale)

        
        
        print "W: %i H: %i" % (self.width, self.height)

        self.label = pyglet.text.Label('Hello world',
                                  font_name='Times New Roman',
                                  font_size = 9,
                                  x=0,
                                  y=self.height,
                                  anchor_x='left',
                                  anchor_y='top')
    
    def on_draw(self):
        self.clear()
        pyglet.gl.glColor4f(0, 1, 1, 1.0)
        self.drawBodies()
        self.label.draw()
        
    def updateStats(self,newText):
        self.label.text = newText;
        
    def updateBodies(self,newbodies):
        self.bodies = newbodies
        self.N = len(newbodies)
        

        self.points = []
        for i in range(0,self.N*2):
            self.points.append(float(0))
        i=0
        for b in self.bodies:
            self.points[i] = b.x * self.scale / 2 + self.WindowBoxSize / 2
            self.points[i+1] = b.y * self.scale / 2 + self.WindowBoxSize / 2
            i += 2

    def drawBodies(self): #R is max radius, used for scale
        pyglet.graphics.draw(self.N,pyglet.gl.GL_POINTS,
                             ('v2f',self.points)
                             )


    
    def on_mouse_press(self,x,y,button,modifiers):
        if button == mouse.LEFT:
            print "Left Mouse button pressed."

    
    def on_key_press(self,symbol,modifiers):
        if symbol == key.A:
            print "The 'A' key was pressed"

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
