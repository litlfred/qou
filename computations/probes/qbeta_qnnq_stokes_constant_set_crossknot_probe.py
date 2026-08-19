#!/usr/bin/env python3
"""qbeta_qnnq_stokes_constant_set_crossknot_probe.py — the GGM Stokes
FACTORIZATION CONSTANT SET is the same for 4_1 and 5_2, which prunes the
candidate readings of {3,4} and hands the 6_1 third-knot test a sharp,
discriminating prediction.

Bean: qou-qnnq (G3 Stokes keystone, internal-derivation leg).
Scope: (a). No fit. No c_k wired. Nothing to production. No tier change.

WHAT IS ESTABLISHED IN THE CORPUS (not re-derived here)
-------------------------------------------------------
  * 4_1: S+(0) = [[1,3],[0,1]]; GGM eq-98 off-diagonal spectrum {3,4}.
    Lean-proved q->0 anchor (QOU.QBeta.StokesQZeroDTCount), witness
    computations/aomega-qzero-dt-count.witness.json.
  * 5_2: S+(0) = [[1,4,0],[0,1,0],[-3,-9,1]], S-(0) = [[1,0,3],[-4,1,-3],[0,0,1]],
    certified exactly against GGM's printed (96/97) factorization, whose
    constants are {3,4}.  Witness
    computations/probes/qbeta-g3-5two-stokes-sandwich.witness.json.
  * #boundary-parabolic flat connections (certified, bean qou-btvl):
    4_1 = 3 (2 irreducible + abelian), 5_2 = 4 (3 + abelian).
  * Braid index 3 for both (computations/knot_braid_database.py: both
    words are 3-strand; 4_1 = (s1 s2^-1)^2, 5_2 = s1^-1 s2 s1^-1 s2^2).

THE ONE NEW OBSERVATION
-----------------------
4_1 and 5_2 carry the SAME Stokes constant set {3,4} while differing in
every other candidate driver:

    driver                     4_1      5_2      same?
    crossing number             4        5        NO
    #bdry-parabolic conns       3        4        NO
    geometric block size      2x2      3x3        NO
    braid index                 3        3       YES

So a reading of {3,4} as a function of crossing number, of #connections,
or of the geometric block size is NOT knot-independent in the way the
data is; only a braid-index-indexed reading survives these two points.

The surviving CANDIDATE (explicitly NOT derived, see DISCIPLINE below) is
the Wedderburn pair of the Hecke algebra at the braid index n:

    ( #blocks , sum of block dims ) = ( p(n) , I(n) )

with p(n) = #partitions of n and I(n) = #involutions in S_n (the classical
Frobenius-Schur identity sum_{lambda |- n} dim V_lambda = I(n), verified
here from hook lengths).  n = 3 gives (3, 4).

DISCRIMINATING PREDICTION FOR THE OPEN THIRD-KNOT TEST
------------------------------------------------------
6_1 has braid index 4 and #boundary-parabolic connections 5 (A-polynomial
L-degree certified in qou-btvl).  The corpus records 6_1's independent
resurgence DT count as THE missing piece of the third-knot test.  The two
live candidates predict DIFFERENT things there:

    R1  (DT_max = #connections)  ->  a 5 in the spectrum
    W   (Wedderburn at braid idx) ->  the PAIR {5, 10}

The 10 is the discriminator: R1 does not produce it.

DISCIPLINE (AGENTS.md)
----------------------
This probe reports a scope-(a) CONSISTENCY of one candidate across two
knots plus a scope-(a) NEGATIVE for three others.  Two points do not
force a rule -- per AGENTS.md the coincidence-trap bar is "across knots
AND structurally forced", and the structural forcing is NOT supplied
here.  {3,4} is NOT declared derived; qou-qnnq stays open.  All
arithmetic below is exact integer / Fraction -- no float anywhere.
"""

from __future__ import annotations

import json
import os
import sys
from fractions import Fraction

sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))

REPO = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))


# ---------------------------------------------------------------- partitions
def partitions(n: int, maximum: int | None = None) -> list[tuple[int, ...]]:
    """All partitions of n as weakly-decreasing tuples (exact, integer)."""
    if maximum is None:
        maximum = n
    if n == 0:
        return [()]
    out: list[tuple[int, ...]] = []
    for first in range(min(n, maximum), 0, -1):
        for rest in partitions(n - first, first):
            out.append((first,) + rest)
    return out


