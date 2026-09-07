#!/usr/bin/env python3
"""
Probe — check every coordination edge set the corpus derives against the BULK
CRITERION, and measure what surface growth the AME data actually require.

CONTEXT. #6780 rejected the production braid word's chain against the AME chart
(its bond count is A - 1, so its per-nucleon law is the p = 1 member of
B/A = a - b*A^(-p), and RSS(1) = 147.0 against RSS(p*) = 38.2). It left the
sharpened question: what edge set could supply a surface term at all?

`QOU.Mass.CoordinationBulkCriterion` answers the general form. An edge set whose
bond count is AFFINE, M(A) = alpha*A + beta, has per-nucleon binding
eps*alpha + eps*beta/A EXACTLY — the p = 1 member, whatever alpha and beta are —
so by perNucleonExp_exponent_inj it is never a surface term. And the criterion an
edge set must satisfy is

    HasBulk(A_surf)  <=>  A_surf -> infinity   (there IS a growing surface)
                     AND  A_surf/A -> 0        (there IS an interior)

WHAT IS MEASURED:
  1. both derived edge sets on main are affine, verified against the corpus's own
     data — the chain's A - 1 and the deltahedron's 3A - 6, the latter loaded out
     of `geometric_saturation_and_labelling_probe.py` rather than re-typed here;
  2. the affine per-nucleon identity, and that profiling the exponent of an exact
     affine law returns p = 1 — which also validates #6780's profiler against a
     known answer rather than only against data;
  3. each edge set against HasBulk, both clauses separately;
  4. that NON-AFFINE IS NOT SUFFICIENT: the complete graph is non-affine and is
     refuted for the OPPOSITE reason, being superlinear (CoordinationSaturation).
     The target is specifically sublinear-but-unbounded surface growth;
  4b. WHAT IS NOT COVERED, measured rather than asserted. The enumeration of
     derived edge sets is empirical — the corpus keeps its own list at
     QOU.Hecke.BoundedDegreeCoulomb and it is longer than two. Max-contact
     sphere packing is derived-in-principle, is NOT the deltahedron family in
     general, and is NOT known to be affine, so Part 1 does not reach it; the
     degree-capped count is piecewise and so not affine on R. The honest claim
     is about AFFINE edge sets, not about every edge set the corpus derives;
  5. what the DATA require: under CoordinationSurfaceDeficit the deficit is
     (eps(k-k')/2)*(A_surf/A), so #6780's fitted p implies A_surf ~ A^(1-p). Every
     one of #6780's five analysis variants gives 1-p strictly inside (0,1), i.e.
     the data require an edge set WITH a bulk.

NOTHING IS WIRED AND NOTHING IS FITTED. The framework side contributes only edge
sets that already exist on main; no coefficient is chosen against data.

Arithmetic: mpmath 50 dps. No float64 anywhere.
"""
from __future__ import annotations

import ast
import itertools
import os
import sys
from pathlib import Path

import mpmath as mp

sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), ".."))
import _path_bridge  # noqa: E402, F401

mp.mp.dps = 50
TOL = mp.mpf(10) ** (-40)
ROOT = Path(__file__).resolve().parents[2]
GEOM = ROOT / "computations/probes/geometric_saturation_and_labelling_probe.py"

# #6780's five analysis variants, verbatim from its recorded output
P6780 = [("full basis, all nuclides", mp.mpf("0.363999")),
         ("A >= 16", mp.mpf("0.570005")),
         ("A >= 40", mp.mpf("0.582326")),
         ("no pairing column", mp.mpf("0.402725")),
         ("N = Z +- 1 only", mp.mpf("0.22917"))]


def load_corpus_deltahedron():
    """Load `deltahedron` OUT OF the corpus probe rather than re-typing it.

    That module imports networkx at module level and networkx is not installed
    here, so a plain import fails. The function itself uses only itertools, so
    parse the file and compile just that one FunctionDef: this verifies the
    CORPUS's edge sets, not a copy of them that could drift from it.
    """
    tree = ast.parse(GEOM.read_text())
    fn = next(n for n in tree.body
              if isinstance(n, ast.FunctionDef) and n.name == "deltahedron")
    ns: dict = {"itertools": itertools}
    exec(compile(ast.Module(body=[fn], type_ignores=[]), str(GEOM), "exec"), ns)
    return ns["deltahedron"]


