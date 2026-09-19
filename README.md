# Yes, $(2K_2,K_4)$-free graphs are recolorable

This repository contains the computer-assisted verification accompanying the paper

**Yes, $(2K_2,K_4)$-free graphs are recolorable**  
Henry Echeverría and Owen Henderschedt.

The proof reduces several repetitive finite structural calculations to attachment profiles relative to small induced cores. The mathematical reduction to these finite calculations is proved in the paper. The program in this repository checks the resulting finite certificates exhaustively.

## What the verifier checks

The verifier checks the finite calculations used in the computer-assisted portions of the proof. In particular, it verifies:

1. that every stated core is $(2K_2,K_4)$-free;
2. the complete list of admissible attachment profiles for each core;
3. the permitted edge and nonedge relations between profiles;
4. the local neighborhood comparisons used in the reducedness arguments;
5. the complete lists of possible rescuing profiles in each elimination round;
6. the simultaneous elimination rounds and the final surviving profiles;
7. every recorded induced copy of the obstruction graphs $B_{10}$ and $B_{11}$; and
8. the profile-relation table used in the proof for the core $B_{10}$.

The current certificate data includes the worked example $K_0$, Certificates B.1--B.20, and the special cores $B_{10}$ and $B_{11}$.

## Files

- `verify.py` — general verification logic;
- `certificates.py` — the finite core and certificate data from the paper;
- `expected_output.txt` — output of a successful complete verification;
- `.github/workflows/verify.yml` — GitHub Actions workflow that runs the verifier automatically.

No external Python packages are required.

## Running the verification

With Python 3 installed, run

```bash
python verify.py