def hook_length_dim(lam: tuple[int, ...]) -> int:
    """dim of the S_n irrep V_lambda via the hook-length formula (exact)."""
    n = sum(lam)
    conj = [sum(1 for part in lam if part > j) for j in range(lam[0])] if lam else []
    num = 1
    for k in range(1, n + 1):
        num *= k
    den = 1
    for i, row in enumerate(lam):
        for j in range(row):
            arm = row - j - 1
            leg = conj[j] - i - 1
            den *= arm + leg + 1
    assert num % den == 0, "hook-length formula must divide exactly"
    return num // den


def involutions(n: int) -> int:
    """I(n) = I(n-1) + (n-1) I(n-2), I(0)=I(1)=1 (exact)."""
    a, b = 1, 1
    for k in range(2, n + 1):
        a, b = b, b + (k - 1) * a
    return b


def wedderburn_pair(n: int) -> tuple[int, int]:
    """(#Wedderburn blocks, sum of block dims) for H_n(q) / S_n."""
    lams = partitions(n)
    return len(lams), sum(hook_length_dim(l) for l in lams)


# ------------------------------------------------------------------ witnesses
def load_witness(relpath: str) -> dict:
    with open(os.path.join(REPO, relpath), encoding="utf-8") as fh:
        return json.load(fh)


def offdiagonal_entries(mat: list[list]) -> set[int]:
    """|entries| off the diagonal, zeros dropped (exact integers)."""
    out: set[int] = set()
    for i, row in enumerate(mat):
        for j, val in enumerate(row):
            if i == j:
                continue
            v = abs(int(val))
            if v:
                out.add(v)
    return out


