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


# ---------------------------------------------------------------------
# Core B11
# ---------------------------------------------------------------------

B11 = {
    "name": "B11",
    "description": "the B11 core",

    "ordered_vertices": [
        "c1", "c2", "c3", "c4", "c5",
        "f", "a", "g", "x", "b", "q",
    ],

    "off_cycle_order": ["f", "a", "g", "x", "b", "q"],

    "construction": [
        ("f", "F", 1, []),
        ("a", "Y", 1, []),
        ("g", "F", 2, []),
        ("x", "Y", 2, ["a"]),
        ("b", "Y", 5, ["a", "g"]),
        ("q", "R", 2, ["f", "a", "g", "x"]),
    ],

    "excluded_cycle_types": [],

    "admissible_profiles": [
        "U[000001]",
        "Z[000000]",
        "F1[000001]",
        "F2[000011]",
        "Y1[000111]",
        "Y2[010001]",
        "Y2[010011]",
        "Y5[011000]",
        "Y5[011100]",
        "R1[011001]",
        "R1[111001]",
        "R2[100110]",
        "R2[111100]",
        "R3[111011]",
        "R4[111100]",
        "R5[101110]",
    ],

    # These four profiles are individually admissible, but adjoining
    # a vertex with the indicated profile creates an induced B10.
    "direct_exclusions": [
        {
            "label": "B11.D1",
            "profile": "Y5[011100]",
            "obstruction": "B10",
            "witness": [
                "c2", "c1", "c5", "c4", "c3",
                "g", "x", "f", "v", "q",
            ],
        },
        {
            "label": "B11.D2",
            "profile": "U[000001]",
            "obstruction": "B10",
            "witness": [
                "c2", "x", "c5", "g", "c3",
                "c4", "c1", "b", "v", "a",
            ],
        },
        {
            "label": "B11.D3",
            "profile": "R1[111001]",
            "obstruction": "B10",
            "witness": [
                "c2", "x", "c5", "g", "c3",
                "c4", "v", "b", "f", "a",
            ],
        },
        {
            "label": "B11.D4",
            "profile": "Y2[010011]",
            "obstruction": "B10",
            "witness": [
                "c2", "c1", "c5", "c4", "c3",
                "g", "v", "f", "b", "q",
            ],
        },
    ],

    # After the four direct B10-exclusions above, all remaining
    # admissible profiles are eliminated in one reducedness round.
    "elimination_rounds": [
        [
            {
                "profile": "Z[000000]",
                "direction": "profile_le_core",
                "core_vertex": "c1",
                "expected_rescuers": [],
            },
            {
                "profile": "Y5[011000]",
                "direction": "profile_le_core",
                "core_vertex": "b",
                "expected_rescuers": ["Y2[010001]"],
            },
            {
                "profile": "R2[111100]",
                "direction": "profile_le_core",
                "core_vertex": "q",
                "expected_rescuers": [],
            },
            {
                "profile": "R4[111100]",
                "direction": "profile_le_core",
                "core_vertex": "c4",
                "expected_rescuers": [],
            },
            {
                "profile": "R2[100110]",
                "direction": "profile_le_core",
                "core_vertex": "c2",
                "expected_rescuers": [],
            },
            {
                "profile": "R5[101110]",
                "direction": "profile_le_core",
                "core_vertex": "c5",
                "expected_rescuers": [],
            },
            {
                "profile": "F1[000001]",
                "direction": "profile_le_core",
                "core_vertex": "f",
                "expected_rescuers": ["R1[011001]"],
            },
            {
                "profile": "Y2[010001]",
                "direction": "profile_le_core",
                "core_vertex": "x",
                "expected_rescuers": ["Y5[011000]"],
            },
            {
                "profile": "R1[011001]",
                "direction": "profile_le_core",
                "core_vertex": "c1",
                "expected_rescuers": ["F1[000001]"],
            },
            {
                "profile": "F2[000011]",
                "direction": "profile_le_core",
                "core_vertex": "g",
                "expected_rescuers": [],
            },
            {
                "profile": "R3[111011]",
                "direction": "profile_le_core",
                "core_vertex": "c3",
                "expected_rescuers": [],
            },
            {
                "profile": "Y1[000111]",
                "direction": "profile_le_core",
                "core_vertex": "a",
                "expected_rescuers": [],
            },
        ],
    ],

    # The only nonempty rescuer lists above require these two edges,
    # and each such edge creates an induced B10.
    "obstruction_relations": [
        {
            "label": "B11.R1",
            "sigma": "Y5[011000]",
            "tau": "Y2[010001]",
            "relation": "edge",
            "obstruction": "B10",
            "witness": [
                "c2", "c1", "c5", "c4", "c3",
                "g", "w", "f", "v", "q",
            ],
        },
        {
            "label": "B11.R2",
            "sigma": "F1[000001]",
            "tau": "R1[011001]",
            "relation": "edge",
            "obstruction": "B10",
            "witness": [
                "c2", "x", "c5", "g", "c3",
                "c4", "w", "b", "v", "a",
            ],
        },
    ],

    "surviving_profiles": [],
}


OBSTRUCTIONS = {
    "B10": B10,
    "B11": B11,
}


# ---------------------------------------------------------------------
# Certificates B.1--B.4: the U-branch of Claim 9
#
# In this branch U = {u}, F1 = {f}, and Y1 is empty.  Claim 8 also
# gives that u is complete to every R_i and to Z.  Thus an outside
# R- or Z-vertex must have u-bit 1.  These are branch assumptions
# proved in the manuscript before the certificates are used.
# ---------------------------------------------------------------------

U_BRANCH_REQUIRED_BITS = [
    {
        "kinds": ["R", "Z"],
        "position": 1,
        "value": "1",
    },
]


# ---------------------------------------------------------------------
# Certificate B.1
# ---------------------------------------------------------------------

