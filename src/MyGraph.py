from Graph import Graph
"""
Graph class implementation
"""

class MyGraph(Graph):

    def __init__(self):
        self.graph = {}

    def add_vertex(self, v):
        if v is None: return False
        self.graph[v] = []
        return True

    def add_edge(self, v, w):
        if v is None or w is None: return False
        self.graph[v].append(w)
        return True

    def delete_vertex(self, v):
        if v is None: return False
        if self.graph.get(c) is None: return False
        self.graph.pop(v)
        return True

    def delete_edge(self, v, w):
        if v is None or w is None: return False
        if self.graph.get(v) is None: return False
        self.graph[v].remove(w)
        return False

    def edge_exists(self, v, w):
        if v is None or w is None: raise TypeError("argument is None")
        if self.graph.get(v) is None or self.graph.get(w) is None: 
            raise ValueError("no such element in v")
        
        return True

    def order(self):
        return len(self.graph)

    def edge_amount(self):
        amount = 0
        for edge in self.graph.values():
            amount += len(edge)
        return amount

    def get_vertex(self, i):
        if i is None: raise TypeError("argument is None")
        if i < 0: raise ValueError("invalid (negative) value")
        if i > len(self.graph) - 1: raise IndexError("no such element in index given")
        return list(self.graph.keys())[i]

    def get_vertex_edges_list(self, v):
        if v is None: raise TypeError("argument is None") 
        return self.graph[v]

    def get_vertexes_list(self):
        return list(self.graph.keys())