import pyglet
import pyglet.gl
import math
import graph
import person
from PIL import Image
import random

def draw_circle(num_verts, center_x, center_y, radius):

    global vertices

    vertices = []

    # Some of these values can be cached for efficiency
    for i in range(num_verts):
        angle_rad = 2 * i * math.pi / num_verts
        cos_theta = math.cos(angle_rad)
        sin_theta = math.sin(angle_rad)
        vertices.append((cos_theta - sin_theta) * radius + center_x)
        vertices.append((cos_theta + sin_theta) * radius + center_y)

    return vertices



class graphicsWindow(pyglet.window.Window):

    def __init__(self, people, graph):

        # Constructor for graphicsWindow class
        super(graphicsWindow, self).__init__()

        # Use graph to produce coordinate conversion
        self.range_lon, self.range_lat = graph.map_range()

        # Set list of people
        self.people = people
        self.num_people = len(people)

        # Set initial positions
        self.set_positions(people)


    def set_positions(self, people):

        self.x = []
        self.y = []

        for i in range(self.num_people):
            self.x.append(people[i].x)
            self.y.append(people[i].y)


    def convert_coordinate(self, lon, lat):

        lon = (lon - self.range_lon[0]) / (self.range_lon[1] - self.range_lon[0])
        lon = lon * width

        lat = (lat - self.range_lat[0]) / (self.range_lat[1] - self.range_lat[0])
        lat = lat * height

        return lon, lat


    def update(self, dt):
        '''
        self.x_pos = [i + self.x_vel for i in self.x_pos]
        self.y_pos = [i + self.y_vel for i in self.y_pos]
        '''

        for i in range(self.num_people):
            people[i].update_position()

        self.set_positions(people)


    def on_draw(self):

        # Clear the graphics buffer
        pyglet.gl.glClearColor(1, 1, 1, 1)
        pyglet.gl.glClear(pyglet.gl.GL_COLOR_BUFFER_BIT)

        # Draw background
        sprite.draw()

#        coords = []
#        for i in range(self.num_people):
#            coords.append(self.x)
#            coords.append(self.y)


        pyglet.gl.glColor3f(1, 0, 0)
        #pyglet.gl.glPointSize(10)

        num_verts = 8  # Number of vertices of circle.
        radius = 2  # Radius of circles.

        for i in range(self.num_people):

            lon, lat = self.convert_coordinate(self.x[i], self.y[i])
            coords = draw_circle(num_verts, lon, lat, radius)

            coords_list = pyglet.graphics.vertex_list(num_verts, ('v2f', coords))
            coords_list.draw(pyglet.gl.GL_POLYGON)


# this is the main game engine loop
if __name__ == '__main__':

    # Load background image
    image = 'oxford.png'
    im = Image.open(image)
    width, height = im.size
    for_sprite = pyglet.image.load_animation(image)
    sprite = pyglet.sprite.Sprite(img=for_sprite)

    # Load graph
    graph = graph.CustomGraph('stuff_provided/planet_-1.275,51.745_-1.234,51.762.osm.gz')

    # Load people
    people = person.generate_people(graph, 100, 'home', 'random')

    # Create an instance of a window
    window = graphicsWindow(people, graph)
    window.set_size(width, height)

    # Tell pyglet the on_draw() & update() timestep.
    pyglet.clock.schedule_interval(window.update, 1 / 30.0)

    # Run pyglet
    pyglet.app.run()