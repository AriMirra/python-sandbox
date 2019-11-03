import java.util.List;

public interface Graph {
    class Edge {
        int from;
        int to;

        Edge(int from, int to) {
            this.from = from;
            this.to = to;
        }
    }

    void addVertex(String v);

    void addEdge(Edge e);

    void deleteVertex(String v);

    void deleteEdge(Edge e);

    boolean edgeExists(int v, int w);

    List<Integer> getAdjacentList(int v);
}
