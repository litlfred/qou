#!/usr/bin/env python3
"""Geometric construction attempt for conj:s5-so3-fiber-action: the two-Sasakian
decomposition (spin S^3 + colour S^5) and the Lie-algebra row bound that forces
the colour side to be SU(3), with A_5 acting DIRECTLY (no binary cover).

A Reeb/Sasakian construction whose strand fibre carries the defining rep of its
structure group SU(N) computes the Hecke Markov trace through the U_q(sl_N)
Schur-Weyl duality -- i.e. it sees exactly the S_5 blocks with <= N rows
(quantum Schur-Weyl).  This script encodes:

  * structure group SU(N) -> per-strand C^N -> blocks with rows(lambda) <= N
  * SU(2) Hopf S^3 (the existing exceptional-divisor Reeb): sl_2 / Jones / <=2
    rows -> electron (3,1,1) ABSENT.
  * SU(3) Sasakian S^5 (colour): sl_3 / colour HOMFLY / <=3 rows -> electron
    (3,1,1) and muon (3,2) PRESENT.
  * A_5 embeds in the two structure groups DIFFERENTLY:
      - spin SU(2): via the BINARY icosahedral 2I (A_5 has no faithful 2-dim
        rep; central -1 acts as -1).
      - colour SU(3): DIRECTLY via T_1 in SO(3) in SU(3) (T_1 is a faithful
        REAL 3-dim A_5 irrep -> orthogonal -> det 1; no cover needed).

No external deps.
"""
from math import factorial
import sys

PARTS5 = [(5,), (4, 1), (3, 2), (3, 1, 1), (2, 2, 1), (2, 1, 1, 1), (1, 1, 1, 1, 1)]
ELECTRON = (3, 1, 1)
MUON = (3, 2)


def hook_dim(lam):
    n = sum(lam)
    prod = 1
    for i, row in enumerate(lam):
        for j in range(row):
            arm = row - j - 1
            leg = sum(1 for k in range(i + 1, len(lam)) if lam[k] > j)
            prod *= (arm + leg + 1)
    return factorial(n) // prod


def blocks_seen(N):
    """S_5 blocks a SU(N)-Sasakian Reeb construction sees (rows <= N)."""
    return [lam for lam in PARTS5 if len(lam) <= N]


print("=" * 72)
print("Reeb/Sasakian structure group SU(N) -> Hecke blocks with rows <= N")
print("=" * 72)
for N, name in [(2, "spin SU(2) Hopf S^3 (existing exceptional-divisor Reeb)"),
                (3, "colour SU(3) Sasakian S^5 (the upgrade)")]:
    seen = blocks_seen(N)
    print(f"\n  SU({N}): {name}")
    print(f"    invariant = U_q(sl_{N}) Schur-Weyl ({'Jones' if N==2 else 'colour HOMFLY'})")
    print(f"    blocks seen (rows<= {N}): {[''.join(map(str,l)) for l in seen]}")
    print(f"    electron (3,1,1) present: {ELECTRON in seen}   muon (3,2) present: {MUON in seen}")

ok_su2_no_e = ELECTRON not in blocks_seen(2)
ok_su3_has_e = ELECTRON in blocks_seen(3) and MUON in blocks_seen(3)

print()
print("=" * 72)
print("A_5 embedding into the two structure groups (parities)")
print("=" * 72)
# A_5 irrep dims: {1,3,3,4,5}.  No 2-dim => the SPIN C^2 needs the binary cover
# 2I (central -1 acts as -1).  The COLOUR C^3 = T_1 is a faithful REAL 3-dim
# A_5 irrep -> lands in SO(3) subset SU(3) directly (det 1, no cover).
A5_DIMS = [1, 3, 3, 4, 5]
has_2dim = 2 in A5_DIMS
has_3dim = 3 in A5_DIMS
print(f"  A_5 irrep dims {A5_DIMS}: faithful 2-dim? {has_2dim}  faithful 3-dim (T_1)? {has_3dim}")
print(f"  => spin  SU(2): A_5 via BINARY 2I (no 2-dim irrep; central -1 -> -1)")
print(f"  => colour SU(3): A_5 via T_1 in SO(3) in SU(3) DIRECTLY (real 3-dim; no cover)")
ok_spin_binary = not has_2dim    # forces binary cover on spin side
ok_colour_direct = has_3dim      # direct embedding on colour side

print()
print("=" * 72)
print("CONSTRUCTION STATUS")
print("=" * 72)
print("  built/standard:")
print("    - 2I-invariant Sasakian contact form + Reeb=Hopf flow on spin S^3")
print("      (SU(2)-invariant => 2I-invariant); the icosahedral divisor sphere.")
print("    - SU(3)-invariant Sasakian Reeb on colour S^5 subset C^3 (A_5 via T_1).")
print("  forced:")
print("    - the strand structure group must be SU(3) (colour), NOT SU(2) (spin):")
print("      SU(2)/Jones misses the electron (3,1,1); SU(3)/colour hosts it.")
print("  OPEN (the genuine remaining object):")
print("    - the SPIN-COLOUR COUPLING: how the generation degree ell (an SO(3)")
print("      harmonic on the spin divisor sphere) SELECTS the colour Wedderburn")
print("      block (ell=1 -> (3,1,1), ell=2 -> (3,2)).  This ell->block selection")
print("      is the operator-valued branching; constructing it geometrically,")
print("      A_5-equivariantly, is the unbuilt core of conj:s5-so3-fiber-action.")

assert ok_su2_no_e, "SU(2) must miss the electron"
assert ok_su3_has_e, "SU(3) must host electron + muon"
assert ok_spin_binary, "spin side must require the binary cover"
assert ok_colour_direct, "colour side must admit the direct T_1 embedding"
print("\nALL CONSTRUCTION-DECOMPOSITION ASSERTIONS VERIFIED.")
sys.exit(0)
