from collections import defaultdict

# Example graph class

class Graph:
    # constructor
    def __init__(self, V):
        self.V = V  # number of vertices
        # default dictionary to store graph
        self.graph = defaultdict(list)
        self.adj = [[] for i in range(V)]  # adjacency lists

    # function to add edge to graph
    def addEdge(self, u, v):
        self.graph[u].append(v)
        self.adj[u].append(v)

    """ BFT Applications:
        Shortest path and minimum spanning tree for unweighted graph
        Peer to peer networks
        Crawlers in search engines
        Social networking websites
        GPS Navigation systems
        Broadcasting in network
        Garbage collection
        Cycle detection in undirected graph
        Ford-Fulkerson Algorithm
        Test if graph is bipartite
        Path Finding
        Finding all nodes within one connected component
    """
    
    # function to print BFT of graph
    def BFT(self, s):
        # mark all vertices not visited
        visited = [False] * (len(self.graph))
        # create queue for BFS
        queue = []
        # mark source node as visited and enqueue it
        queue.append(s)
        visited[s] = True
        # while queue is not empty
        while queue:
            # dequeue a vertex from queue and print it
            s = queue.pop(0)
            print(s)

            # get all adjacent vertices of the dequeued vertex s.
            # If an adjacent has not been visited, mark it as 
            # visited and enqueue it
            for i in self.graph[s]:
                if visited[i] == False:
                    queue.append(i)
                    visited[i] = True

    """ DFT Applications: 
        For weighted graph, produces minimum spanning tree of all pair shortest path tree;
        Detecting cycles - check for back edges;
        Path finding
        Topological Sorting
        Test if graph is bipartite 
        Finding strongly connected compononents of a graph
        Solving puzzles with only one solution - mazes
    """

    # function used by DFT recursion
    def DFTUtil(self, v, visited):
        # mark current node as visited and print it
        visited[v] = True
        print(v)

        # recur for all the vertices adjacent to this vertex
        for i in self.graph[v]:
            if visited[i] == False:
                self.DFTUtil(i, visited)

    # function for DFT; uses DFTUtil
    def DFT(self, v):
        # mark all vertices as not visited
        visited = [False] * (max(self.graph)+1)
        # call recursive helper function to print DFT
        self.DFTUtil(v, visited)

    # function for iterative DFT using a Stack
    def DFTStack(self, s):
        visited = [False for i in range(self.V)]

        # create stack
        stack = []
        # push current source node
        stack.append(s)

        while len(stack):
            # pop a vertex from stack and print it
            s = stack[-1]
            stack.pop()

            # stack may contain same vertex twice. We need to print the popped item only if not visited
            if (not visited[s]):
                print(s)
                visited[s] = True

            # get all adjacent vertices of popped vertex s. If adjacent has not been visited, push to stack
            for node in self.adj[s]:
                if (not visited[node]):
                    stack.append(node)

if __name__ == "__main__":
    # g = Graph() 
    # g.addEdge(0, 1) 
    # g.addEdge(0, 2) 
    # g.addEdge(1, 2) 
    # g.addEdge(2, 0) 
    # g.addEdge(2, 3) 
    # g.addEdge(3, 3) 
    
    # print ("Following is Breadth First Traversal"
    #                 " (starting from vertex 2)") 
    # # g.BFT(2) 
    # g.DFT(2)

    g = Graph(5); # Total 5 vertices in graph  
    g.addEdge(1, 0);  
    g.addEdge(0, 2);  
    g.addEdge(2, 1);  
    g.addEdge(0, 3);  
    g.addEdge(1, 4);  
    
    print("Following is Depth First Traversal")  
    g.DFTStack(0) 
    # This code is contributed by ankush_953 