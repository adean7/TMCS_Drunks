""""Class of People """

class people():
    """Class for people objects which traverse the node"""

    def __init__(self,start_node):

        # Get these from the graph object via node ID
        self.x=0
        self.y=0
        self.current_node=start_node #Via node ID
        self.name="Bob"
        self.next_node=self.make_decision()
        self.total_distance=self.calc_distance()
        self.traveled_distance=0
        self.speed=self.calc_speed()


    def make_decision(self,connected_nodes):
        """Function to decide which node to travel to next based on current node"""
        #make choice from connected_nodes
        next_node==None
        return next node
        pass

    def calc_distance(selfs):
        #set distance to next node
        """Calculate distance between nodes"""
        distance=0
        return distance

    def calc_speed(selfs):
        # define speed
        """Calculate speed to travel between selected node"""
        self.speed=0
        return self.speed

    def updated_distance(self):
        """Update distance travelled"""

        pass


    def check_at_node(selfs):
        """Check if person has reached node"""
        if self.traveled_distance>self.total_distance:
            return True


