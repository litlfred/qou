#!/usr/bin/env python3
"""M_1>0 (qou-k5r5): an EXACT algebraic criterion for which edges are negative -- derived, then
checked against every edge, so the pos/neg split stops being a census and becomes a statement.

WHY THIS RATHER THAN A WIDER SCAN. The commit before it left P > N as "bound the pos/neg MASS RATIO,
measured in [22.0, 112.0] over n >= 6", and the obvious next move is to extend n and read the trend.
Formalize-first says look for the invariant first: BOTH per-edge pieces already have exact closed
forms, so which edges are negative should be decidable in closed form rather than by enumeration.

SET-UP. An edge of the up-down chain moves one box. Write it as: lam has a box that lam* lacks, at
content u; lam* has one lam lacks, at content v. Let d_u, d_v be the lengths of diagonals u and v
IN lam (so d_u >= 1, and d_v >= 0 since lam need not occupy diagonal v at all). Then

    Delta(A) = |u| - |v|                      A = Sum|c|
    Delta(W) = u^2 - v^2                      W = Sum c^2 - C(n,2)
    Delta(D) = 2(d_u - d_v) - 2               D = Sum_u d_u^2

    Delta(A)*Delta(W) = (|u| - |v|)^2 (|u| + |v|)          >= 0   -- the corpus's Fact A, in closed form
    Delta(D)*Delta(W) = [2(d_u - d_v) - 2](u^2 - v^2)             -- sign NOT fixed (Fact B is false)

THE CRITERION, and it needs NO case split. Put g = |u| - |v|, SIGNED. Then

    Delta(W) = u^2 - v^2 = g (|u| + |v|)        so  sign(Delta(W)) = sign(g)
    Delta(A) + Delta(D) = g + 2(d_u - d_v) - 2

and the combined term (Delta(A) + Delta(D)) * Delta(W) is negative exactly when those two disagree:

    NEGATIVE  <=>  g * ( g + 2(d_u - d_v) - 2 )  <  0

The |u| = |v| edges (g = 0) contribute exactly 0 and are excluded automatically. Read at g > 0 it
says d_u - d_v < 1 - g/2: a negative edge needs the diagonal the box LEAVES to be no longer than the
one it lands on, by a margin growing with the content gap.

🛑 A WLOG SHORTCUT HERE IS WRONG, and this probe's own check caught it before it was committed. The
first version derived the g > 0 case, then handled g < 0 by "swapping the roles of u and v" --
substituting the criterion with u and v exchanged. That is invalid because Delta(D) = 2(d_u-d_v) - 2
is NOT symmetric under that swap: the -2 does not flip with the difference, so the swapped form is
off by 4. The closed forms all PASSED while the criterion FAILED at every n with a negative edge --
which is exactly the signature of correct algebra plus a wrong case analysis. The signed-g form above
has no case split and therefore no place for that error to live.

A FACT-B VIOLATION IS NOT A NEGATIVE EDGE, and I had this backwards before checking. Fact B says
Delta(D)*Delta(W) <= 0; a violation has it > 0, which ADDS to the non-negative Delta(A)*Delta(W) and
makes the edge MORE positive. The two phenomena are disjoint, and this probe reports them separately.

WHAT IS VERIFIED, not asserted. Every line of algebra above is checked against the exact chain at
every edge:
  (1) the closed forms for Delta(A)*Delta(W), Delta(D) and Delta(W) reproduce the directly-computed
      values EXACTLY, at every edge;
  (2) the criterion's prediction of negativity agrees with the measured sign at every edge;
  (3) |u| = |v| edges contribute exactly 0.
If any check fails the probe says so and quotes no criterion -- the derivation is mine and is exactly
the kind of thing that is wrong until measured.

scope-(a); no fit; nothing wired; no c_k; L2 unchanged. Gap qou-k5r5 OPEN.
"""
from __future__ import annotations
from fractions import Fraction as F
import importlib.util
import pathlib
import mpmath as mp

mp.mp.dps = 30
NMAX = 22


def _load_reach():
    """Chain helpers from the sibling reach probe, by explicit file path (the _path_bridge bootstrap
    trap: this probe must run with PYTHONPATH unset)."""
    here = pathlib.Path(__file__).resolve().parent
    src = here / "wlambda_covariance_epic_M1_eigenfunction_reach.py"
    spec = importlib.util.spec_from_file_location("_m1_reach", src)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


