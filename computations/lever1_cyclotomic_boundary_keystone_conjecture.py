#!/usr/bin/env python3
"""
lever1_cyclotomic_boundary_keystone_conjecture.py — the Habiro-tail cyclotomic boundary sits
EXACTLY at the framework's calibration+keystone order (n=5), and the McKay 2I↔Ê₈ value map
(#3685) supplies the MECHANISM. States conj:cyclotomic-boundary-at-keystone. (lever-1 / z2bn.)

CONTEXT (anti-duplication, honest): the D(m) *arithmetic* — closed forms, (q−1)² universal,
bar-even, cyclotomic head + growing generic (NOT Salem, NOT special-function) non-cyclotomic
core — was already derived on 2026-06-28 (Stages 7-9:
`docs/audits/2026-06-28-lever1-binding-{correction-cyclotomic-core-growth,core-bar-symmetric-
irreducible,core-root-distribution}.md`, through m=11). This probe does NOT re-derive that; it
CITES it and adds the observations the corpus does not have: (i) the boundary's ALIGNMENT with
the framework's calibration/keystone structure, and (ii) a rep-theory MECHANISM via the merged
McKay value map (#3685).

THE ALIGNMENT (observation i). The na-Stokes body-order n indexes both the Habiro tail D(n)
and the framework's calibration/keystone data:

  n | a_D^(n)=lw(n−1) | framework role                    | D(n)
  2 | lw(1)           | CAL c=1 (muon / leptonic anchor)  | 0        (cyclotomic-pure)
  3 | lw(2)           | CAL c=2 (Hopf / former gate)      | (q−1)²Φ₃
  4 | lw(3)           | CAL c=3 (proton / Family-A)       | (q−1)²Φ₃  (× q-clear)
  5 | lw(4)           | KEYSTONE  S₅ ⊃ A₅ (icosahedral)   | cyclotomic (Φ₂²Φ₃Φ₆)
  6 | lw(5)           | first order BEYOND cal+keystone   | NON-cyclotomic (deg-8 core)

So the cyclotomic-pure regime `n ≤ 5` is EXACTLY the framework's {3 calibration orders} ∪
{S₅ keystone}; the first non-cyclotomic content appears at the first body-order n=6 that is
neither a calibration nor the keystone.

THE MECHANISM (observation ii, the NEW strengthening — ties to merged #3685). S(n)=Σ_{λ⊢n}dim_q(λ),
so the arithmetic of D(n) is governed by the dim_q(λ). At the keystone n=5 the merged McKay
2I↔Ê₈ value map (`docs/audits/2026-07-12-keystone-wlambda-derivation-mckay-e8-route.md`,
`KeystoneMcKayValueMap.lean`, EXACT no-fit) shows the four bwS0 conjugation classes {λ,λ'} of
S₅ carry values

    {(5),(1⁵)}      -> [1]_q          (McKay node: trivial,  E₈ mark 1)
    {(4,1),(2,1⁴)}  -> [4]_q          (A₅ standard,          E₈ mark 4)
    {(3,2),(2,2,1)} -> [5]_q          (A₅ 5-dim,             E₈ mark 5)
    {(3,1,1)} self  -> [5]_q + 1      (A₅ split 3⊕3′,        E₈ mark 6)

— EXACTLY the E₈ Coxeter marks [mark]_q. This is available because A₅ ≅ 2I/{±1} is the
ICOSAHEDRAL group and 2I ↔ Ê₈ (McKay). The McKay-ADE ladder of alternating groups is FINITE:

    A₄ ≅ tetrahedral  (binary 2T ↔ Ê₆)   — dims mostly single q-integers
    A₅ ≅ icosahedral  (binary 2I ↔ Ê₈)   — dims = E₈ marks [mark]_q  (KEYSTONE)
    A₆ ≅ PSL(2,9)     — NOT a binary polyhedral group, NO McKay-ADE datum

A₅ is the LAST alternating group that is (the rotation group of) a Platonic solid / binary
polyhedral / McKay-ADE group. At n=6 the dim_q(λ) become genuine COMPOUND products of several
cyclotomics (only 4/11 partitions have dim_q a single [m]_q, vs 6/7 at n=5 — the one exception
being the McKay split node [5]_q+1), the McKay-mark structure is GONE, and D(6) leaves the
cyclotomic (Habiro) ring. The two candidate causes therefore UNIFY:

conj:cyclotomic-boundary-at-keystone (scope-(a), CORRELATION not proved causation):
  D(n) is cyclotomic (Habiro-pure) ⟺ n ≤ 5 = the keystone order. n=5 is distinguished as the
  LAST exceptional-Lie alternating group, from two dovetailing sides:
    (a) n=5 = |S₅ keystone|, A₅ = icosahedral = LAST McKay-ADE alternating group (2I↔Ê₈); the
        keystone dims are the E₈ marks [mark]_q (#3685, exact). A₆ (n=6) is the first non-McKay.
    (b) n=6 = the UNIQUE symmetric group with a nontrivial OUTER AUTOMORPHISM (S₆) — the one
        exceptional S_n — coinciding with the non-cyclotomic onset from the other side.
  The arithmetic MECHANISM is Stage-7's Φ_d-rule (Φ_d first divides D(d+1)); the rep-theory
  mechanism is the McKay-mark exit at A₆. The CAUSATION (does the A₅→A₆ McKay exit / S₆ anomaly
  FORCE the boundary?) is OPEN — the formalization target.

Discipline: correlation only, magnitudes not interpreted (numerology guard). Binding D(n), NOT
the Q_β c_k ladder. Reproduces the Stage-7 boundary minimally (cross-check); CITES Stages 7-9 for
the full arithmetic and #3685 for the McKay value map. Scope-(a), no fit, no wiring.

Audit: docs/audits/2026-07-12-lever1-cyclotomic-boundary-keystone-conjecture.md
"""
from __future__ import annotations
import sys
from pathlib import Path

