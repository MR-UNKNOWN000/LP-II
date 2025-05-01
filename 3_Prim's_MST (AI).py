import sys

class Graph():
    def __init__(self, vertices):
        self.V = vertices
        self.graph = [[0 for column in range(vertices)]
                      for row in range(vertices)]

    def printMST(self, parent):
        print("Edge \tWeight")
        for i in range(1, self.V):
            print(parent[i]+1, "-", i+1, "\t", self.graph[parent[i]][i])

    def minKey(self, key, mstSet):
        min = sys.maxsize
        min_index = -1

        for v in range(self.V):
            if key[v] < min and not mstSet[v]:
                min = key[v]
                min_index = v

        return min_index

    def primMST(self):
        key = [sys.maxsize] * self.V
        parent = [None] * self.V
        key[0] = 0
        mstSet = [False] * self.V
        parent[0] = -1

        for _ in range(self.V):
            u = self.minKey(key, mstSet)
            mstSet[u] = True

            for v in range(self.V):
                if self.graph[u][v] > 0 and not mstSet[v] and key[v] > self.graph[u][v]:
                    key[v] = self.graph[u][v]
                    parent[v] = u

        self.printMST(parent)

if __name__ == '__main__':
    g = Graph(6)
    g.graph = [
        [0, 2, 0, 1, 4, 0],  # Node 1
        [2, 0, 3, 0, 0, 7],  # Node 2
        [0, 3, 0, 5, 0, 8],  # Node 3
        [1, 0, 5, 0, 9, 0],  # Node 4
        [4, 0, 0, 9, 0, 0],  # Node 5
        [0, 7, 8, 0, 0, 0]   # Node 6
    ]

    g.primMST()



    '''✅ Title:
Minimum Spanning Tree using Prim’s Algorithm

✅ Algorithm Steps:
Start with a graph represented by an adjacency matrix or list.

Initialize a key array to track minimum edge weight for each vertex (initially infinity).

Mark all vertices as not included in MST (using a boolean array).

Start from the first vertex (key[0] = 0), and select the vertex with the minimum key not yet in the MST.

Include this vertex in the MST.

Update key values and parent index of adjacent vertices.

If the weight of the edge from current to adjacent is less than the key value and vertex is not in MST, update it.

Repeat steps 4–6 until all vertices are included.

Print the parent array to show the MST edges and their weights.

✅ Sample Output:
nginx
Copy
Edit
Edge    Weight
1 - 4    1
2 - 1    2
3 - 2    3
4 - 1    1
5 - 1    4
6 - 2    7
(Output may vary depending on graph input. Each line shows an edge and its weight in the MST.)

✅ Time and Space Complexity:
Time Complexity: O(V²) using an adjacency matrix

Space Complexity: O(V²) for the matrix and O(V) for auxiliary arrays

✅ Short Theory:
Prim’s Algorithm is a greedy algorithm used to find the Minimum Spanning Tree (MST) of a connected, weighted, undirected graph. It builds the MST by starting from an arbitrary vertex and always choosing the minimum weight edge that connects a new vertex to the MST. The algorithm continues until all vertices are included.

✅ Features:
Greedy approach ensuring optimal MST

Efficient for dense graphs

Maintains a parent[] array to reconstruct MST

Works only for connected graphs

✅ Viva Questions & Answers:
Q1: What does Prim’s algorithm do?
A1: It finds the Minimum Spanning Tree (MST) of a connected, undirected, weighted graph.

Q2: What is a Minimum Spanning Tree?
A2: A subset of edges that connects all vertices with minimum possible total weight and no cycles.

Q3: What is the difference between Prim’s and Kruskal’s algorithms?
A3: Prim’s grows the MST from one vertex; Kruskal’s adds the smallest edge overall while avoiding cycles.

Q4: Which data structures are used in Prim’s algorithm?
A4: Arrays (key[], parent[], mstSet[]) and an adjacency matrix (or list).

Q5: Why do we use sys.maxsize?
A5: It represents infinity to initialize the key array with maximum possible values.

Q6: What is the time complexity of Prim’s algorithm?
A6: O(V²) with an adjacency matrix; O(E log V) with a min-heap and adjacency list.

Q7: Can Prim’s algorithm work on disconnected graphs?
A7: No, it only works on connected graphs.

Q8: How is the MST represented in the output?
A8: Using the parent[] array where each entry shows which vertex is connected to which.

Q9: What is the starting point of Prim’s algorithm?
A9: Any arbitrary vertex; commonly vertex 0 is chosen.

Q10: Is Prim’s algorithm greedy or dynamic?
A10: It is a greedy algorithm.'''

    