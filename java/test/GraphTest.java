import org.junit.Before;
import org.junit.Test;

import java.util.ArrayList;
import java.util.List;

import static org.junit.Assert.*;

public class GraphTest {


    private static DirectedGraph init() {
        List<String> vertexes = new ArrayList<>();
        vertexes.add("A");
        vertexes.add("B");
        vertexes.add("C");
        vertexes.add("D");

        List<Graph.Edge> edges = new ArrayList<>();
        edges.add(new Graph.Edge(0, 1));
        edges.add(new Graph.Edge(0, 3));
        edges.add(new Graph.Edge(1, 3));
        edges.add(new Graph.Edge(2, 0));
        edges.add(new Graph.Edge(2, 3));
        edges.add(new Graph.Edge(3, 1));

        return new DirectedGraph(vertexes, edges);
    }

    private static DirectedGraph initEulerian() {
        List<String> vertexes = new ArrayList<>();
        vertexes.add("A");
        vertexes.add("B");
        vertexes.add("C");
        vertexes.add("D");

        List<Graph.Edge> edges = new ArrayList<>();
        edges.add(new Graph.Edge(0, 1));
        edges.add(new Graph.Edge(0, 2));
        edges.add(new Graph.Edge(1, 2));
        edges.add(new Graph.Edge(1, 3));
        edges.add(new Graph.Edge(2, 3));

        return new DirectedGraph(vertexes, edges);
    }

    @Test
    public void deleteVertexTest() {
        DirectedGraph g = init();
        assertTrue(g.edgeExists(2,0));
        g.deleteVertex("C");
        assertFalse(g.edgeExists(2,0));
    }

    @Test
    public void getAdjacentListTest() {
        DirectedGraph g = init();
        List<Integer> result = new ArrayList<>();
        result.add(3);
        assertEquals(result, g.getAdjacentList(1));
    }

    @Test
    public void DFSTest() {
        DirectedGraph g = init();
        assertTrue(g.DFS("C", "B"));
        assertFalse(g.DFS("A","C"));
    }

    @Test
    public void BFSTest() {
        DirectedGraph g = init();
        assertTrue(g.BFS("C", "B"));
        assertFalse(g.BFS("A","C"));
    }

    @Test
    public void randomGraphTest() {
        DirectedGraph g = DirectedGraph.randomGraph(1,4,6);
        System.out.println("test");
    }

    @Test
    public void fleuryTest() {
        initEulerian().fleury();
    }
}
