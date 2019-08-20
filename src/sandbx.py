# you will need to install matplotlib (pip install matplotlib)
import matplotlib.pyplot as plt

data = [['a', 1, 1], ['b', 3, 2]]

for item in data:
    plt.plot(item, 'ro-')
plt.show()
from graph import Graph


def plot_graph(graph):
    """
    graph has:
    - Vertex list
    - Edge list
    """
    # [[0, 1], [1, 2]]
    # 'a', 'b', 'c'
    for i in range(0, len(graph.edges)):
        pass
    plt.show()


graph_demo = Graph()
graph_demo.add_vertex("Hay")
graph_demo.add_vertex("una")
graph_demo.add_vertex("serpiente")
graph_demo.add_vertex("en")
graph_demo.add_vertex("mi")
graph_demo.add_vertex("Bota")
graph_demo.add_edge(graph_demo.get_vertex_position("Hay"), graph_demo.get_vertex_position("una"))
graph_demo.add_edge(graph_demo.get_vertex_position("una"), graph_demo.get_vertex_position("serpiente"))
graph_demo.add_edge(graph_demo.get_vertex_position("serpiente"), graph_demo.get_vertex_position("en"))
graph_demo.add_edge(graph_demo.get_vertex_position("en"), graph_demo.get_vertex_position("mi"))
graph_demo.add_edge(graph_demo.get_vertex_position("mi"), graph_demo.get_vertex_position("Bota"))

plot_graph(graph_demo)


def get_adjacent(graph, index):
    if graph.is_empty(): return []
    for i in range(1, len(graph.vertexes)):
        pass

# Especificar y escribir algoritmos para resolver los siguientes problemas. 
# Considerar que el grafo es simple y puede tener lazos. Calcular O grande. 
# a)Mostrar el grafo.
def show_graph(graph):
    # beginner: prints, advanced: matplotlib B)
    pass
# b)Retornar la cantidad de lazos de un grafo.
def tie_quantity(graph):
    """check for"""
    for i in range(0, graph.size()):
        pass
# c)Retornar un arreglo con los vértices que tienen lazos. 

# d)Dado un vértice informar si es aislado. 
# e)Calcular cuantos vértices son aislados. 
# f)Retornar todos los vértices aislados. 
# g)Dado un grafo debe retornar otro grafo sin lazos y sin vértices aislados. 
# h)Calcular y mostrar la matriz de adyacencia. 
# i)Calcular y mostrar la matriz de incidencia.
