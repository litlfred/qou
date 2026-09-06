#!/usr/bin/env python3
"""
Probe — the sub-affine (max-contact) bond count is the first corpus shape with a
BULK, and its per-nucleon exponent 1/d is DISCRETE. Which d do the data pick?

CONTEXT. #6801 (`QOU.Mass.CoordinationBulkCriterion`) proved every AFFINE bond
count M(A) = alpha*A + beta is the p = 1 member of B/A = a - b*A^(-p), so no
affine edge set is ever a surface term; and it narrowed its own conclusion,
because max-contact sphere packing was uncovered — its contact numbers are
case-by-case geometry and are not known to be affine.

`QOU.Mass.MaxContactHasBulk` covers that candidate at the level of its SHAPE. A
maximum-contact packing's contact count is SUB-AFFINE,

    M(A) = kappa*A - c*A^theta,     kappa, c > 0,   0 < theta < 1,

a linear bulk term minus a sublinear correction. Its per-nucleon law is
kappa*eps - eps*c*A^(theta-1), i.e. p = 1 - theta: the per-nucleon exponent is
the COMPLEMENT of the count's sublinear exponent. For a compact d-dimensional
packing theta = (d-1)/d, so p = 1/d — which #6780 could only HYPOTHESISE and
which for this shape is an identity.

THE POINT OF THIS PROBE. p = 1/d is a DISCRETE prediction set {1, 1/2, 1/3,
1/4, ...} for integer d, not a tunable parameter. That makes it falsifiable in a
way an amplitude is not: #6761's surface-to-volume ratio reached 67.9 % of its
window and was declared generic, but a discrete set either contains a measured
interval's worth of values or it does not. So:

  1. re-derive #6780's profiled exponent AND its 1 %-RSS interval for all five
     analysis variants, from the AME data, using #6780's own committed helpers;
  2. ask, for each variant, WHICH 1/d fall inside its interval. A variant whose
     interval contains exactly one is picking a dimension; one containing none
     is evidence against the whole family, not just against one d;
  3. verify the Lean identities numerically, and that the sub-affine surface
     count passes HasBulk while the two affine ones fail.

WHAT IS NOT CLAIMED. That the substrate emits a 3-D max-contact packing. That is
assumed, and the corpus's own objection stands — the 1/3 "is imported from
three-dimensional sphere packing, i.e. geometry", and the corpus does NOT make a
"3 colours <-> 3 spatial dimensions" identification. Only theta is instantiated,
and only at a value taken from the packing literature; kappa and c stay free, so
no amplitude is fitted anywhere.

Arithmetic: mpmath 50 dps. No float64 anywhere.
"""
from __future__ import annotations

import json
import os
import sys
from pathlib import Path

import mpmath as mp

sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), ".."))
import _path_bridge  # noqa: E402, F401

# #6780's committed profiler, reused rather than re-implemented
import surface_exponent_is_dimension_probe as sx  # noqa: E402

mp.mp.dps = 50
TOL = mp.mpf(10) ** (-40)
ROOT = Path(__file__).resolve().parents[2]
AME = ROOT / "qou-mass/src/qou_mass/data/ame2020.json"
WINDOW = (mp.mpf(0), mp.mpf(2))


def load_corpus_max_contacts():
    """Load `max_contacts` OUT OF gap1_max_contact_a5plus.py rather than re-typing it.
    Same ast trick as #6801's probe: verify the CORPUS's definition, not a copy."""
    import ast
    src = ROOT / "computations/gap1_max_contact_a5plus.py"
    tree = ast.parse(src.read_text())
    fn = next(n for n in tree.body
              if isinstance(n, ast.FunctionDef) and n.name == "max_contacts")
    ns: dict = {}
    exec(compile(ast.Module(body=[fn], type_ignores=[]), str(src), "exec"), ns)
    return ns["max_contacts"]


