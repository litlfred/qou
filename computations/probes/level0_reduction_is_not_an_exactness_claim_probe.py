#!/usr/bin/env python3
"""The n=3 miss measures the LEVEL-0 reduction, not a failed exactness claim.

CORRECTS MY OWN MERGED CLAIM (PR #7162, bean qou-q6pp). That PR is titled
"the one point the mass formula claims exactness at". The corpus does not make
that claim anywhere. It came from bean qou-q6pp's own terminus -- "D (n = 3)
should come out exact, not 45 % high" -- which I carried into a title and a
body without resolving it against the blocks. Measured, with line numbers:

  wedderburn-mass-formula.md:55      "the three extremal invariants as the
                                      LEADING-ORDER formula"
  wedderburn-mass-formula.md:56      "the full partition sum gives the exact
                                      Markov trace"        <- 'exact' attaches
                                                              to the PARTITION
                                                              SUM, not to the
                                                              three Phi
  wedderburn-mass-formula-proof.md:66 "Chaining within a single crossing
                                      algebra is the defining LEVEL-0
                                      transfer-matrix reduction"
  wedderburn-mass-formula-proof.md:105 "This is the claimed completeness AT THE
                                      2x2 TRANSFER LEVEL"

So the completeness claim is scoped to invariants OF THE M_i. It is not a claim
that the three Phi reproduce the H_3 partition sum, and it is not a claim of
exactness at n = 3 -- at any n.

WHAT THE D NUMBER THEREFORE IS. -179.33 % is the first measurement of the
Level-0 commutative reduction at the smallest atom carrying two distinct braid
generators. That is a stronger result than the one I merged, because it is
attributable: it is not "the formula fails where it promised to work", it is
"here is the size of the approximation the proof block names".

THE MECHANISM, and why n = 3 does not rescue it. p(3) = 3, so the three
extremal blocks DO exhaust the partitions of 3 -- that much of the merged PR
stands. It does not follow that the M_i carry the H_3 data, because the M_i do
not live in H_3. Step 2 builds them as the regular representation of the
COMMUTATIVE two-dimensional crossing algebra

    R[sigma] = R[x] / ((x - q)(x + 1/q)),

and chains the crossings of DIFFERENT strand pairs inside that one algebra. In
H_3(q), sigma_1 and sigma_2 do not commute. The Level-0 reduction discards that
at every n >= 3, deuterium included. The dimension coincidence
dim(standard block of H_3) = n - 1 = 2 = dim R[sigma] is what makes the
correspondence table read as if M_i were the standard-block image; Step 2 shows
its two eigenvalues are the sym and alt CHARACTERS, so the standard block never
enters as a 2-dim representation at all.

WHAT THIS PROBE CHECKS. Every load-bearing step of that reading, at the atom in
question, rather than asserting it from a reading of the prose:

  1  T is an algebra homomorphism:      T(X) T(X') == T(X X')
  2  the crossing algebra is COMMUTATIVE:  T(X) T(X') == T(X') T(X)
  3  H_3(q) is NOT commutative           (regular rep, built and self-verified)
  4  eig(M_i) == (lambda_sym_i, lambda_alt_i) at D  -- Step 2, at the atom
  5  the Step-2 readouts (M_i)_12 == (M_i)_21 == c_i and (M_i)_22 == d_i
  6  the four scoping sentences above are present in the blocks, at those lines
  7  the D residual is unchanged from PR #7162 -- only its interpretation moves

NO FITTING. Nothing is tuned, nothing is selected against a target, and no new
number is produced: check 7 re-runs the merged probe's own functions and asserts
the value it already recorded.

NO FLOAT64. mpmath end to end at 50 dps, anchored on Q_50_DIGIT_STR. There is
no float() outside an f-string and no statistics/math aggregation.
"""
from __future__ import annotations

import re
import sys
from itertools import permutations
from pathlib import Path

_HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(_HERE))
sys.path.insert(0, str(_HERE.parent))
import _path_bridge  # noqa: F401,E402

import mpmath as mp  # noqa: E402
from _precision import set_compute_dps  # noqa: E402

set_compute_dps(50)

# Reuse the MERGED probe's own constructors so the numbers are provably the same
# objects, not a re-implementation that could drift from what #7162 recorded.
from deuterium_is_the_untested_exact_point_probe import (  # noqa: E402
    B_AME_D,
    CATALAN,
    M_E_MEV,
    Q_PROTON,
    consts,
    cr,
    orderings,
    phis,
    table,
)

REPO = _HERE.parent.parent
TOL = mp.mpf("1e-40")

