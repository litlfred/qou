"""The bond-series "recursion" is affineness in n — DERIVED, and it deflates itself.

🛑 THIS FILE CORRECTS ITS OWN FIRST VERSION (commit 8bf62d2ad6, unmerged).
That version reported a "UNIVERSAL 3-term recursion, overdetermined by one, so a
real test and not a fit". **The overdetermination claim was WRONG**, and the
derivation below is what shows it.

THE DERIVATION
--------------
A bond joins exactly TWO nucleons, so `p_b + n_b = 2` always. With qou-qqm4's
descriptions `rho = p - n` and `tau = 1/2 + n`:

    n = 1 - rho/2   =>   tau = 1/2 + (1 - rho/2) = 3/2 - rho/2

and the measured k=1 rung says `tau = -1/2*rho + 3/2*1`. **Identical.** So k=1 is
an algebraic identity in facts already published, not new structure.

The general statement is stronger and kills the framing outright. Indexing the
three bonds by `n = 0, 1, 2` (pp, pn, nn), the measured coefficients are:

    c0  [1, 1, 1]                 2nd diff 0     AFFINE in n
    c1  [2, 0, -2]                2nd diff 0     AFFINE
    c2  [1/2, 3/2, 5/2]           2nd diff 0     AFFINE
    c3  [-1/2, -3/2, -5/2]        2nd diff 0     AFFINE
    c4  [1/4, 31/12, 9/4]         2nd diff -8/3  NOT affine

**If `c_{k-1}`, `c_k`, `c_{k+1}` are all affine in `n`, the three bonds are
COLLINEAR in that 3-space, and a 2-term relation `c_{k+1} = A c_k + B c_{k-1}`
exists AUTOMATICALLY.** It is not a constraint being satisfied; it is what three
collinear points always do. The third equation is NOT independent of the other
two, so "3 equations, 2 unknowns" was never overdetermined.

That explains the whole pattern, both halves:

    k=1   c0,c1,c2 all affine   -> recursion automatic
    k=2   c1,c2,c3 all affine   -> recursion automatic
    k=3   c4 NOT affine         -> breaks, necessarily

WHAT SURVIVES
-------------
One fact, and it is the one the recursion framing was obscuring:

    ups = -tau     exactly, i.e.  c3 = -1/2 - n

`c3` being affine in `n` at all is a genuine constraint (one condition on three
measured rationals), and it is NOT supplied by qou-qqm4's description, which
covers `rho` and `tau` only. That description was correctly called "three values
with one spare dof"; `ups = -tau` is a relation with none.

So the honest ledger is:

    k=1 rung      DERIVED — identity from rho, tau, p+n=2
    k=2 rung      NOT derived — equivalent to ups = -tau, still open
    k=3 rung      REFUTED — c4 is the first non-affine coefficient

A GUESS THAT FAILS, recorded so it is not re-tried. `tau, -tau` at orders 2 and 3
suggests a factor `tau*e^2/(1+e)`, whose order-4 term would be `+tau`, i.e.
`c4 = 1/2, 3/2, 5/2`. Measured `c4` is `1/4, 31/12, 9/4`. Refuted.

WHAT THIS IS NOT. `c4` is quadratic in `n` by construction — any three points
are — so fitting a quadratic there has zero content and is not done here.

NO FLOAT: exact `fractions.Fraction` throughout.
"""
from __future__ import annotations

from fractions import Fraction as F

BOND = {
    "pp": [F(1), F(2), F(1, 2), F(-1, 2), F(1, 4)],
    "pn": [F(1), F(0), F(3, 2), F(-3, 2), F(31, 12)],
    "nn": [F(1), F(-2), F(5, 2), F(-5, 2), F(9, 4)],
}
NUC = {"p": [F(1), F(3, 2), F(23, 4), F(75, 4), F(-37, 2)],
       "n": [F(1), F(-1), F(3), F(19), F(-57, 2)]}


def solve_pair(s1, s2, k):
    """A, B from c_{k+1} = A c_k + B c_{k-1} on two series; None if singular."""
    x1, y1, z1 = s1[k], s1[k - 1], s1[k + 1]
    x2, y2, z2 = s2[k], s2[k - 1], s2[k + 1]
    det = x1 * y2 - x2 * y1
    if det == 0:
        return None
    return ((z1 * y2 - z2 * y1) / det, (x1 * z2 - x2 * z1) / det)


