import person
import graph

# Import the graph
graph = graph.CustomGraph('stuff_provided/planet_-1.275,51.745_-1.234,51.762.osm.gz')

# Create a person at a starting node
start_node = list(graph.nodes)[0]
people_list = person.generate_people(graph,2,'home','random')


# Have bob wander around for a bit
for j in range(2):
    for i in range(200):
        people_list[j].update_position()
        print(i, people_list[j].current_node, people_list[j].next_node, people_list[j].traveled_distance, people_list[j].total_distance)
