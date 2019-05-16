import osm2graph    # premade module uesd to convert map file to graph
import gzip         # the map file is compressed with the gzip algorithm
import networkx
import random

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


# Out of date - do not use
def make_graph(gzip_file, only_roads=True):
    """
    Create a graph object, including scalar distances between nodes
    :param gzip_file:       gzip file to open file froms
    :param only_roads:
    :return:                graph object
    """

    # Create graph object using provided parser
    with gzip.open(gzip_file) as infile:
        graph = osm2graph.read_osm(infile, only_roads)


    # Add the distances between nodes

    # Get a list of node IDs
    node_IDs = list(graph.nodes)

    for ID in node_IDs:

        # Find coordinates of the start node
        start_lon = graph.nodes[ID]['lon']
        start_lat = graph.nodes[ID]['lat']

        # Find the neighbours of the node
        neighbour_IDs = list(graph.neighbors(ID))

        for final_ID in neighbour_IDs:

            # Find coordinates of the end node
            final_lon = graph.nodes[final_ID]['lon']
            final_lat = graph.nodes[final_ID]['lat']

            # Calculate the distance between the two nodes
            d = osm2graph.haversine(start_lon, start_lat, final_lon, final_lat)
            graph[ID][final_ID]['distance'] = d

    return graph


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

        # Add the distances between nodes
        # Get a list of node IDs
        node_IDs = list(self.nodes)

        for ID in node_IDs:

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

        # Add a list of pubs and homes
        self.pub_list = make_node_subset(self, 0.1)
        self.home_list = make_node_subset(self, 0.2)


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