CERT_B1 = {
    "name": "B.1",
    "description": "Claim 9, Case 1",

    "off_cycle_order": ["f", "u", "y", "yp"],

    "construction": [
        ("f", "F", 1, []),
        ("u", "U", None, []),
        ("y", "Y", 3, ["f"]),
        ("yp", "Y", 4, ["f", "y"]),
    ],

    "excluded_cycle_types": [
        ("U", None),
        ("F", 1),
        ("Y", 1),
    ],

    "required_bits": U_BRANCH_REQUIRED_BITS,

    "admissible_profiles": [
        "Z[0111]",
        "Z[1101]",
        "Z[1110]",
        "F2[0001]",
        "F5[0010]",
        "Y2[0010]",
        "Y3[1001]",
        "Y4[1010]",
        "Y5[0001]",
        "R1[0111]",
        "R2[1101]",
        "R3[0111]",
        "R3[1110]",
        "R4[0111]",
        "R4[1101]",
        "R5[1110]",
    ],

    "elimination_rounds": [
        [
            {
                "profile": "Y2[0010]",
                "direction": "profile_le_core",
                "core_vertex": "f",
                "expected_rescuers": [],
            },
            {
                "profile": "Y3[1001]",
                "direction": "core_le_profile",
                "core_vertex": "y",
                "expected_rescuers": [],
            },
            {
                "profile": "Y4[1010]",
                "direction": "core_le_profile",
                "core_vertex": "yp",
                "expected_rescuers": [],
            },
            {
                "profile": "Z[1101]",
                "direction": "profile_le_core",
                "core_vertex": "c4",
                "expected_rescuers": [],
            },
            {
                "profile": "Z[1110]",
                "direction": "profile_le_core",
                "core_vertex": "c3",
                "expected_rescuers": [],
            },
            {
                "profile": "R2[1101]",
                "direction": "profile_le_core",
                "core_vertex": "c2",
                "expected_rescuers": [],
            },
            {
                "profile": "R5[1110]",
                "direction": "profile_le_core",
                "core_vertex": "c5",
                "expected_rescuers": [],
            },
            {
                "profile": "R4[1101]",
                "direction": "core_le_profile",
                "core_vertex": "c4",
                "expected_rescuers": [],
            },
            {
                "profile": "R3[1110]",
                "direction": "core_le_profile",
                "core_vertex": "c3",
                "expected_rescuers": [],
            },
            {
                "profile": "Z[0111]",
                "direction": "profile_le_core",
                "core_vertex": "c1",
                "expected_rescuers": [],
            },
            {
                "profile": "Y5[0001]",
                "direction": "profile_le_core",
                "core_vertex": "f",
                "expected_rescuers": [],
            },
            {
                "profile": "R1[0111]",
                "direction": "core_le_profile",
                "core_vertex": "c1",
                "expected_rescuers": [],
            },
        ],
    ],

    "surviving_profiles": [
        "F5[0010]",
        "F2[0001]",
        "R3[0111]",
        "R4[0111]",
    ],
}


# ---------------------------------------------------------------------
# Certificate B.2
# ---------------------------------------------------------------------

CERT_B2 = {
    "name": "B.2",
    "description": "Claim 9, Case 2",

    "off_cycle_order": ["f", "u", "y"],

    "construction": [
        ("f", "F", 1, []),
        ("u", "U", None, []),
        ("y", "Y", 3, ["f"]),
    ],

    "excluded_cycle_types": [
        ("U", None),
        ("F", 1),
        ("Y", 1),
        ("Y", 4),
    ],

    "required_bits": U_BRANCH_REQUIRED_BITS,

    "admissible_profiles": [
        "Z[011]",
        "Z[110]",
        "Z[111]",
        "F2[000]",
        "F5[001]",
        "Y2[001]",
        "Y3[100]",
        "Y5[000]",
        "R1[011]",
        "R1[110]",
        "R2[110]",
        "R3[011]",
        "R3[111]",
        "R4[011]",
        "R4[110]",
        "R5[110]",
        "R5[111]",
    ],

    "elimination_rounds": [
        [
            {
                "profile": "Y5[000]",
                "direction": "profile_le_core",
                "core_vertex": "u",
                "expected_rescuers": [],
            },
            {
                "profile": "R1[011]",
                "direction": "core_le_profile",
                "core_vertex": "c1",
                "expected_rescuers": [],
            },
            {
                "profile": "F2[000]",
                "direction": "profile_le_core",
                "core_vertex": "u",
                "expected_rescuers": [],
            },
            {
                "profile": "R5[111]",
                "direction": "profile_le_core",
                "core_vertex": "c5",
                "expected_rescuers": [],
            },
            {
                "profile": "R4[110]",
                "direction": "core_le_profile",
                "core_vertex": "c4",
                "expected_rescuers": [],
            },
            {
                "profile": "Z[011]",
                "direction": "profile_le_core",
                "core_vertex": "c1",
                "expected_rescuers": [],
            },
            {
                "profile": "R3[011]",
                "direction": "profile_le_core",
                "core_vertex": "c3",
                "expected_rescuers": [],
            },
        ],
        [
            {
                "profile": "R2[110]",
                "direction": "core_le_profile",
                "core_vertex": "c2",
                "expected_rescuers": ["Y5[000]"],
            },
            {
                "profile": "R3[111]",
                "direction": "core_le_profile",
                "core_vertex": "c3",
                "expected_rescuers": ["Y5[000]"],
            },
        ],
    ],

    "surviving_profiles": [
        "Y3[100]",
        "Z[110]",
        "R5[110]",
        "R1[110]",
        "F5[001]",
        "Y2[001]",
        "R4[011]",
        "Z[111]",
    ],
}


# ---------------------------------------------------------------------
# Certificate B.3
# ---------------------------------------------------------------------

