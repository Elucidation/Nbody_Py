import pyglet
from pyglet.window import key, mouse

window = pyglet.window.Window()

label = pyglet.text.Label('Hello world',
                          font_name='Times New Roman',
                          font_size = 36,
                          x=window.width/2,
                          y=window.height/2,
                          anchor_x='center',
                          anchor_y='center')

image = pyglet.resource.image('prof2.jpg')

@window.event
def on_draw():
    window.clear()
    pyglet.gl.glColor4f(1, 1, 1, 1)
    image.blit(0,0)
    label.draw()

    pyglet.gl.glColor4f(1.0, 0, 0, 1.0)
    pyglet.graphics.draw(2,pyglet.gl.GL_LINES,
                         ('v2i',(400,350,530,435))
                         )
    pyglet.gl.glColor4f(0, 1, 1, 1.0)
    drawPoint(400,200)
    
def drawPoint(x,y):
    pyglet.graphics.draw(1,pyglet.gl.GL_POINTS,
                         ('v2i',(x,y))
                         )


@window.event
def on_mouse_press(x,y,button,modifiers):
    if button == mouse.LEFT:
        print "Left Mouse button pressed."

@window.event
def on_key_press(symbol,modifiers):
    if symbol == key.A:
        print "The 'A' key was pressed"

##Shows all events
##window.push_handlers(pyglet.window.event.WindowEventLogger())

pyglet.app.run()