def affine_bond_count(alpha, beta, A):
    return alpha * A + beta


def profile_exponent(pairs, lo=mp.mpf("0.05"), hi=mp.mpf(3)):
    """Profile p in y = a - b*A^(-p) over exact (A, y) pairs. At fixed p the model
    is linear in (a, b), so each p is one exact 2x2 solve; grid then golden
    section. Returns (p*, RSS(p*))."""
    def rss(p):
        X = [[mp.mpf(1), mp.mpf(A) ** (-p)] for A, _ in pairs]
        y = [v for _, v in pairs]
        n = len(pairs)
        XtX, Xty = mp.matrix(2, 2), mp.matrix(2, 1)
        for i in range(2):
            for j in range(2):
                XtX[i, j] = sum(X[r][i] * X[r][j] for r in range(n))
            Xty[i] = sum(X[r][i] * y[r] for r in range(n))
        c = mp.lu_solve(XtX, Xty)
        return sum((y[r] - (c[0] * X[r][0] + c[1] * X[r][1])) ** 2 for r in range(n))

    best = None
    for i in range(41):
        p = lo + (hi - lo) * i / 40
        r = rss(p)
        if best is None or r < best[1]:
            best = (p, r)
    step = (hi - lo) / 40
    a, b = max(lo, best[0] - step), min(hi, best[0] + step)
    gr = (mp.sqrt(5) - 1) / 2
    c_, d_ = b - gr * (b - a), a + gr * (b - a)
    fc, fd = rss(c_), rss(d_)
    for _ in range(80):
        if fc < fd:
            b, d_, fd = d_, c_, fc
            c_ = b - gr * (b - a)
            fc = rss(c_)
        else:
            a, c_, fc = c_, d_, fd
            d_ = a + gr * (b - a)
            fd = rss(d_)
        if b - a < mp.mpf("1e-20"):
            break
    p = (a + b) / 2
    return p, rss(p)


