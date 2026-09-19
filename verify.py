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


def cycle_vertex(i):
    """
    Return c_i, with indices interpreted modulo 5.

    Thus cycle_vertex(6) = "c1" and cycle_vertex(0) = "c5".
    """
    i = ((i - 1) % 5) + 1
    return f"c{i}"


def cycle_neighborhood(kind, i=None):
    """
    Return the prescribed neighborhood on the fixed 5-cycle
    for one of the cycle types U, Z, F_i, Y_i, R_i.

    The cycle is c1 c2 c3 c4 c5 c1.
    """
    C = {cycle_vertex(j) for j in range(1, 6)}

    if kind == "U":
        assert i is None
        return C

    if kind == "Z":
        assert i is None
        return set()

    assert kind in {"F", "Y", "R"}
    assert i is not None

    if kind == "F":
        return C - {cycle_vertex(i)}

    if kind == "Y":
        return {
            cycle_vertex(i),
            cycle_vertex(i - 2),
            cycle_vertex(i + 2),
        }

    if kind == "R":
        return {
            cycle_vertex(i - 1),
            cycle_vertex(i + 1),
        }


def profile_neighborhood(kind, i, bits, off_cycle_order):
    """
    Return the neighborhood in the core prescribed by an attachment profile.

    kind, i specify the cycle type. For U and Z, use i=None.

    bits is a string of 0s and 1s, read in the order given by
    off_cycle_order.

    Example:
        profile_neighborhood("Y", 2, "110", ["f", "a", "g"])

    represents the profile Y_2[110].
    """
    assert len(bits) == len(off_cycle_order)
    assert all(bit in {"0", "1"} for bit in bits)

    S = cycle_neighborhood(kind, i)

    for bit, vertex in zip(bits, off_cycle_order):
        if bit == "1":
            S.add(vertex)

    return S


def main():
    print("Recolorability of (2K_2, K_4)-Free Graphs")
    print("Finite certificate verifier")
    print()

    # Cycle-type tests.
    assert cycle_neighborhood("U") == {
        "c1", "c2", "c3", "c4", "c5"
    }

    assert cycle_neighborhood("Z") == set()

    assert cycle_neighborhood("F", 1) == {
        "c2", "c3", "c4", "c5"
    }

    assert cycle_neighborhood("Y", 1) == {
        "c1", "c3", "c4"
    }

    assert cycle_neighborhood("R", 1) == {
        "c2", "c5"
    }

    # Indices are taken modulo 5.
    assert cycle_neighborhood("Y", 5) == {
        "c2", "c3", "c5"
    }

    # Profile test: Y_2[110] relative to (f, a, g).
    assert profile_neighborhood(
        "Y",
        2,
        "110",
        ["f", "a", "g"],
    ) == {
        "c2", "c4", "c5", "f", "a"
    }

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

    # For an edge between two new vertices, an edge in their common
    # neighborhood would create a K_4.
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
    print("Cycle types and attachment profiles passed.")


if __name__ == "__main__":
    main()
