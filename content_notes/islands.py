# Write a function that takes a 2D binary array and returns the number of 1
# islands. An island consists of 1s that are connected to the north, south,
# east or west. For example:
#
# connected components

class Stack:
    def __init__(self):
        self.stack = []
    
    def push(self, value):
        self.stack.append(value)

    def pop(self):
        if self.size() > 0:
            return self.stack.pop()
        else:
            return None

    def size(self):
        return len(self.stack)

islands = [[1, 0, 0, 1, 1, 0, 1, 1, 0, 1],
           [0, 0, 1, 1, 0, 1, 0, 0, 0, 0],
           [0, 1, 1, 1, 0, 0, 0, 1, 0, 1],
           [0, 0, 1, 0, 0, 1, 0, 0, 1, 1],
           [0, 0, 1, 1, 0, 1, 0, 1, 1, 0],
           [0, 1, 0, 1, 1, 1, 0, 1, 0, 0],
           [0, 0, 1, 0, 0, 1, 1, 0, 0, 0],
           [1, 0, 1, 1, 0, 0, 0, 1, 1, 0],
           [0, 1, 1, 0, 0, 0, 1, 1, 0, 0],
           [0, 0, 1, 1, 0, 1, 0, 0, 1, 0]]



# islands = [[0, 1, 0, 1, 0],
#            [1, 1, 0, 1, 1],
#            [0, 0, 1, 0, 0],
#            [1, 0, 1, 0, 0],
#            [1, 1, 0, 0, 0]]

# function to get neighbors of island found at islands position row, col
def get_neighbors(row, col, islands):
    # create empty array to store neighbors
    neighbors = []

    # check if input row is greater than 0, allowing us to 
    # subract 1 when calling the position in the islands array
    # Also check if islands at position row-1, col is 1
    if row > 0 and islands[row-1][col] == 1:
        # if so, append (row-1, col) tuple to the neighbors array
        neighbors.append((row-1, col))
    # check if input row is less than the length of islands-1
    # allowing us to add 1 when calling the position in the islands array
    # also check if islands at position row+1, col is 1
    if row < (len(islands)-1) and islands[row+1][col] == 1:
        # if so, append (row+1, col) tuple to the neighbors array
        neighbors.append((row+1, col))
    # check if input col is greater than 0 allowing us to
    # subract 1 when calling the position in the islands array
    # also check if islands at position row, col-1 is 1
    if col > 0 and islands[row][col-1] == 1:
        # if so, append (row, col-1) tuple to neighbors
        neighbors.append((row, col-1))
    # check if input col is less than length of islands at position row - 1
    # allowing us to add 1 when calling the position in the islands array
    # also check if islands at position row, col+1 is 1
    if col < len(islands[row]) - 1 and islands[row][col+1] == 1:
        # if so, append (row, col+1) tuple to neighbors
        neighbors.append((row, col+1))

    return neighbors

def dft(row, col, islands, visited):
    # create empty stack
    s = Stack()

    # push inputs (row, col) into stack as a tuple 
    s.push((row, col))

    # while stack is not empty
    while s.size() > 0:
        r, c = s.pop()  # create variables r, c and set them equal to row, col popped from stack

        # check if tuple (r, c) is in visited
        if (r, c) not in visited:
            # add (r, c) as a tuple in visited array
            visited.add((r, c))

            # get neighbors of row 'r' and column 'c' in islands
            for neighbor in get_neighbors(r, c, islands):
                # push neighbor into stack
                s.push(neighbor)

def island_counter(islands):
    # create new set for visited islands; store (row, col) tuples here
    visited = set()

    island_count = 0

    # walk through each cell in the islands matrix
    for row in range(len(islands)):
        for col in range(len(islands[row])):

            # if it's not visited and it's a 1
            if (row, col) not in visited and islands[row][col] == 1:

                # DFT from that cell, marking each as visited
                dft(row, col, islands, visited)

                # increment island counter
                island_count += 1

    return island_count

if __name__ == "__main__":
    # print(get_neighbors(2, 3, islands))  # should return [(1, 3), (2, 2)]
    # print(get_neighbors(3, 4, islands))  # should return []
    # print(get_neighbors(1, 2, islands))  # should return [(2, 2), (1, 1), (1, 3)]
    print(island_counter(islands))  # should return 4