CERT_B3 = {
    "name": "B.3",
    "description": "Claim 9, Case 2 with r in R1[110]",

    "off_cycle_order": ["f", "u", "y", "r"],

    "construction": [
        ("f", "F", 1, []),
        ("u", "U", None, []),
        ("y", "Y", 3, ["f"]),
        ("r", "R", 1, ["f", "u"]),
    ],

    "excluded_cycle_types": [
        ("U", None),
        ("F", 1),
        ("Y", 1),
        ("Y", 4),
    ],

    "required_bits": U_BRANCH_REQUIRED_BITS,

    "admissible_profiles": [
        "Z[1100]",
        "F2[0001]",
        "F5[0011]",
        "Y2[0011]",
        "Y3[1000]",
        "Y5[0000]",
        "R1[0110]",
        "R1[1100]",
        "R2[1101]",
        "R3[0110]",
        "R3[1110]",
        "R4[1100]",
        "R5[1111]",
    ],

    "elimination_rounds": [
        [
            {
                "profile": "Y5[0000]",
                "direction": "profile_le_core",
                "core_vertex": "f",
                "expected_rescuers": [],
            },
            {
                "profile": "R1[0110]",
                "direction": "core_le_profile",
                "core_vertex": "c1",
                "expected_rescuers": [],
            },
            {
                "profile": "Y3[1000]",
                "direction": "core_le_profile",
                "core_vertex": "y",
                "expected_rescuers": [],
            },
            {
                "profile": "F2[0001]",
                "direction": "profile_le_core",
                "core_vertex": "u",
                "expected_rescuers": [],
            },
            {
                "profile": "Z[1100]",
                "direction": "profile_le_core",
                "core_vertex": "c4",
                "expected_rescuers": [],
            },
            {
                "profile": "Y2[0011]",
                "direction": "profile_le_core",
                "core_vertex": "f",
                "expected_rescuers": [],
            },
            {
                "profile": "R1[1100]",
                "direction": "core_le_profile",
                "core_vertex": "r",
                "expected_rescuers": [],
            },
            {
                "profile": "R5[1111]",
                "direction": "profile_le_core",
                "core_vertex": "c5",
                "expected_rescuers": [],
            },
            {
                "profile": "R4[1100]",
                "direction": "core_le_profile",
                "core_vertex": "c4",
                "expected_rescuers": [],
            },
            {
                "profile": "R3[0110]",
                "direction": "profile_le_core",
                "core_vertex": "c3",
                "expected_rescuers": [],
            },
        ],
        [
            {
                "profile": "R3[1110]",
                "direction": "core_le_profile",
                "core_vertex": "c3",
                "expected_rescuers": ["Y5[0000]"],
            },
            {
                "profile": "R2[1101]",
                "direction": "core_le_profile",
                "core_vertex": "c2",
                "expected_rescuers": ["Y5[0000]"],
            },
        ],
    ],

    "surviving_profiles": [
        "F5[0011]",
    ],
}


# ---------------------------------------------------------------------
# Certificate B.4
# ---------------------------------------------------------------------