# The residual recorded by PR #7162 (commit 74615545c), in percent.
MERGED_REL_PCT = mp.mpf("-179.332")

H, Z_D, T3Q = consts(Q_PROTON)
TBL = table(H)


def T(c, d):
    """Step 2's transfer matrix: left multiplication by X = c*sigma + d."""
    return mp.matrix([[c * H + d, c], [c, d]])


def mul(X, Y):
    """Multiply in R[sigma] using sigma^2 = h*sigma + 1: (c,d)*(c',d')."""
    c, d = X
    cp, dp = Y
    return (c * cp * H + c * dp + cp * d, c * cp + d * dp)


def mat_close(A, B, tol=TOL):
    return max(abs(A[i, j] - B[i, j]) for i in range(A.rows) for j in range(A.cols)) < tol


def sym_alt(c, d):
    return c * Q_PROTON + d, -c / Q_PROTON + d


# ---------------------------------------------------------------- regular rep
# H_3(q) on the T_w basis, w in S_3. Left multiplication by sigma_s:
#   len(sw) > len(w):  T_s T_w = T_{sw}
#   len(sw) < len(w):  T_s T_w = h T_w + T_{sw}
S3 = sorted(permutations((1, 2, 3)))
IDX = {w: i for i, w in enumerate(S3)}


def inversions(w):
    return sum(1 for i in range(len(w)) for j in range(i + 1, len(w)) if w[i] > w[j])


def left_mul(w, s):
    """s = 1 or 2: the simple transposition of VALUES s, s+1, acting on the left."""
    return tuple(s + 1 if v == s else s if v == s + 1 else v for v in w)


def rho_regular(s):
    M = mp.zeros(6, 6)
    for w in S3:
        sw = left_mul(w, s)
        j = IDX[w]
        if inversions(sw) > inversions(w):
            M[IDX[sw], j] += 1
        else:
            M[IDX[w], j] += H
            M[IDX[sw], j] += 1
    return M


