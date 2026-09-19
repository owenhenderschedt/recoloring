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


def is_complete_between(G, A, B):
    """
    Return True exactly when every vertex of A is adjacent to
    every vertex of B.
    """
    A = set(A)
    B = set(B)

    for u in A:
        if not B <= G[u]:
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


def nonedge_permitted(G, S, T):
    """
    Test whether two individually admissible new vertices x and y,
    with core neighborhoods S and T, may be nonadjacent.

    By the two-vertex attachment rule, xy is permitted as a nonedge
    exactly when S - T is complete to T - S.
    """
    S = set(S)
    T = set(T)
    V = set(G)

    assert S <= V
    assert T <= V

    return is_complete_between(G, S - T, T - S)


def edge_permitted(G, S, T):
    """
    Test whether two individually admissible new vertices x and y,
    with core neighborhoods S and T, may be adjacent.

    By the two-vertex attachment rule, xy is permitted as an edge
    exactly when both S intersect T and the vertices outside
    S union T are independent.
    """
    S = set(S)
    T = set(T)
    V = set(G)

    assert S <= V
    assert T <= V

    return (
        is_independent(G, S & T)
        and is_independent(G, V - (S | T))
    )


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

    # One-vertex attachment tests.

    # Failure by K_4.
    assert not one_vertex_admissible(
        triangle,
        {0, 1, 2},
    )

    # Failure by induced 2K_2.
    edge_and_isolated = make_graph(
        vertices=[0, 1, 2],
        edges=[(0, 1)],
    )

    assert not one_vertex_admissible(
        edge_and_isolated,
        {2},
    )

    # Valid attachment to an induced C_5.
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

    # Two-vertex attachment tests.

    # Here S - T = {0} and T - S = {1}.
    # Since 01 is an edge, the nonedge between the two new vertices
    # is permitted.
    single_edge = make_graph(
        vertices=[0, 1],
        edges=[(0, 1)],
    )

    assert nonedge_permitted(
        single_edge,
        {0},
        {1},
    )

    # If 01 is absent, the same proposed nonedge creates an induced
    # 2K_2, so it is not permitted.
    two_isolated = make_graph(
        vertices=[0, 1],
        edges=[],
    )

    assert not nonedge_permitted(
        two_isolated,
        {0},
        {1},
    )

    # For an edge between two new vertices, a common adjacent pair
    # in the core would create a K_4.
    assert not edge_permitted(
        single_edge,
        {0, 1},
        {0, 1},
    )

    # If the common neighborhood and the vertices outside S union T
    # are both independent, the edge is permitted.
    assert edge_permitted(
        path,
        {0, 1},
        {1, 2},
    )

    print("Basic graph tests passed.")
    print("One-vertex attachment tests passed.")
    print("Two-vertex attachment tests passed.")


if __name__ == "__main__":
    main()
