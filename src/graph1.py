class Graph1:
    vertexes = []
    edges = [[]]

    def __init__(self):
        pass

    def add_vertex(self, item):  # item can be a string or an instance of something
        if item is None:
            print("addVertex ==> item is None")
            return
        else:
            self.vertexes.append(item)
        self.print_graph("addVertex")

    def add_edge(self, index_a, index_b):
        if (index_a or index_b) is None:
            print("addEdge ==> index_a or index_b is None")
            return
        else:
            self.edges.append([index_a, index_b])
        self.print_graph("addEdge")

    def delete_vertex(self, index):
        if index is None:
            print("deleteVertex ==> index is None")
            return
        elif self.vertexes[index] is None:
            print("deleteVertex ==> vertex does not exist")
            return
        else:
            self.vertexes.remove(index)
            for i in range(len(self.edges)):
                if (self.edges[i][0] or self.edges[i][1]) == index:
                    self.edges.remove(i)
        self.print_graph("deleteVertex")

    def delete_edge(self, index_a, index_b):
        self.print_graph("deleteEdge")

    def get_vertex_position(self, object_):
        if object_ is None:
            print('getVertexPosition ==> object_ is None')
            return -1
        for i in self.vertexes:
            if self.vertexes[i] == object_:
                graph.print_graph('')
                return i
        self.print_graph("getVertexPosition")
        return -1

    def print_graph(self, message):
        print(message + " ==> Vertexes: " + str(self.vertexes) + ", edges: " + str(self.edges))

    # def addVertex(self):
    #     pass
    # def addVertex(self):
    #     pass


graph = Graph1()
graph.add_vertex("a")
graph.add_vertex("b")
graph.add_vertex("c")
graph.add_vertex("d")
graph.add_edge(0, 1)
graph.add_edge(1, 2)
graph.add_edge(2, 3)
graph.add_edge(3, 0)
