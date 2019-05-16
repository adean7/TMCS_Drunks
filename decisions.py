import random

def node_to_bar():
    """Returns the next node on the shortest path toward the nearest bar"""
    nearest_bar = find_nearest_bar()
    next_node = find_next_node(self.current_node, nearest_bar)
    return next_node

def random_node(connected_node):
    """Returns a random node among the connected nodes"""
    num_nodes = len(connected_node)
    rand_node_index = random.randint(0,num_nodes-1)
    next_node = connected_node[rand_node_index]
    return next_node

def node_to_home():
    """Returns the next node on the shortest path toward home"""
    next_node = find_next_node(self.current_node, self.home_node)
    return next_node

def node_flee_zombies(node_list):
    """Returns the node with the least number of zombies on it"""
    num_zombies = []
    for node in connected_node:
        num_zombies.append(node_list[node].zombies)
    next_node = num_zombies.index(min(num_zombies))
    return next_node



if __name__ == '__main__':
    current_node = '1'
    connected_node = ['2', '3', '4']
    print(choose_random_node(connected_node))