CERT_B4 = {
    "name": "B.4",
    "description": "Claim 9, Case 2 with g' in F5[001]",

    "off_cycle_order": ["f", "u", "y", "gp"],

    "construction": [
        ("f", "F", 1, []),
        ("u", "U", None, []),
        ("y", "Y", 3, ["f"]),
        ("gp", "F", 5, ["y"]),
    ],

    "excluded_cycle_types": [
        ("U", None),
        ("F", 1),
        ("Y", 1),
        ("Y", 4),
        ("R", 1),
    ],

    "required_bits": U_BRANCH_REQUIRED_BITS,

    "admissible_profiles": [
        "Z[0110]",
        "Z[1101]",
        "Z[1111]",
        "F5[0010]",
        "Y2[0011]",
        "Y3[1001]",
        "Y5[0000]",
        "R2[1101]",
        "R3[0110]",
        "R3[1111]",
        "R4[1101]",
        "R5[1101]",
        "R5[1110]",
    ],

    "elimination_rounds": [
        [
            {
                "profile": "Y5[0000]",
                "direction": "profile_le_core",
                "core_vertex": "f",
                "expected_rescuers": [],
            },
            {
                "profile": "R4[1101]",
                "direction": "core_le_profile",
                "core_vertex": "c4",
                "expected_rescuers": [],
            },
            {
                "profile": "F5[0010]",
                "direction": "core_le_profile",
                "core_vertex": "gp",
                "expected_rescuers": [],
            },
            {
                "profile": "Z[1111]",
                "direction": "profile_le_core",
                "core_vertex": "c3",
                "expected_rescuers": [],
            },
            {
                "profile": "Z[0110]",
                "direction": "profile_le_core",
                "core_vertex": "c1",
                "expected_rescuers": [],
            },
            {
                "profile": "R3[1111]",
                "direction": "core_le_profile",
                "core_vertex": "c3",
                "expected_rescuers": [],
            },
            {
                "profile": "R3[0110]",
                "direction": "profile_le_core",
                "core_vertex": "c3",
                "expected_rescuers": [],
            },
            {
                "profile": "R5[1110]",
                "direction": "core_le_profile",
                "core_vertex": "c5",
                "expected_rescuers": [],
            },
            {
                "profile": "R2[1101]",
                "direction": "core_le_profile",
                "core_vertex": "c2",
                "expected_rescuers": [],
            },
        ],
        [
            {
                "profile": "Y3[1001]",
                "direction": "core_le_profile",
                "core_vertex": "y",
                "expected_rescuers": ["Z[1111]"],
            },
        ],
        [
            {
                "profile": "Z[1101]",
                "direction": "profile_le_core",
                "core_vertex": "c2",
                "expected_rescuers": ["Y3[1001]"],
            },
        ],
    ],

    "surviving_profiles": [
        "R5[1101]",
        "Y2[0011]",
    ],
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

CERT_B5 = {
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

    "core_comparisons": [
        {
            "left": "a",
            "right": "g",
            "expected_rescuers": ["Y2[010]"],
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


# ---------------------------------------------------------------------
# Certificate B.6
# ---------------------------------------------------------------------

CERT_B6 = {
    "name": "B.6",
    "description": "Claim 10 after adjoining x in Y2[010]",

    "off_cycle_order": ["f", "a", "g", "x"],

    "construction": [
        ("f", "F", 1, []),
        ("a", "Y", 1, []),
        ("g", "F", 2, []),
        ("x", "Y", 2, ["a"]),
    ],

    "excluded_cycle_types": [
        ("U", None),
        ("F", 1),
    ],

    "admissible_profiles": [
        "Z[0000]",
        "Z[1111]",
        "F2[0000]",
        "Y1[0001]",
        "Y2[0100]",
        "Y3[1001]",
        "Y3[1101]",
        "Y4[1011]",
        "Y4[1110]",
        "Y5[0110]",
        "Y5[0111]",
        "R1[0110]",
        "R1[1110]",
        "R1[1111]",
        "R2[1001]",
        "R2[1011]",
        "R2[1111]",
        "R3[1110]",
        "R4[0000]",
        "R4[1111]",
        "R5[1011]",
    ],

    "elimination_rounds": [
        [
            {
                "profile": "Z[0000]",
                "direction": "profile_le_core",
                "core_vertex": "c1",
                "expected_rescuers": [],
            },
            {
                "profile": "R2[1111]",
                "direction": "core_le_profile",
                "core_vertex": "c2",
                "expected_rescuers": [
                    "Y4[1110]",
                    "Y5[0110]",
                    "Y5[0111]",
                ],
            },
            {
                "profile": "R4[0000]",
                "direction": "profile_le_core",
                "core_vertex": "f",
                "expected_rescuers": [],
            },
            {
                "profile": "R1[1111]",
                "direction": "core_le_profile",
                "core_vertex": "c1",
                "expected_rescuers": [
                    "Y3[1001]",
                    "Y3[1101]",
                    "Y4[1011]",
                ],
            },
            {
                "profile": "Y5[0110]",
                "direction": "core_le_profile",
                "core_vertex": "c1",
                "expected_rescuers": ["R2[1111]"],
            },
            {
                "profile": "R4[1111]",
                "direction": "core_le_profile",
                "core_vertex": "c4",
                "expected_rescuers": [],
            },
            {
                "profile": "Y4[1110]",
                "direction": "core_le_profile",
                "core_vertex": "c3",
                "expected_rescuers": [
                    "R2[1011]",
                    "R2[1111]",
                ],
            },
            {
                "profile": "R1[1110]",
                "direction": "core_le_profile",
                "core_vertex": "c1",
                "expected_rescuers": [
                    "Y4[1011]",
                    "Y4[1110]",
                ],
            },
            {
                "profile": "Y3[1001]",
                "direction": "core_le_profile",
                "core_vertex": "c2",
                "expected_rescuers": ["R1[1111]"],
            },
            {
                "profile": "Y3[1101]",
                "direction": "core_le_profile",
                "core_vertex": "c2",
                "expected_rescuers": ["R1[1111]"],
            },
            {
                "profile": "R2[1011]",
                "direction": "core_le_profile",
                "core_vertex": "c2",
                "expected_rescuers": [
                    "Y4[1011]",
                    "Y4[1110]",
                ],
            },
            {
                "profile": "Y4[1011]",
                "direction": "core_le_profile",
                "core_vertex": "c5",
                "expected_rescuers": [
                    "R1[1110]",
                    "R1[1111]",
                ],
            },
            {
                "profile": "Y5[0111]",
                "direction": "core_le_profile",
                "core_vertex": "c1",
                "expected_rescuers": ["R2[1111]"],
            },
            {
                "profile": "Z[1111]",
                "direction": "profile_le_core",
                "core_vertex": "c4",
                "expected_rescuers": [
                    "Y3[1001]",
                    "Y5[0110]",
                ],
            },
        ],
        [
            {
                "profile": "F2[0000]",
                "direction": "core_le_profile",
                "core_vertex": "g",
                "expected_rescuers": ["R2[1011]"],
            },
            {
                "profile": "Y2[0100]",
                "direction": "core_le_profile",
                "core_vertex": "x",
                "expected_rescuers": [
                    "Y5[0111]",
                    "R1[1111]",
                ],
            },
            {
                "profile": "R1[0110]",
                "direction": "core_le_profile",
                "core_vertex": "c1",
                "expected_rescuers": ["Y4[1110]"],
            },
            {
                "profile": "R3[1110]",
                "direction": "core_le_profile",
                "core_vertex": "c3",
                "expected_rescuers": ["Y5[0110]"],
            },
            {
                "profile": "Y1[0001]",
                "direction": "core_le_profile",
                "core_vertex": "a",
                "expected_rescuers": [
                    "Y3[1101]",
                    "R2[1111]",
                ],
            },
            {
                "profile": "R2[1001]",
                "direction": "core_le_profile",
                "core_vertex": "c2",
                "expected_rescuers": ["Y4[1011]"],
            },
            {
                "profile": "R5[1011]",
                "direction": "core_le_profile",
                "core_vertex": "c5",
                "expected_rescuers": ["Y3[1001]"],
            },
        ],
    ],

    "obstruction_relations": [
        {
            "label": "C.2",
            "sigma": "Y5[0110]",
            "tau": "R2[1111]",
            "relation": "nonedge",
            "obstruction": "B11",
            "witness": [
                "c1", "c2", "c3", "c4", "c5",
                "f", "a", "g", "x", "v", "w",
            ],
        },
        {
            "label": "C.3",
            "sigma": "Y4[1110]",
            "tau": "R2[1011]",
            "relation": "nonedge",
            "obstruction": "B11",
            "witness": [
                "c2", "x", "c4", "g", "c1",
                "c5", "c3", "v", "w", "a", "f",
            ],
        },
        {
            "label": "C.4",
            "sigma": "Y4[1110]",
            "tau": "R2[1111]",
            "relation": "nonedge",
            "obstruction": "B10",
            "witness": [
                "c1", "c5", "f", "c3", "a",
                "c4", "c2", "w", "v", "x",
            ],
        },
        {
            "label": "C.5",
            "sigma": "Y4[1110]",
            "tau": "R1[1110]",
            "relation": "nonedge",
            "obstruction": "B10",
            "witness": [
                "c2", "x", "c5", "g", "v",
                "c4", "w", "c1", "f", "a",
            ],
        },
        {
            "label": "C.6",
            "sigma": "R1[1110]",
            "tau": "Y4[1011]",
            "relation": "nonedge",
            "obstruction": "B11",
            "witness": [
                "c1", "a", "c4", "f", "c2",
                "c3", "c5", "w", "v", "x", "g",
            ],
        },
        {
            "label": "C.7",
            "sigma": "Y3[1001]",
            "tau": "R1[1111]",
            "relation": "nonedge",
            "obstruction": "B11",
            "witness": [
                "c2", "c1", "c5", "c4", "c3",
                "g", "x", "f", "a", "v", "w",
            ],
        },
        {
            "label": "C.8",
            "sigma": "Y3[1101]",
            "tau": "R1[1111]",
            "relation": "nonedge",
            "obstruction": "B10",
            "witness": [
                "c1", "c2", "c3", "c4", "c5",
                "f", "a", "g", "v", "w",
            ],
        },
        {
            "label": "C.9",
            "sigma": "R2[1011]",
            "tau": "Y4[1011]",
            "relation": "nonedge",
            "obstruction": "B10",
            "witness": [
                "c1", "a", "c3", "f", "w",
                "c4", "v", "c2", "g", "x",
            ],
        },
        {
            "label": "C.10",
            "sigma": "Y4[1011]",
            "tau": "R1[1111]",
            "relation": "nonedge",
            "obstruction": "B10",
            "witness": [
                "c2", "c3", "g", "c5", "x",
                "c4", "c1", "w", "v", "a",
            ],
        },
        {
            "label": "C.11",
            "sigma": "Y5[0111]",
            "tau": "R2[1111]",
            "relation": "nonedge",
            "obstruction": "B10",
            "witness": [
                "c2", "c1", "c5", "c4", "c3",
                "g", "x", "f", "v", "w",
            ],
        },
        {
            "label": "C.12",
            "sigma": "Y5[0110]",
            "tau": "Z[1111]",
            "relation": "edge",
            "obstruction": "B10",
            "witness": [
                "x", "c2", "v", "g", "c4",
                "c3", "w", "c5", "a", "f",
            ],
        },
        {
            "label": "C.13",
            "sigma": "Y3[1001]",
            "tau": "Z[1111]",
            "relation": "edge",
            "obstruction": "B10",
            "witness": [
                "a", "c1", "v", "f", "c4",
                "c5", "w", "c3", "x", "g",
            ],
        },
    ],

    "surviving_profiles": [],
}


# ---------------------------------------------------------------------
# Certificate B.7
# ---------------------------------------------------------------------

CERT_B7 = {
    "name": "B.7",
    "description": "Claim 11, Step 1, Case A",

    "off_cycle_order": ["f", "a", "y", "p", "q"],

    "construction": [
        ("f", "F", 1, []),
        ("a", "Y", 1, []),
        ("y", "Y", 3, ["f", "a"]),
        ("p", "Y", 5, ["a"]),
        ("q", "R", 5, ["f", "p"]),
    ],

    "excluded_cycle_types": [
        ("U", None),
        ("F", 1),
        ("F", 2),
        ("F", 5),
    ],

    "admissible_profiles": [
        "Z[00000]",
        "Z[11000]",
        "Y1[00110]",
        "Y1[00111]",
        "Y2[01101]",
        "Y2[01111]",
        "Y3[10010]",
        "Y3[11000]",
        "Y3[11001]",
        "Y4[10110]",
        "Y5[01001]",
        "R1[01101]",
        "R2[10010]",
        "R2[11000]",
        "R3[00110]",
        "R3[11110]",
        "R4[11001]",
        "R5[10010]",
        "R5[10110]",
        "R5[11010]",
    ],

    "direct_exclusions": [
        {
            "label": "C.15",
            "profile": "Y1[00111]",
            "obstruction": "B10",
            "witness": [
                "c1", "c2", "f", "c4", "v",
                "c3", "c5", "q", "y", "p",
            ],
        },
        {
            "label": "C.16",
            "profile": "R5[11010]",
            "obstruction": "B10",
            "witness": [
                "c1", "c2", "f", "c4", "a",
                "c3", "c5", "v", "y", "p",
            ],
        },
    ],

    "surviving_profiles": [
        "Z[00000]",
        "Z[11000]",
        "Y1[00110]",
        "Y2[01101]",
        "Y2[01111]",
        "Y3[10010]",
        "Y3[11000]",
        "Y3[11001]",
        "Y4[10110]",
        "Y5[01001]",
        "R1[01101]",
        "R2[10010]",
        "R2[11000]",
        "R3[00110]",
        "R3[11110]",
        "R4[11001]",
        "R5[10010]",
        "R5[10110]",
    ],

    "core_comparisons": [
        {
            "left": "q",
            "right": "c5",
            "expected_rescuers": [],
        },
    ],
}


# ---------------------------------------------------------------------
# Certificate B.8
# ---------------------------------------------------------------------

CERT_B8 = {
    "name": "B.8",
    "description": "Claim 11, Step 1, Case B",

    "off_cycle_order": ["f", "a", "y", "p", "q"],

    "construction": [
        ("f", "F", 1, []),
        ("a", "Y", 1, []),
        ("y", "Y", 3, ["f", "a"]),
        ("p", "R", 1, ["f", "a"]),
        ("q", "Y", 1, ["p"]),
    ],

    "excluded_cycle_types": [
        ("U", None),
        ("F", 1),
        ("F", 2),
        ("F", 5),
    ],

    "admissible_profiles": [
        "Z[00000]",
        "Y1[00010]",
        "Y1[00110]",
        "Y2[01101]",
        "Y2[01111]",
        "Y3[10000]",
        "Y3[11000]",
        "Y3[11001]",
        "Y4[10101]",
        "R1[01101]",
        "R1[11001]",
        "R2[10010]",
        "R2[11010]",
        "R3[00110]",
        "R3[11101]",
        "R4[00000]",
        "R4[11001]",
        "R5[10110]",
        "R5[10111]",
    ],

    "direct_exclusions": [
        {
            "label": "C.17",
            "profile": "R5[10111]",
            "obstruction": "B10",
            "witness": [
                "c1", "c2", "c3", "c4", "v",
                "f", "a", "q", "y", "p",
            ],
        },
        {
            "label": "C.18",
            "profile": "Y4[10101]",
            "obstruction": "B11",
            "witness": [
                "a", "p", "f", "v", "c1",
                "c2", "c4", "y", "q", "c5", "c3",
            ],
        },
    ],

    "surviving_profiles": [
        "Z[00000]",
        "Y1[00010]",
        "Y1[00110]",
        "Y2[01101]",
        "Y2[01111]",
        "Y3[10000]",
        "Y3[11000]",
        "Y3[11001]",
        "R1[01101]",
        "R1[11001]",
        "R2[10010]",
        "R2[11010]",
        "R3[00110]",
        "R3[11101]",
        "R4[00000]",
        "R4[11001]",
        "R5[10110]",
    ],

    "core_comparisons": [
        {
            "left": "q",
            "right": "a",
            "expected_rescuers": [],
        },
    ],
}


# ---------------------------------------------------------------------
# Certificate B.9
# ---------------------------------------------------------------------

CERT_B9 = {
    "name": "B.9",
    "description": "Claim 11, Step 2, Case 1",

    "off_cycle_order": ["f", "a"],

    "construction": [
        ("f", "F", 1, []),
        ("a", "Y", 1, []),
    ],

    "excluded_cycle_types": [
        ("U", None),
        ("F", 1),
        ("F", 2),
        ("F", 5),
        ("Y", 2),
        ("Y", 5),
    ],

    # In this subcase a is anticomplete to Y3 union Y4, and
    # no vertex of R1[11] occurs.
    "excluded_profiles": [
        "Y3[11]",
        "Y4[11]",
        "R1[11]",
    ],

    "admissible_profiles": [
        "Z[00]",
        "Z[11]",
        "Y1[00]",
        "Y3[10]",
        "Y4[10]",
        "R1[01]",
        "R2[10]",
        "R2[11]",
        "R3[00]",
        "R3[11]",
        "R4[00]",
        "R4[11]",
        "R5[10]",
        "R5[11]",
    ],

    "elimination_rounds": [
        [
            {
                "profile": "Z[00]",
                "direction": "profile_le_core",
                "core_vertex": "c1",
                "expected_rescuers": [],
            },
            {
                "profile": "R5[11]",
                "direction": "core_le_profile",
                "core_vertex": "c5",
                "expected_rescuers": [],
            },
            {
                "profile": "R3[00]",
                "direction": "profile_le_core",
                "core_vertex": "f",
                "expected_rescuers": [],
            },
            {
                "profile": "R3[11]",
                "direction": "core_le_profile",
                "core_vertex": "c3",
                "expected_rescuers": [],
            },
            {
                "profile": "R4[00]",
                "direction": "profile_le_core",
                "core_vertex": "f",
                "expected_rescuers": [],
            },
            {
                "profile": "R4[11]",
                "direction": "core_le_profile",
                "core_vertex": "c4",
                "expected_rescuers": [],
            },
            {
                "profile": "Y4[10]",
                "direction": "core_le_profile",
                "core_vertex": "c5",
                "expected_rescuers": [],
            },
            {
                "profile": "Y3[10]",
                "direction": "core_le_profile",
                "core_vertex": "c2",
                "expected_rescuers": [],
            },
            {
                "profile": "R1[01]",
                "direction": "core_le_profile",
                "core_vertex": "c1",
                "expected_rescuers": [],
            },
            {
                "profile": "R2[11]",
                "direction": "core_le_profile",
                "core_vertex": "c2",
                "expected_rescuers": [],
            },
        ],
        [
            {
                "profile": "Y1[00]",
                "direction": "core_le_profile",
                "core_vertex": "a",
                "expected_rescuers": [
                    "R2[11]",
                    "R5[11]",
                ],
            },
            {
                "profile": "R2[10]",
                "direction": "core_le_profile",
                "core_vertex": "c2",
                "expected_rescuers": ["Y4[10]"],
            },
            {
                "profile": "R5[10]",
                "direction": "core_le_profile",
                "core_vertex": "c5",
                "expected_rescuers": ["Y3[10]"],
            },
            {
                "profile": "Z[11]",
                "direction": "profile_le_core",
                "core_vertex": "c3",
                "expected_rescuers": ["Y4[10]"],
            },
        ],
    ],

    "surviving_profiles": [],
}


# ---------------------------------------------------------------------
# Certificate B.10
# ---------------------------------------------------------------------

CERT_B10 = {
    "name": "B.10",
    "description": "Claim 11, Step 2, Case 2",

    "off_cycle_order": ["f", "a", "x"],

    "construction": [
        ("f", "F", 1, []),
        ("a", "Y", 1, []),
        ("x", "Y", 2, ["a"]),
    ],

    # In this branch U is empty and all F-classes except the chosen
    # vertex f have already been excluded.  Claim 11, Case 1 also gives
    # that a is anticomplete to Y3 union Y4.
    "excluded_cycle_types": [
        ("U", None),
        ("F", 1),
        ("F", 2),
        ("F", 3),
        ("F", 4),
        ("F", 5),
    ],

    "excluded_profiles": [
        "Y3[111]",
        "Y4[110]",
    ],

    "admissible_profiles": [
        "Z[000]",
        "Z[110]",
        "Z[111]",
        "Y1[001]",
        "Y2[010]",
        "Y3[101]",
        "Y4[101]",
        "Y5[010]",
        "Y5[011]",
        "R1[010]",
        "R1[110]",
        "R1[111]",
        "R2[101]",
        "R2[111]",
        "R3[000]",
        "R3[110]",
        "R4[000]",
        "R4[001]",
        "R4[110]",
        "R4[111]",
        "R5[101]",
        "R5[110]",
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
                "profile": "R1[010]",
                "direction": "core_le_profile",
                "core_vertex": "c1",
                "expected_rescuers": [],
            },
            {
                "profile": "R4[110]",
                "direction": "profile_le_core",
                "core_vertex": "c4",
                "expected_rescuers": [],
            },
        ],
        [
            {
                "profile": "R3[110]",
                "direction": "profile_le_core",
                "core_vertex": "c3",
                "expected_rescuers": ["R1[010]"],
            },
            {
                "profile": "R4[111]",
                "direction": "profile_le_core",
                "core_vertex": "c4",
                "expected_rescuers": ["R1[010]"],
            },
        ],
    ],

    "surviving_profiles": [
        "R3[000]",
        "R4[000]",
        "Y5[010]",
        "Y2[010]",
        "Z[110]",
        "R5[110]",
        "R1[110]",
        "Y1[001]",
        "R4[001]",
        "R2[101]",
        "R5[101]",
        "Y4[101]",
        "Y3[101]",
        "Y5[011]",
        "Z[111]",
        "R2[111]",
        "R1[111]",
    ],

    "core_comparisons": [
        {
            "left": "c1",
            "right": "x",
            "expected_rescuers": ["R5[110]"],
        },
    ],
}


# ---------------------------------------------------------------------
# Certificate B.11
# ---------------------------------------------------------------------

CERT_B11 = {
    "name": "B.11",
    "description": "Claim 11, Step 2, Case 2 after adjoining q' in R5[110]",

    "off_cycle_order": ["f", "a", "x", "q"],

    "construction": [
        ("f", "F", 1, []),
        ("a", "Y", 1, []),
        ("x", "Y", 2, ["a"]),
        ("q", "R", 5, ["f", "a"]),
    ],

    "excluded_cycle_types": [
        ("U", None),
        ("F", 1),
        ("F", 2),
        ("F", 3),
        ("F", 4),
        ("F", 5),
    ],

    "excluded_profiles": [
        "Y3[1110]",
        "Y4[1100]",
    ],

    "admissible_profiles": [
        "Z[0000]",
        "Z[1100]",
        "Y1[0011]",
        "Y2[0100]",
        "Y3[1011]",
        "Y5[0101]",
        "Y5[0111]",
        "R1[0101]",
        "R1[1101]",
        "R1[1111]",
        "R2[1010]",
        "R2[1011]",
        "R2[1110]",
        "R3[1100]",
        "R4[0011]",
        "R4[1111]",
        "R5[1010]",
        "R5[1100]",
    ],

    "elimination_rounds": [
        [
            {
                "profile": "Z[0000]",
                "direction": "profile_le_core",
                "core_vertex": "c1",
                "expected_rescuers": [],
            },
            {
                "profile": "Z[1100]",
                "direction": "profile_le_core",
                "core_vertex": "c3",
                "expected_rescuers": [],
            },
            {
                "profile": "R2[1010]",
                "direction": "core_le_profile",
                "core_vertex": "c2",
                "expected_rescuers": [],
            },
            {
                "profile": "R2[1110]",
                "direction": "core_le_profile",
                "core_vertex": "c2",
                "expected_rescuers": ["Y5[0111]"],
            },
            {
                "profile": "R1[0101]",
                "direction": "core_le_profile",
                "core_vertex": "c1",
                "expected_rescuers": [],
            },
            {
                "profile": "Y5[0101]",
                "direction": "core_le_profile",
                "core_vertex": "c1",
                "expected_rescuers": [],
            },
            {
                "profile": "R1[1101]",
                "direction": "core_le_profile",
                "core_vertex": "c1",
                "expected_rescuers": ["Y3[1011]"],
            },
            {
                "profile": "R4[0011]",
                "direction": "profile_le_core",
                "core_vertex": "c4",
                "expected_rescuers": [
                    "R1[1101]",
                    "R2[1110]",
                ],
            },
            {
                "profile": "R2[1011]",
                "direction": "core_le_profile",
                "core_vertex": "c2",
                "expected_rescuers": [],
            },
            {
                "profile": "Y3[1011]",
                "direction": "core_le_profile",
                "core_vertex": "c2",
                "expected_rescuers": [
                    "R1[1101]",
                    "R1[1111]",
                ],
            },
            {
                "profile": "Y5[0111]",
                "direction": "core_le_profile",
                "core_vertex": "c1",
                "expected_rescuers": ["R2[1110]"],
            },
            {
                "profile": "R1[1111]",
                "direction": "core_le_profile",
                "core_vertex": "c1",
                "expected_rescuers": ["Y3[1011]"],
            },
            {
                "profile": "R4[1111]",
                "direction": "core_le_profile",
                "core_vertex": "c4",
                "expected_rescuers": [],
            },
        ],
        [
            {
                "profile": "Y2[0100]",
                "direction": "core_le_profile",
                "core_vertex": "x",
                "expected_rescuers": [
                    "Y5[0111]",
                    "R1[1111]",
                ],
            },
            {
                "profile": "R5[1100]",
                "direction": "core_le_profile",
                "core_vertex": "q",
                "expected_rescuers": ["R2[1011]"],
            },
            {
                "profile": "R3[1100]",
                "direction": "core_le_profile",
                "core_vertex": "c3",
                "expected_rescuers": ["Y5[0101]"],
            },
            {
                "profile": "R5[1010]",
                "direction": "core_le_profile",
                "core_vertex": "c5",
                "expected_rescuers": ["Y3[1011]"],
            },
            {
                "profile": "Y1[0011]",
                "direction": "core_le_profile",
                "core_vertex": "a",
                "expected_rescuers": ["R2[1110]"],
            },
        ],
    ],

    "obstruction_relations": [
        {
            "label": "C.19",
            "sigma": "R2[1110]",
            "tau": "Y5[0111]",
            "relation": "nonedge",
            "obstruction": "B11",
            "witness": [
                "c2", "c1", "a", "c4", "f",
                "q", "x", "c3", "c5", "v", "w",
            ],
        },
        {
            "label": "C.20",
            "sigma": "R1[1101]",
            "tau": "Y3[1011]",
            "relation": "nonedge",
            "obstruction": "B11",
            "witness": [
                "c1", "c2", "f", "c4", "a",
                "c3", "c5", "q", "x", "v", "w",
            ],
        },
        {
            "label": "C.21",
            "sigma": "R2[1110]",
            "tau": "R4[0011]",
            "relation": "edge",
            "obstruction": "B10",
            "witness": [
                "c5", "c1", "v", "c3", "c4",
                "a", "w", "f", "x", "q",
            ],
        },
        {
            "label": "C.22",
            "sigma": "R1[1101]",
            "tau": "R4[0011]",
            "relation": "edge",
            "obstruction": "B10",
            "witness": [
                "x", "c2", "v", "q", "c4",
                "f", "w", "a", "c5", "c3",
            ],
        },
        {
            "label": "C.23",
            "sigma": "Y3[1011]",
            "tau": "R1[1111]",
            "relation": "nonedge",
            "obstruction": "B10",
            "witness": [
                "c2", "c1", "a", "c4", "f",
                "q", "x", "c3", "w", "v",
            ],
        },
    ],

    "surviving_profiles": [],
}


# ---------------------------------------------------------------------
# Certificate B.12
# ---------------------------------------------------------------------

CERT_B12 = {
    "name": "B.12",
    "description": "Claim 11, Step 2, Case 3",

    "off_cycle_order": ["f", "a", "r"],

    "construction": [
        ("f", "F", 1, []),
        ("a", "Y", 1, []),
        ("r", "R", 1, ["f", "a"]),
    ],

    "excluded_cycle_types": [
        ("U", None),
        ("F", 1),
        ("F", 2),
        ("F", 3),
        ("F", 4),
        ("F", 5),
    ],

    "excluded_profiles": [
        "Y3[110]",
        "Y4[110]",
    ],

    "admissible_profiles": [
        "Z[000]",
        "Z[110]",
        "Y1[001]",
        "Y2[010]",
        "Y2[011]",
        "Y3[100]",
        "Y4[100]",
        "Y5[010]",
        "Y5[011]",
        "R1[010]",
        "R1[110]",
        "R2[101]",
        "R2[111]",
        "R3[000]",
        "R3[001]",
        "R3[110]",
        "R4[000]",
        "R4[001]",
        "R4[110]",
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
                "profile": "R1[010]",
                "direction": "core_le_profile",
                "core_vertex": "c1",
                "expected_rescuers": [],
            },
            {
                "profile": "R2[101]",
                "direction": "core_le_profile",
                "core_vertex": "c2",
                "expected_rescuers": [],
            },
            {
                "profile": "R5[101]",
                "direction": "core_le_profile",
                "core_vertex": "c5",
                "expected_rescuers": [],
            },
        ],
        [
            {
                "profile": "R3[110]",
                "direction": "profile_le_core",
                "core_vertex": "c3",
                "expected_rescuers": ["R1[010]"],
            },
            {
                "profile": "R4[110]",
                "direction": "profile_le_core",
                "core_vertex": "c4",
                "expected_rescuers": ["R1[010]"],
            },
        ],
    ],

    "surviving_profiles": [
        "R3[000]",
        "R4[000]",
        "Y4[100]",
        "Y3[100]",
        "Y5[010]",
        "Y2[010]",
        "Z[110]",
        "R1[110]",
        "R3[001]",
        "Y1[001]",
        "R4[001]",
        "Y5[011]",
        "Y2[011]",
        "R2[111]",
        "R5[111]",
    ],

    "core_comparisons": [
        {
            "left": "c1",
            "right": "r",
            "expected_rescuers": [
                "Y3[100]",
                "Y4[100]",
            ],
        },
    ],
}


