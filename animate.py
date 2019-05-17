import pyglet
import pyglet.gl
import math
import graph
import person
from PIL import Image
#import random


def circle_vertices(num_verts, radius, center_x=0, center_y=0):
    """ Calculate the positions of the vertices in a circle """

    verts_x = []
    verts_y = []

    for i in range(num_verts):
        angle_rad = 2 * i * math.pi / num_verts
        cos_theta = math.cos(angle_rad)
        sin_theta = math.sin(angle_rad)

        verts_x.append((cos_theta - sin_theta) * radius + center_x)
        verts_y.append((cos_theta + sin_theta) * radius + center_y)

    return verts_x, verts_y


def draw_circle(center_x, center_y, verts_x, verts_y):

    coords = []

    for i in range(len(verts_x)):
        coords.append(center_x + verts_x[i])
        coords.append(center_y + verts_y[i])

    return coords



class graphicsWindow(pyglet.window.Window):

    def __init__(self, people, graph, num_verts=8, radius=2.):

        # Constructor for graphicsWindow class
        super(graphicsWindow, self).__init__()

        # Use graph to produce coordinate conversion
        self.range_lon, self.range_lat = graph.map_range()

        # Set list of people
        self.people = people
        self.num_people = len(people)

        # Set initial positions
        self.set_positions(people)

        # Get the coordinates of the vertices on a circle
        self.verts_x, self.verts_y = circle_vertices(num_verts, radius)

        # Set window timer
        self.timer = 0


    def set_positions(self, people):

        self.x = []
        self.y = []

        for i in range(self.num_people):
            self.x.append(people[i].x)
            self.y.append(people[i].y)


    def convert_coordinate(self, lon, lat):

        lon = (lon - self.range_lon[0]) / (self.range_lon[1] - self.range_lon[0])
        lon = lon * img_width

        lat = (lat - self.range_lat[0]) / (self.range_lat[1] - self.range_lat[0])
        lat = lat * img_height

        return lon, lat


    def update(self, dt):
        self.timer += 1
        print (self.timer)
        for i in range(self.num_people):
            people[i].update_position(self.timer)

        self.set_positions(people)

        # Update the window timer



    def on_draw(self):

        # Clear the graphics buffer
        #pyglet.gl.glClearColor(1, 1, 1, 1)
        pyglet.gl.glClear(pyglet.gl.GL_COLOR_BUFFER_BIT)

        # Draw background
        sprite.draw()

        # Set people colour and size (only use size if not using draw_circle)
        pyglet.gl.glColor3f(1, 0, 0)
        #pyglet.gl.glPointSize(10)


        for i in range(self.num_people):

            # If the person is flagged to be shown
            if people[i].show:

                # Convert coordinates to image coordinates
                lon, lat = self.convert_coordinate(self.x[i], self.y[i])

                # Construct a circle
                coords = draw_circle(lon, lat, self.verts_x, self.verts_y)

                # Draw circles
                coords_list = pyglet.graphics.vertex_list(len(self.verts_x), ('v2f', coords))
                coords_list.draw(pyglet.gl.GL_POLYGON)  # Use .GL_POINTS if circles don't need to be filled


# This is the main game engine loop
if __name__ == '__main__':

    # Load background image
    image = 'oxford.png'
    im = Image.open(image)
    img_width, img_height = im.size
    sprite = pyglet.sprite.Sprite(img=pyglet.image.load_animation(image))

    # Load graph
    graph = graph.CustomGraph('stuff_provided/planet_-1.275,51.745_-1.234,51.762.osm.gz')

    # Load people
    people = person.generate_people(graph, 100, 'home', 'random')

    # Create an instance of a window
    window = graphicsWindow(people, graph)
    window.set_size(img_width, img_height)

    # Tell pyglet the on_draw() & update() timestep
    pyglet.clock.schedule_interval(window.update, 1 / 30.0)

    # Run pyglet
    sprite.draw()
    pyglet.app.run()