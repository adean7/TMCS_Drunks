import pyglet
import pyglet.gl
import math
import random

def draw_circle(num_verts, center_x, center_y, radius):
    global vertices
    vertices = []
    for i in range(num_verts):
        angle_rad = 2 * i * math.pi / num_verts
        cos_theta = math.cos(angle_rad)
        sin_theta = math.sin(angle_rad)
        vertices.append((cos_theta - sin_theta) * radius + center_x)
        vertices.append((cos_theta + sin_theta) * radius + center_y)
    return vertices

class graphicsWindow(pyglet.window.Window):
    def __init__(self):
        super(graphicsWindow, self).__init__()  # constructor for graphicsWindow class
        self.x = [30]
        self.y = [30]
        self.xvel = 3
        self.yvel = 3
        self.num_people = len(self.x)

    def update(self, dt,):
        ''' Do things. '''
        self.x = [i + self.xvel for i in self.x]
        self.y = [i + self.yvel for i in self.y]

    def on_draw(self):
        # clear the graphics buffer
        pyglet.gl.glClearColor(1, 1, 1, 1)
        pyglet.gl.glClear(pyglet.gl.GL_COLOR_BUFFER_BIT)
        sprite.draw()
        coords = []
        for i in range(self.num_people):
            coords.append(self.x[i])
            coords.append(self.y[i])

        pyglet.gl.glColor3f(1, 0, 0)
        #pyglet.gl.glPointSize(10)
        num_verts = 10  # Number of vertices of circle.
        radius = 2  # Radius of circles.
        coords = draw_circle(num_verts, self.x[0], self.y[0], radius)
        coords_list = pyglet.graphics.vertex_list(num_verts, ('v2f', coords)) #'''self.num_people'''
        coords_list.draw(pyglet.gl.GL_POLYGON)

# this is the main game engine loop
if __name__ == '__main__':
    image = pyglet.image.load_animation('oxford.png')   # Background image.
    sprite = pyglet.sprite.Sprite(img=image)
    window = graphicsWindow()  # Initialize a window class.
    pyglet.clock.schedule_interval(window.update, 1 / 10.0)  # Tell pyglet the on_draw() & update() timestep.
    pyglet.app.run()  # Run pyglet.