import person
import graph
import networkx

graph_test = graph.make_graph('stuff_provided/planet_-1.275,51.745_-1.234,51.762.osm.gz')
start_node=list(graph_test.nodes)[0]
bob=person.people(start_node,graph_test)