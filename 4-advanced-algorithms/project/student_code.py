import heapq
import math
import sys
from collections import defaultdict 

class PrioritySet(object):
    """
    Class that implements a priority set.
    
    Members:
        heap (array): Represents the heap that will keep the sorted entries of the set.
        labels (set): The set of the labels for each entry in the priority set.
    """
    def __init__(self):
        """
        Initializes an instance of the PrioritySet class.
        """
        self.heap   = []
        self.labels = set()

    def push(self, label, priority):
        """
        Pushes a new entry to the PrioritySet.
    
        Arguments:
            label (str):   The label for the entry.
            priority(int): The priority for the entry.
        """
        if not label in self.labels:
            heapq.heappush(self.heap, (priority, label))
            self.labels.add(label)

    def pop(self):
        """
        Pops the value with the lowest priority value.
        """
        priority, label = heapq.heappop(self.heap)
        self.labels.remove(label)
        return priority, label
    
    def __contains__(self, label):
        """
        Checks if a label is contained in the priority set.
        
        Returns:
            (bool) True, if the value is in the priority set. Otherwise, false.
        """
        return label in self.labels
    
    def __len__(self):
        """
        Gets the length of the priority set.
        
        Returns:
            (int) The size of the priority set.
        """
        return len(self.labels)

    def __repr__(self):
        return str(self.heap)

def get_distance(first_node, second_node):
    """
    Gets the euclidean distance between 2 points.

    Arguments:
        first_node (tuple):  (x, y) tuple that represents the first point.
        second_node (tuple): (x, y) tuple that represents the second point.

    Returns:
        (int) The distance between the given points.
    """
    x_difference = pow(second_node[0] - first_node[0], 2)
    y_difference = pow(second_node[1] - first_node[1], 2)
    return math.sqrt(x_difference + y_difference)   

def get_optimal_path(nearest_neighbors_list, start_node, goal_node):
    """
    Gets the optimal path between 2 points from the list of nearest neighbors.

    Arguments:
        nearest_neighbors_list (array): The list of nearest neighbors.
        start_node (int): The start node index.
        goal_node (int):  The goal node index.

    Returns:
        (int) The distance between the given points.
    """
    current_node = goal_node
    
    final_path = list()
    
    while current_node != start_node:
        final_path.append(current_node)
        current_node = nearest_neighbors_list[current_node]
    
    final_path.append(start_node)
    final_path.reverse()
    
    return final_path

def shortest_path(complete_map, start, goal):
    """
    Gets the shortest path between 2 points on a map.

    Arguments:
        complete_map (map): The map with intersections and roads.
        start (int): The start node index.
        goal (int):  The goal node index.

    Returns:
        (int) The distance between the given points.
    """
    #f-score: f = g + h
    #g-score: the path cost of a node
    #h: heuristic used to estimate distance between a node and the goal. In this case, the euclidian distance between two nodes as the heuristic.
    nodes             = complete_map.intersections 
    roads             = complete_map.roads
    goal_node         = nodes[goal]
    frontier          = PrioritySet()
    explored          = set()
    g_scores          = defaultdict(lambda: sys.maxindex) 
    nearest_neighbors = {}
    g_scores[start]   = 0
    
    frontier.push(start, get_distance(nodes[start], goal_node))
    
    while len(frontier) > 0:
        score, node_name = frontier.pop()
        node        = nodes[node_name]
        
        if node == goal:
            break
        else:
            explored.add(node_name)
            
            for neighbor in roads[node_name]:
                if neighbor in explored:
                    continue
                    
                neighbor_node = nodes[neighbor]
                g_score       = g_scores[node_name] + get_distance(node, neighbor_node)
                
                if not neighbor in frontier or g_score < g_scores[neighbor]:              
                    g_scores[neighbor] = g_score
                    f_score = g_score + get_distance(goal_node, neighbor_node)
                    nearest_neighbors[neighbor] = node_name
                    frontier.push(neighbor, f_score) 
                 
    return get_optimal_path(nearest_neighbors, start, goal)