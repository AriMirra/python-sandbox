import java.util.*;
import java.util.stream.Collectors;

public class DirectedGraph implements Graph {
    private List<String> vertexes;
    private List<Edge> edges;

    DirectedGraph(List<String> vertexes, List<Edge> edges) {
        this.vertexes = vertexes;
        this.edges = edges;
    }

    @Override
    public void addVertex(String v) {
        vertexes.add(v);
    }

    @Override
    public void addEdge(Edge e) {
        edges.add(e);
    }

    @Override
    public void deleteVertex(String v) {
        int index = vertexes.indexOf(v);
        edges = edges.stream()
                .filter(e -> e.from != index && e.to != index)
                .collect(Collectors.toCollection(ArrayList::new));
        vertexes.remove(v);
    }

    @Override
    public void deleteEdge(Edge e) {
        edges.remove(e);
    }

    @Override
    public boolean edgeExists(int v, int w) {
        return edges.contains(new Edge(v, w));
    }

    @Override
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
        for (Edge e : edges) {

        }
        return false;
    }

    boolean DFS(String from, String to) {
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
            return hasPathDFS(v, to, visited);
        }
        return false;
    }

    boolean BFS(String from, String to) {
        LinkedList<Integer> nextToVisit = new LinkedList<>();
        HashSet<Integer> visited = new HashSet<>();
        int fromIndex = vertexes.indexOf(from);
        nextToVisit.add(fromIndex);
        while (!nextToVisit.isEmpty()) {
            int v = nextToVisit.remove();
            if (vertexes.get(v).equals(to)) return true;
            if (visited.contains(v)) continue;
            visited.add(v);
            nextToVisit.addAll(getChildren(v));
        }
        return false;
    }

    int bfsCount(String from, String to, HashSet<Integer> visited) {
        LinkedList<Integer> nextToVisit = new LinkedList<>();
        int count = 0;
        int fromIndex = vertexes.indexOf(from);
        nextToVisit.add(fromIndex);
        while (!nextToVisit.isEmpty()) {
            int v = nextToVisit.remove();
            if (vertexes.get(v).equals(to)) return count;
            else count++;
            if (visited.contains(v)) continue;
            visited.add(v);
            nextToVisit.addAll(getChildren(v));
        }
        return -1;
    }

    private Set<Integer> getChildren(int i) {
        return edges.stream()
                .filter(e -> e.from == i)
                .map(e -> e.to)
                .collect(Collectors.toSet());
    }

    static DirectedGraph randomGraph(int vertexNameLength, int vertexAmount, int edgesAmount) {
        if (vertexAmount > 26) vertexAmount = 26;
        List<String> vs = getRandomStrings(vertexNameLength, vertexAmount);
        List<Edge> edges = getRandomEdges(vs, edgesAmount);
        return new DirectedGraph(vs, edges);
    }

    private static List<String> getRandomStrings(int length, int amount) {
        String alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ";
        Set<String> strings = new HashSet<>();
        while (strings.size() < amount) {
            StringBuilder sb = new StringBuilder(length);
            for (int i = 0; i < length; i++) {
                int index = (int) (alphabet.length() * Math.random());
                sb.append(alphabet.charAt(index));
            }
            strings.add(sb.toString());
        }
        return new ArrayList<>(strings);
    }

    private static List<Edge> getRandomEdges(List<String> vs, int amount) {
        if (amount > vs.size()) amount = vs.size() - 1;
        Random r = new Random();
        int length = vs.size();
        Set<Edge> edges = new HashSet<>();
        while (edges.size() < amount) {
            int v1 = r.nextInt(length);
            int v2 = r.nextInt(length);
            if (v1 == v2) continue;
            edges.add(new Edge(v1, v2));
        }
        return new ArrayList<>(edges);
    }

    void fleury() {
        int startingIndex = 0;
        for (int i = 0; i < vertexes.size(); i++) {
            if (getAdjacentList(startingIndex).size() % 2 == 1) {
                startingIndex = i;
                break;
            }
        }

        printEulerUtil(startingIndex);
        System.out.println();
    }

    private void printEulerUtil(Integer u) {
        for (int i = 0; i < getAdjacentList(u).size(); i++) {
            Integer v = getAdjacentList(u).get(i);
            if (isValidNextEdge(u, v)) {
                System.out.print(u + "->" + v + "  ");
                deleteEdge(new Edge(u, v));
                printEulerUtil(v);
            }
        }
    }

    private boolean isValidNextEdge(Integer u, Integer v) {
        if (getAdjacentList(u).size() == 1) {
            return true;
        }

        HashSet<Integer> isVisited = new HashSet<>(vertexes.size());
        int count1 = bfsCount(vertexes.get(0), vertexes.get(u), isVisited);

        deleteEdge(new Edge(u, v));
        isVisited = new HashSet<>(vertexes.size());
        int count2 = bfsCount(vertexes.get(0), vertexes.get(u), isVisited);

        addEdge(new Edge(u, v));
        return count1 <= count2;
    }

}