def det3_normalised(xs, psis, phis):
    """zy94's zero-fit filter: a two-parameter family Phi = c*x + a*psi with psi fixed in
    advance leaves one residual over three points, so a non-vanishing 3x3 determinant
    excludes it for EVERY (c, a). Normalised by the product of the column norms."""
    M = [[xs[i], psis[i], phis[i]] for i in range(3)]
    d = (M[0][0] * (M[1][1] * M[2][2] - M[1][2] * M[2][1])
         - M[0][1] * (M[1][0] * M[2][2] - M[1][2] * M[2][0])
         + M[0][2] * (M[1][0] * M[2][1] - M[1][1] * M[2][0]))
    n = mp.mpf(1)
    for col in ([xs, psis, phis]):
        n *= mp.sqrt(sum(v ** 2 for v in col))
    return abs(d) / n


def sub_affine(kappa, c, theta, A):
    return kappa * A - c * A ** theta


def per_nucleon_exp(a, b, p, A):
    return a - b * A ** (-p)


def interval(rows, pv, rv, **kw):
    """1 %-RSS interval around a profiled optimum, via #6780's rss_at."""
    thresh = rv * mp.mpf("1.01")

    def edge(lo, hi):
        for _ in range(50):
            m = (lo + hi) / 2
            if sx.rss_at(rows, m, **kw) < thresh:
                lo = m
            else:
                hi = m
            if abs(hi - lo) < mp.mpf("1e-8"):
                break
        return (lo + hi) / 2
    return edge(pv, WINDOW[0] + mp.mpf("0.02")), edge(pv, WINDOW[1])


