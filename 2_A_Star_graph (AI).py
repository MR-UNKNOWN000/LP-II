import heapq

def a_star_search(graph, heuristics, start, goal):
    # Priority queue: (f(n), g(n), current_node, path)
    open_list = [(heuristics[start], 0, start, [start])]
    visited = set()

    while open_list:
        f, g, current, path = heapq.heappop(open_list)

        if current == goal:
            return path, g

        visited.add(current)

        for neighbor, cost in graph[current]:
            if neighbor not in visited:
                g_new = g + cost
                f_new = g_new + heuristics[neighbor]
                heapq.heappush(open_list, (f_new, g_new, neighbor, path + [neighbor]))

    return None, float('inf')

# Define the graph
graph = {
    'a': [('b', 4), ('c', 3)],
    'b': [('f', 5), ('e', 12)],
    'c': [('d', 7), ('e', 10)],
    'd': [('e', 2)],
    'e': [('z', 5)],
    'f': [('z', 16)],
    'z': []
}

# Define heuristic values (h(n))
heuristics = {
    'a': 14,
    'b': 12,
    'c': 11,
    'd': 6,
    'e': 4,
    'f': 11,
    'z': 0
}

# Run A* from 'a' to 'z'
path, cost = a_star_search(graph, heuristics, 'a', 'z')

print(f"Path found: {' -> '.join(path)}")
print(f"Total cost: {cost}")

'''✅ Title:
A* Search Algorithm Implementation

✅ Algorithm Used:
A Search Algorithm*

Steps:
Initialize a priority queue with the starting node and its heuristic value.

While the priority queue is not empty:

Pop the node with the lowest f(n) value (f(n) = g(n) + h(n)).

If this node is the goal node, return the path and cost.

Otherwise, for each neighboring node:

Calculate the cost g(n) and heuristic h(n).

Add the neighbor to the priority queue with the updated values.

Repeat the above steps until the goal is found or all nodes are explored.

✅ Flowchart Description:
A* Algorithm Flow:

sql
Copy
Edit
Start → Initialize open list with start node → While open list is not empty:
   → Pop node with lowest f(n) value
   → If node is goal, return path
   → For each neighbor, update g(n), h(n), and push to open list
   → End
✅ Feature Requirements:
Python 3.x

Data Structures: heapq (priority queue), dictionary, and set

Heuristic values for each node

Graph represented as an adjacency list

✅ Short Theory:
A* is an informed search algorithm used for pathfinding and graph traversal. It calculates the cost f(n) by combining the actual cost to reach the node (g(n)) and the heuristic estimate to the goal (h(n)). The algorithm is guaranteed to find the shortest path in graphs where the heuristic is admissible (never overestimates the actual cost).

✅ Time and Space Complexity:
Time Complexity:

A*: O((V + E) * log V) where V is the number of vertices and E is the number of edges.

Space Complexity:

A*: O(V) for storing the nodes in the priority queue and visited set.

✅ Important Definitions:
A Search*: A pathfinding and graph traversal algorithm that combines the best features of Dijkstra's algorithm and greedy best-first search. It uses a heuristic to guide its search and guarantee the shortest path in graphs with admissible heuristics.

Heuristic: A function h(n) that estimates the cost from a given node n to the goal node.

g(n): The cost from the start node to the current node.

f(n): The total estimated cost, f(n) = g(n) + h(n).

✅ Sample Input/Output:
Sample Input:

yaml
Copy
Edit
Run A* from 'a' to 'z'
Graph: 
a: [(b, 4), (c, 3)]
b: [(f, 5), (e, 12)]
c: [(d, 7), (e, 10)]
d: [(e, 2)]
e: [(z, 5)]
f: [(z, 16)]
z: []

Heuristic values: 
a: 14, b: 12, c: 11, d: 6, e: 4, f: 11, z: 0
Sample Output:

rust
Copy
Edit
Path found: a -> c -> d -> e -> z
Total cost: 18
✅ Viva Questions with Answers:
Q1: What is the A* algorithm?
A1: A* is a search algorithm used for finding the shortest path in a graph. It combines the benefits of Dijkstra's algorithm (which finds the shortest path) and greedy best-first search (which uses heuristics to guide the search).

Q2: How does A* use heuristics?
A2: A* uses a heuristic to estimate the cost from the current node to the goal, which helps prioritize the nodes to explore, making it more efficient than Dijkstra's algorithm.

Q3: What is the f(n) in A*?
A3: f(n) is the total estimated cost to reach the goal from node n, calculated as f(n) = g(n) + h(n), where g(n) is the cost from the start node to n, and h(n) is the heuristic estimate to the goal.

Q4: What are the advantages of A* over other search algorithms?
A4: A* guarantees finding the shortest path (if the heuristic is admissible) and is more efficient than algorithms like Dijkstra's because it uses heuristics to guide the search.

Q5: What happens if the heuristic used in A* is not admissible?
A5: If the heuristic is not admissible (i.e., it overestimates the cost), A* may not find the optimal path.

Q6: What is the difference between A* and Dijkstra's algorithm?
A6: Dijkstra's algorithm is a special case of A* where the heuristic h(n) is zero for all nodes. Dijkstra's algorithm does not use any estimate to guide the search, while A* does, making A* more efficient in many cases.

Q7: What data structure is used for the open list in A*?
A7: A priority queue (min-heap) is used to manage the open list, which allows efficient extraction of the node with the lowest f(n) value.

Q8: Why is a visited set used in A*?
A8: A visited set is used to keep track of nodes that have already been processed, preventing the algorithm from revisiting them and getting stuck in loops.

Q9: Can A* be used for real-time applications?
A9: Yes, A* is commonly used in robotics, video games, and navigation systems for real-time pathfinding, as it efficiently finds the shortest path.

Q10: What is the role of g(n) and h(n) in the A* algorithm?
A10: g(n) is the cost to reach node n from the start node, and h(n) is the heuristic estimate of the cost from n to the goal. Their sum, f(n) = g(n) + h(n), is used to prioritize nodes in the search.

Q11: What type of graphs can A* be applied to?
A11: A* can be applied to both directed and undirected graphs, as long as an admissible heuristic is available.

Q12: What happens if two nodes have the same f(n) value in A*?
A12: If two nodes have the same f(n) value, A* will explore them in the order they were added to the open list, often prioritizing the node with the smaller g(n) value.

Q13: How do you know if the goal has been reached in A*?
A13: The goal is considered reached when the node with the goal's label is popped from the priority queue, and the corresponding path is returned.

Q14: How can A* handle dynamic graphs?
A14: A* can handle dynamic graphs by re-calculating paths when changes occur, although it may need to reprocess certain parts of the graph based on the changes.

Q15: Is A* guaranteed to find the shortest path?
A15: Yes, if the heuristic used in A* is admissible (never overestimates the true cost), the algorithm is guaranteed to find the shortest path.

'''