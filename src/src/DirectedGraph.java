import java.util.ArrayList;
import java.util.List;
import java.util.stream.Collectors;

public class DirectedGraph implements Graph {
    private List<String> vertexes;
    private List<Edge> edges;

    public DirectedGraph(List<String> vertexes, List<Edge> edges) {
        this.vertexes = vertexes;
        this.edges = edges;
    }

    public void addVertex(String v) {
        vertexes.add(v);
    }

    public void addEdge(Edge e) {
        edges.add(e);
    }

    public void deleteVertex(String v) {
        int index = vertexes.indexOf(v);
        edges = edges.stream()
                .filter(e -> e.from != index && e.to != index)
                .collect(Collectors.toCollection(ArrayList::new));
        vertexes.remove(v);
    }

    public void deleteEdge(Edge e) {
        edges.remove(e);
    }

    public boolean edgeExists(int v, int w) {
        return edges.contains(new Edge(v, w));
    }

    public List<Integer> getAdjacentList(int v) {
        ArrayList<Integer> result = new ArrayList<>(vertexes.size());
        for (Edge e: edges) {
            if (e.from == v) result.add(e.to);
        }
        return result;
    }

}
