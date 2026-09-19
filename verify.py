"""
Finite verification for the paper

    Recolorability of (2K_2, K_4)-Free Graphs.

The program verifies the attachment-profile calculations used in the
computer-assisted portions of the proof.

Python 3; no external packages are required.
"""

from itertools import combinations, product

from certificates import K0


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


def add_vertex(G, vertex, neighbors):
    """
    Add a new vertex with the specified neighborhood.

    The function modifies G in place.
    """
    assert vertex not in G

    neighbors = set(neighbors)
    assert neighbors <= set(G)

    G[vertex] = set()

    for u in neighbors:
        G[vertex].add(u)
        G[u].add(vertex)


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


def edge_count(G, vertices):
    """Return the number of edges induced by the given vertices."""
    S = set(vertices)

    return sum(len(G[u] & S) for u in S) // 2


def is_2k2_k4_free(G):
    """
    Return True exactly when G contains neither an induced 2K_2
    nor a K_4.
    """
    for four_vertices in combinations(G, 4):
        S = set(four_vertices)
        number_of_edges = edge_count(G, S)

        if number_of_edges == 6:
            return False

        if (
            number_of_edges == 2
            and all(len(G[u] & S) == 1 for u in S)
        ):
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
    """
    assert len(bits) == len(off_cycle_order)
    assert all(bit in {"0", "1"} for bit in bits)

    S = cycle_neighborhood(kind, i)

    for bit, vertex in zip(bits, off_cycle_order):
        if bit == "1":
            S.add(vertex)

    return S


def fixed_cycle():
    """Return the fixed induced cycle c1 c2 c3 c4 c5 c1."""
    vertices = [cycle_vertex(i) for i in range(1, 6)]

    edges = [
        (cycle_vertex(i), cycle_vertex(i + 1))
        for i in range(1, 6)
    ]

    return make_graph(vertices, edges)


def add_typed_vertex(
    G,
    vertex,
    kind,
    i=None,
    earlier_neighbors=(),
):
    """
    Add an off-cycle vertex of a specified cycle type.
    """
    neighborhood = (
        cycle_neighborhood(kind, i)
        | set(earlier_neighbors)
    )

    add_vertex(G, vertex, neighborhood)


def build_core(certificate):
    """
    Construct the core specified by a certificate.

    The construction begins with the fixed C_5 and adds the
    off-cycle vertices in the displayed order.
    """
    G = fixed_cycle()

    for vertex, kind, i, earlier_neighbors in certificate["construction"]:
        add_typed_vertex(
            G,
            vertex,
            kind,
            i,
            earlier_neighbors,
        )

    return G


def all_cycle_types():
    """Iterate through U, Z, and all F_i, Y_i, R_i cycle types."""
    yield "U", None
    yield "Z", None

    for kind in ("F", "Y", "R"):
        for i in range(1, 6):
            yield kind, i


def profile_label(kind, i, bits):
    """Return the paper-style label of an attachment profile."""
    if i is None:
        cycle_type = kind
    else:
        cycle_type = f"{kind}{i}"

    return f"{cycle_type}[{bits}]"


def admissible_profiles(G, off_cycle_order):
    """
    Return all one-vertex admissible profiles relative to the core G.
    """
    profiles = []

    for kind, i in all_cycle_types():
        for bit_tuple in product(
            "01",
            repeat=len(off_cycle_order),
        ):
            bits = "".join(bit_tuple)

            S = profile_neighborhood(
                kind,
                i,
                bits,
                off_cycle_order,
            )

            if one_vertex_admissible(G, S):
                profiles.append(
                    profile_label(kind, i, bits)
                )

    return profiles


def verify_certificate(certificate):
    """
    Verify the basic data attached to one core certificate.

    At this stage this checks:
      - the core is (2K_2, K_4)-free;
      - the computed admissible profiles agree exactly with
        the list stated in the certificate.
    """
    G = build_core(certificate)

    assert is_2k2_k4_free(G)

    computed_profiles = admissible_profiles(
        G,
        certificate["off_cycle_order"],
    )

    expected_profiles = certificate["admissible_profiles"]

    assert computed_profiles == expected_profiles

    return len(computed_profiles)


def run_internal_tests():
    """Run small sanity checks for the basic verification routines."""

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

    assert cycle_neighborhood("Y", 5) == {
        "c2", "c3", "c5"
    }

    assert profile_neighborhood(
        "Y",
        2,
        "110",
        ["f", "a", "g"],
    ) == {
        "c2", "c4", "c5", "f", "a"
    }

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

    assert not one_vertex_admissible(
        triangle,
        {0, 1, 2},
    )

    edge_and_isolated = make_graph(
        vertices=[0, 1, 2],
        edges=[(0, 1)],
    )

    assert not one_vertex_admissible(
        edge_and_isolated,
        {2},
    )

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

    single_edge = make_graph(
        vertices=[0, 1],
        edges=[(0, 1)],
    )

    assert nonedge_permitted(
        single_edge,
        {0},
        {1},
    )

    two_isolated = make_graph(
        vertices=[0, 1],
        edges=[],
    )

    assert not nonedge_permitted(
        two_isolated,
        {0},
        {1},
    )

    assert not edge_permitted(
        single_edge,
        {0, 1},
        {0, 1},
    )

    assert edge_permitted(
        path,
        {0, 1},
        {1, 2},
    )


def main():
    print("Recolorability of (2K_2, K_4)-Free Graphs")
    print("Finite certificate verifier")
    print()

    run_internal_tests()

    number_of_profiles = verify_certificate(K0)

    print("Internal tests passed.")
    print(
        f"{K0['name']}: "
        f"{number_of_profiles} admissible profiles verified."
    )


if __name__ == "__main__":
    main()