import sympy as sp

HERE = Path(__file__).resolve().parent
for p in (str(HERE / "substrate"), str(HERE)):
    if p not in sys.path:
        sys.path.insert(0, p)

q = sp.symbols('q')

FRAMEWORK_ROLE = {
    2: "CAL c=1 (muon / leptonic anchor)",
    3: "CAL c=2 (Hopf / former gate)",
    4: "CAL c=3 (proton / Family-A)",
    5: "KEYSTONE  S₅ ⊃ A₅ (icosahedral / Bring)",
    6: "first order BEYOND {calibration ∪ keystone}",
    7: "beyond",
}

# McKay-ADE ladder of alternating groups (standard rep-theory facts; documentation, not fit).
MCKAY_ADE_LADDER = {
    4: ("A₄ ≅ tetrahedral", "binary 2T ↔ Ê₆", True),
    5: ("A₅ ≅ icosahedral", "binary 2I ↔ Ê₈", True),
    6: ("A₆ ≅ PSL(2,9)", "NOT binary polyhedral — no McKay-ADE datum", False),
}


def qint(k):
    return sp.Integer(0) if k == 0 else sp.cancel((q ** k - q ** (-k)) / (q - 1 / q))

def qfac(n):
    r = sp.Integer(1)
    for k in range(1, n + 1):
        r *= qint(k)
    return sp.cancel(r)

def parts(n, m=None):
    if m is None:
        m = n
    if n == 0:
        yield ()
        return
    for k in range(min(n, m), 0, -1):
        for r in parts(n - k, k):
            yield (k,) + r

def hooks(lam):
    conj = [sum(1 for r in lam if r > j) for j in range(lam[0])]
    return [(row - j - 1) + (conj[j] - i - 1) + 1
            for i, row in enumerate(lam) for j in range(row)]

def dimq(lam):
    d = qfac(sum(lam))
    for h in hooks(lam):
        d /= qint(h)
    return sp.cancel(d)

def S(n):
    return sp.cancel(sum(dimq(l) for l in parts(n))) if n > 0 else sp.Integer(1)

def single_qint_mark(expr, maxm=30):
    """Return m if expr == [m]_q (single q-integer), else m if expr == [m]_q + 1 (McKay split
    node signature), else None. Distinguishes the two by a 'split' flag."""
    for m in range(1, maxm):
        if sp.simplify(expr - qint(m)) == 0:
            return (m, False)
    for m in range(1, maxm):
        if sp.simplify(expr - (qint(m) + 1)) == 0:
            return (m, True)
    return None

def mckay_mark_count(n):
    """Count partitions λ⊢n whose dim_q is a McKay mark: a single [m]_q, or the split [m]_q+1."""
    single = 0
    split = 0
    for lam in parts(n):
        r = single_qint_mark(dimq(lam))
        if r is None:
            continue
        if r[1]:
            split += 1
        else:
            single += 1
    return single, split, sum(1 for _ in parts(n))

def is_cyclotomic(poly):
    if sp.Poly(poly, q).degree() < 1:
        return True
    for k in range(1, 80):
        if sp.expand(poly - sp.cyclotomic_poly(k, q)) == 0:
            return True
    return False

