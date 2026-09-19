"""
Finite certificate data for the paper

    Yes, (2K_2, K_4)-free graphs are recolorable.

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
# Core B10
# ---------------------------------------------------------------------

B10 = {
    "name": "B10",
    "description": "the B10 core",

    "ordered_vertices": [
        "c1", "c2", "c3", "c4", "c5",
        "f", "a", "g", "y", "r",
    ],

    "off_cycle_order": ["f", "a", "g", "y", "r"],

    "construction": [
        ("f", "F", 1, []),
        ("a", "Y", 1, []),
        ("g", "F", 2, []),
        ("y", "Y", 3, ["f", "a"]),
        ("r", "R", 1, ["f", "a", "g"]),
    ],

    "excluded_cycle_types": [],

    "admissible_profiles": [
        "Z[00000]",
        "Z[11100]",
        "F1[00011]",
        "F2[00001]",
        "Y1[00001]",
        "Y1[00011]",
        "Y2[01011]",
        "Y3[10000]",
        "Y3[11000]",
        "Y4[10110]",
        "R1[01110]",
        "R1[11100]",
        "R2[10001]",
        "R2[11101]",
        "R3[00110]",
        "R3[00111]",
        "R3[11110]",
        "R4[00000]",
        "R4[11100]",
        "R5[10011]",
        "R5[10111]",
    ],

    "elimination_rounds": [
        [
            {
                "profile": "Z[00000]",
                "direction": "profile_le_core",
                "core_vertex": "c1",
                "expected_rescuers": [],
            },
            {
                "profile": "Z[11100]",
                "direction": "profile_le_core",
                "core_vertex": "c4",
                "expected_rescuers": [],
            },
            {
                "profile": "F1[00011]",
                "direction": "profile_le_core",
                "core_vertex": "f",
                "expected_rescuers": [],
            },
            {
                "profile": "Y3[10000]",
                "direction": "profile_le_core",
                "core_vertex": "y",
                "expected_rescuers": [],
            },
            {
                "profile": "R1[01110]",
                "direction": "profile_le_core",
                "core_vertex": "c1",
                "expected_rescuers": [],
            },
            {
                "profile": "R2[10001]",
                "direction": "profile_le_core",
                "core_vertex": "c2",
                "expected_rescuers": [],
            },
            {
                "profile": "R2[11101]",
                "direction": "core_le_profile",
                "core_vertex": "c2",
                "expected_rescuers": [],
            },
            {
                "profile": "R3[11110]",
                "direction": "profile_le_core",
                "core_vertex": "c3",
                "expected_rescuers": [],
            },
            {
                "profile": "R4[00000]",
                "direction": "profile_le_core",
                "core_vertex": "f",
                "expected_rescuers": [],
            },
            {
                "profile": "R4[11100]",
                "direction": "profile_le_core",
                "core_vertex": "c4",
                "expected_rescuers": [],
            },
            {
                "profile": "R5[10011]",
                "direction": "profile_le_core",
                "core_vertex": "c5",
                "expected_rescuers": [],
            },
        ],
        [
            {
                "profile": "F2[00001]",
                "direction": "profile_le_core",
                "core_vertex": "g",
                "expected_rescuers": ["R5[10011]"],
            },
            {
                "profile": "Y1[00011]",
                "direction": "profile_le_core",
                "core_vertex": "a",
                "expected_rescuers": ["Y3[10000]"],
            },
        ],
        [
            {
                "profile": "Y3[11000]",
                "direction": "core_le_profile",
                "core_vertex": "y",
                "expected_rescuers": ["Y1[00011]"],
            },
            {
                "profile": "R5[10111]",
                "direction": "core_le_profile",
                "core_vertex": "c5",
                "expected_rescuers": ["F2[00001]"],
            },
        ],
    ],

    "surviving_profiles": [
        "R1[11100]",
        "R3[00110]",
        "Y4[10110]",
        "Y1[00001]",
        "Y2[01011]",
        "R3[00111]",
    ],

    # A row begins with the diagonal entry and then continues to the
    # right, exactly as in the triangular table in the manuscript.
    # 0 = forced nonedge, 1 = forced edge, *=both permitted,
    # x = neither permitted.
    "relation_table": {
        "profiles": [
            "R1[11100]",
            "R3[00110]",
            "Y4[10110]",
            "Y1[00001]",
            "Y2[01011]",
            "R3[00111]",
        ],
        "rows": [
            ["0", "*", "0", "1", "1", "*"],
            ["0", "0", "x", "x", "0"],
            ["0", "1", "1", "x"],
            ["0", "1", "0"],
            ["0", "x"],
            ["0"],
        ],
    },
}


OBSTRUCTIONS = {
    "B10": B10,
}


# ---------------------------------------------------------------------
# Certificate B.5
#
# Core K = (C; f, a, g) with
#
#     f in F1,
#     a in Y1 and fa a nonedge,
#     g in F2 and g nonadjacent to f and a.
#
# This is the core used in Claim 10 of the main theorem.
# ---------------------------------------------------------------------

B5 = {
    "name": "B.5",
    "description": "Claim 10 core",

    "off_cycle_order": ["f", "a", "g"],

    "construction": [
        ("f", "F", 1, []),
        ("a", "Y", 1, []),
        ("g", "F", 2, []),
    ],

    # In the main-theorem branch, U is empty and F1 = {f}.
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
                "expected_rescuers": ["R1[111]"],
            },
        ],
        [
            {
                "profile": "R5[111]",
                "direction": "core_le_profile",
                "core_vertex": "c5",
                "expected_rescuers": ["Y3[110]"],
            },
        ],
    ],

    "obstruction_relations": [
        {
            "label": "C.1",
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
    B5,
    B10,
]