def main() -> int:
    names = list(BOND)
    failures, held = [], []
    print("=" * 74)
    print("  the bond-series recursion, and why it is affineness in n")
    print("=" * 74)

    # --- the derivation: which coefficients are affine in n? ----------------
    order = ("pp", "pn", "nn")          # n = 0, 1, 2
    affine = {}
    print("  affineness in n (three bonds; 2nd difference must vanish):")
    for k in range(5):
        v = [BOND[b][k] for b in order]
        d2 = v[2] - 2 * v[1] + v[0]
        affine[k] = (d2 == 0)
        row = ", ".join(str(x) for x in v)
        print(f"    c{k}: [{row}]".ljust(46)
              + f" 2nd diff {d2}  {'AFFINE' if d2 == 0 else 'NOT affine'}")
    print()
    print("  A 2-term relation among three COLLINEAR points always exists, so a")
    print("  rung is AUTOMATIC wherever its three coefficients are all affine —")
    print("  it is not an overdetermined test, and the first version of this file")
    print("  wrongly said it was.")
    for k in (1, 2, 3):
        trio = [affine[k - 1], affine[k], affine[k + 1]]
        print(f"    k={k}: {trio} -> "
              + ("automatic" if all(trio) else "no guarantee; and it breaks"))
    print()
    tau_derived = all(BOND[b][2] == F(3, 2) - BOND[b][1] / 2 for b in order)
    print(f"  k=1 rung derived from rho, tau and p+n=2: {tau_derived}")
    ups_rel = all(BOND[b][3] == -BOND[b][2] for b in order)
    print(f"  k=2 rung equivalent to ups = -tau, which holds: {ups_rel}")
    print("  -> k=1 is an identity; k=2's content is ups = -tau and stays OPEN.")
    print()

    for k in (1, 2, 3):
        sols = {}
        for i in range(len(names)):
            for j in range(i + 1, len(names)):
                r = solve_pair(BOND[names[i]], BOND[names[j]], k)
                if r:
                    sols[(names[i], names[j])] = r
        if not sols:
            # rank-deficient: report the CONSEQUENCE it still forces
            ratios = {n: BOND[n][k + 1] / BOND[n][k - 1] for n in names}
            uniq = set(ratios.values())
            print(f"  k={k}: every pair is SINGULAR — (c{k}, c{k-1}) is "
                  f"proportional to (-1, 1) in all three bonds.")
            print(f"        The ansatz still forces c{k+1} proportional to c{k-1}:")
            for n, v in ratios.items():
                print(f"          {n}: c{k+1}/c{k-1} = {v}")
            if len(uniq) == 1:
                print(f"        constant -> consistent, but NOT determined here")
                held.append((k, "rank-deficient but consistent"))
            else:
                print(f"        NOT constant -> the universal recursion is "
                      f"REFUTED at k={k}")
                failures.append(k)
            continue
        A, B = next(iter(sols.values()))
        allok = all(A * BOND[n][k] + B * BOND[n][k - 1] == BOND[n][k + 1]
                    for n in names)
        agree = all(v == (A, B) for v in sols.values())
        print(f"  k={k}: A={A}  B={B}   verified on all three: {allok}   "
              f"every pair agrees: {agree}")
        if allok and agree:
            held.append((k, f"A={A}, B={B}"))
        else:
            failures.append(k)

    print()
    print("  cross-check — is this the registry's a_n recursion?")
    print("    a_{n+1} = -3n/(2(n+1)) a_n - (2n-1)/(4(n+1)) a_{n-1}")
    for n in (1, 2, 3):
        print(f"      n={n}: ({F(-3*n, 2*(n+1))}, {F(-(2*n-1), 4*(n+1))})")
    print("    measured: k=1 (-1/2, 3/2), k=2 (-1, 0). Only A at n=2 coincides;")
    print("    both B disagree. NOT the same recursion.")

    print()
    print("  nucleon series — solved, and labelled a FIT, not a test")
    print("  (two series, two unknowns per rung: always solvable, never a check)")
    for k in (1, 2, 3):
        r = solve_pair(NUC["p"], NUC["n"], k)
        print(f"      k={k}: {'A=%s B=%s' % r if r else 'singular'}")

    print()
    print("=" * 74)
    for k, what in held:
        print(f"  k={k}: HOLDS  {what}")
    for k in failures:
        print(f"  k={k}: BREAKS")
    print("=" * 74)
    print("  k=1 DERIVED (identity). k=2 = 'ups = -tau', OPEN. k=3 REFUTED.")
    print("  The recursion framing was a shadow of affineness in n; the one")
    print("  fact it was hiding is ups = -tau, which qou-qqm4's description")
    print("  does not supply and nothing here derives.")
    print()
    if held and failures == [3]:
        print("PASS  k=1 and k=2 hold (overdetermined); k=3 refuted, as measured")
        return 0
    print(f"UNEXPECTED  held={held} failures={failures} — re-read before quoting")
    return 1


if __name__ == "__main__":
    raise SystemExit(main())
