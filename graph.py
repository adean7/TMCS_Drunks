import osm2graph    # premade module uesd to convert map file to graph
import gzip         # the map file is compressed with the gzip algorithm
import networkx
import random
import numpy
import pickle

# Graph object is a dictionary where each ID corresponds to a node
# Each node object is itself a dictionary containing information

# to get longitude and latitude of a node
#   lon = graph.nodes[node_ID]['lon']
#   lat = graph.nodes[node_ID]['lat']

# to get a list of IDs of connected nodes
#   neighbors = list(graph.neighbors(node_ID))

# The connections between nodes are are also dictionaries containing information
# to get the distance between 2 nodes
#   distance = graph[node_ID_1][node_ID_2]['distance']


def make_node_subset(node_graph, fraction):
    """
    Randomly selects a fraction of nodes to create a subset
    """

    node_IDs = list(node_graph.nodes)
    node_list = []

    for ID in node_IDs:

        if (random.random() < fraction):
            node_list.append(ID)

    return node_list

    #    def find_nearest_pub(self):
    #        """Returns the node ID of the nearest pub"""
    #        distances = []
    #        for pub in self.graph.pub_list:
    #            # Find shortest distance between current_node and the bar
    #            d = networkx.shortest_path_length(self.graph, self.current_node, pub)
    #            distances.append(d)
    #        next_node = self.graph.pub_list.index(min(distances))
    #        return next_node


class CustomGraph(networkx.Graph):
    """
    Graph of nodes. Each connection has the node-node distance specified
    """

    def __init__(self, gzip_file, only_roads=True):

        # Create the base graph from parser
        with gzip.open(gzip_file) as infile:
            base_graph = osm2graph.read_osm(infile, only_roads)

        # Return the largest connected graph
        nodes_of_largest_graph = max(networkx.connected_components(base_graph), key=len)
        base_graph = base_graph.subgraph(nodes_of_largest_graph)

        # Init the object based on the base graph
        super().__init__(base_graph)

        # Add a list of pubs and homes
        self.pub_list = make_node_subset(self, 0.001)   # 0.001
        self.home_list = make_node_subset(self, 0.2)

        #print(self.pub_list)

        # Get a list of node IDs
        node_IDs = list(self.nodes)

        for stride, ID in enumerate(node_IDs):
            # Find coordinates of the start node
            start_lon = self.nodes[ID]['lon']
            start_lat = self.nodes[ID]['lat']

            # Find the neighbours of the node
            neighbour_IDs = list(self.neighbors(ID))

            for final_ID in neighbour_IDs:
                # Find coordinates of the end node
                final_lon = self.nodes[final_ID]['lon']
                final_lat = self.nodes[final_ID]['lat']

                # Calculate the distance between the two nodes
                d = osm2graph.haversine(start_lon, start_lat, final_lon, final_lat)
                self[ID][final_ID]['distance'] = d


            # If node is already a pub
            if (ID in self.pub_list):
                self.nodes[ID]['nearest_pub'] = ID

            # Otherwise find the nearest pub
            else:
                self.nodes[ID]['nearest_pub'] = self.nearest_node_from_list(ID, self.pub_list)
            
            # Label each node with the number of zombies
            self.nodes[ID]['num_zombies']=0
            
            print(stride, len(node_IDs))


    def nearest_node_from_list(self, start_node, target_list):
        """ Returns the ID of the nearest node from a list of possible nodes """

        # Get the shortest paths to pubs
        distances = []

        for target_node in target_list:

            distances.append(
                networkx.shortest_path_length(self, start_node, target_node, weight='distance')
            )

        # Return the index of the closest pub
        return numpy.argmin(distances)

    def count_zombies_node(self,list_of_people):
        """Counts number of zombies recently on each node"""
        node_IDs = list(self.nodes)

        # set number of zombies on each node to zero
        for node in node_IDs:
            self.nodes[node]['num_zombies'] = 0
        for i in range(len(list_of_people)):
            if list_of_people[i].type == 'zombie':
                self.nodes[list_of_people[i].current_node]['num_zombies']+=1


    #    self.num_on_edge[]

    def map_range(self):
        """
        Returns the range of longitude and latitude values for the graph
        """

        # Get a list of longitude and latitudes
        node_IDs = list(self.nodes)

        longitudes = []
        latitudes = []

        for ID in node_IDs:

            longitudes.append( self.nodes[ID]['lon'] )
            latitudes.append( self.nodes[ID]['lat'] )

        # Calculate the range of longitudes and latitudes
        range_longitudes = [min(longitudes), max(longitudes)]
        range_latitudes = [min(latitudes), max(latitudes)]

        return range_longitudes, range_latitudes

# Create an instance of a graph and export it using pickle
if __name__ == '__main__':

    G = CustomGraph('stuff_provided/planet_-1.275,51.745_-1.234,51.762.osm.gz')
    pickle.dump(G, open("graph.pkl", "wb"))






