import random

def node_to_bar()
    nearest_bar = find_nearest_bar()
    next_node = find_next_node(self.current_node, nearest_bar)
    return next_node

def random_node(connected_node):
    num_nodes = len(connected_node)
    rand_node_index = random.randint(0,num_nodes-1)
    next_node = connected_node[rand_node_index]
    return next_node

def node_to_home():
    next_node = find_next_node(self.current_node, self.home_node)
    return  next_node



def node_flee_zombie()


if __name__ == '__main__':
    current_node = '1'
    connected_node = ['2', '3', '4']
    print(choose_random_node(connected_node))
