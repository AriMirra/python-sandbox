import java.util.List;
import java.util.Objects;

public interface Graph {
    class Edge {
        int from;
        int to;

        Edge(int from, int to) {
            this.from = from;
            this.to = to;
        }

        @Override
        public boolean equals(Object obj) {
            Edge e = (Edge) obj;
            System.out.println("comparing:" + this + " to " + e);
            return e.from == this.from && e.to == this.to;
        }

        @Override
        public String toString() {
            return "{ from: " + from + ", to: " + to + " }";
        }

        @Override
        public int hashCode() {
            return Objects.hash(from, to);
        }
    }

    void addVertex(String v);

    void addEdge(Edge e);

    void deleteVertex(String v);

    void deleteEdge(Edge e);

    boolean edgeExists(int v, int w);

    List<Integer> getAdjacentList(int v);
}