def main() -> int:
    checks: list[tuple[str, bool]] = []
    EPS = mp.mpf("2.924246314")   # #6611's derived per-bond energy, MeV; a scale only

    # ---- 1. both derived edge sets are affine ------------------------------
    print("  EDGE SETS DERIVED ON MAIN, against the affine form M(A) = alpha*A + beta\n")
    print(f"    {'edge set':<34}{'alpha':>7}{'beta':>7}   verified against")

    def chain_bonds(A):   # CoordinationSurfaceDeficit.bondCount 2 1 (A-2) 2
        return (mp.mpf(2) * (mp.mpf(A) - 2) + mp.mpf(1) * mp.mpf(2)) / 2
    ok = all(abs(chain_bonds(A) - affine_bond_count(mp.mpf(1), mp.mpf(-1), mp.mpf(A))) < TOL
             for A in (2, 3, 4, 12, 56, 208))
    checks.append(("chain: bondCount(k=2, k'=1, A_surf=2) = A - 1 = affine(1, -1), six A", ok))
    print(f"    {'production chain (path graph)':<34}{'1':>7}{'-1':>7}   handshake count, six A")

    delta = load_corpus_deltahedron()
    rows, accepted = [], []
    for A in range(2, 25):
        try:
            E = delta(A)
        except Exception:
            continue
        accepted.append(A)
        rows.append((A, len(E), 3 * A - 6 if A >= 3 else None))
    euler_ok = all(e == eu for A, e, eu in rows if A >= 4)
    checks.append(("deltahedron: every hardcoded |E| in the corpus equals 3A - 6 for A >= 4", euler_ok))
    ok = all(abs(mp.mpf(3 * A - 6) - affine_bond_count(mp.mpf(3), mp.mpf(-6), mp.mpf(A))) < TOL
             for A in (4, 5, 6, 7))
    checks.append(("deltahedron: 3A - 6 = affine(3, -6)", ok))
    print(f"    {'convex deltahedron contact graph':<34}{'3':>7}{'-6':>7}   "
          f"corpus |E| at A = {accepted}")

    # ---- 2. the affine per-nucleon identity, and the profiler on a known answer
    print("\n  THE AFFINE IDENTITY  eps*(alpha*A + beta)/A = eps*alpha + eps*beta/A")
    for nm, al, be in [("chain", mp.mpf(1), mp.mpf(-1)), ("deltahedron", mp.mpf(3), mp.mpf(-6))]:
        ok = all(abs(EPS * affine_bond_count(al, be, mp.mpf(A)) / A - (EPS * al + EPS * be / A)) < TOL
                 for A in (2, 4, 12, 56, 208))
        checks.append((f"{nm}: the affine per-nucleon identity holds exactly, five A", ok))
        pairs = [(A, EPS * affine_bond_count(al, be, mp.mpf(A)) / A) for A in range(4, 260, 4)]
        p_star, rss_star = profile_exponent(pairs)
        print(f"    {nm:<14}profiled exponent of its own exact law: p* = {mp.nstr(p_star, 12)}"
              f"   RSS = {mp.nstr(rss_star, 4)}")
        checks.append((f"{nm}: profiling the exponent of its EXACT law returns p = 1 to 1e-8 "
                       f"(this also validates #6780's profiler against a known answer)",
                       abs(p_star - 1) < mp.mpf("1e-8")))

    # ---- 3. the bulk criterion, both clauses -------------------------------
    print("\n  THE BULK CRITERION   HasBulk(A_surf)  <=>  A_surf -> inf  AND  A_surf/A -> 0")
    print(f"    {'surface count A_surf(A)':<32}{'A_surf at A=10^4':>18}{'A_surf/A at A=10^4':>21}  verdict")
    BIG = mp.mpf(10) ** 4
    cands = [("chain:        A_surf = 2", lambda A: mp.mpf(2)),
             ("deltahedron:  A_surf = A", lambda A: A),
             ("packing:      A_surf = A^(2/3)", lambda A: A ** (mp.mpf(2) / 3))]
    verdicts = {}
    for nm, f in cands:
        grows = f(BIG * 100) > f(BIG) * 10          # unbounded: grows with A
        vanishes = f(BIG) / BIG < mp.mpf("0.05")    # interior: fraction small
        verdicts[nm] = grows and vanishes
        print(f"    {nm:<32}{mp.nstr(f(BIG), 6):>18}{mp.nstr(f(BIG) / BIG, 6):>21}  "
              f"{'HAS BULK' if verdicts[nm] else 'NO BULK'}")
    checks.append(("chain fails HasBulk — its surface is CONSTANT, so there is no growing surface "
                   "(boundedSurface_not_hasBulk)", not verdicts["chain:        A_surf = 2"]))
    checks.append(("deltahedron fails HasBulk — every nucleon is a hull vertex, so the surface "
                   "FRACTION does not vanish: d = 3 with no interior (linearSurface_not_hasBulk)",
                   not verdicts["deltahedron:  A_surf = A"]))
    checks.append(("a sublinear power surface satisfies HasBulk — the case CoordinationSurfaceDeficit "
                   "assumed (powerSurface_hasBulk)", verdicts["packing:      A_surf = A^(2/3)"]))

    # the corpus's deltahedron family does not even reach large A
    print(f"\n    NOTE: the corpus records deltahedra only for A in {accepted} — the largest has "
          f"{max(accepted)} nucleons.")
    print(f"    HasBulk is an A -> infinity criterion, so on the corpus's ACTUAL data it is not")
    print(f"    statable for the deltahedron at all; the A_surf = A row above is the idealisation.")
    checks.append(("the corpus's hardcoded deltahedron family stops at A = 7 — smaller even than the "
                   "convex-deltahedron family {4..10, 12} its own docstring names — so the asymptotic "
                   "criterion is applied to its IDEALISATION, never to its data",
                   accepted == [2, 3, 4, 5, 6, 7]))

    # ---- 4. non-affine is NOT sufficient -----------------------------------
    print("\n  NON-AFFINE IS NECESSARY, NOT SUFFICIENT")
    def complete(A):
        return mp.mpf(A) * (mp.mpf(A) - 1) / 2
    second_diff = [complete(A + 2) - 2 * complete(A + 1) + complete(A) for A in (4, 10, 50)]
    checks.append(("the complete graph is NOT affine (its second difference in A is 1, not 0)",
                   all(abs(d - 1) < TOL for d in second_diff)))
    pn = [EPS * complete(A) / A for A in (10, 100, 1000)]
    checks.append(("...and it is refuted for the opposite reason: its per-nucleon binding is "
                   "UNBOUNDED (CoordinationSaturation.bounded_degree_saturates)",
                   pn[0] < pn[1] < pn[2] and pn[2] > 100 * pn[0]))
    print(f"    complete graph: second difference = {mp.nstr(second_diff[0], 4)} (affine would be 0), "
          f"B/A at A = 10, 100, 1000: {', '.join(mp.nstr(v, 5) for v in pn)}")
    print(f"    So the corpus's one non-affine edge set is SUPERlinear and already refuted. The")
    print(f"    target is sublinear-but-unbounded surface growth, which nothing on main produces.")

    # ---- 5. what the DATA require ------------------------------------------
    print("\n  WHAT THE DATA REQUIRE — under perNucleon_split the deficit is (eps(k-k')/2)*(A_surf/A),")
    print("  so #6780's fitted p implies A_surf ~ A^(1-p). Is that a bulk?")
    print(f"    {'#6780 variant':<28}{'p*':>11}{'implied 1-p':>14}   0 < 1-p < 1?")
    all_bulk = True
    for nm, p in P6780:
        theta = 1 - p
        inside = 0 < theta < 1
        all_bulk = all_bulk and inside
        print(f"    {nm:<28}{mp.nstr(p, 6):>11}{mp.nstr(theta, 6):>14}   {'yes' if inside else 'NO'}")
    checks.append(("EVERY #6780 variant implies a surface exponent strictly inside (0, 1): the data "
                   "require an edge set WITH a bulk, and no AFFINE edge set has one (the unqualified "
                   "'no edge set on main' would overclaim — see section 6)", all_bulk))
    theta_all = 1 - P6780[0][1]
    print(f"    all-nuclide implied surface exponent {mp.nstr(theta_all, 6)} against the compact-packing "
          f"2/3 = {mp.nstr(mp.mpf(2) / 3, 6)}")
    checks.append(("the all-nuclide implied surface exponent is within 0.05 of the compact-packing 2/3 "
                   "(a consistency check, NOT a prediction — #6780 measured this exponent mass-cut "
                   "dependent)", abs(theta_all - mp.mpf(2) / 3) < mp.mpf("0.05")))

    # ---- 6. what this probe does NOT cover, measured rather than asserted --
    print("\n  EDGE SETS THIS PROBE DOES NOT COVER — the enumeration is EMPIRICAL, so the")
    print("  conclusion is scope-(a) and is about AFFINE edge sets, not about every derived one.")

    # the degree-capped count is piecewise, so not affine on R: its second difference is
    # nonzero at the knee A = k+1 and zero after it.
    def capped(A, k=12):
        return mp.mpf(A) * min(mp.mpf(A) - 1, mp.mpf(k)) / 2
    knee = capped(12) - 2 * capped(13) + capped(14)          # spans the knee at A = 13
    far = capped(60) - 2 * capped(61) + capped(62)           # well past it
    checks.append(("the degree-capped count A*min(A-1,k)/2 is PIECEWISE, not affine on R: its "
                   "second difference is -6 at the knee and 0 far past it "
                   "(SaturationInvisibleToCumulants) — Part 2 still reaches it, Part 1 does not",
                   abs(knee + 6) < TOL and abs(far) < TOL))
    print(f"    degree-capped A*min(A-1,12)/2 : second difference {mp.nstr(knee, 4)} at the knee, "
          f"{mp.nstr(far, 4)} far past it -> piecewise, not affine")
    print( "    max-contact sphere packing    : contact numbers for A >= 5 are case-by-case geometry")
    print( "                                    (computations/binding_edge_set_selection.py); NOT the")
    print( "                                    deltahedron family in general, and NOT known to be")
    print( "                                    affine. OUT OF SCOPE — Part 1 does not cover it.")
    print( "    alpha-cluster contact deltahedra: a second-level edge set on n_alpha = A/4 vertices")
    print( "                                    (bk_alpha_geometry_selection.py). Not covered here.")

    checks.append(("NO-FLOAT64: every reported quantity is an mpmath mpf",
                   all(isinstance(v, mp.mpf) for v in [EPS, TOL, theta_all, BIG, knee, far] + second_diff + pn)))

    print("\n  checks")
    for nm, ok in checks:
        print(f"    [{'PASS' if ok else 'FAIL'}] {nm}")
    npass = sum(1 for _, o in checks if o)
    print(f"\n  {npass}/{len(checks)} checks passed")
    return 0 if npass == len(checks) else 1


if __name__ == "__main__":
    raise SystemExit(main())
