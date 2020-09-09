from util import Stack, Queue

"""
Simple graph implementation
"""
from util import Stack, Queue  # These may come in handy

class Graph:

    """Represent a graph as a dictionary of vertices mapping labels to edges."""
    def __init__(self):
        self.vertices = {}

    def add_vertex(self, vertex_id):
        """
        Add a vertex to the graph.
        """
        self.vertices[vertex_id] = set()

    def add_edge(self, v1, v2):
        """
        Add a directed edge to the graph.
        """
        if v1 in self.vertices and v2 in self.vertices:
            self.vertices[v1].add(v2)
        else:
            raise IndexError("That vertex does not exist!")

    def get_neighbors(self, vertex_id):
        """
        Get all neighbors (edges) of a vertex.
        """
        return self.vertices[vertex_id]

    def bft(self, starting_vertex):
        """
        Print each vertex in breadth-first order
        beginning from starting_vertex.
        """
        # Create queue to hold nodes needed to visit
        to_visit = Queue()
        # create set to hold nodes already visited
        visited = set()
        # add starting node to the queue
        to_visit.enqueue(starting_vertex)
        # while queue is not empty:
        while to_visit.size() > 0:
            # dequee first entry
            v = to_visit.dequeue()

            # if not visited before
            if v not in visited:
                # print out the vertex
                print(v)
                # Add to the visited set
                visited.add(v)
                # enqueue all its neighbors
                for n in self.get_neighbors(v):
                    to_visit.enqueue(n)
        
    def dft(self, starting_vertex):
        """
        Print each vertex in depth-first order
        beginning from starting_vertex.
        """
        # Create stack to hold nodes to visit
        to_visit = Stack()
        # Create set to hold visited nodes
        visited = set()
        # add starting vertex to stack
        to_visit.push(starting_vertex)
        # While stack not empty
        while to_visit.size() > 0:
            # pop first entry
            v = to_visit.pop()

            # if not yet visited
            if v not in visited:
                # print out the vertex
                print(v)

                # add to visited set
                visited.add(v)

                # push all its neighbors into the stack
                for n in self.get_neighbors(v):
                    #print(f"Adding: {n}")
                    to_visit.push(n)

    def dft_recursive(self, starting_vertex, visited=set()):
        """
        Print each vertex in depth-first order
        beginning from starting_vertex.

        This should be done using recursion.
        """
        # here we only need to create our visited set
        # We then need to check if our starting_vertex is in 
        # the visited setg, if not, add it in
        # Then we need to iterate through each of the starting vertex's
        # neighbors, recursively calling this function using those
        # neighbors

        if starting_vertex not in visited:
            visited.add(starting_vertex)
            print(starting_vertex)

        for n in self.get_neighbors(starting_vertex):
            if n not in visited:
                self.dft_recursive(n, visited)

    def bfs(self, starting_vertex, destination_vertex):
        """
        Return a list containing the shortest path from
        starting_vertex to destination_vertex in
        breath-first order.
        """
        # create an empty queue
        path = Queue()

        # create a path to the starting vertex id
        path.enqueue([starting_vertex])

        # create a set to store visited vertices
        visited = set()

        # While queue is not empty
        while path.size() > 0:
            # dequeue first path
            vert = path.dequeue()
            # check if last vertex in path has been visited
            if vert[-1] not in visited:
                # check if vert is the target
                if vert[-1] == destination_vertex:
                    return vert
                else:
                    visited.add(vert[-1])
                    for n in self.get_neighbors(vert[-1]):
                        second_path = list(vert)
                        second_path.append(n)
                        path.enqueue(second_path)

    def dfs(self, starting_vertex, destination_vertex):
        """
        Return a list containing a path from
        starting_vertex to destination_vertex in
        depth-first order.
        """
        # create stack
        path = Stack()

        # create path to starting vertex
        path.push([starting_vertex])

        # create set for visited vertices
        visited = set()

        # While stack is not empty
        while path.size() > 0:
            # pop first path
            vert = path.pop()
            # check if last vertex in path has been visited
            if vert[-1] not in visited:
                # check if vert is target
                if vert[-1] == destination_vertex:
                    return vert
                else:
                    visited.add(vert[-1])
                    for n in self.get_neighbors(vert[-1]):
                        second_path = list(vert)
                        second_path.append(n)
                        path.push(second_path)

    def dfs_recursive(self, starting_vertex, destination_vertex, visited=set(), path=list()):
        """
        Return a list containing a path from
        starting_vertex to destination_vertex in
        depth-first order.

        This should be done using recursion.
        """
        # create path to starting vertex
        path = list(path)
        path.append(starting_vertex)

        # check if last vertex in the path is in visited
        if path[-1] not in visited:
            # check if last vertex is the destination vertex
            if path[-1] == destination_vertex:
                return path
            else:
                # add last vertex to visited
                visited.add(path[-1])
                # check neighbors of vertex
                for n in self.get_neighbors(path[-1]):
                    if n not in visited:
                        new_path = self.dfs_recursive(n, destination_vertex, visited, path)            
                        if new_path is not None:
                            return new_path

        return None


