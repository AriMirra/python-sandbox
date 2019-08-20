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
    vertexes = graph.get_vertex_list()
    for i in range(0, len(vertexes)):
        row = []
        for j in range(0, len(vertexes)):
            try:
                if (graph.get_vertex_edge_list(vertexes[i])[j] == vertexes[i]):
                    row.append(1)
                else:
                    row.append(0)
            except IndexError:
                row.append(0)

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
    """ E ----- F   (demo_graph_2)
        |  ____/
        | / 
        G ----- H
    """
    demo_graph_2 = MyGraph()
    demo_graph_2.add_vertex("E")
    demo_graph_2.add_vertex("F")
    demo_graph_2.add_vertex("G")
    demo_graph_2.add_vertex("H")
    demo_graph_2.add_edge("E", "F")
    demo_graph_2.add_edge("F", "E")
    demo_graph_2.add_edge("E", "G")
    demo_graph_2.add_edge("G", "E")
    demo_graph_2.add_edge("F", "G")
    demo_graph_2.add_edge("G", "F")
    demo_graph_2.add_edge("G", "H")
    demo_graph_2.add_edge("H", "G")
