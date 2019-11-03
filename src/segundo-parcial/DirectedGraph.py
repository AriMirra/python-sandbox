# TODO: import Graph xd1
"""
Directed Graph class implementation
"""

class DirectedGraph():
    vertexes  = []
    edges     = []

    def __init__(self):
        pass

    def add_vertex(self, vertex):
        if vertex is None:
            # print("vertex is None")
            return
        if self.index_of_vertex(vertex) is not -1:
            # print("vertex already exists")
            return
        self.vertexes.append(vertex)

    def add_edge(self, edge):
        if edge is None:
            return
        if self.index_of_edge(edge) is not -1:
            # edge exists, and multigraph is not allowed
            return 
        self.edges.append(edge)
        for v in vertexes:
            if v.compare_to(edge.from_vertex) is 0:
                v.add_adjacent(edge.to_vertex)

    def remove_vertex(self, vertex):
        pass

    def remove_edge(self, edge):
        pass

    def plot(self):
        # matplotlib render visual of graph ?
        pass

    def index_of_vertex(self, vertex):
        for i in range(len(self.vertexes)):
            if vertex.compare_to(self.vertexes[i]) is 0:
                return i
        return -1
        
    def index_of_edge(self, edge):
        for i in range(len(self.edges)):
            if edge.compare_to(self.edges[i]) is 0:
                return i
        return -1
        
    class Vertex():
        key = None
        adjacents = []

        def __init__(self, key):
            if key is None: raise Exception("vertex key cant be None")
            self.key = key
            
        def compare_to(self, vertex):
            if self.key is vertex.key:
                return 0
            return -1

        def add_adjacent(self, vertex):
            if vertex is None: return
            if self.adjacents.index(vertex) is not -1: return
            self.adjacents.append(vertex)

    class Edge():
        value = None
        from_vertex = None
        to_vertex = None

        def __init__(self, value, from_vertex, to_vertex):
            if value or from_vertex or to_vertex is None: raise Exception("invalid Edge constructor")
            self.value = value
            self.from_vertex = from_vertex
            self.to_vertex = to_vertex
            
        def compare_to(self, edge):
            if (self.from_vertex is edge.from_vertex) and (self.to_vertex is edge.to_vertex):
                return 0
            return -1