def dfs(visited,graph,node):
    if node not in visited:
        print(node,end = " ")
        visited.add(node)
        for neighbour in graph[node]:
            dfs(visited, graph, neighbour)

def bfs(visited,graph,node,queue):
    visited.add(node)
    queue.append(node)

    while queue:
        s = queue.pop(0)
        print(s,end = " ")
        for neighbour in graph[s]:
            if neighbour not in visited:
                visited.add(neighbour)
                queue.append(neighbour)

def main():
    visited1 = set() # TO keep track of DFS visited nodes
    visited2 = set() # TO keep track of BFS visited nodes
    queue = []       # For BFS
    n = int(input("Enter number of nodes : "))
    graph = dict()

    for i in range(1,n+1):
        edges = int(input("Enter number of edges for node {} : ".format(i)))
        graph[i] = list()
        for j in range(1,edges+1):
            node = int(input("Enter edge {} for node {} : ".format(j,i)))
            graph[i].append(node)

    print("The following is DFS")
    dfs(visited1, graph, 1)
    print()
    print("The following is BFS")
    bfs(visited2, graph, 1, queue)

if __name__=="__main__":
    main()


    # graph = {
    #     '1' : ['2','3'],
    #     '2' : ['4', '5'],
    #     '3' : ['6','7'],
    #     '4' : [],
    #     '5' : [],
    #     '6' : [],
    #     '7' : []
    #     DFS : 1 2 4 5 3 6 7 
    #     BFS : 1 2 3 4 5 6 7 
    # }

'''
🔹 AI Practical: Graph Traversal using DFS and BFS
✅ Title:
Graph Traversal using Depth First Search (DFS) and Breadth First Search (BFS)

✅ Algorithm Used:
🔸 Depth First Search (DFS)
Steps:

Start from the selected node.

Visit the node and mark it as visited.

Recursively visit all unvisited neighbors.

🔸 Breadth First Search (BFS)
Steps:

Start from the selected node.

Visit the node and mark it as visited.

Add it to a queue.

While the queue is not empty:

Remove a node from the queue.

Visit all its unvisited neighbors and add them to the queue.

✅ Flowchart Description:
If you need a visual, I can generate a diagram. Here's the logical flow for both:

DFS Flow:

sql
Copy
Edit
Start → Visit node → Add to visited → For each neighbor:
   → If not visited → Recur DFS → End
BFS Flow:

sql
Copy
Edit
Start → Visit node → Add to visited → Enqueue
→ While queue not empty:
   → Dequeue node → Visit neighbors → If not visited → Mark & Enqueue → End
✅ Feature Requirements:
Python 3.x

Data structures: set, list, and dict

Input from user (number of nodes and edges)

Knowledge of recursive functions and queue usage

✅ Short Theory:
Graph traversal is the process of visiting each node in a graph exactly once. Two popular techniques are:

DFS (Depth First Search): Explores as far as possible along each branch before backtracking.

BFS (Breadth First Search): Explores all neighbors at the current level before moving deeper.

These algorithms are essential for solving problems like pathfinding, connected components, and cycle detection in AI and other domains.

✅ Important Definitions:
Graph: A collection of nodes (vertices) connected by edges.

DFS: Traversal technique that uses recursion (or a stack) to explore depth-wise.

BFS: Traversal technique that uses a queue to explore level-wise.

Visited Set: Keeps track of already visited nodes to prevent infinite loops.

✅ Sample Input/Output:
Let’s say the input is:

vbnet
Copy
Edit
Nodes: 3  
Node 1 connects to: 2, 3  
Node 2 connects to: (none)  
Node 3 connects to: (none)  
DFS Output: 1 2 3
BFS Output: 1 2 3

✅ Time and Space Complexity:
🔸 Time Complexity:
DFS: O(V + E)

BFS: O(V + E)

🔸 Space Complexity:
DFS: O(V)

BFS: O(V)

✅ Which Algorithm Uses a Queue?
DFS: Does not use a queue; uses recursion (stack).

BFS: Uses a queue to store nodes.

✅ Which is Better and Why?
DFS:

Use Case: Useful for deep exploration, solving puzzles, topological sorting, and detecting cycles.

Advantages: Memory-efficient in deep trees, fast for long paths.

Disadvantages: May not find the shortest path in unweighted graphs, and can get stuck in cycles without a visited set.

BFS:

Use Case: Best for finding the shortest path in an unweighted graph, connectivity checks, and minimum steps in puzzles.

Advantages: Guarantees the shortest path, explores level by level.

Disadvantages: Requires more memory due to the queue and may be slower in sparse graphs.

✅ Summary:
BFS: Best for shortest path, level-wise exploration.

DFS: Best for deep exploration and exhaustive searches.

✅ Viva Questions with Answers:
Q1: What is a graph in data structures?
A: A graph is a non-linear data structure consisting of vertices (nodes) and edges that connect pairs of nodes.

Q2: What are the types of graphs?
A: Directed, Undirected, Weighted, Unweighted, Cyclic, and Acyclic graphs.

Q3: What is DFS?
A: DFS (Depth First Search) is a graph traversal technique that explores as far as possible along each branch before backtracking.

Q4: What is BFS?
A: BFS (Breadth First Search) is a graph traversal technique that visits all the neighbors of a node before moving to the next level.

Q5: What data structure is used in DFS?
A: Stack (implicitly through recursion or explicitly using a stack).

Q6: What data structure is used in BFS?
A: Queue

Q7: Is DFS recursive or iterative in your code?
A: Recursive

Q8: Can BFS be implemented recursively?
A: BFS is typically implemented using a queue (iteratively), but it can be simulated recursively with extra effort.

Q9: What is the time complexity of DFS and BFS?
A: O(V + E), where V = vertices and E = edges.

Q10: What happens if we don’t use a visited set?
A: It may cause infinite loops if the graph contains cycles.

Q11: What kind of problems can be solved using DFS and BFS?
A: Pathfinding, cycle detection, shortest path (BFS), connected components, and solving puzzles/mazes.

Q12: What is the difference between tree traversal and graph traversal?
A: Tree traversal is simpler as trees don’t have cycles, while graph traversal requires tracking visited nodes to avoid repetition or infinite loops.

Q13: What is the input format for this practical?
A: The user inputs the number of nodes, number of edges per node, and the connected nodes (edges) manually.

Q14: Is the graph directed or undirected in your code?
A: Directed, since edges are added in one direction only.

Q15: Can we find the shortest path using DFS?
A: DFS is not ideal for shortest path. BFS is better suited for unweighted graphs because it explores level by level.

'''