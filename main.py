import person
import graph

# Import the graph
graph = graph.CustomGraph('stuff_provided/planet_-1.275,51.745_-1.234,51.762.osm.gz')

# Create a person at a starting node
start_node = list(graph.nodes)[0]
bob = person.person(start_node, graph)

# Have bob wander around for a bit
for i in range(200):

    bob.update_position()
    print(i, bob.current_node, bob.next_node, bob.traveled_distance, bob.total_distance)
