""" This should able to analyse
a graph and classify it as:
- Vertex quantity
- Edge quantity
- If its directed or not
- If its reflexive or not
- If its transitive or not
- If its disperse or dense
- simple directed, simple undirected, multi
- ...
"""


def edge_exists(graph, v, w):
    pass


def path_exists(graph, v, w, *args, **kwargs):
    visited = kwargs.get('visited',  [False] * len(graph.vertexes))
    if v == w or edge_exists(graph, v, w):
        return True

    visited[v] = True
    adjacent = graph.get_adjacent(v)
    if len(adjacent) == 0:
        return False

    i = 0
    for a in adjacent:
        if not visited[i] and path_exists(graph, adjacent[i], w, visited=visited):
            return True

    return False
