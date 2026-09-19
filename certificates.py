"""
Finite certificate data for the paper

    Recolorability of (2K_2, K_4)-Free Graphs.

This file contains the cores and finite claims checked by verify.py.
It contains data only; the verification logic is in verify.py.
"""


# ---------------------------------------------------------------------
# Definition of B10
#
# Ordered vertices:
#
#     (c1, c2, c3, c4, c5, f, a, g, y, r)
#
# with
#
#     f in F1,
#     a in Y1,
#     g in F2,
#     y in Y3, adjacent to f and a,
#     r in R1, adjacent to f, a, and g.
# ---------------------------------------------------------------------

B10 = {
    "name": "B10",

    "ordered_vertices": [
        "c1", "c2", "c3", "c4", "c5",
        "f", "a", "g", "y", "r",
    ],

    "construction": [
        ("f", "F", 1, []),
        ("a", "Y", 1, []),
        ("g", "F", 2, []),
        ("y", "Y", 3, ["f", "a"]),
        ("r", "R", 1, ["f", "a", "g"]),
    ],
}


OBSTRUCTIONS = {
    "B10": B10,
}


# ---------------------------------------------------------------------
# Worked example K0
# ---------------------------------------------------------------------

K0 = {
    "name": "K0",
    "description": "worked example",

    "off_cycle_order": ["f", "a"],

    "construction": [
        ("f", "F", 1, []),
        ("a", "Y", 1, []),
    ],

    "excluded_cycle_types": [],

    "admissible_profiles": [
        "U[00]",
        "Z[00]",
        "Z[11]",
        "F1[00]",
        "F2[00]",
        "F5[00]",
        "Y1[00]",
        "Y2[01]",
        "Y3[10]",
        "Y3[11]",
        "Y4[10]",
        "Y4[11]",
        "Y5[01]",
        "R1[01]",
        "R1[11]",
        "R2[10]",
        "R2[11]",
        "R3[00]",
        "R3[11]",
        "R4[00]",
        "R4[11]",
        "R5[10]",
        "R5[11]",
    ],
}


# ---------------------------------------------------------------------
# Table A.1: overlap
#
# Core:
#
#     f in F1,
#     a in Y1, nonadjacent to f,
#     g in F2, nonadjacent to f and a.
#
# Normalization gives U = empty and F1 = {f}.
# ---------------------------------------------------------------------

A1 = {
    "name": "A.1",
    "description": "overlap",

    "off_cycle_order": ["f", "a", "g"],

    "construction": [
        ("f", "F", 1, []),
        ("a", "Y", 1, []),
        ("g", "F", 2, []),
    ],

    "excluded_cycle_types": [
        ("U", None),
        ("F", 1),
    ],

    "admissible_profiles": [
        "Z[000]",
        "Z[111]",
        "F2[000]",
        "Y1[000]",
        "Y2[010]",
        "Y3[100]",
        "Y3[110]",
        "Y4[101]",
        "Y4[111]",
        "Y5[011]",
        "R1[011]",
        "R1[111]",
        "R2[100]",
        "R2[101]",
        "R2[111]",
        "R3[001]",
        "R3[111]",
        "R4[000]",
        "R4[111]",
        "R5[100]",
        "R5[101]",
        "R5[111]",
    ],

    "elimination_rounds": [
        [
            {
                "profile": "Z[000]",
                "direction": "profile_le_core",
                "core_vertex": "c1",
                "expected_rescuers": [],
            },
            {
                "profile": "R4[000]",
                "direction": "profile_le_core",
                "core_vertex": "f",
                "expected_rescuers": [],
            },
            {
                "profile": "R4[111]",
                "direction": "core_le_profile",
                "core_vertex": "c4",
                "expected_rescuers": [],
            },
            {
                "profile": "Y3[110]",
                "direction": "core_le_profile",
                "core_vertex": "c2",
                "expected_rescuers": [
                    "R1[111]",
                ],
            },
        ],

        [
            {
                "profile": "R5[111]",
                "direction": "core_le_profile",
                "core_vertex": "c5",
                "expected_rescuers": [],
            },
        ],
    ],

    "obstruction_relations": [
        {
            "sigma": "Y3[110]",
            "tau": "R1[111]",
            "relation": "nonedge",
            "obstruction": "B10",

            "witness": [
                "c1", "c2", "c3", "c4", "c5",
                "f", "a", "g", "v", "w",
            ],
        },
    ],

    "surviving_profiles": [
        "Y1[000]",
        "F2[000]",
        "R2[100]",
        "R5[100]",
        "Y3[100]",
        "Y2[010]",
        "R3[001]",
        "R2[101]",
        "R5[101]",
        "Y4[101]",
        "R1[011]",
        "Y5[011]",
        "Z[111]",
        "R2[111]",
        "R3[111]",
        "Y4[111]",
        "R1[111]",
    ],
}


CERTIFICATES = [
    K0,
    A1,
]
