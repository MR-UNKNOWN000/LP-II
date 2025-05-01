class DisjointSet:
    def __init__(self, n):
        self.parent = list(range(n))
    
    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])  # Path compression
        return self.parent[x]
    
    def union(self, x, y):
        xroot = self.find(x)
        yroot = self.find(y)
        if xroot == yroot:
            return False
        self.parent[yroot] = xroot
        return True

def kruskal_mst(edges, n):
    # Sort edges based on weight
    edges.sort(key=lambda x: x[2])
    
    ds = DisjointSet(n)
    mst = []
    total_weight = 0

    for u, v, weight in edges:
        if ds.union(u, v):
            mst.append((u, v, weight))
            total_weight += weight

    return mst, total_weight

# Define edges (u, v, weight)
edges = [
    (0, 1, 4),
    (0, 7, 8),
    (1, 2, 8),
    (1, 7, 11),
    (2, 3, 7),
    (2, 8, 2),
    (2, 5, 4),
    (3, 4, 9),
    (3, 5, 14),
    (4, 5, 10),
    (5, 6, 2),
    (6, 7, 1),
    (6, 8, 6),
    (7, 8, 7),
]

n = 9  # Number of vertices (0 to 8)

mst, total_weight = kruskal_mst(edges, n)

print("Edges in MST:")
for u, v, weight in mst:
    print(f"{u} - {v}: {weight}")

print(f"Total weight of MST: {total_weight}")

'''✅ Title:
Minimum Spanning Tree (MST) using Kruskal’s Algorithm

✅ Algorithm Steps:
Input: A weighted undirected graph as a list of edges.

Sort all edges in non-decreasing order of their weights.

Initialize a Disjoint Set (Union-Find) for cycle detection.

Initialize MST as an empty list.

For each edge in the sorted list:

If the edge connects two different sets (i.e., no cycle):

Add the edge to MST.

Perform union of the two sets.

Repeat until MST contains (V - 1) edges.

Output the MST and total weight.

✅ Python Output (for the provided graph):
yaml
Copy
Edit
Edges in MST:
6 - 7: 1
2 - 8: 2
5 - 6: 2
0 - 1: 4
2 - 5: 4
2 - 3: 7
0 - 7: 8
3 - 4: 9
Total weight of MST: 37
✅ Time and Space Complexity:
Time Complexity: O(E log E)
(due to edge sorting + union-find operations with path compression)

Space Complexity: O(V)
(for parent array in disjoint set)

✅ Data Structures Used:
List → to store edges and MST.

Disjoint Set (Union-Find) → to detect and avoid cycles efficiently.

✅ Short Theory:
Kruskal’s Algorithm is a Greedy algorithm used to find the Minimum Spanning Tree of a weighted undirected graph. It works by sorting all edges by weight and adding them to the MST, ensuring no cycles using a Disjoint Set (Union-Find structure).

✅ Features:
Greedy strategy.

Efficient with sparse graphs.

Ensures no cycles in the MST.

Uses Disjoint Set for optimization.

✅ Viva Questions & Answers:
Q1: What is Kruskal’s algorithm used for?
A1: To find the Minimum Spanning Tree (MST) of a graph.

Q2: What is the core data structure used in Kruskal's?
A2: Disjoint Set (Union-Find).

Q3: What is a spanning tree?
A3: A subgraph that connects all vertices without any cycles and with minimum number of edges (V-1).

Q4: Can Kruskal’s algorithm handle negative weights?
A4: Yes, as long as it is an undirected graph.

Q5: How are cycles avoided in Kruskal’s algorithm?
A5: Using Union-Find (Disjoint Set) to detect if two nodes are already in the same set.

Q6: What is the time complexity of Kruskal’s algorithm?
A6: O(E log E), where E is the number of edges.

Q7: What is path compression in Disjoint Set?
A7: An optimization that flattens the structure of the tree, speeding up future find() operations.

Q8: When does Kruskal’s algorithm stop?
A8: When (V-1) edges have been added to the MST.

Q9: What happens if the graph is disconnected?
A9: Kruskal’s algorithm will not produce a valid MST — it works only for connected graphs.

Q10: Is Kruskal better than Prim’s algorithm?
A10: Kruskal is better for sparse graphs; Prim’s is often better for dense graphs with adjacency matrix.'''