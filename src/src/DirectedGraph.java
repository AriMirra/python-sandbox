import java.util.*;
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
        for (Edge e : edges) {
            if (e.from == v) result.add(e.to);
        }
        return result;
    }

    public boolean plainSearch(String from, String to) {
        // TODO: ask Alicia
        int fromIndex = vertexes.indexOf(from);
        int toIndex = vertexes.indexOf(to);
        for (Edge e: edges) {

        }
        return false;
    }

    public boolean DFS(String from, String to) {
        HashSet<Integer> visited = new HashSet<>();
        int fromIndex = vertexes.indexOf(from);
        int toIndex = vertexes.indexOf(to);
        return hasPathDFS(fromIndex, toIndex, visited);
    }

    private boolean hasPathDFS(int from, int to, HashSet<Integer> visited) {
        if (visited.contains(from)) return false;
        if (from == to) return true;
        visited.add(from);
        Set<Integer> children = getChildren(from);
        for (int v : children) {
            hasPathDFS(v, to, visited);
        }
        return false;
    }

    public boolean BFS(String from, String to) {
        LinkedList<Integer> nextToVisit = new LinkedList<>();
        HashSet<Integer> visited = new HashSet<>();
        int fromIndex = vertexes.indexOf(from);
        nextToVisit.add(fromIndex);
        while(!nextToVisit.isEmpty()) {
            int v = nextToVisit.remove();
            if (vertexes.get(v).equals(to)) return true;
            if (visited.contains(v)) continue;
            visited.add(v);
            nextToVisit.addAll(getChildren(v));
        }
        return false;
    }

    private Set<Integer> getChildren(int i) {
        return edges.stream()
                .filter(e -> e.from == i)
                .map(e -> e.to)
                .collect(Collectors.toSet());
    }

}
