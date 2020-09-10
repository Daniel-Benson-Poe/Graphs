# Create an adjacency list that includes edge weights
class Graph:
    def __init__(self):
        self.vertices = {
            "A" : {"B" : 1},
            "B" : {"C" : 3, "D" : 2},
            "C" : {},
            "D" : {},
            "E" : {"D" : 1},
        }

# We'll represent that same data using an adjacency matrix
class Graph:
    def __init__(self):
        self.edges = [[0,1,0,0,0],
                      [0,0,3,2,0],
                      [0,0,0,0,0],
                      [0,0,0,0,0],
                      [0,1,0,1,0],]

# CHALLENGE 1:
# Start with adjacency list
class Graph:
    def __init__(self):
        self.vertices = {
            "A" : {"B" : 1},
            "B" : {"C" : 3, "D" : 2, "E" : 1},
            "C" : {"E" : 4},
            "D" : {"E" : 2},
            "E" : {"F" : 3},
            "F" : {},
            "G" : {"D" : 1}
        }

# Next using adjacency matrix
class Graph:
    def __init__(self):
        self.edges = [[0,1,0,0,0,0,0],
                      [0,0,3,2,1,0,0],
                      [0,0,0,0,4,0,0],
                      [0,0,0,0,2,0,0],
                      [0,0,0,1,0,3,0],
                      [0,0,0,0,0,0,0],
                      [0,0,0,1,0,0,0]
                      ]