if __name__ == '__main__':
    graph = Graph()  # Instantiate your graph
    # https://github.com/LambdaSchool/Graphs/blob/master/objectives/breadth-first-search/img/bfs-visit-order.png
    graph.add_vertex(1)
    graph.add_vertex(2)
    graph.add_vertex(3)
    graph.add_vertex(4)
    graph.add_vertex(5)
    graph.add_vertex(6)
    graph.add_vertex(7)
    graph.add_edge(5, 3)
    graph.add_edge(6, 3)
    graph.add_edge(7, 1)
    graph.add_edge(4, 7)
    graph.add_edge(1, 2)
    graph.add_edge(7, 6)
    graph.add_edge(2, 4)
    graph.add_edge(3, 5)
    graph.add_edge(2, 3)
    graph.add_edge(4, 6)

    '''
    Should print:
        {1: {2}, 2: {3, 4}, 3: {5}, 4: {6, 7}, 5: {3}, 6: {3}, 7: {1, 6}}
    '''
    # print(graph.vertices)
    # print(graph.get_neighbors(3))
    # for n in graph.get_neighbors(2):
    #     print(n)

    # '''
    # Valid BFT paths:
    #     1, 2, 3, 4, 5, 6, 7
    #     1, 2, 3, 4, 5, 7, 6
    #     1, 2, 3, 4, 6, 7, 5
    #     1, 2, 3, 4, 6, 5, 7
    #     1, 2, 3, 4, 7, 6, 5
    #     1, 2, 3, 4, 7, 5, 6
    #     1, 2, 4, 3, 5, 6, 7
    #     1, 2, 4, 3, 5, 7, 6
    #     1, 2, 4, 3, 6, 7, 5
    #     1, 2, 4, 3, 6, 5, 7
    #     1, 2, 4, 3, 7, 6, 5
    #     1, 2, 4, 3, 7, 5, 6
    # '''
    # graph.bft(1)

    # '''
    # Valid DFT paths:
    #     1, 2, 3, 5, 4, 6, 7
    #     1, 2, 3, 5, 4, 7, 6
    #     1, 2, 4, 7, 6, 3, 5
    #     1, 2, 4, 6, 3, 5, 7
    # '''
    # graph.dft(1)
    # graph.dft_recursive(1)

    # '''
    # Valid BFS path:
    #     [1, 2, 4, 6]
    # '''
    # print(graph.bfs(1, 6))

    # '''
    # Valid DFS paths:
    #     [1, 2, 4, 6]
    #     [1, 2, 4, 7, 6]
    # '''
    # print(graph.dfs(1, 6))
    print(graph.dfs_recursive(1, 6))

    # To Test Part 1
    # graph = Graph()  # instantiate graph
    # graph.add_vertex('0')
    # graph.add_vertex('1')
    # graph.add_vertex('2')
    # graph.add_vertex('3')
    # graph.add_edge('0', '1')
    # graph.add_edge('1', '0')
    # graph.add_edge('0', '3')
    # graph.add_edge('3', '0')
    # print(graph.vertices)