# ---------------------------------------------------------------------
# Certificate B.13
# ---------------------------------------------------------------------

CERT_B13 = {
    "name": "B.13",
    "description": "Claim 11, Step 2, Case 3 after adjoining y in Y3[100]",

    "off_cycle_order": ["f", "a", "r", "y"],

    "construction": [
        ("f", "F", 1, []),
        ("a", "Y", 1, []),
        ("r", "R", 1, ["f", "a"]),
        ("y", "Y", 3, ["f"]),
    ],

    "excluded_cycle_types": [
        ("U", None),
        ("F", 1),
        ("F", 2),
        ("F", 3),
        ("F", 4),
        ("F", 5),
    ],

    "excluded_profiles": [
        "Y3[1100]",
        "Y4[1101]",
    ],

    "admissible_profiles": [
        "Z[0000]",
        "Y1[0010]",
        "Y1[0011]",
        "Y2[0101]",
        "Y2[0111]",
        "Y3[1000]",
        "Y5[0101]",
        "Y5[0111]",
        "R1[0101]",
        "R1[1100]",
        "R2[1010]",
        "R3[0011]",
        "R3[1101]",
        "R4[0000]",
        "R4[1100]",
        "R5[1011]",
        "R5[1111]",
    ],

    "elimination_rounds": [
        [
            {
                "profile": "Z[0000]",
                "direction": "profile_le_core",
                "core_vertex": "c1",
                "expected_rescuers": [],
            },
            {
                "profile": "R4[0000]",
                "direction": "profile_le_core",
                "core_vertex": "c4",
                "expected_rescuers": [],
            },
            {
                "profile": "R2[1010]",
                "direction": "core_le_profile",
                "core_vertex": "c2",
                "expected_rescuers": [],
            },
            {
                "profile": "R1[0101]",
                "direction": "core_le_profile",
                "core_vertex": "c1",
                "expected_rescuers": [],
            },
            {
                "profile": "Y5[0101]",
                "direction": "core_le_profile",
                "core_vertex": "c1",
                "expected_rescuers": [],
            },
            {
                "profile": "Y2[0101]",
                "direction": "core_le_profile",
                "core_vertex": "c1",
                "expected_rescuers": ["R5[1111]"],
            },
            {
                "profile": "R3[0011]",
                "direction": "profile_le_core",
                "core_vertex": "f",
                "expected_rescuers": ["Y5[0101]"],
            },
            {
                "profile": "Y1[0011]",
                "direction": "core_le_profile",
                "core_vertex": "a",
                "expected_rescuers": ["R5[1111]"],
            },
            {
                "profile": "R5[1011]",
                "direction": "core_le_profile",
                "core_vertex": "c5",
                "expected_rescuers": [],
            },
            {
                "profile": "Y5[0111]",
                "direction": "core_le_profile",
                "core_vertex": "c1",
                "expected_rescuers": [],
            },
            {
                "profile": "Y2[0111]",
                "direction": "core_le_profile",
                "core_vertex": "c1",
                "expected_rescuers": ["R5[1111]"],
            },
            {
                "profile": "R5[1111]",
                "direction": "core_le_profile",
                "core_vertex": "c5",
                "expected_rescuers": [
                    "Y2[0101]",
                    "Y2[0111]",
                ],
            },
        ],
        [
            {
                "profile": "Y3[1000]",
                "direction": "core_le_profile",
                "core_vertex": "y",
                "expected_rescuers": ["Y1[0011]"],
            },
            {
                "profile": "R1[1100]",
                "direction": "core_le_profile",
                "core_vertex": "r",
                "expected_rescuers": [
                    "Y2[0111]",
                    "Y5[0111]",
                ],
            },
            {
                "profile": "R4[1100]",
                "direction": "core_le_profile",
                "core_vertex": "c4",
                "expected_rescuers": ["Y2[0101]"],
            },
            {
                "profile": "Y1[0010]",
                "direction": "core_le_profile",
                "core_vertex": "a",
                "expected_rescuers": ["R5[1111]"],
            },
            {
                "profile": "R3[1101]",
                "direction": "core_le_profile",
                "core_vertex": "c3",
                "expected_rescuers": ["Y5[0101]"],
            },
        ],
    ],

    "obstruction_relations": [
        {
            "label": "C.24",
            "sigma": "Y2[0101]",
            "tau": "R5[1111]",
            "relation": "nonedge",
            "obstruction": "B11",
            "witness": [
                "c1", "c2", "f", "c4", "a",
                "c3", "c5", "w", "v", "r", "y",
            ],
        },
        {
            "label": "C.25",
            "sigma": "Y5[0101]",
            "tau": "R3[0011]",
            "relation": "edge",
            "obstruction": "B10",
            "witness": [
                "r", "a", "v", "y", "f",
                "c3", "w", "c5", "c2", "c4",
            ],
        },
        {
            "label": "C.26",
            "sigma": "Y1[0011]",
            "tau": "R5[1111]",
            "relation": "nonedge",
            "obstruction": "B10",
            "witness": [
                "c1", "c2", "c3", "c4", "w",
                "f", "v", "a", "y", "r",
            ],
        },
        {
            "label": "C.27",
            "sigma": "Y2[0111]",
            "tau": "R5[1111]",
            "relation": "nonedge",
            "obstruction": "B10",
            "witness": [
                "c2", "c1", "a", "c4", "f",
                "w", "v", "c3", "r", "y",
            ],
        },
    ],

    "surviving_profiles": [],
}


CERTIFICATES = [
    K0,
    CERT_B1,
    CERT_B2,
    CERT_B3,
    CERT_B4,
    CERT_B5,
    CERT_B6,
    CERT_B7,
    CERT_B8,
    CERT_B9,
    CERT_B10,
    CERT_B11,
    CERT_B12,
    CERT_B13,
    B10,
    B11,
]
