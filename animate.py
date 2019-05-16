import pyglet
import pyglet.gl
import math
import graph
import person
from PIL import Image
import random

graph_test = graph.make_graph('stuff_provided/planet_-1.275,51.745_-1.234,51.762.osm.gz')

image = 'oxford.png'
im = Image.open(image)
width, height = im.size

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
        self.list_people = []   # List of people objects.
        self.num_people = len(graph_test)     # Number of people to initialise.
        for i in range(self.num_people):
            start_node = list(graph_test.nodes)[i]
            self.list_people.append(person.person(start_node, graph_test))  # Adds 5 people objects to the list of people.
        self.x_pos = []
        self.y_pos = []
        for i in range(self.num_people):
            self.x_pos.append(self.list_people[i].x)    # Adds x positions of people objects.
            self.y_pos.append(self.list_people[i].y)    # Adds y positions of people objects.

        '''
        print("min x pos is ", min(self.x_pos))
        print("max x pos is ", max(self.x_pos))
        print("min y pos is ", min(self.y_pos))
        print("max y pos is ", max(self.y_pos))
        '''
        ''' Renormalising coordinates to fit in window. '''
        '''       Image size is 23.79 by 12.82 cm.      '''
        self.x_pos = [i - min(self.x_pos) for i in self.x_pos]
        self.x_pos = [i / max(self.x_pos) for i in self.x_pos]
        self.x_pos = [i * width for i in self.x_pos]
        self.y_pos = [i - min(self.y_pos) for i in self.y_pos]
        self.y_pos = [i / max(self.y_pos) for i in self.y_pos]
        self.y_pos = [i * height for i in self.y_pos]

        self.x_vel = 1  # Standard x velocity for now.
        self.y_vel = 1  # Standard y velocity for now.

    def update(self, dt):
        '''
        self.x_pos = [i + self.x_vel for i in self.x_pos]
        self.y_pos = [i + self.y_vel for i in self.y_pos]
        '''
        pass

    def on_draw(self):
        # clear the graphics buffer
        pyglet.gl.glClearColor(1, 1, 1, 1)
        pyglet.gl.glClear(pyglet.gl.GL_COLOR_BUFFER_BIT)
        sprite.draw()
        coords = []
        for i in range(self.num_people):
            coords.append(self.x_pos)
            coords.append(self.y_pos)

        pyglet.gl.glColor3f(1, 0, 0)
        #pyglet.gl.glPointSize(10)
        num_verts = 8  # Number of vertices of circle.
        radius = 2  # Radius of circles.
        for i in range(self.num_people):
            coords = draw_circle(num_verts, self.x_pos[i], self.y_pos[i], radius)
            coords_list = pyglet.graphics.vertex_list(num_verts, ('v2f', coords))
            coords_list.draw(pyglet.gl.GL_POLYGON)

# this is the main game engine loop
if __name__ == '__main__':
    for_sprite = pyglet.image.load_animation(image)   # Background image.
    sprite = pyglet.sprite.Sprite(img=for_sprite)
    window = graphicsWindow()  # Initialize a window class.
    window.set_size(width, height)
    pyglet.clock.schedule_interval(window.update, 1 / 10.0)  # Tell pyglet the on_draw() & update() timestep.
    pyglet.app.run()  # Run pyglet.