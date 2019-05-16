# Random walk on a graph -- Simulating a drunk outbreak

You've got a brilliant idea coming back from the pub: you will create a startup
that maintain a network of public toilets, and you will charge the city council
based on how many people use them. You have everything sorted: you will have
connected toilets coated with a smart compound to keep them clean. One problem
remains: you need to optimise the placement of the toilets so you get a maximum
of use to charge with the minimum amount of hardware. With this project, you
will simulate drunk people wandering in town in order to make decisions about
your business, and you will display your simulation using
[pyGlet](../outlines/I-pyGlet-GameMechanics.md).

I provide a map of the city taken from [OpenStreeMap](https://www.openstreetmap.org).
The map is a compressed XML file that describes the city as a graph where each
intersection or bend in a road is a vertex (also called node), and each road is
an edge. I also provide a parser that reads the XML file and returns a graph to
be used with the [NetworkX library](https://networkx.github.io/).

The simplest model is to represent drunk persons as "tokens" on the graph which
starts on a random node, and which randomly move from one node to a connected one.
Once this simple rule is implemented, more complex ones can be added:

* Are the drunk people more likely to start near pubs?
* Do the drunk people aim for a random "home" on the map?
* Do they aim for your toilets if there are some in the area?
* Do they gather where they are other drunk people?
* Do they try to avoid police patrols?
* Are they actually zombies?

Beyond the project, similar models are used to simulate metabolic pathways.

Here is how to use the provided code:

```python
# Assuming your code, the provided code, and the map file are in the same directory
import osm2graph

import gzip  # the map file is compressed with the gzip algorithm

with gzip.open('planet_-1.275,51.745_-1.234,51.762.osm.gz') as infile:
    graph = osm2graph.read_osm(infile)

# Get a list of all the node names
node_names = list(graph.nodes)
# Get the name of the first node
first_node = node_names[0]
# Get the longitude and latitude of the first node
longitude = graph.nodes[first_node]['lon']
latitude = graph.nodes[first_node]['lat']

# Get a list of the edges. Each edge is a tuple of the node names at its
# extremities.
edge_list = list(graph.edges)
```

Look at the documentation of [NetworkX](https://networkx.github.io/) to see how
to manipulate the `graph` object.