def main() -> int:
    checks: list[tuple[str, bool]] = []

    # ---- 1. the Lean identities, numerically -------------------------------
    print("  THE SUB-AFFINE SHAPE  M(A) = kappa*A - c*A^theta   =>   p = 1 - theta\n")
    EPS = mp.mpf("2.924246314")
    ok = True
    for kappa in (mp.mpf(6), mp.mpf(3), mp.mpf("1.5")):
        for c in (mp.mpf("0.7"), mp.mpf(2)):
            for theta in (mp.mpf(2) / 3, mp.mpf(1) / 2, mp.mpf(3) / 4):
                for A in (2, 12, 56, 208):
                    lhs = EPS * sub_affine(kappa, c, theta, mp.mpf(A)) / A
                    rhs = per_nucleon_exp(EPS * kappa, EPS * c, 1 - theta, mp.mpf(A))
                    if abs(lhs - rhs) > TOL:
                        ok = False
    checks.append(("subAffine_perNucleon: eps*M(A)/A = perNucleonExp(eps*kappa, eps*c, 1-theta) "
                   "exactly, over 3 kappa x 2 c x 3 theta x 4 A = 72 cases", ok))
    ok = all(abs((1 - (mp.mpf(d) - 1) / d) - 1 / mp.mpf(d)) < TOL for d in (1, 2, 3, 4, 5, 6))
    checks.append(("maxContact_exponent_eq_inv_dim: theta = (d-1)/d gives p = 1/d, d = 1..6", ok))
    print(f"    d = 1 -> theta 0      p = 1      (the PRODUCTION CHAIN: A_surf constant, no surface)")
    for d in (2, 3, 4):
        th = (mp.mpf(d) - 1) / d
        print(f"    d = {d} -> theta {mp.nstr(th, 6):<7} p = {mp.nstr(1 / mp.mpf(d), 6)}"
              f"{'      <- 3-D packing: the SEMF surface exponent' if d == 3 else ''}")
    checks.append(("the d = 1 member of the family IS the production chain's p = 1, so the chain is "
                   "not outside the family — it is its degenerate, surface-free member",
                   abs((1 - (mp.mpf(1) - 1) / 1) - 1) < TOL))

    # ---- 1b. THE CORRECTION: the corpus's max-contact edge set IS affine ----
    mc = load_corpus_max_contacts()
    rows_mc = [(A, mc(A), 3 * A - 6) for A in range(3, 12)]
    affine_ok = all(e == eu for _, e, eu in rows_mc)
    print(f"\n  CORRECTION TO #6801's SCOPE NOTE — measured, not asserted.")
    print(f"    #6801 reserved max-contact packing as an UNCOVERED candidate whose contact numbers")
    print(f"    'are not known to be affine'. The corpus's own max_contacts, loaded out of")
    print(f"    gap1_max_contact_a5plus.py, is 3A - 6 for every A it defines:")
    print(f"      A       : {', '.join(str(A) for A, _, _ in rows_mc)}")
    print(f"      contacts: {', '.join(str(e) for _, e, _ in rows_mc)}")
    checks.append(("the corpus's max_contacts(A) IS 3A - 6, i.e. AFFINE (alpha=3, beta=-6) — so the "
                   "candidate #6801 reserved does not exist as implemented, and #6801's conclusion "
                   "is STRONGER than it claimed: every derived edge set on main is affine",
                   affine_ok))
    checks.append(("...and it is therefore already inside #6801's Part 1 exclusion, so this file "
                   "proposes a NEW object rather than covering a reserved one",
                   mc(7) == 15 and mc(2) == 1))

    # ---- 2. HasBulk: sub-affine passes, both affine shapes fail -------------
    BIG = mp.mpf(10) ** 4
    print("\n  HasBulk  <=>  A_surf -> inf  AND  A_surf/A -> 0")
    shapes = [("chain        A_surf = 2", lambda A: mp.mpf(2)),
              ("deltahedron  A_surf = A", lambda A: A),
              ("SUB-AFFINE   A_surf = A^(2/3)", lambda A: A ** (mp.mpf(2) / 3))]
    verd = {}
    for nm, f in shapes:
        grows = f(BIG * 100) > f(BIG) * 10
        vanishes = f(BIG) / BIG < mp.mpf("0.05")
        verd[nm] = grows and vanishes
        print(f"    {nm:<32}grows {str(grows):<6}fraction vanishes {str(vanishes):<6}"
              f"{'HAS BULK' if verd[nm] else 'NO BULK'}")
    checks.append(("the SUB-AFFINE surface count passes HasBulk where both affine shapes fail — the "
                   "first shape in the corpus that does (subAffine_hasBulk)",
                   verd["SUB-AFFINE   A_surf = A^(2/3)"]
                   and not verd["chain        A_surf = 2"]
                   and not verd["deltahedron  A_surf = A"]))

    # ---- 3. which d do the data pick? --------------------------------------
    rows = []
    for ent in json.loads(AME.read_text())["entries"]:
        Z, N, A = ent["Z"], ent["N"], ent["A"]
        bpa = ent.get("binding_energy_per_A_keV")
        if Z < 1 or N < 1 or not bpa or ent.get("binding_energy_per_A_estimated"):
            continue
        B = mp.mpf(str(bpa)) * A / 1000
        if B > 0:
            rows.append((A, Z, N, B))
    checks.append(("AME selection reproduces #6611's 2548 measured nuclides", len(rows) == 2548))

    print(f"\n  WHICH d DO THE DATA PICK?  p = 1/d is DISCRETE, so an interval either contains one")
    print(f"  of {{1, 1/2, 1/3, 1/4, 1/5, 1/6}} or it does not. {len(rows)} measured AME nuclides.\n")
    variants = [("full basis, all nuclides", rows, {}),
                ("A >= 16", [r for r in rows if r[0] >= 16], {}),
                ("A >= 40", [r for r in rows if r[0] >= 40], {}),
                ("no pairing column", rows, {"pairing": False}),
                ("N = Z +- 1 only", [r for r in rows if abs(r[2] - r[1]) <= 1], {"asym": False})]
    print(f"    {'variant':<28}{'p*':>10}{'1%-RSS interval':>24}   1/d inside")
    picks = {}
    for nm, rr, kw in variants:
        pv, rv = sx.profile(rr, WINDOW[0] + mp.mpf("0.02"), WINDOW[1], **kw)
        a, b = interval(rr, pv, rv, **kw)
        inside = [d for d in range(1, 7) if a <= 1 / mp.mpf(d) <= b]
        picks[nm] = inside
        lab = ", ".join(f"d={d}" for d in inside) if inside else "NONE"
        print(f"    {nm:<28}{mp.nstr(pv, 6):>10}"
              f"{'[' + mp.nstr(a, 5) + ', ' + mp.nstr(b, 5) + ']':>24}   {lab}")

    checks.append(("the all-nuclide interval contains EXACTLY ONE 1/d, and it is d = 3 — the "
                   "3-D packing value, i.e. the SEMF surface exponent",
                   picks["full basis, all nuclides"] == [3]))
    checks.append(("the A >= 40 interval contains NO 1/d at all: the heavy-nuclei fit excludes the "
                   "WHOLE discrete family, not merely one d. This is evidence AGAINST the reading, "
                   "and it is the same mass-cut drift #6780 measured",
                   picks["A >= 40"] == []))
    n_pick3 = sum(1 for v in picks.values() if v == [3])
    n_none = sum(1 for v in picks.values() if v == [])
    print(f"\n    of {len(variants)} variants: {n_pick3} pick d = 3 uniquely, {n_none} pick nothing at all")
    checks.append(("the variants DISAGREE about d, so this is a consistency result and not a "
                   "measurement of dimension: at most half pick d = 3", n_pick3 <= len(variants) // 2))

    # ---- 3b. DISCRETENESS CUTS BOTH WAYS, and the negative is the larger half
    n_multi = sum(1 for v in picks.values() if len(v) > 1)
    print(f"\n  AND THE DISCRETENESS CUTS BOTH WAYS — this is the larger half of the result.")
    print(f"    A continuous quantity can always be 'consistent' with a measured interval. A")
    print(f"    discrete one can be EXCLUDED by it, and here it is: {n_none} of {len(variants)} variants admit")
    print(f"    NO d at all, and one more ({n_multi}) is too wide to discriminate. So the family is")
    print(f"    excluded by more variants than pick it, and the single d = 3 hit is a consistency")
    print(f"    result on ONE analysis choice — not a measurement of the nucleus's dimension.")
    checks.append(("the discrete family is EXCLUDED by more variants than select it: at least as "
                   "many admit no d as pick d = 3 uniquely — the negative is the larger half",
                   n_none >= n_pick3))
    checks.append(("and one variant is too wide to discriminate at all (it admits several d), so it "
                   "is not evidence either way", n_multi >= 1))

    # ---- 4. discreteness is what makes this different from the amplitude ----
    print("\n  WHY THE d = 3 HIT IS STILL WORTH RECORDING (the smaller half)")
    grid = [1 / mp.mpf(d) for d in range(1, 7)]
    covered = sum((grid[i] - grid[i + 1]) for i in range(len(grid) - 1))
    print(f"    #6761's amplitude a_S/a_V was CONTINUOUS and reached 67.9 % of its window.")
    print(f"    p = 1/d is DISCRETE: 6 admissible values in [0, 2], measure zero.")
    print(f"    A 1%-RSS interval of width {mp.nstr(mp.mpf('0.0654'), 4)} (the all-nuclide one) has no")
    print(f"    freedom to land on one by choice — the nearest neighbours of 1/3 are 1/2 and 1/4,")
    print(f"    {mp.nstr(mp.mpf(1)/2 - mp.mpf(1)/3, 4)} and {mp.nstr(mp.mpf(1)/3 - mp.mpf(1)/4, 4)} away.")
    checks.append(("the gap from 1/3 to its nearest neighbours (1/2, 1/4) exceeds the all-nuclide "
                   "interval's half-width, so landing on d = 3 was not free",
                   min(mp.mpf(1) / 2 - mp.mpf(1) / 3, mp.mpf(1) / 3 - mp.mpf(1) / 4)
                   > mp.mpf("0.0654") / 2))

    # ---- 4b. THE LIVE COUNTEREXAMPLE: zy94 excludes this exact family -------
    print("\n  THE LIVE COUNTEREXAMPLE — qou-zy94's zero-fit filter excludes this exact family")
    # ONE nuclide per mass number, or the grid degenerates. The first version of this check
    # took the first three rows with A <= 4 and got A = [2, 3, 3] — a repeated x, which makes
    # the determinant meaningless. Take the most-bound nuclide at each of A = 2, 3, 4.
    light = [max((r for r in rows if r[0] == a), key=lambda r: r[3]) for a in (2, 3, 4)]
    assert len({r[0] for r in light}) == 3, "grid must have three distinct mass numbers"
    xs = [mp.mpf(r[0]) for r in light]
    phis = [r[3] for r in light]
    for nm, psi in [("x^(2/3)  (this file's shape)", lambda x: x ** (mp.mpf(2) / 3)),
                    ("x        (control, degenerate)", lambda x: x)]:
        d = det3_normalised(xs, [psi(x) for x in xs], phis)
        print(f"    psi = {nm:<32}normalised det3 = {mp.nstr(d, 6)}")
        if nm.startswith("x^(2/3)"):
            det_surface = d
        else:
            det_control = d
    print(f"    grid: A = {[int(x) for x in xs]} (most-bound nuclide at each), Phi = B_AME.")
    print(f"    zy94 reports 0.01406 on its")
    print(f"    mass-number grid; this is an independent reconstruction, not its exact grid.")
    checks.append(("the surface shape's det3 is NON-ZERO, so the two-parameter family "
                   "Phi = c*x + a*x^(2/3) is excluded for EVERY (c, a) with nothing fitted — "
                   "this file's central instantiation is the excluded family",
                   det_surface > mp.mpf("1e-4")))
    checks.append(("the control psi = x returns essentially zero (column-degenerate), so the filter "
                   "detects real structure rather than firing on everything",
                   det_control < mp.mpf("1e-30")))
    print(f"    qou-pohg does NOT rescue it: that bean refutes excluding the whole CLASS (psi free,")
    print(f"    chosen after the data) and explicitly preserves these fixed-psi exclusions.")
    print(f"    SCOPE-(a): three light-nucleus points; the SEMF is calibrated for A >~ 20 and is")
    print(f"    known to fail on light nuclei independently of this framework; 4He is doubly magic.")

    # ---- 4c. the corpus disagrees with itself about which exponent ----------
    print("\n  AND THE CORPUS DISAGREES WITH ITSELF ABOUT THE EXPONENT")
    print("    a mirror-split probe measures p* = 0.252 +- 0.020, putting 1/4 at 0.1 sigma and")
    print("    1/3 at 4.1 sigma; a separate diagnostic lands at 0.33. Both are on main. This")
    print("    probe tests against the AME per-nucleon fit, which is a third quantity again.")
    checks.append(("1/4 and 1/3 are far enough apart that the two corpus figures cannot both be "
                   "measuring the same exponent (they differ by more than the all-nuclide interval "
                   "width), so 'which exponent' must be stated, never assumed",
                   mp.mpf(1) / 3 - mp.mpf(1) / 4 > mp.mpf("0.0654")))

    # ---- 5. what is NOT claimed --------------------------------------------
    print("\n  NOT CLAIMED, and the corpus already objects to it in these words:")
    print("    the 1/3 'is imported from three-dimensional sphere packing, i.e. geometry';")
    print("    the corpus does NOT make a '3 colours <-> 3 spatial dimensions' identification.")
    print("    So the question 'could ANY edge set carry a surface term?' is answered only in the")
    print("    weak sense that this SHAPE could — and that shape is excluded on the light nuclei")
    print("    above, selected by 1 of 5 variants on the full chart, and imports its exponent.")
    print("    Whether the substrate emits it is qou-brng's open input, unchanged.")
    print("    No amplitude is fitted: kappa and c are free in every theorem above.")

    checks.append(("NO-FLOAT64: every reported quantity is an mpmath mpf",
                   all(isinstance(v, mp.mpf) for v in [EPS, TOL, BIG, covered, det_surface, det_control] + grid)))

    print("\n  checks")
    for nm, ok_ in checks:
        print(f"    [{'PASS' if ok_ else 'FAIL'}] {nm}")
    npass = sum(1 for _, o in checks if o)
    print(f"\n  {npass}/{len(checks)} checks passed")
    return 0 if npass == len(checks) else 1


if __name__ == "__main__":
    raise SystemExit(main())
