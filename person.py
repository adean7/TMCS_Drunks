""""Class of People """
import random

class person():
    """Class for people objects which traverse the node"""

    def __init__(self, start_node, graph_object):

        # Set graph
        self.graph=graph_object

        # Set current node and the neighbors
        self.current_node = start_node  # Via node ID

        # Can generate name from list later
        self.name="Bob"
        self.type='drunk'
        self.home=start_node

        # Select a path from the starting node
        self.make_decision()


    def random_node(self, neighbor_list):
        """ Randomly selects the next node from the list of connected nodes """

        next_node = random.choice(neighbor_list)
        return next_node


    def make_decision(self):
        """Function to decide which node to travel to next based on current node"""

        # Select the next node
        # Currently selects at random from connected nodes
        neighbors = list(self.graph.neighbors(self.current_node))
        self.next_node = self.random_node(neighbors)

        # Set speed
        # Constant for now, may change later
        self.speed = 1.0

        # Set the relevant positions from the nodes
        self.new_path_positions(self.current_node, self.next_node)


    def new_path_positions(self, start_node, final_node):
        """ Sets the relevant positions and distances when a new path is selected
        Inputs:     start_node  ID of the starting node
                    final_node  ID of the final node
        """

        # Set start node positions
        start_x = self.graph.nodes[start_node]['lon']
        start_y = self.graph.nodes[start_node]['lat']

        # Set final node positions
        final_x = self.graph.nodes[final_node]['lon']
        final_y = self.graph.nodes[final_node]['lat']

        # Total distance between the nodes
        self.traveled_distance = 0
        self.total_distance = self.graph[start_node][final_node]['distance']

        # Unit vector between the two nodes
        final_x = (final_x - start_x) / self.total_distance
        final_y = (final_y - start_y) / self.total_distance
        self.unit_vector = [final_x, final_y]

        # Set person positions at the starting node
        self.x = start_x
        self.y = start_y


    def update_position(self, dt=1):
        """ Update the positions of a person
        Inputs:     dt, time step
        """

        # Calculate the scalar distance moved
        distance_moved = self.speed * dt

        # Add to the total scalar distance travelled
        self.traveled_distance += distance_moved

        # Check if a node is reached
        if self.check_at_node() == True:

            # If it is, then pick a new path
            # Updates x,y of person to be at the new node within the function
            self.current_node = self.next_node
            self.make_decision()

        else:

            # Otherwise update x,y to be along the paths
            self.x += distance_moved * self.unit_vector[0]
            self.y += distance_moved * self.unit_vector[1]


    def check_at_node(self):
        """ Check if person has reached node """
        if (self.traveled_distance >= self.total_distance):
            return True
        else:
            return False


