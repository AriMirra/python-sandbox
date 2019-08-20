"""
==== Matrixes functions and other theory =====================

Graph has a dict and operates with it, the keys are
vertexes and the values are lists with all connections
with other vertexes.
    Graph1 = {"A": ["B", "C"], "B": ["A"], "C": ["B"]}

==== Super drawing ===========================================
    (A)--<>--(B)     // example from above
     |       A
     |     /
     |   /
     V / 
    (C)

==== Directed and non directed ===============================
If A has connection with B but not otherwise, the connection
will be directed in one side, if both have reciprocal
connection between each other, will be non directed.

"""
from graph import MyGraph

def adjacency_matrix(graph):
    matrix = []
    vertexes = graph.get_vertexes_list()
    for i in range(0, len(vertexes)):
        print("row (i): " + str(i))
        row = []
        print("     vertex: " + str(vertexes[i]))
        edges = graph.get_vertex_edges_list(vertexes[i])
        for j in range(0, len(vertexes)):
            print("     col (j): " + str(j))
            try:
                print("         edge: " + str(edges[j]) + ", vertex: " + str(vertexes[j]))
                if (edges[j] == vertexes[j]):
                    row.append(1)
                else:
                    row.append(0)
            except IndexError:
                row.append(0)
        matrix.append(row)
    return matrix

def incidency_matrix(graph):
    # exists but not really important
    pass

# matrix test
if __name__ == "__main__":
    """ A --> B ---> C 
        (demo_graph_1)

    """
    demo_graph_1 = MyGraph()
    demo_graph_1.add_vertex("A")
    demo_graph_1.add_vertex("B")
    demo_graph_1.add_vertex("C")
    demo_graph_1.add_edge("A", "B")
    demo_graph_1.add_edge("B", "C")
    print(demo_graph_1.get_vertexes_list())
    for vertex in demo_graph_1.get_vertexes_list():
        print(str(vertex) + ": " + str(demo_graph_1.get_vertex_edges_list(vertex)))
    m = adjacency_matrix(demo_graph_1)
    print(m)
    """ E ----- F   (demo_graph_2)
        |  ____/
        | / 
        G ----- H
    """
    # demo_graph_2 = MyGraph()
    # demo_graph_2.add_vertex("E")
    # demo_graph_2.add_vertex("F")
    # demo_graph_2.add_vertex("G")
    # demo_graph_2.add_vertex("H")
    # demo_graph_2.add_edge("E", "F")
    # demo_graph_2.add_edge("F", "E")
    # demo_graph_2.add_edge("E", "G")
    # demo_graph_2.add_edge("G", "E")
    # demo_graph_2.add_edge("F", "G")
    # demo_graph_2.add_edge("G", "F")
    # demo_graph_2.add_edge("G", "H")
    # demo_graph_2.add_edge("H", "G")
