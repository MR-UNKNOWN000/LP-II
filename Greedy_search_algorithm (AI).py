import heapq

def greedy_search(graph, start, goal, heuristic):
    visited = set()
    queue = []

    # Priority queue with tuples: (heuristic_cost, node, path)
    heapq.heappush(queue, (heuristic[start], start, [start]))

    while queue:
        cost, current, path = heapq.heappop(queue)

        if current == goal:
            return path

        if current in visited:
            continue
        visited.add(current)

        for neighbor in graph.get(current, []):
            if neighbor not in visited:
                heapq.heappush(queue, (heuristic[neighbor], neighbor, path + [neighbor]))

    return None  # If no path is found

# Sample graph (adjacency list)
graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': ['F'],
    'F': []
}

# Heuristic values (h(n)): estimated cost from each node to goal 'F'
heuristic = {
    'A': 3,
    'B': 2,
    'C': 1,
    'D': 6,
    'E': 1,
    'F': 0
}

# Define start and goal nodes
start_node = 'A'
goal_node = 'F'

# Run Greedy Search
result = greedy_search(graph, start_node, goal_node, heuristic)

# Output the result
print("Path found by Greedy Search:", result)

'''✅ Title:
Greedy Best-First Search Algorithm

✅ Algorithm Steps:
Initialize a priority queue with the start node, prioritized by heuristic value h(n).

While the queue is not empty:

Remove the node with the lowest heuristic value.

If it’s the goal, return the path.

Else, expand its neighbors not yet visited.

Push neighbors into the queue with their heuristic values.

Continue until the goal is found or the queue is empty.

✅ Short Theory:
Greedy Best-First Search is an informed search algorithm that uses a heuristic function h(n) to estimate the cost from a node to the goal. It always expands the node that appears to be closest to the goal (smallest h(n)), without considering the path cost taken so far.

✅ Features:
Uses a priority queue (min-heap).

Informed search: guided by heuristic.

Faster than uninformed searches in many cases.

Does not guarantee optimal path.

✅ Sample Output:
pgsql
Copy
Edit
Path found by Greedy Search: ['A', 'C', 'F']
✅ Time and Space Complexity:
Time Complexity: O(b^m) where b = branching factor, m = depth.

Space Complexity: O(b^m) due to the priority queue and visited set.

✅ Uses:
Game AI (pathfinding)

Network routing

Robot navigation

✅ Which data structure is used?
Priority Queue using heapq.

✅ Viva Questions & Answers:
Q1: What does Greedy Search prioritize?
A1: It prioritizes nodes with the lowest heuristic value (h(n)).

Q2: Is the solution always optimal?
A2: No, it may find a sub-optimal solution since it doesn't consider path cost g(n).

Q3: What is the main advantage of Greedy Search?
A3: It's faster than uninformed searches because it uses domain-specific knowledge.

Q4: What is the difference between A* and Greedy Best-First Search?
A4: A* uses f(n) = g(n) + h(n), while Greedy uses only h(n).

Q5: Is Greedy Search complete?
A5: No, it may fail to find a solution even if one exists.

'''