def tail_is_cyclotomic(n):
    """True iff D(n) factors entirely into cyclotomics (+ (q−1)² + q-monomial)."""
    D = sp.cancel(S(n) - S(n - 1) - qint(n - 1) * S(n - 2))
    if D == 0:
        return True
    num, _ = sp.fraction(sp.cancel(D))
    _, facs = sp.factor_list(sp.expand(num))
    return all(sp.Poly(f, q).degree() < 1 or is_cyclotomic(f) for f, _m in facs)


def main() -> int:
    print("=== conj:cyclotomic-boundary-at-keystone — the D(n) boundary sits at n=5 (S₅) ===\n")

    # (1) The cyclotomic boundary (minimal cross-check; full arithmetic = Stages 7-9).
    print("--- (i) The cyclotomic boundary (cross-check; full arithmetic = Stages 7-9) ---")
    print(f"  {'n':>2} {'role':<40} {'D(n) cyclotomic?':>17}")
    boundary = None
    cyclo = {}
    for n in range(2, 8):
        c = tail_is_cyclotomic(n)
        cyclo[n] = c
        if not c and boundary is None:
            boundary = n
        print(f"  {n:>2} {FRAMEWORK_ROLE.get(n, ''):<40} {'yes' if c else 'NO — non-cyclotomic':>17}")

    # (2) The McKay value map at the keystone n=5 (dims = E₈ marks); exit at n=6.
    print("\n--- (ii) The McKay mechanism: keystone dim_q = E₈ marks [mark]_q (#3685) ---")
    print("  A₅ ≅ icosahedral, 2I ↔ Ê₈ — the four bwS0 classes {λ,λ'} of S₅ carry E₈ marks:")
    bwS0_5 = [((5,), (1, 1, 1, 1, 1)), ((4, 1), (2, 1, 1, 1)),
              ((3, 2), (2, 2, 1)), ((3, 1, 1),)]
    mark_ok = True
    for cls in bwS0_5:
        lam = cls[0]
        d = dimq(lam)
        r = single_qint_mark(d)
        if r is None:
            mark_ok = False
            tag = "NOT a mark"
        else:
            m, split = r
            tag = f"[{m}]_q" + (" + 1 (split node, mark 6)" if split else f" (mark {m})")
        # bwS0 conjugation symmetry d_q(λ)=d_q(λ') for the paired classes
        if len(cls) == 2:
            assert sp.simplify(dimq(cls[0]) - dimq(cls[1])) == 0, f"bwS0 pairing broken at {cls}"
        print(f"    {str(cls):32} d_q = {tag}")
    print(f"  keystone dims are E₈ McKay marks: {mark_ok}")

    print("\n  McKay-ADE ladder of alternating groups (A₅ = LAST McKay-ADE alternating group):")
    for n in (4, 5, 6):
        name, mck, is_mckay = MCKAY_ADE_LADDER[n]
        s, sp_, tot = mckay_mark_count(n)
        print(f"    n={n}: {name:18} {mck:42} single-[m]_q {s}+split {sp_} / {tot}"
              + ("" if is_mckay else "   <- McKay structure GONE"))
    s5 = mckay_mark_count(5)
    s6 = mckay_mark_count(6)
    mckay_exit_at_6 = (s5[0] + s5[1] >= 6) and (s6[0] + s6[1] <= 5)

    # Findings / conjecture.
    cal_keystone_all_cyclo = all(cyclo[n] for n in (2, 3, 4, 5))
    boundary_at_6 = (boundary == 6)
    keystone_order = 5

    print(f"\n### The alignment + mechanism (the new content)")
    print(f"  • Cyclotomic-pure regime: n ≤ {keystone_order}  (D(2..5) all cyclotomic: {cal_keystone_all_cyclo})")
    print(f"  • = EXACTLY the framework's calibration orders (c=1,2,3 → n=2,3,4) ∪ the S₅ keystone (n=5).")
    print(f"  • MECHANISM: at n=5 the keystone dim_q(λ) are the E₈ McKay marks [mark]_q (#3685, exact);")
    print(f"    A₅ = icosahedral = LAST McKay-ADE alternating group (2I↔Ê₈). At n=6 the McKay-mark")
    print(f"    structure EXITS ({s6[0]+s6[1]}/{s6[2]} marks vs {s5[0]+s5[1]}/{s5[2]} at n=5), A₆ is not")
    print(f"    binary-polyhedral, and D(6) leaves the cyclotomic (Habiro) ring.")
    print(f"\n### conj:cyclotomic-boundary-at-keystone (scope-(a), CORRELATION — causation OPEN)")
    print(f"  D(n) cyclotomic (Habiro-pure) ⟺ n ≤ 5 = keystone order. n=5 = LAST exceptional-Lie")
    print(f"  alternating group, from two dovetailing sides:")
    print(f"    (a) A₅ = icosahedral = last McKay-ADE alt. group (2I↔Ê₈); keystone dims = E₈ marks;")
    print(f"    (b) n=6 = the UNIQUE S_n with a nontrivial OUTER AUTOMORPHISM (S₆) — the one")
    print(f"        exceptional symmetric group, coinciding with the non-cyclotomic onset.")
    print(f"  Mechanism = Stage-7 Φ_d|D(d+1) + the McKay-mark exit at A₆; causation OPEN")
    print(f"  (formalization target). Arithmetic (not-Salem, generic core) = Stages 7-9 (2026-06-28),")
    print(f"  cited; McKay value map = #3685, cited. Magnitudes not interpreted.")

    ok = cal_keystone_all_cyclo and boundary_at_6 and mark_ok and mckay_exit_at_6
    try:
        from witness_base import WitnessBuilder
        wb = WitnessBuilder("lever1-cyclotomic-boundary-keystone-conjecture", engine="sympy")
        wb.set_description(
            "conj:cyclotomic-boundary-at-keystone (lever-1/z2bn). The Habiro-tail D(n) is cyclotomic "
            "(Habiro-pure) exactly for n≤5, and n=5 is the framework's keystone order (S₅⊃A₅ "
            "icosahedral): the cyclotomic-pure regime = {calibration orders c=1,2,3 → n=2,3,4} ∪ "
            "{S₅ keystone n=5}; first non-cyclotomic content at n=6 = first order beyond cal+keystone. "
            "MECHANISM (ties to merged #3685): at n=5 the four bwS0 conjugation classes of S₅ carry "
            "dim_q = the E₈ McKay marks [1]_q,[4]_q,[5]_q,[5]_q+1 (McKay 2I↔Ê₈, exact no-fit); A₅ = "
            "icosahedral = the LAST McKay-ADE alternating group (A₄↔Ê₆, A₅↔Ê₈, A₆ not binary "
            "polyhedral). At n=6 the McKay-mark structure exits (4/11 single-[m]_q vs 6/7+split at "
            "n=5) and D(6) leaves the cyclotomic ring. Two dovetailing candidate causes: (a) A₅ = last "
            "McKay-ADE alt. group; (b) n=6 = the UNIQUE S_n with a nontrivial outer automorphism (S₆). "
            "Mechanism = Stage-7 Φ_d|D(d+1) + McKay-mark exit at A₆; causation OPEN (formalization "
            "target). Arithmetic (not-Salem, generic core) = Stages 7-9 (2026-06-28), CITED not "
            "re-derived; McKay value map = #3685, CITED. Correlation only, magnitudes not interpreted. "
            "Scope-(a), no fit, no wiring.")
        wb.add_data("tail_cyclotomic_by_n", {str(n): bool(cyclo[n]) for n in cyclo})
        wb.add_data("keystone_order", keystone_order)
        wb.add_data("boundary_n", boundary)
        wb.add_data("keystone_dims_are_e8_marks", bool(mark_ok))
        wb.add_data("mckay_mark_count_n5", {"single": s5[0], "split": s5[1], "total": s5[2]})
        wb.add_data("mckay_mark_count_n6", {"single": s6[0], "split": s6[1], "total": s6[2]})
        wb.add_data("mckay_ade_alternating_ladder",
                    {str(n): {"group": MCKAY_ADE_LADDER[n][0], "mckay": MCKAY_ADE_LADDER[n][1],
                              "is_mckay_ade": MCKAY_ADE_LADDER[n][2]} for n in (4, 5, 6)})
        wb.add_assertion(
            name="cyclotomic_boundary_at_keystone_order",
            computed=str(int(bool(ok))), expected="1", tolerance=0,
            source=("D(2..5) all cyclotomic, D(6) first non-cyclotomic — the cyclotomic-pure regime "
                    "n≤5 equals {calibration c=1,2,3 → n=2,3,4} ∪ {S₅ keystone n=5}. MECHANISM: the "
                    "keystone n=5 dims are the E₈ McKay marks [1]_q,[4]_q,[5]_q,[5]_q+1 (A₅ "
                    "icosahedral, 2I↔Ê₈, #3685); A₅ is the last McKay-ADE alternating group and the "
                    "McKay-mark structure exits at A₆ (n=6), where D(6) leaves the cyclotomic ring. "
                    "n=6 is also the unique exceptional S₆ (outer automorphism). Correlation; "
                    "causation open."))
        out = wb.save()
        print(f"\nWitness: {out}")
    except Exception as e:
        print(f"\n(witness skipped: {e})")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
