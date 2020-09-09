### Types of Graphs ###

# What determines the type of graph that should be used? #
    # The nature of the relationship being represented!
# What if the relationship is described as "one way"? #
    # Use a directed graph
    # Example: a representation of debt to others
# Bidirectional exceptions? #
    # Of course there are! 
    # Road maps (all roads are one way) but most roads allow traffic in both directions
# What about a mutual exchange relationship? #
    # That's right! An undirected graph
    # Example: A representation of past exchanges between users
# But what about this cyclic nonsense? #
    # A graph is cyclic if it forms a circle - i.e. if you follow the edges and you arrive at an already-visited vert, it's cyclic
    # Any undirected graph is cyclic - you can travel back across the same edge, returning to an already-visited vert
# Then acyclic should be... #
    # You guessed it! If you cannot form a cycle (i.e. if you follow the edges and it is impossible for you to return to an already-visited vert)
# Weighted graphs can be heavy...but what are they? #
    # They have values associated with their edges - for some graphs, not all edges are made equally
    # The value assigned to a given edge is known as a weight
    # Weights can represent any number of things, such as length of a road between cities.
# DAG nabbit, now we're getting into the complicated stuff. What are Directed Acyclic Graphs? #
    # These are, simply put, directed graphs with not cycles - every edge is directed from earlier to later (think sequential order)
    # What are the use of these things?
        ## Spreadsheet: vertex represents each cell and an edge for where one cell's formulat uses another cell's value
        ## Milestones and activities of largescale project where topological ordering can help optimize the schedule of the projects to use as  little time as possible
        ## Collections of events and their influence on each other: family trees, version histories, etc.
        ## Closer to home: git uses DAG to represent commits.

### GRAPH REPRESENTATIONS ###   

# Adjacency List #
    # The graph stores a list of vertices
    # For each vertex it stores a list of each connected vertex
    # Code example: The keys represent each node/vertex in the graph, while the values in the curly braces represent the corresponding neighbors
        class Graph:
            def __init__(self):
                self.vertices = {
                    "A" : {"B"},
                    "B" : {"C", "D"},
                    "C" : {"E"},
                    "D" : {"F", "G"},
                    "E" : {"C"},
                    "F" : {"C"},
                    "G" : {"A", "F"}
                }

# Adjacency Matrix #
    # An n-dimensional array that can present representation of weighted edges
    # Code example: 0 denotes lack of relationship; any other value present represents edge label or edge weight
        class Graph:
            def __init__(self):
                self.edges = [[0,1,0,0,0,0,0],
                              [0,0,1,1,0,0,0],
                              [0,0,0,0,1,0,0],
                              [0,0,0,0,0,1,1],
                              [0,0,1,0,0,0,0],
                              [0,0,1,0,0,0,0],
                              [1,0,0,0,0,1,0]]

# Understanding the strengths and drawbacks of both
            Space   Add Vert    Remove Vert    Add Edge    Remove Edge    Get All Edges
Matrix      O(V^2)    O(V)         O(V^2)        O(1)          O(1)          O(V)
List        O(V+E)    O(1)         O(V)          O(1)          O(1)          O(1)

### SEARCHING A GRAPH ###

# Bread First Search (BFS)
    # Explores the graph outward in rings of increasing distance from starting vertex
    # Algorithm never attempts to explore a vert it has already explores is is currently exploring
    # Applications:
        # Pathfinding, routing
        # Finding neighbor nodes in P2P network (like BitTorrent)
        # Web Crawlers (Google Search, Yahoo Search, etc)
        # Finding people n connections away on social network
        # Find neighboring locations on graph
        # Broadcasting in a network
        # Cycle detection in a graph
        # Finding connected Components
        # Solving several theoretical graph problems
    # Track which nodes we need to follow up on using a queue (first in, first out)
    # BFS Graph Pseudocode
        BFS(graph, startVert):
            for v of graph.vertexes:
                v.color = white  # implementing white as unvisited verts

            startVert.color = gray  # implementing gray as verts whose neighbors are being explored
                queue.enqueue(startVert)  # insert starting vert into queue

            while !queue.isEmpty():  # Check if the queue is not empty
                u = queue[0]  # Peek at head of the queue, but not to dequeue

                for v of u.neighbors:
                    if v.color == white:
                        v.color = gray
                        queue.enqueue(v)
                
                queue.dequeue()
                u.color = black  # implementing black as verts with no unexplored neighbors

# Depth First Search (DFS)
    # "Dives" down the graph as far ast it can before backtgracking and exploring another branch
    # Neve3r attempts to explore a vert it has already explored or is in the process of exploring
    # Applications:
        # Finding minimum spanning trees of weighted graphs
        # path finding
        # detecting cycles in graphs
        # topological sorting, useful for scheduling sequences of dependent jobs
        # solving and generating mazes
    # Use of recursion for help remembering where we left off earlier on
    # DFS Graph Pseudocode
        DFS(graph):
            for v of graph.verts:
                v.color = white
                v.parent = null
            
            for v of graph.verts:
                if v.color == white:
                    DFS_visit(v)
        
        DFS_visit(v):
            v.color = gray

            for neighbor of v.adjacent_nodes:
                if neighbor.color == white:
                    neighbor.parent = v
                    DFS_visit(neighbor)
            
            v.color = black