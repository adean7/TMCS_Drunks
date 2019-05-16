import random
import networkx

def node_to_bar(bars_list):
    """Returns the next node on the shortest path toward the nearest bar"""
    nearest_bar = find_nearest_bar(node_graph, bars_list)
    next_node = node_shortest_path(node_graph, self.current_node, nearest_bar)
    return next_node

def random_node(connected_node):
    """Returns a random node among the connected nodes"""
    num_nodes = len(connected_node)
    rand_node_index = random.randint(0,num_nodes-1)
    next_node = connected_node[rand_node_index]
    return next_node

def node_to_home():
    """Returns the next node on the shortest path toward home"""
    next_node = node_shortest_path(node_graph, self.current_node, self.home)
    return next_node

def node_flee_zombies(node_graph):
    """Returns the node with the least number of zombies on it"""
    num_zombies = []
    #Find the number of zombies at each of the connected nodes
    for node in connected_node:
        num_zombies.append(zombies_list[node])
    #The next node is the node with the least number of zombies on it
    next_node = num_zombies.index(min(num_zombies))
    return next_node

def node_shortest_path(node_graph, current_node, goal_node):
    """Returns the next node on the shortest path from 'current_node' to 'goal_node'"""
    path = networkx.shortest_path(node_graph, current_node, goal_node)
    next_node = path[0]
    return next_node

def make_bars_list(node_graph, frac_bars):
    """Returns a list of nodes that have been randomly assigned to be bars, each with 'frac_bars' probability"""
    node_IDs = list(node_graph.nodes)
    bars_list = []
    for ID in node_IDs:
        rand_num = random.random()
        if rand_num < frac_bars:
            bars_list.append(ID)
    return bars_list

def find_nearest_bar(node_graph, bars_list):
    """Returns the node ID of the nearest bar"""
    distances = []
    for bar in bars_list:
        #Find shortest distance between current_node and the bar
        d = shortest_path_length(node_graph, self.current_node, bar)
        distances.append(d)
    next_node = bars_list.index(min(d))
    return next_node

def calc_zombies_list(node_graph, person_list):
    """Generate a dictionary of number of zombies on each node"""
    node_IDs = list(node_graph.nodes)
    #Initialize number of zombies on each node to 0
    zombies_list = dict.fromkeys(node_IDs, 0)
    for person in person_list:
        zombies_list[person.current_node] = zombies_list[person.current_node] + 1
    return zombies_list

def to_zombie(self, prob_zombie):
    rand_num = random.random()
    if rand_num < prob_zombie:
        self.setZombie(True)



#Code for simple testing
#if __name__ == '__main__':
#    current_node = '1'
#    connected_node = ['2', '3', '4']
#    print(random_node(connected_node))
