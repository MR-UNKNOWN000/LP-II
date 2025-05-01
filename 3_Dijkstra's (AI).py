import heapq

def dijkstra(graph, start):
    # Distance to all nodes initially infinity
    distances = {node: float('inf') for node in graph}
    distances[start] = 0

    # Priority queue to get the node with the smallest distance
    pq = [(0, start)]

    while pq:
        current_distance, current_node = heapq.heappop(pq)

        # Skip if we already found a better path
        if current_distance > distances[current_node]:
            continue

        for neighbor, weight in graph[current_node]:
            distance = current_distance + weight

            # If new distance is smaller, update it
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(pq, (distance, neighbor))

    return distances

# Define the graph as an adjacency list
graph = {
    'A': [('B', 4), ('C', 5)],
    'B': [('A', 4), ('C', 11), ('D', 9), ('E', 7)],
    'C': [('A', 5), ('B', 11), ('E', 3)],
    'D': [('B', 9), ('F', 2)],
    'E': [('B', 7), ('C', 3), ('F', 6)],
    'F': [('D', 2), ('E', 6)]
}

# Run Dijkstra from source node 'A'
distances = dijkstra(graph, 'A')

print("Shortest distances from A:")
for node in distances:
    print(f"{node}: {distances[node]}")


    '''✅ Title:
Dijkstra’s Algorithm for Shortest Path

✅ Algorithm:
Dijkstra’s algorithm finds the shortest path from a single source node to all other nodes in a weighted graph with non-negative edge weights.

✅ Step-by-step Explanation:
Initialization:

Create a dictionary distances where every node has a distance of infinity initially, except the start node which has a distance of 0.

Priority Queue:

Use a min-heap priority queue to always explore the node with the smallest tentative distance.

Relaxation:

For each neighbor of the current node, calculate the new tentative distance.

If this new distance is less than the previously stored distance, update it and push it into the priority queue.

Repeat Until Queue is Empty:

The algorithm continues until all shortest distances from the source are finalized.

✅ Code Output Example:
Output for source node A:

vbnet
Copy
Edit
Shortest distances from A:
A: 0
B: 4
C: 5
D: 13
E: 8
F: 14
✅ Features / Key Points:
Greedy algorithm.

Uses a priority queue (min-heap).

Finds shortest path from one node to all others.

Only works correctly with non-negative edge weights.

✅ Time and Space Complexity:
Time Complexity: O((V + E) log V) using a priority queue (heap).

Space Complexity: O(V), where V is the number of vertices.

✅ Data Structures Used:
Priority Queue (Min-Heap) → to get the closest node quickly.

Dictionary → to store shortest distances.

✅ Best Among BFS, DFS, and Dijkstra:
Algorithm	Uses	Data Structure	Best For
BFS	Unweighted	Queue	Shortest path (equal cost)
DFS	Graph search	Stack (recursion)	Pathfinding, not shortest
Dijkstra	Weighted graphs (non-negative)	Priority Queue	Shortest path (with costs) ✅

👉 Dijkstra is best for shortest paths in weighted graphs, as BFS doesn't handle weights and DFS doesn't guarantee shortest path.

✅ Viva Questions with Answers:
Q1: What is Dijkstra’s Algorithm used for?
A1: It is used to find the shortest path from a source node to all other nodes in a weighted graph with non-negative weights.

Q2: Which data structure is used in Dijkstra’s Algorithm?
A2: A min-heap (priority queue) is used to efficiently fetch the next closest node.

Q3: Can Dijkstra’s Algorithm work with negative weights?
A3: No, it does not give correct results with negative weights. Use Bellman-Ford for that.

Q4: What is the time complexity of Dijkstra’s Algorithm?
A4: O((V + E) log V), where V is the number of vertices and E is the number of edges.

Q5: How does Dijkstra differ from BFS?
A5: BFS is used for unweighted graphs, while Dijkstra handles weighted graphs and gives the shortest path based on edge weights.

Q6: What happens if we don’t use a priority queue in Dijkstra?
A6: Without a priority queue, finding the next minimum distance node becomes slower, increasing the time complexity to O(V²).

Q7: What does the algorithm return?
A7: It returns the shortest distances from the source node to every other node.

Q8: Is Dijkstra a greedy algorithm?
A8: Yes, it always chooses the node with the smallest known distance, making greedy choices at each step.

Q9: Why does Dijkstra not work with negative weights?
A9: Because it assumes that once a node's shortest path is finalized, it won't change — which is not true in the presence of negative weights.

Q10: What real-life application uses Dijkstra's Algorithm?
A10: GPS navigation systems to find the shortest route between two locations.'''