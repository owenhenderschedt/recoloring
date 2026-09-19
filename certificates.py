"""
Finite certificate data for the paper

    Recolorability of (2K_2, K_4)-Free Graphs.

This file contains the cores and the finite claims checked by verify.py.
It contains data only; the verification logic is in verify.py.
"""


K0 = {
    "name": "K0",
    "off_cycle_order": ["f", "a"],

    # Each tuple is:
    # (vertex, cycle type, index, earlier off-cycle neighbors)
    "construction": [
        ("f", "F", 1, []),
        ("a", "Y", 1, []),
    ],

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
