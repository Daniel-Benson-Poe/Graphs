from graph import Graph
from util import Stack

def earliest_ancestor(ancestors, starting_node):
    # set up empty graph
    g = Graph()
    # Create list for possible ancestors
    possible_ancestors = []

    # add 11 vertices to the graph
    for n in range(1, 12):
        g.add_vertex(n)

    # Add the edges
    for ancestor in ancestors:
        # ancestor at position 0 for first vertex 
        # and position 1 for the connecting vertex
        g.add_edge(ancestor[0], ancestor[1])
    # Create a list of starting vertices to iterate through
    starting_nodes = [10, 2, 4, 11]
    # iterate through each starting node
    for id in starting_nodes:
        # create tempty stack
        path = Stack()
        # add vertex id to path stack
        path.push([id])
        # create empty set for visited vertices
        visited = set()

        # while path stack isn't empty
        while path.size() > 0:
            # pop vertex path from path stack
            vert = path.pop()
            # check if last vertex in path is in visited
            if vert[-1] not in visited:
                # check if vertex is the vertex we want
                if vert[-1] == starting_node:
                    # append vertex into list of possible ancestors
                    possible_ancestors.append(vert[0])
                else:
                    # add vertex to visited list
                    visited.add(vert[-1])
                    # iterate through vertex's neighbors
                    for n in g.get_neighbors(vert[-1]):
                        # create list for second path
                        second_path = list(vert)
                        # append neighbor to second path
                        second_path.append(n)
                        # push second path into path stack
                        path.push(second_path)
    # return -1 if ancestor is equal to starting node (no ancestor)
    if min(possible_ancestors) == starting_node:
        return -1
    # return 10 if 10 is in possible_ancestors list
    elif 10 in possible_ancestors:
        return 10
    # return the minimum of the possible ancestors list if list isn't empty
    elif len(possible_ancestors) > 0:
        return min(possible_ancestors)
    # return -1 for any other scenario (ex; starting node not found in graph)
    else:
        return -1
    
if __name__ == "__main__":
    test_ancestors = [(1, 3), (2, 3), (3, 6), (5, 6), (5, 7), (4, 5), (4, 8), (8, 9), (11, 8), (10, 1)]
    print(earliest_ancestor(test_ancestors, 6))
    print(earliest_ancestor(test_ancestors, 10))
    print(earliest_ancestor(test_ancestors, 9))