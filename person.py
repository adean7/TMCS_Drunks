""""Class of People """
import networkx
import random

def calc_distance(x1,y1,x2,y2):
    # set distance to next node
    """Calculate distance between nodes"""
    distance = 1
    return distance

def calc_speed(distance):
    # define speed
    """Calculate speed to travel between selected node"""
    speed = 1
    return speed

class people():
    """Class for people objects which traverse the node"""

    def __init__(self,start_node,graph_object):
        self.graph=graph_object
        self.current_node = start_node  # Via node ID
        self.next_node = None

        # Get these from the graph object via node ID
        self.x=self.graph.nodes[self.current_node]['lon']
        self.y=self.graph.nodes[self.current_node]['lat']
        self.neighbors = list(self.graph.neighbors(self.current_node))

        # Can generate name from list later
        self.name="Bob"
        self.type='drunk'
        self.home=start_node

        self.traveled_distance = 0
        self.speed = 0

        self.make_decision()

    def random_node(self):
        num_nodes = len(self.neighbors)
        rand_node_index = random.randint(0, num_nodes - 1)
        next_node = self.neighbors[rand_node_index]
        return next_node

    def make_decision(self):
        """Function to decide which node to travel to next based on current node"""
        # make choice from connected_nodes

        self.next_node = self.random_node()
        self.total_distance = self.graph[self.current_node][self.next_node]['distance']
        self.traveled_distance=0
        self.speed = 1.0
        print ("Decision Made")
        print ("Next node: ", self.next_node)
        print ("Distance: ", self.total_distance)




    def updated_traveled_distance(self):
        """Update distance travelled"""
        pass


    def check_at_node(self):
        """Check if person has reached node"""
        if self.traveled_distance >= self.total_distance:
            return True
        else:
            return False


