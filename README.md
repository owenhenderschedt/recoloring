# Recolorability of $(2K_2,K_4)$-Free Graphs

This repository contains the computer-assisted verification accompanying the paper

**Recolorability of $(2K_2,K_4)$-Free Graphs**.

The proof reduces several finite structural calculations to attachment profiles relative to small induced subgraphs. The verification program checks the finite calculations appearing in the paper.

In particular, the program verifies:

1. the admissible attachment profiles for each core;
2. the permitted adjacency and nonadjacency relations between profiles;
3. the complete lists of possible rescuers for the displayed local comparisons;
4. the elimination rounds used in the proof; and
5. the specified induced copies of the obstructions \(B_{10}\) and \(B_{11}\).

The mathematical reduction to these finite checks is proved in the paper. The program is used only for the exhaustive finite verification.

## Running the verification

Instructions will be added once the verifier is complete.

## Files

- `verify.py` — verification program;
- `certificates.py` — finite cores and certificates used by the verifier;
- `expected_output.txt` — output of a successful verification run.

The accompanying webpage is available at:

https://recoloring.owenh-math.com
