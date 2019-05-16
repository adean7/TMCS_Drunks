import osm2graph    # premade module uesd to convert map file to graph
import gzip         # the map file is compressed with the gzip algorithm

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
            print(d)
            graph[ID][final_ID]['distance'] = d

    return graph

#   G = make_graph('stuff_provided/planet_-1.275,51.745_-1.234,51.762.osm.gz')






