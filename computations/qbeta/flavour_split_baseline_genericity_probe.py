#!/usr/bin/env python3
"""Is the flavour-split baseline `(q-1)^2 (1-q^-4)/3` SELECTED, or merely IN RANGE?

WHY THIS RUNS BEFORE ANY ATTEMPT TO DERIVE IT
---------------------------------------------
`conj:flavor-split-habiro-derivation` states the position plainly:

    X_baseline(q) = (q-1)^2 (1 - q^-4)/3  ~  0.00137571

    "is a structured near-match, not a derived closed form: it reproduces the
     target to a residual of ~1.76e-6 absolute (~0.128% relative), and its
     status is that of a candidate whose categorical derivation is open."

Bean `qou-qqm4` carries "derive the `(q-1)^2/3`" as its live target.  AGENTS.md
SS"Defined residual != derived decomposition" item 2 says to ask, before building
on a near-match, whether the offset is **forced** or **merely in range** -- the
`sleak_offset_genericity_check` pattern, where a sign flip attributed to
`Vol(4_1)` turned out to be produced by every constant in a window of width
0.049.  This probe runs that instrument on the flavour split.

It is NOT an attack on the form and it derives nothing.  It measures one thing:
how much company the corpus form has at its own accuracy.

WHAT IS MEASURED
----------------
A family of "simple substrate monomials with a small rational prefactor":

    X = (p/k) * prod_i s_i^{e_i},    e_i >= 0,   sum_i e_i <= MAX_DEGREE

over the substrate scalars the corpus itself uses -- `hbar_q = 1 - 1/q`,
`h = q - 1/q`, `[2]_q = q + 1/q`, `q - 1`, `z_D = q^3/(q^2+1)`, `[3]_q` -- with
`p, k` in `1..PREFACTOR_MAX`.  The corpus form is a member: AGENTS.md records the
identity `delta = hbar_q^2 * h * [2]_q / 3`, i.e. exponents `(2,1,1,0,0,0)` at
`p/k = 1/3`, total degree 4.

Four statistics, in increasing sharpness:

  (A) how many family members land inside the corpus form's own relative miss;
  (B) what fraction of MONOMIALS admit SOME prefactor landing inside -- this
      separates "the monomial structure carries information" from "the rational
      prefactor is doing all the work";
  (C) the closest members, ranked, so it is visible whether the corpus form is
      distinguished at all;
  (D) the tolerance at which the corpus form becomes the UNIQUE member.  That is
      the decisive number: if (D) is orders of magnitude tighter than the 0.128 %
      the form achieves, then at its own accuracy the form is one of many.

The target is the experimental flavour split
`delta = (m_n - m_p)/M_N`, `M_N = (m_p+m_n)/2`, computed from the CODATA 2022
**neutron-proton mass ratio** `r = 1.00137841946 +/- 4.0e-10` as
`delta = 2(r-1)/(r+1)` -- the highest-precision handle, and dimensionless, so no
MeV conversion enters.  `q0` is the proton pin (standing owner directive
2026-08-07).

Run: python3 computations/qbeta/flavour_split_baseline_genericity_probe.py
"""

from __future__ import annotations

from fractions import Fraction
from itertools import product

from mpmath import mp, mpf

mp.dps = 60

MAX_DEGREE = 4          # the corpus form's own total degree (2 + 1 + 1)
PREFACTOR_MAX = 12      # p, k in 1..12


def substrate_scalars(q):
    """The substrate scalars the corpus itself names, in a fixed order."""
    return [
        ("hbar_q", 1 - 1 / q),
        ("h", q - 1 / q),
        ("[2]_q", q + 1 / q),
        ("q-1", q - 1),
        ("z_D", q**3 / (q**2 + 1)),
        ("[3]_q", q**2 + 1 + q**-2),
    ]


def monomials(names, vals, max_deg):
    """All exponent tuples with non-negative entries summing to <= max_deg."""
    n = len(names)
    for exps in product(range(max_deg + 1), repeat=n):
        if 0 < sum(exps) <= max_deg:
            v = mpf(1)
            for e, s in zip(exps, vals):
                if e:
                    v *= s**e
            yield exps, v


def label(names, exps, frac):
    body = " * ".join(f"{n}^{e}" if e > 1 else n
                      for n, e in zip(names, exps) if e)
    return f"({frac}) * {body}"