def main() -> int:
    checks: list[tuple[str, bool, str]] = []

    # -- C1 -- the Wedderburn pair, exact, cross-checked two ways -----------
    pairs = {n: wedderburn_pair(n) for n in range(2, 7)}
    inv_ok = all(pairs[n][1] == involutions(n) for n in pairs)
    checks.append((
        "C1_wedderburn_pair_matches_involution_count",
        inv_ok,
        "sum_lambda dim V_lambda == #involutions(S_n) for n=2..6 "
        f"(hook-length vs recursion): {pairs}",
    ))
    checks.append((
        "C1b_H3_pair_is_3_4",
        pairs[3] == (3, 4),
        f"(p(3), sum dim) = {pairs[3]} -- partitions of 3 are (3),(2,1),(1,1,1) "
        "with dims 1,2,1",
    ))

    # -- C2 -- the two committed Stokes witnesses --------------------------
    w41 = load_witness("computations/aomega-qzero-dt-count.witness.json")
    s41 = w41["data"]["Splus0"]
    set41_qzero = offdiagonal_entries(s41)
    # GGM eq 98: the full off-diagonal spectrum of 4_1 is the pair {3,4}
    set41 = {3, 4}
    checks.append((
        "C2a_fourone_qzero_offdiagonal_is_3",
        set41_qzero == {3},
        f"4_1 S+(0) = {s41}; off-diagonal {sorted(set41_qzero)} "
        "(the eq-98 spectrum is the pair {3,4})",
    ))

    w52 = load_witness(
        "computations/probes/qbeta-g3-5two-stokes-sandwich.witness.json")
    s52p = [[int(x) for x in row] for row in w52["data"]["q0_targets"]["S_plus_0"]]
    s52m = [[int(x) for x in row] for row in w52["data"]["q0_targets"]["S_minus_0"]]
    ent52 = offdiagonal_entries(s52p) | offdiagonal_entries(s52m)
    # 9 = 3*3 is a COMPOSITE entry of the product, not an elementary constant:
    # GGM's printed (96/97) factorization constants are {3,4} (certified by
    # qbeta_g3_5two_stokes_sandwich.py check K1).
    set52 = {v for v in ent52 if v in (3, 4)}
    checks.append((
        "C2b_fivetwo_elementary_constants_are_3_4",
        set52 == {3, 4} and ent52 == {3, 4, 9},
        f"5_2 S+(0)={s52p}, S-(0)={s52m}; off-diagonal magnitudes "
        f"{sorted(ent52)}; elementary printed-factorization constants {{3,4}} "
        "(9 = 3*3 is a composite product entry)",
    ))

    checks.append((
        "C2c_constant_set_is_shared",
        set41 == set52 == {3, 4},
        "4_1 and 5_2 carry the SAME Stokes factorization constant set {3,4}",
    ))

    # -- C3 -- which candidate drivers survive two knots -------------------
    drivers = {
        #  name                  4_1   5_2
        "crossing_number":       (4,   5),
        "n_bdry_parab_conns":    (3,   4),
        "geometric_block_size":  (2,   3),
        "braid_index":           (3,   3),
    }
    constant_set_is_shared = (set41 == set52)
    survivors = [k for k, (a, b) in drivers.items() if (a == b) == constant_set_is_shared]
    pruned = [k for k in drivers if k not in survivors]
    checks.append((
        "C3_only_braid_index_covaries_with_the_constant_set",
        survivors == ["braid_index"],
        f"shared constant set across the two knots; drivers that also agree: "
        f"{survivors}; drivers that DIFFER and so cannot index it: {pruned}",
    ))

    # -- C4 -- the discriminating 6_1 prediction ---------------------------
    six_one_braid_index = 4          # 6_1 braid index (KnotInfo; = K4_1 in census)
    six_one_conns = 5                # certified A-poly L-degree, bean qou-btvl
    pred_W = set(wedderburn_pair(six_one_braid_index))
    pred_R1 = {six_one_conns}
    checks.append((
        "C4_sixone_predictions_are_discriminating",
        pred_W == {5, 10} and pred_R1 == {5} and pred_W != pred_R1,
        f"6_1 (braid index {six_one_braid_index}, #conns {six_one_conns}): "
        f"Wedderburn candidate predicts {sorted(pred_W)}; R1 (#connections) "
        f"predicts {sorted(pred_R1)}. The 10 is the discriminator.",
    ))

    # ------------------------------------------------------------- report --
    print("=" * 78)
    print("qou-qnnq: the Stokes constant set across 4_1 and 5_2 -- what it prunes")
    print("=" * 78)
    print()
    print(f"{'driver':<24}{'4_1':>8}{'5_2':>8}   same?")
    print("-" * 78)
    for name, (a, b) in drivers.items():
        print(f"{name:<24}{a:>8}{b:>8}   {'YES' if a == b else 'NO'}")
    print(f"{'Stokes constant set':<24}{'{3,4}':>8}{'{3,4}':>8}   YES")
    print()
    print("Wedderburn pair (p(n), sum dim V_lambda) = (p(n), #involutions S_n):")
    for n in sorted(pairs):
        print(f"  n = {n}:  {pairs[n]}")
    print()

    n_pass = 0
    for name, ok, detail in checks:
        print(f"[{'PASS' if ok else 'FAIL'}] {name}")
        print(f"       {detail}")
        n_pass += bool(ok)
    print()
    print(f"{n_pass}/{len(checks)} checks passed")
    print()
    print("VERDICT (scope-(a)):")
    print("  PRUNED  -- crossing number, #boundary-parabolic connections, and")
    print("             geometric block size each DIFFER between 4_1 and 5_2")
    print("             while the constant set does not, so none of them can")
    print("             index {3,4}.  (Scope-(a): these are excluded as the")
    print("             INDEX of the constant set, not excluded from the")
    print("             physics -- #connections remains R1's live handle for")
    print("             DT_max, a different quantity.)")
    print("  SURVIVES-- a braid-index-indexed reading; the Hecke H_3 Wedderburn")
    print("             pair (3,4) is a CANDIDATE, NOT a derivation.  Two knots")
    print("             of equal braid index do not force a rule; the structural")
    print("             forcing is absent and qou-qnnq stays OPEN.")
    print("  TEST    -- 6_1 (braid index 4): Wedderburn predicts {5,10} vs R1's")
    print("             {5}.  The corpus already names 6_1's independent")
    print("             resurgence DT count as the missing third-knot datum")
    print("             (bean qou-btvl); this makes that datum discriminating.")

    all_ok = all(ok for _, ok, _ in checks)
    return 0 if all_ok else 1


if __name__ == "__main__":
    raise SystemExit(main())
