import pyglet
import pyglet.gl
import math
from graph import CustomGraph
import person
from PIL import Image
import pickle


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

    return verts_x, verts_y, len(verts_x)


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
        self.verts_x, self.verts_y, self.num_verts = circle_vertices(num_verts, radius)

        # Set window timer
        self.timer = 0

        self.color_list = {
            'home': [0, 0, 1],  # Blue # People going home
            'random': [1, 0, 0],  # Red
            'pub': [0, 0.5, 0],  # Green # People who are drunk
            'none': [0, 0, 0]  # Black
            }

    def get_colour(self, arg):
        self.color = self.color_list.get(arg.type, 'none')

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

    def update(self, dt, graph):
        # Update the window timer
        self.timer += 1
        graph.count_zombies_node(self.people)
        for i in range(self.num_people):
            if graph.nodes[people[i].current_node]['num_zombies'] > 0:
                self.people[i].type = 'zombie'
            self.people[i].update_position(self.timer)


        self.set_positions(people)

    def on_draw(self):
        # Clear the graphics buffer
        #pyglet.gl.glClearColor(1, 1, 1, 1)
        pyglet.gl.glClear(pyglet.gl.GL_COLOR_BUFFER_BIT)

        # Draw background
        sprite_background.draw()

        # Set initial colour as white
        pyglet.gl.glColor3f(1, 1, 1)

        # Draw homes
        for ID in home_list:
            # Convert coordinates to image coordinates
            lon, lat = self.convert_coordinate(graph.nodes[ID]['lon'], graph.nodes[ID]['lat'])

            # Draw sprites
            sprite_home.x, sprite_home.y = lon, lat
            sprite_home.draw()

        # Draw pubs
        for ID in pub_list:
            # Convert coordinates to image coordinates
            lon, lat = self.convert_coordinate(graph.nodes[ID]['lon'], graph.nodes[ID]['lat'])

            # Draw sprites
            sprite_pub.x, sprite_pub.y = lon, lat
            sprite_pub.draw()

        # Draw people
        for i in range(self.num_people):

            # If the person is flagged to be shown
            if people[i].show:

                # Convert coordinates to image coordinates
                lon, lat = self.convert_coordinate(self.x[i], self.y[i])

                # Construct a circle
                coords = draw_circle(lon, lat, self.verts_x, self.verts_y)

                # Set draw colour depending on person type
                self.get_colour(people[i])
                pyglet.gl.glColor3f(self.color[0], self.color[1], self.color[2])

                # Draw circles
                coords_list = pyglet.graphics.vertex_list(self.num_verts, ('v2f', coords))
                coords_list.draw(pyglet.gl.GL_POLYGON)  # Use .GL_POINTS if circles don't need to be filled


# This is the main game engine loop
if __name__ == '__main__':

    # Load background image
    img_background = 'oxford.png'
    im = Image.open(img_background)
    img_width, img_height = im.size
    sprite_background = pyglet.sprite.Sprite(img=pyglet.image.load(img_background))

    # Load home image
    img_home = 'home.png'
    img_obj_home = pyglet.image.load(img_home)
    img_obj_home.anchor_x = int(img_obj_home.width*0.52) #* 0.5
    img_obj_home.anchor_y = int(img_obj_home.height*0.3) #* 0.5
    sprite_home = pyglet.sprite.Sprite(img_obj_home)
    sprite_home.scale = 0.4

    # Load pub image
    img_pub = 'pub.png'
    img_obj_pub = pyglet.image.load(img_pub)
    sprite_pub = pyglet.sprite.Sprite(img_obj_pub)
    sprite_pub.scale = 1

    # Load graph
#    graph = graph.CustomGraph('stuff_provided/planet_-1.275,51.745_-1.234,51.762.osm.gz')
    graph = pickle.load(open('graph.pkl', 'rb'))

    # Load people
    #people_home = person.generate_people(graph, 50, 'home', 'random')
    #people_rand = person.generate_people(graph, 50, 'random', 'random')
    people_pub = person.generate_people(graph, 150, 'pub', 'random')
    people = people_pub #+ people_home + people_rand #

    # Load homes
    home_list = graph.home_list

    # Load pubs
    pub_list = graph.pub_list

    # Create an instance of a window
    window = graphicsWindow(people, graph)
    window.set_size(img_width, img_height)

    # Tell pyglet the on_draw() & update() timestep
    pyglet.clock.schedule_interval(window.update, 1 / 30.0, graph)

    # Run pyglet
    pyglet.app.run()