def main() -> int:
    ok = True

    from qou_substrate.constants import Q_50_DIGIT_STR, Q_MP            # noqa: PLC0415
    from qou_substrate.codata import codata                       # noqa: PLC0415

    q0 = Q_MP
    _np = codata("neutron-proton mass ratio")
    r = mpf(_np.value_str)
    target = 2 * (r - 1) / (r + 1)
    target_err = 2 * 2 * mpf(_np.uncertainty_str) / (r + 1) ** 2

    print("0. INPUTS")
    print(f"   q0 (proton pin)          = {mp.nstr(q0, 20)}")
    print(f"   m_n/m_p (CODATA 2022)    = {_np.value_str} +/- {_np.uncertainty_str}")
    print(f"   delta_target = 2(r-1)/(r+1) = {mp.nstr(target, 12)}"
          f"  +/- {mp.nstr(target_err, 3)}")

    names = [n for n, _ in substrate_scalars(q0)]
    vals = [v for _, v in substrate_scalars(q0)]

    corpus = (q0 - 1) ** 2 * (1 - q0**-4) / 3
    corpus_exps = (2, 1, 1, 0, 0, 0)                 # hbar^2 * h * [2]
    check = mpf(1)
    for e, s in zip(corpus_exps, vals):
        check *= s**e
    check /= 3
    ident = abs(check - corpus) / abs(corpus)
    good = ident < mpf("1e-40")
    ok &= good
    corpus_miss = abs(corpus - target) / target
    print()
    print("1. THE CORPUS FORM, AND ITS MEMBERSHIP IN THE FAMILY")
    print(f"   (q-1)^2 (1-q^-4)/3       = {mp.nstr(corpus, 12)}")
    print(f"   hbar_q^2 * h * [2]_q / 3 = {mp.nstr(check, 12)}   "
          f"rel {mp.nstr(ident, 3)}   {'IDENTICAL' if good else 'MISMATCH'}")
    print(f"   relative miss vs target  = {mp.nstr(corpus_miss * 100, 6)} %"
          f"   (the block reports ~0.128 %)")

    # rational prefactor grid, deduplicated
    grid = sorted({Fraction(p, k) for p in range(1, PREFACTOR_MAX + 1)
                   for k in range(1, PREFACTOR_MAX + 1)})
    grid_mp = [(f, mpf(f.numerator) / f.denominator) for f in grid]
    mons = list(monomials(names, vals, MAX_DEGREE))

    print()
    print(f"2. THE FAMILY: {len(mons)} monomials (degree 1..{MAX_DEGREE}) x "
          f"{len(grid)} distinct prefactors p/k, p,k <= {PREFACTOR_MAX}")
    print(f"   = {len(mons) * len(grid)} members")

    # ---- (A) + (B) + (C) ----------------------------------------------------
    hits = []
    mons_with_hit = 0
    ranked = []
    for exps, v in mons:
        hit_this_monomial = False
        best_local = None
        for f, fv in grid_mp:
            x = fv * v
            rel = abs(x - target) / target
            if best_local is None or rel < best_local[0]:
                best_local = (rel, f)
            if rel <= corpus_miss:
                hits.append((rel, f, exps))
                hit_this_monomial = True
        if hit_this_monomial:
            mons_with_hit += 1
        ranked.append((best_local[0], best_local[1], exps))

    hits.sort(key=lambda t: t[0])
    ranked.sort(key=lambda t: t[0])

    print()
    print("3. (A) HOW MANY MEMBERS LAND INSIDE THE CORPUS FORM'S OWN MISS")
    print(f"   members within {mp.nstr(corpus_miss * 100, 4)} % of the target : "
          f"{len(hits)}  of  {len(mons) * len(grid)}"
          f"   ({100 * len(hits) / (len(mons) * len(grid)):.4f} %)")

    print()
    print("   (B) HOW MANY MONOMIALS ADMIT *SOME* PREFACTOR THAT LANDS INSIDE")
    print(f"   monomials with at least one hit : {mons_with_hit} of {len(mons)}"
          f"   ({100 * mons_with_hit / len(mons):.2f} %)")
    print("   -> this is the statistic that separates structure from prefactor")
    print("      freedom: a high fraction means the monomial carries little and")
    print("      the rational p/k is doing the work.")

    print()
    print("   (C) THE TEN CLOSEST MEMBERS  (best prefactor per monomial)")
    corpus_rank = None
    for i, (rel, f, exps) in enumerate(ranked[:10], 1):
        mark = ""
        if exps == corpus_exps and f == Fraction(1, 3):
            mark = "   <== THE CORPUS FORM"
        print(f"   {i:>3}. rel {mp.nstr(rel, 4):>12}   {label(names, exps, f)}{mark}")
    for i, (rel, f, exps) in enumerate(ranked, 1):
        if exps == corpus_exps and f == Fraction(1, 3):
            corpus_rank = i
            break
    print(f"   corpus form's rank among {len(ranked)} monomials "
          f"(each at its own best prefactor): {corpus_rank}")

    # ---- (D) the uniqueness tolerance --------------------------------------
    print()
    print("   (D) AT WHAT TOLERANCE IS THE CORPUS FORM THE *UNIQUE* MEMBER?")
    others = [rel for rel, f, exps in ranked
              if not (exps == corpus_exps and f == Fraction(1, 3))]
    nearest_other = min(others)
    print(f"   nearest competitor's relative miss : {mp.nstr(nearest_other, 6)}")
    print(f"   corpus form's relative miss        : {mp.nstr(corpus_miss, 6)}")
    if nearest_other < corpus_miss:
        print(f"   -> the corpus form is NOT the closest member of its own family;")
        print(f"      {sum(1 for x in others if x < corpus_miss)} monomials beat it.")
    else:
        print(f"   -> the corpus form IS the closest; it is unique below "
              f"{mp.nstr(nearest_other, 4)}, i.e. a factor "
              f"{mp.nstr(nearest_other / corpus_miss, 4)} tighter than it achieves.")

    # ---- (E) the fair counter-statistic: SIMPLE prefactors only -------------
    print()
    print("   (E) THE FAIR COUNTER-STATISTIC — UNIT-NUMERATOR PREFACTORS ONLY")
    print("   The corpus form's prefactor is `1/3`.  Its competitors above need")
    print("   `8/9`, `4/7`, `11/2`.  A two-integer prefactor is a second tuned")
    print("   choice, so the comparison at equal simplicity restricts to `1/k`.")
    unit_grid = [(f, fv) for f, fv in grid_mp if f.numerator == 1]
    ranked_unit = []
    for exps, v in mons:
        best_local = None
        for f, fv in unit_grid:
            rel = abs(fv * v - target) / target
            if best_local is None or rel < best_local[0]:
                best_local = (rel, f)
        ranked_unit.append((best_local[0], best_local[1], exps))
    ranked_unit.sort(key=lambda t: t[0])
    unit_rank = next(i for i, (_, f, e) in enumerate(ranked_unit, 1)
                     if e == corpus_exps and f == Fraction(1, 3))
    print(f"   grid restricted to 1/k, k <= {PREFACTOR_MAX}: "
          f"{len(unit_grid)} prefactors, {len(mons) * len(unit_grid)} members")
    for i, (rel, f, exps) in enumerate(ranked_unit[:5], 1):
        mark = "   <== THE CORPUS FORM" if (exps == corpus_exps
                                            and f == Fraction(1, 3)) else ""
        print(f"   {i:>3}. rel {mp.nstr(rel, 4):>12}   {label(names, exps, f)}{mark}")
    n_unit_hits = sum(1 for rel, _, _ in ranked_unit if rel <= corpus_miss)
    print(f"   corpus form's rank under unit numerators : {unit_rank} of {len(mons)}")
    print(f"   monomials with a unit-numerator hit inside its miss : {n_unit_hits}")

    print()
    print("4. WHAT THIS DOES AND DOES NOT SAY")
    print("   It does NOT refute the form, and it derives nothing.  A genericity")
    print("   count bears on whether the 0.128 % agreement is EVIDENCE for this")
    print("   particular expression -- AGENTS.md SS'Defined residual != derived")
    print("   decomposition' item 2.  A structural derivation, if one is found,")
    print("   is unaffected by how much company the form has numerically.")
    print("   Scope (a) throughout: this family, this degree cap, this prefactor")
    print("   grid.  A different basis gives a different count.")

    print()
    print("VERDICT:", "PASS — genericity measured" if ok else "FAIL")
    return 0 if ok else 1


if __name__ == "__main__":
    raise SystemExit(main())
