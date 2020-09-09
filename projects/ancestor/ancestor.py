from graph import Graph
from util import Stack

def earliest_ancestor(ancestors, starting_node):
    # set up empty graph
    g = Graph()
    possible_ancestors = []

    # add 11 vertices to the graph
    for n in range(1, 12):
        g.add_vertex(n)

    # Add the edges
    for ancestor in ancestors:
        g.add_edge(ancestor[0], ancestor[1])
    starting_nodes = [10, 2, 4, 11]
    for id in starting_nodes:
        path = Stack()
        path.push([id])
        visited = set()

        while path.size() > 0:
            vert = path.pop()
            if vert[-1] not in visited:
                if vert[-1] == starting_node:
                    possible_ancestors.append(vert[0])
                else:
                    visited.add(vert[-1])
                    for n in g.get_neighbors(vert[-1]):
                        second_path = list(vert)
                        second_path.append(n)
                        path.push(second_path)
    if min(possible_ancestors) == starting_node:
        return -1
    elif 10 in possible_ancestors:
        return 10
    elif len(possible_ancestors) > 0:
        return min(possible_ancestors)
    else:
        return -1
    
if __name__ == "__main__":
    test_ancestors = [(1, 3), (2, 3), (3, 6), (5, 6), (5, 7), (4, 5), (4, 8), (8, 9), (11, 8), (10, 1)]
    print(earliest_ancestor(test_ancestors, 6))
    print(earliest_ancestor(test_ancestors, 10))
    print(earliest_ancestor(test_ancestors, 9))