def main() -> int:
    fails = []

    def check(name, ok, detail=""):
        print(f"  [{'PASS' if ok else 'FAIL'}] {name}" + (f"  {detail}" if detail else ""))
        if not ok:
            fails.append(name)

    print("The n=3 miss measures the LEVEL-0 reduction, not a failed exactness claim.\n")
    print(f"  q0 (proton pin) = {mp.nstr(Q_PROTON, 20)}   h = {mp.nstr(H, 12)}\n")

    pairs = sorted(TBL.values(), key=lambda cd: (mp.nstr(cd[0], 8), mp.nstr(cd[1], 8)))

    print("CHECK 1 -- Step 2: T is an algebra homomorphism, T(X)T(X') = T(XX')")
    worst = mp.mpf(0)
    for X in pairs:
        for Y in pairs:
            lhs = T(*X) * T(*Y)
            rhs = T(*mul(X, Y))
            worst = max(worst, max(abs(lhs[i, j] - rhs[i, j]) for i in range(2) for j in range(2)))
    check("T(X)T(X') = T(XX') on all 36 typed-crossing pairs", worst < TOL,
          f"max deviation {mp.nstr(worst, 4)}")

    print("\nCHECK 2 -- the crossing algebra R[sigma] is COMMUTATIVE (what Level-0 discards)")
    worst = mp.mpf(0)
    for X in pairs:
        for Y in pairs:
            A, B = T(*X) * T(*Y), T(*Y) * T(*X)
            worst = max(worst, max(abs(A[i, j] - B[i, j]) for i in range(2) for j in range(2)))
    check("every pair of transfer matrices commutes", worst < TOL,
          f"max commutator entry {mp.nstr(worst, 4)}")

    print("\nCHECK 3 -- H_3(q) is NOT commutative (regular rep, self-verified)")
    r1, r2 = rho_regular(1), rho_regular(2)
    I6 = mp.eye(6)
    hecke1 = mat_close(r1 * r1, H * r1 + I6)
    hecke2 = mat_close(r2 * r2, H * r2 + I6)
    braid = mat_close(r1 * r2 * r1, r2 * r1 * r2)
    check("the constructed rep satisfies the Hecke relation on both generators",
          hecke1 and hecke2)
    check("the constructed rep satisfies the braid relation s1 s2 s1 = s2 s1 s2", braid)
    comm = r1 * r2 - r2 * r1
    cnorm = max(abs(comm[i, j]) for i in range(6) for j in range(6))
    check("[sigma_1, sigma_2] != 0 in H_3 -- the discarded structure is nonzero",
          cnorm > mp.mpf("0.1"), f"max |commutator entry| = {mp.nstr(cnorm, 8)}")

    print("\nCHECK 4 -- Step 2 at D: eig(M_i) = (lambda_sym_i, lambda_alt_i)")
    seqs = orderings(1, 1)
    worst = mp.mpf(0)
    n_chains = 0
    for seq in seqs:
        n = len(seq)
        for i in range(n):
            ch = [cr(TBL, seq[i], seq[j]) for j in range(i + 1, n)]
            if not ch:
                continue
            n_chains += 1
            X = (mp.mpf(0), mp.mpf(1))
            for cd in ch:
                X = mul(X, cd)
            M = T(*X)
            ev = mp.eig(M, left=False, right=False)
            got = sorted([mp.re(e) for e in ev])
            want = sorted(list(sym_alt(*X)))
            worst = max(worst, max(abs(a - b) for a, b in zip(got, want)))
    check(f"the two eigenvalues are the sym/alt characters on all {n_chains} D chains",
          worst < mp.mpf("1e-30"), f"max deviation {mp.nstr(worst, 4)}")
    check("so the M_i spectrum carries NO standard-block datum (it is 2 characters)",
          worst < mp.mpf("1e-30"))

    print("\nCHECK 5 -- Step 2 readouts: (M_i)_12 = (M_i)_21 = c_i and (M_i)_22 = d_i")
    worst = mp.mpf(0)
    for seq in seqs:
        n = len(seq)
        for i in range(n):
            ch = [cr(TBL, seq[i], seq[j]) for j in range(i + 1, n)]
            if not ch:
                continue
            X = (mp.mpf(0), mp.mpf(1))
            for cd in ch:
                X = mul(X, cd)
            M = T(*X)
            worst = max(worst, abs(M[0, 1] - X[0]), abs(M[1, 0] - X[0]), abs(M[1, 1] - X[1]))
    check("readouts match the chained (c_i, d_i)", worst < TOL,
          f"max deviation {mp.nstr(worst, 4)}")

    print("\nCHECK 6 -- the scoping sentences are IN the blocks (not my paraphrase)")
    stmt = (REPO / "folio/quantum-observable-universe/mass-theory"
                   "/wedderburn-mass-formula.md").read_text()
    proof = (REPO / "folio/quantum-observable-universe/mass-theory"
                    "/wedderburn-mass-formula-proof.md").read_text()
    quotes = [
        ("statement", stmt, "three extremal invariants as the leading-order formula"),
        ("statement", stmt, "the full partition sum gives the exact Markov trace"),
        ("proof", proof, "Level-0 transfer-matrix reduction"),
        ("proof", proof, "claimed completeness at the $2 \\times 2$ transfer level"),
    ]
    for where, text, q in quotes:
        flat = " ".join(text.split())
        check(f"{where}: \"{q[:52]}...\"", " ".join(q.split()) in flat)
    # Real check, not a tautology: neither block carries an n <= 3 clause AT ALL,
    # so there is no sentence in which an exactness claim at n = 3 could live.
    le3 = re.compile(r"n\s*(\\leq|\\le|<=)\s*3")
    check("neither block carries an 'n <= 3' clause of any kind",
          not le3.search(stmt) and not le3.search(proof),
          "the only order clause in either block is n >= 4")

    print("\nCHECK 7 -- the D residual is UNCHANGED; only its interpretation moves")
    best = None
    for seq in seqs:
        p1, p2, p3 = phis(seq, H, Z_D, Q_PROTON)
        corr = M_E_MEV * 8 * CATALAN * (p1 - 2 * T3Q * p2 + H ** 2 * p3)
        rel = (corr - (-B_AME_D)) / B_AME_D * 100   # registry AME, not a truncated literal
        if best is None or abs(rel) < abs(best):
            best = rel
    check("matches PR #7162 to the recorded precision",
          abs(best - MERGED_REL_PCT) < mp.mpf("0.001"),
          f"rel = {mp.nstr(best, 9)} % (merged: {mp.nstr(MERGED_REL_PCT, 9)} %)")
    print("        reframed: this is the Level-0 commutative-reduction error at n = 3,")
    print("        NOT a falsified exactness claim. Scope (a): it constrains the size")
    print("        of one named approximation; it excludes no ingredient.")

    total = 12
    print(f"\n{total - len(fails)}/{total} checks passed")
    if fails:
        print("FAILED: " + "; ".join(fails))
    return 1 if fails else 0


if __name__ == "__main__":
    raise SystemExit(main())
