"""
Finite certificate data for the paper

    Recolorability of (2K_2, K_4)-Free Graphs.

This file contains the cores and finite claims checked by verify.py.
It contains data only; the verification logic is in verify.py.
"""


# ---------------------------------------------------------------------
# Worked example K0
# ---------------------------------------------------------------------

K0 = {
    "name": "K0",
    "description": "worked example",
    "off_cycle_order": ["f", "a"],

    # Each tuple is
    # (vertex, cycle type, index, earlier off-cycle neighbors).
    "construction": [
        ("f", "F", 1, []),
        ("a", "Y", 1, []),
    ],

    # No additional branch restrictions are imposed in this example.
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
# Current indexing:
#
#     f in F_1,
#     a in Y_1, nonadjacent to f,
#     g in F_2, nonadjacent to f and a.
#
# The normalized assumptions give U = empty and F_1 = {f}.
# Thus no U-profile and no additional F_1-profile is permitted.
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
}


CERTIFICATES = [
    K0,
    A1,
]
