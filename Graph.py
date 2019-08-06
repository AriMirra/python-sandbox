class Graph:
    vertexes = []
    edges = []

    def __init__(self):
        pass

    def addVertex(self, item):  # item can be a string or an instance of something
        if item is None:
            print("addVertex ==> item is None")
            return
        else:
            self.vertexes.append(item)
        self.printGraph("addVertex")

    def addEdge(self, index_a, index_b):
        if (index_a or index_b) is None:
            print("addEdge ==> index_a or index_b is None")
            return
        else:
            self.edges.append([index_a, index_b])
        self.printGraph("addEdge")

    def deleteVertex(self, index):
        if index is None:
            print("deleteVertex ==> index is None")
            return
        elif self.vertexes[index] is None:
            print("deleteVertex ==> vertex does not exist")
            return
        else:
            self.vertexes.remove(index)
            for i in self.edges:
                if (self.edges[i][0] or self.edges[i][1]) == index:
                    self.edges.remove(i)
        self.printGraph("deleteVertex")

    def deleteEdge(self, index_a, index_b):
        self.printGraph("deleteEdge")

    def getVertexPosition(self, object):
        if object is None:
            print('getVertexPosition ==> object is None')
            return -1
        for i in self.vertexes:
            if self.vertexes[i] == object:
                graph.printGraph()
                return i
        self.printGraph("getVertexPosition")
        return -1

    def printGraph(self, message):
        print(message + " ==> Vertexes: " + str(self.vertexes) + ", edges: " + str(self.edges))

    # def addVertex(self):
    #     pass
    # def addVertex(self):
    #     pass


graph = Graph()
graph.addVertex("a")
graph.addVertex("b")
graph.addVertex("c")
graph.addVertex("d")
graph.addEdge(0, 1)
graph.addEdge(1, 2)
graph.addEdge(2, 3)
graph.addEdge(3, 0)