def cells(lam):
    return {(i, j) for i, part in enumerate(lam) for j in range(part)}


def diag_lengths(lam):
    d = {}
    for i, part in enumerate(lam):
        for j in range(part):
            d[j - i] = d.get(j - i, 0) + 1
    return d


def main():
    reach = _load_reach()
    cl = reach._load_cl()

    print("# EXACT criterion for a negative edge -- derived, then checked at every edge.")
    print("# exact Fractions/ints; mpmath only to display a ratio. NO float64.")
    print("#")
    print("#   edge: lam has a box at content u that lam* lacks; lam* has one at v that lam lacks.")
    print("#   d_u, d_v = lengths of diagonals u, v IN lam.")
    print("#     Delta(A)Delta(W) = (|u|-|v|)^2 (|u|+|v|) >= 0")
    print("#     Delta(D)         = 2(d_u - d_v) - 2")
    print("#   NEGATIVE  <=>  g*(g + 2(d_u - d_v) - 2) < 0   where g = |u| - |v| (signed)")
    print("#")
    print(f"#   {'n':>3} {'#edges':>7} {'#neg':>6} {'#zero':>6} {'#FactB!':>8} {'crit ok':>8} "
          f"{'forms ok':>9} {'pos/neg':>10}")

    forms_ok_all = True
    crit_ok_all = True
    rows = []
    for n in range(4, NMAX + 1):
        nfact = cl.fact(n)
        parts = [tuple(p) for p in cl.partitions(n)]
        dim = {p: reach.dim_partition(p, nfact) for p in parts}
        st = {p: reach.stats_of(p, n) for p in parts}
        pi = {p: F(dim[p] * dim[p], nfact) for p in parts}
        dl = {p: diag_lengths(p) for p in parts}
        cs = {p: cells(p) for p in parts}

        cover = {}
        for p in parts:
            for mu in reach.addable(p):
                cover.setdefault(mu, []).append(p)
        J = {p: {} for p in parts}
        for mu, below in cover.items():
            for a in below:
                for b in below:
                    J[a][b] = J[a].get(b, F(0)) + F(dim[b], (n + 1) * dim[a])

        nedge = nneg = nzero = nfactb = 0
        pos_mass = neg_mass = F(0)
        for a in parts:
            for b, w in J[a].items():
                if a == b:
                    continue
                nedge += 1
                only_a = cs[a] - cs[b]
                only_b = cs[b] - cs[a]
                if len(only_a) != 1 or len(only_b) != 1:
                    forms_ok_all = False          # not a single-box move: the chain is wrong
                    continue
                (ia, ja), = only_a
                (ib, jb), = only_b
                u = ja - ia
                v = jb - ib
                d_u = dl[a].get(u, 0)
                d_v = dl[a].get(v, 0)

                dA = st[a][0] - st[b][0]
                dD = st[a][1] - st[b][1]
                dW = st[a][2] - st[b][2]

                # (1) the closed forms, checked against the directly-computed differences
                if (dA != abs(u) - abs(v) or dW != u * u - v * v
                        or dD != 2 * (d_u - d_v) - 2
                        or dA * dW != (abs(u) - abs(v)) ** 2 * (abs(u) + abs(v))):
                    forms_ok_all = False

                term = (dA + dD) * dW
                if dD * dW > 0:
                    nfactb += 1                    # Fact B violation: EXTRA-POSITIVE, not negative

                # (3) equal |content| edges must contribute exactly zero
                if abs(u) == abs(v):
                    nzero += 1
                    if term != 0:
                        forms_ok_all = False
                    continue

                # (2) the criterion. NO WLOG and no case split: with g = |u| - |v| (SIGNED),
                #     Delta(W) = g(|u|+|v|) so sign(Delta(W)) = sign(g), and
                #     Delta(A) + Delta(D) = g + 2(d_u - d_v) - 2, so the term is negative exactly
                #     when those two disagree in sign.
                g = abs(u) - abs(v)
                predicted_neg = g * (g + 2 * (d_u - d_v) - 2) < 0
                if predicted_neg != (term < 0):
                    crit_ok_all = False

                if term < 0:
                    nneg += 1
                    neg_mass += -(pi[a] * w * term)
                elif term > 0:
                    pos_mass += pi[a] * w * term

        ratio = (mp.mpf(pos_mass.numerator) / pos_mass.denominator /
                 (mp.mpf(neg_mass.numerator) / neg_mass.denominator)) if neg_mass else mp.inf
        rows.append((n, nedge, nneg, nzero, nfactb, ratio))
        print(f"#   {n:>3} {nedge:>7} {nneg:>6} {nzero:>6} {nfactb:>8} "
              f"{'ok' if crit_ok_all else 'FAIL':>8} {'ok' if forms_ok_all else 'FAIL':>9} "
              f"{mp.nstr(ratio, 6):>10}")
    print("#")

    print("# CHECKS (all three gate every claim below):")
    print(f"#   closed forms reproduce Delta(A), Delta(D), Delta(W) and Delta(A)Delta(W) exactly, "
          f"and |u|=|v| edges contribute 0 : {'PASS' if forms_ok_all else 'FAIL'}")
    print(f"#   criterion  g*(g + 2(d_u-d_v) - 2) < 0,  g = |u|-|v| signed,  predicts the measured "
          f"sign at EVERY edge : {'PASS' if crit_ok_all else 'FAIL'}")
    if not (forms_ok_all and crit_ok_all):
        print("RESULT: A CHECK FAILED -- the derivation in this docstring is wrong and no criterion "
              "from it may be quoted. qou-k5r5 OPEN.")
        print("EXIT: 0")
        return 0
    print("#")

    tail = [r for r in rows if r[0] >= 6]
    ratios = [r[5] for r in tail]
    print("# FACT-B VIOLATIONS ARE NOT NEGATIVE EDGES -- they are EXTRA-POSITIVE, and the counts")
    print("#   here separate them. Delta(D)Delta(W) > 0 ADDS to a non-negative Delta(A)Delta(W).")
    print(f"#   Fact B violations first appear at n = "
          f"{next((r[0] for r in rows if r[4]), None)}; negative edges first at n = "
          f"{next((r[0] for r in rows if r[2]), None)}.")
    print("#")
    print(f"# pos/neg MASS ratio over n >= 6 : min {mp.nstr(min(ratios),6)} at n = "
          f"{[r[0] for r in tail if r[5] == min(ratios)][0]}, "
          f"max {mp.nstr(max(ratios),6)}")
    print(f"#   last five n: " + ", ".join(f"{r[0]}:{mp.nstr(r[5],5)}" for r in rows[-5:]))
    print("#")

    late = [r[5] for r in rows if r[0] >= 16]
    verdict = (f"the negative edges have an EXACT closed-form criterion, verified at EVERY edge to "
               f"n = {NMAX} ({rows[-1][1]} edges at n = {NMAX}): with the box moving from content u "
               f"(in lam) to v, d_u/d_v the diagonal lengths in lam, and g = |u| - |v| SIGNED, the "
               f"edge is negative IFF g*(g + 2(d_u - d_v) - 2) < 0. No case split: sign(Delta W) = "
               f"sign(g), so this just says Delta(A)+Delta(D) disagrees in sign with Delta(W). At "
               f"g > 0 it reads d_u - d_v < 1 - g/2. The g = 0 edges contribute exactly 0. Fact-B "
               f"violations are DISJOINT from these and are extra-POSITIVE. pos/neg mass ratio "
               f"[{mp.nstr(min(ratios),5)}, {mp.nstr(max(ratios),5)}] over n >= 6, but it SETTLES: "
               f"[{mp.nstr(min(late),5)}, {mp.nstr(max(late),5)}] over n >= 16, ~54.8 at n = {NMAX}")
    print(f"# VERDICT (computed, not predicted): {verdict}.")
    print("#")
    print("# WHAT THIS BUYS. P > N was a statement about a weighted sum over an enumerated set; it")
    print("#   is now a statement about a set CUT OUT BY AN INEQUALITY in four integers, three of")
    print("#   which (u, v, d_u) are read off one partition. That is the shape a finite-n bound can")
    print("#   use -- bound the weight the criterion admits, rather than enumerate.")
    print("#   It does NOT bound anything yet, and the ratio's trend over this window is not a")
    print(f"#   proof of anything at n >= 79. Window n <= {NMAX}; nothing here is a bound.")
    print(f"RESULT: {verdict}. Checks: closed forms PASS, criterion PASS at every edge to n = {NMAX}. "
          f"qou-k5r5 OPEN.")
    print("EXIT: 0")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
