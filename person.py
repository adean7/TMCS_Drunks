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
        self.calc_distance()
        self.calc_speed()


    def make_decision(self):
        """Function to decide which node to travel to next based on current node"""
        #return next node
        pass

    def calc_distance(selfs):
        #set distance to next node
        """Calculate distance between nodes"""
        pass

    def calc_speed(selfs):
        # define speed
        """Calculate speed to travel between selected node"""
        self.speed=1
        pass


