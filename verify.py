"""
Finite verification for the paper

    Recolorability of (2K_2, K_4)-Free Graphs.

The program verifies the attachment-profile calculations used in the
computer-assisted portions of the proof.

Python 3; no external packages are required.
"""


def make_graph(vertices, edges):
    """
    Return the adjacency dictionary of a finite simple graph.

    vertices is an iterable of vertex labels.
    edges is an iterable of unordered pairs (u, v).
    """
    G = {v: set() for v in vertices}

    for u, v in edges:
        assert u in G and v in G
        assert u != v
        G[u].add(v)
        G[v].add(u)

    return G


def is_independent(G, vertices):
    """Return True exactly when the given vertices induce an independent set."""
    S = set(vertices)

    for u in S:
        if G[u] & S:
            return False

    return True


def is_triangle_free(G, vertices):
    """Return True exactly when the given vertices induce no triangle."""
    S = set(vertices)

    for u in S:
        for v in G[u] & S:
            if G[u] & G[v] & S:
                return False

    return True


def one_vertex_admissible(G, S):
    """
    Test the one-vertex attachment rule.

    A new vertex x with neighborhood S in the core G is admissible
    exactly when

      (i) G[S] is triangle-free; and

      (ii) for every h in S, the vertices outside
           S union N_G(h) form an independent set.

    These are precisely the conditions preventing a new K_4 or
    induced 2K_2 containing x.
    """
    S = set(S)
    V = set(G)

    assert S <= V

    if not is_triangle_free(G, S):
        return False

    for h in S:
        outside = V - S - G[h]

        if not is_independent(G, outside):
            return False

    return True


def main():
    print("Recolorability of (2K_2, K_4)-Free Graphs")
    print("Finite certificate verifier")
    print()

    # Basic graph tests.
    path = make_graph(
        vertices=[0, 1, 2],
        edges=[(0, 1), (1, 2)],
    )

    triangle = make_graph(
        vertices=[0, 1, 2],
        edges=[(0, 1), (1, 2), (2, 0)],
    )

    assert is_independent(path, {0, 2})
    assert not is_independent(path, {0, 1})
    assert is_triangle_free(path, {0, 1, 2})
    assert not is_triangle_free(triangle, {0, 1, 2})

    # Condition (i): attaching a vertex to all three vertices of a
    # triangle would create K_4.
    assert not one_vertex_admissible(
        triangle,
        {0, 1, 2},
    )

    # Condition (ii): if the core consists of an edge 0--1 and an
    # isolated vertex 2, attaching a new vertex only to 2 would
    # create the induced 2K_2 with edges x2 and 01.
    edge_and_isolated = make_graph(
        vertices=[0, 1, 2],
        edges=[(0, 1)],
    )

    assert not one_vertex_admissible(
        edge_and_isolated,
        {2},
    )

    # A vertex adjacent to every vertex of an induced C_5 passes
    # the one-vertex attachment test.
    cycle5 = make_graph(
        vertices=[0, 1, 2, 3, 4],
        edges=[
            (0, 1),
            (1, 2),
            (2, 3),
            (3, 4),
            (4, 0),
        ],
    )

    assert one_vertex_admissible(
        cycle5,
        {0, 1, 2, 3, 4},
    )

    print("Basic graph tests passed.")
    print("One-vertex attachment tests passed.")


if __name__ == "__main__":
    main()
