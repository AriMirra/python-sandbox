# from src.Graph import Graph  # idea
from Graph import Graph

"""
Graph class implementation
"""


class MyGraph(Graph):

    def __init__(self, directed=False):
        self.graph = {}
        self.directed = directed

    def add_vertex(self, v):
        if v is None:
            return False
        for key in self.graph.keys():
            self.graph[key].extend([0])
        self.graph[v] = [0] * (len(self.graph) + 1)
        return True

    def add_edge(self, v, w):
        if v is None or w is None:
            return False
        vertexes = list(self.graph.keys())
        v_exists = False
        w_exists = False
        if self.directed:  # add only when matching
            for vertex in vertexes:
                if vertex is v:
                    v_exists = True
                    for i in range(0, len(vertexes)):
                        if vertexes[i] is w:
                            self.graph[v][i] = 1
                            w_exists = True
            if not v_exists or not w_exists:
                raise ValueError("v does not exists in graph")
        else:  # 1 edge means 2 in reality 
            pass
        return True

    def delete_vertex(self, v):
        if v is None:
            return False
        if self.graph.get(v) is None:
            return False
        self.graph.pop(v)
        return True

    def delete_edge(self, v, w):
        if v is None or w is None:
            return False
        if self.graph.get(v) is None:
            return False
        self.graph[v].remove(w)
        return False

    def edge_exists(self, v, w):
        if v is None or w is None:
            raise TypeError("argument is None")
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
        if i is None:
            raise TypeError("argument is None")
        if i < 0:
            raise ValueError("invalid (negative) value")
        if i > len(self.graph) - 1:
            raise IndexError("no such element in index given")
        return list(self.graph.keys())[i]

    def get_vertex_edges_list(self, v):
        if v is None:
            raise TypeError("argument is None")
        return self.graph[v]

    def get_vertexes_list(self):
        return list(self.graph.keys())

    def print_graph(self):
        print(self.graph)

    def get_adjacent_list(self, v):
        pass


# test
if __name__ == "__main__":
    # demo_graph = MyGraph(True)
    # demo_graph.add_vertex("a")
    # demo_graph.print_graph()
    # demo_graph.add_vertex("b")
    # demo_graph.print_graph()
    # demo_graph.add_vertex("c")
    # demo_graph.print_graph()
    # demo_graph.add_edge("a", "b")
    # demo_graph.print_graph()
    # demo_graph.add_edge("c", "b")
    # demo_graph.print_graph()
    pass
