#!/usr/bin/env python3
"""GS filtration / jet-grade shape: does the SURVIVING FILTRATION carry magic?

This closes the gap the q-degree probe left. `symbolic_nf_q_degree_magic_probe`
measured the **q-degree** of the six normal-form coefficients and found no
magic signal (A = 2..20, merged as 09af8355f9). But the q-degree is NOT the
Groebner-Shirshov filtration. The corpus's grading -- the one
`prop:jet-prefix-gb-filtration` and `bond-order-eq-jet-degree-proof` are about
-- indexes by the **Coxeter length of the normal-form word**, not by degree in
q. That grading had not been measured.

    NF_BASIS = [(), (0,), (1,), (0,1), (1,0), (0,1,0)]
    jet grade =  0     1     1      2      2       3

So coefficient 0 sits at grade 0, coefficients 1-2 at grade 1, 3-4 at grade 2,
and 5 at grade 3. The observable is the SHAPE: how the normal form's weight is
distributed across those grades.

## The ceiling, which is unconditional and is the real finding

    H_3 quotient (what build_atom_nf_mp carries):   4 grades, 0..3
    full H_{3A} tower:  max Coxeter length C(3A,2)
        A=2 -> 15    A=4 -> 66    A=8 -> 276    A=20 -> 1770

At A = 20 the production chain truncates a **1771-grade filtration to 4**.
That is arithmetic, not a measurement, and it holds regardless of anything
below.

## 🛑 What this probe does NOT conclude, and why

The tempting step is: "the n-nucleon cluster sits at jet degree n
(`bond-order-eq-jet-degree-proof`), the quotient caps at 3, therefore >=4-body
clusters have no graded home and magic 8/20/28 are structurally unreachable."

**That is not claimed here** -- because the two gradings are not the same
grading, which the bond sweep below measures directly rather than assumes.

Three corrections to earlier drafts of this file, all of my own claims:

  * `QOU.Mass.BodyOrderJetGrading.body_eq_graded` is NOT left assumed. It is
    a hypothesis FIELD of that structure, but it is DISCHARGED for the
    bond-product model by `body_eq_graded_of_bond_product` in
    `QOU/Knot/BodyOrderExpansion.lean` (sorry-free).
  * The two models do NOT "index in opposite directions". `prod_bonds_graded`
    *defines* `gradedTerm n` as the coefficient at bond-grade `|s| - n`, and
    `esymm_eq_compl_sum` is exactly the complement bijection that absorbs the
    reversal. There is no direction mismatch to reconcile.
  * "Bond count is recoverable from the H_3 shape" -- wrong, and it reversed
    between a toy and the canonical builder. The toy appended every bond as
    `MINUS_H_HALF` at the END of the word, past C(A,2), and gave 13 distinct
    shapes for 13 bond counts. The canonical builder interleaves TYPE-DEPENDENT
    bonds (pp->ZERO_D, nn->MINUS_H, pn->MINUS_H_HALF) after each nucleon block.
    Monotone appending buys monotone term growth, hence spurious injectivity.
    This is why `build_atom_nf_bonds` carries a keep-all control asserted in
    the witness: a lookalike construction must not be able to pass again.

What actually blocks the body-order reading is a cardinality fact plus a
lossiness fact, both measured here on the canonical builder:

  * **Cardinality.** The bond-product grading takes `|s| + 1 = C(A,2) + 1`
    values (7 at A=4, 191 at A=20). The GS word-length grading takes 4, at
    every A. No bijection exists, so the identification is false -- not
    unproved, false.
  * **Lossiness.** The folding is many-to-one *on bond count*. At Z=2, N=2
    the 7 bond counts m = 0..6 give only **6** distinct normalised shapes
    (m=5 collides with m=3); over the 222 configurations (Z, N <= 4, every
    m <= C(A,2)) there are **115 collisions** and only 107 distinct shapes.
    So the H_3 normal form does not determine even the NUMBER of bonds, let
    alone which bonds.

That is a stronger statement than the identification would have given: the
ceiling is not "191 grades faithfully folded into 4", it is lossy folding.
It is still NOT an exclusion of many-body structure -- weight, not grade
index, is where any surviving many-body information would live, and this
probe does not rule that out.

## Measured

Exhaustive: every (Z, N) at every A = 2..20, so the contrast is at fixed
algebra with only nucleon composition varying. Weight per grade is the exact
term count of the Laurent coefficients (`fractions.Fraction` throughout, no
float, no evaluation at any numerical q).

The shape is nearly CONSTANT -- ~(0.168, 0.337, 0.332, 0.163) -- and its total
range over all 228 configurations is small:

    grade 0: 0.1141 .. 0.2062      grade 2: 0.2474 .. 0.3574
    grade 1: 0.3185 .. 0.3711      grade 3: 0.1385 .. 0.1787

Clean magic/non-magic separations occur on **4 of 19 levels**, and both of the
usual controls reject them:

  * **All are at A <= 5**, where the groups are tiny (A=2 is 2 magic vs 1
    non-magic; A=4 is 1 vs 4) and a clean split is likely by chance. Nothing
    separates at any A >= 6 -- including A=8 and A=20, the levels that
    actually reach magic Z = 8 and Z = 20.
  * **The directions contradict.** Grade 3 is `magic_above` at A=2 and
    `magic_below` at A=4 and A=5. A quantity that flips sign between levels is
    measuring the level, not the magic number.

The probe computes the null rate per level rather than asserting the split is
unlikely, and reports `contradictory` per grade explicitly.

PRECISION: exact over Q. Term counts are integers; fractions are
`fractions.Fraction`. Nothing is evaluated at any numerical q, so the
NO-FLOAT64 discipline is satisfied structurally.
"""
from __future__ import annotations

import argparse
import os
import sys
import time
from fractions import Fraction
from math import comb  # float64-ok: exact integer binomial coefficient

sys.path[:0] = ['/home/user/qou/computations/probes',
                '/home/user/qou/computations',
                '/home/user/qou/computations/substrate']

from symbolic_nf_q_degree_magic_probe import (  # noqa: E402
    build_atom_nf_lau, ground_state_ordering, hm_lau, lau_one,
    MAGIC, MINUS_H, MINUS_H_HALF, ZERO_D,
)

#: Coxeter length of each element of ``NF_BASIS`` -- the jet vertical degree.
NF_BASIS = [(), (0,), (1,), (0, 1), (1, 0), (0, 1, 0)]
GRADE = [len(w) for w in NF_BASIS]          # 0, 1, 1, 2, 2, 3
MAX_GRADE = max(GRADE)


def jet_shape(Z: int, N: int) -> tuple[list[int], list[Fraction]]:
    """Term count per jet grade, and its exact normalised shape."""
    nf = build_atom_nf_lau(Z, N)
    t = [0] * (MAX_GRADE + 1)
    for i, c in enumerate(nf):
        t[GRADE[i]] += len(c)
    tot = sum(t)
    return t, [Fraction(x, tot) for x in t]


def null_rate(n_magic: int, n_non: int) -> Fraction:
    """P(one observable splits the two groups cleanly) under exchangeability."""
    return Fraction(2, comb(n_magic + n_non, n_magic))


# ── Is this grading the BOND-PRODUCT grading? ─────────────────────────────
#
# The question is whether the GS word-length filtration (0..3) can be
# identified with the bond-product / Mayer grading (0..|s|, |s| = C(A,2)).
# It is answered by varying the bond SET inside the canonical construction
# and watching what the H_3 grading does.

def build_atom_nf_bonds(Z: int, N: int, keep) -> list:
    """``build_atom_nf_lau`` with the inter-nucleon bond set filtered.

    ``keep(prev, k) -> bool`` decides whether bond ``(prev, k)`` is laid.
    With ``keep`` always true this is byte-identical to the canonical
    builder -- asserted as a control, so the sweep is provably the corpus
    construction with bonds removed, not a lookalike.
    """
    A = Z + N
    nf = [lau_one(), {}, {}, {}, {}, {}]
    if A == 0:
        return nf
    o = ground_state_ordering(Z, N)
    for k in range(A):
        if o[k] == "p":
            for _ in range(3):
                nf = hm_lau(nf, *ZERO_D, 0)
                nf = hm_lau(nf, *MINUS_H, 1)
            nf = hm_lau(nf, *ZERO_D, 0)
            nf = hm_lau(nf, *MINUS_H_HALF, 0)
            nf = hm_lau(nf, *MINUS_H_HALF, 1)
            nf = hm_lau(nf, *ZERO_D, 0)
            nf = hm_lau(nf, *ZERO_D, 0)
        else:
            for _ in range(3):
                nf = hm_lau(nf, *ZERO_D, 0)
                nf = hm_lau(nf, *MINUS_H, 1)
            nf = hm_lau(nf, *MINUS_H_HALF, 0)
            nf = hm_lau(nf, *MINUS_H_HALF, 0)
            nf = hm_lau(nf, *MINUS_H, 1)
            nf = hm_lau(nf, *ZERO_D, 0)
            nf = hm_lau(nf, *ZERO_D, 0)
        for prev in range(k):
            if not keep(prev, k):
                continue
            ti, tj = o[prev], o[k]
            if ti == "p" and tj == "p":
                nf = hm_lau(nf, *ZERO_D, 0)
            elif ti == "n" and tj == "n":
                nf = hm_lau(nf, *MINUS_H, 0)
            else:
                nf = hm_lau(nf, *MINUS_H_HALF, 0)
    for _ in range(Z):
        nf = hm_lau(nf, *MINUS_H, 1)
    return nf


def _first_m(m: int):
    """Keep the first ``m`` bonds in the construction's own lay order."""
    seen = [0]

    def keep(_prev: int, _k: int) -> bool:
        seen[0] += 1
        return seen[0] <= m
    return keep


def _grade_terms(nf) -> list[int]:
    t = [0] * (MAX_GRADE + 1)
    for i, c in enumerate(nf):
        t[GRADE[i]] += len(c)
    return t


def saturation_walk() -> list[dict]:
    """How many crossings before all 4 grades are populated?

    The ceiling is not 4-by-convention: the support GROWS 1 -> 2 -> 3 -> 4
    with word length and then never grows again, however many bonds follow.
    """
    nf = [lau_one(), {}, {}, {}, {}, {}]
    out = []
    for i in range(MAX_GRADE + 1):
        t = _grade_terms(nf)
        out.append({"crossings": i,
                    "support": [g for g in range(MAX_GRADE + 1) if t[g] > 0],
                    "terms_by_grade": t})
        nf = hm_lau(nf, *MINUS_H_HALF, i % 2)
    return out


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--max-A", type=int, default=20)
    ap.add_argument("--bond-max-Z", type=int, default=4,
                    help="bond sweep runs every Z, N <= this")
    a = ap.parse_args()
    t0 = time.time()

    print("=== the ceiling (unconditional arithmetic) ===", flush=True)
    print(f"  H_3 quotient jet grades: 0..{MAX_GRADE}  ({MAX_GRADE + 1} grades)", flush=True)
    for A in (2, 4, 8, 20):
        print(f"  full H_{{3A}} at A={A:>2}: max Coxeter length C({3*A},2) = "
              f"{comb(3*A, 2):>4}", flush=True)

    rows = []
    print(f"\n=== exhaustive scan, A = 2..{a.max_A} ===", flush=True)
    for A in range(2, a.max_A + 1):
        for Z in range(A, -1, -1):
            N = A - Z
            t, f = jet_shape(Z, N)
            rows.append({"A": A, "Z": Z, "N": N,
                         "any_magic": (Z in MAGIC) or (N in MAGIC),
                         "terms_by_grade": t,
                         "shape": [str(x) for x in f],
                         "_f": f})
        print(f"  A={A} done ({A+1} configurations)", flush=True)

    print("\n=== per-level separation, with its own null rate ===", flush=True)
    per_level = {}
    observed = 0
    expected = Fraction(0)
    for A in range(2, a.max_A + 1):
        lv = [r for r in rows if r["A"] == A]
        mg = [r for r in lv if r["any_magic"]]
        nm = [r for r in lv if not r["any_magic"]]
        if not mg or not nm:
            continue
        p = null_rate(len(mg), len(nm))
        dirs = []
        for g in range(MAX_GRADE + 1):
            mv = [r["_f"][g] for r in mg]
            nv = [r["_f"][g] for r in nm]
            d = ("magic_above" if min(mv) > max(nv)
                 else "magic_below" if max(mv) < min(nv) else "interleaved")
            dirs.append(d)
            if d != "interleaved":
                observed += 1
        expected += p * (MAX_GRADE + 1)
        per_level[A] = {"n_magic": len(mg), "n_non_magic": len(nm),
                        "null_p_per_observable": str(p), "directions": dirs}
        if any(d != "interleaved" for d in dirs):
            print(f"  A={A:<2} {len(mg)}v{len(nm)}  P={float(p):.3f}/obs  {dirs}",  # float64-ok: stdout display of exact Fraction
                  flush=True)

    print(f"\n  observed clean separations : {observed}", flush=True)
    print(f"  expected under the null    : {float(expected):.2f}", flush=True)  # float64-ok: stdout display of exact Fraction

    print("\n=== cross-level replication per grade ===", flush=True)
    replication = {}
    for g in range(MAX_GRADE + 1):
        hits = {A: v["directions"][g] for A, v in per_level.items()
                if v["directions"][g] != "interleaved"}
        vals = set(hits.values())
        contradictory = ("magic_above" in vals) and ("magic_below" in vals)
        replication[str(g)] = {"separating_levels": {str(k): v for k, v in hits.items()},
                               "contradictory": contradictory,
                               "consistent": len(vals) == 1 and bool(hits)}
        print(f"  grade {g}: {hits or 'none'}   CONTRADICTORY={contradictory}",
              flush=True)

    spreads = {}
    for g in range(MAX_GRADE + 1):
        v = [r["_f"][g] for r in rows]
        spreads[str(g)] = {"min": str(min(v)), "max": str(max(v))}
        print(f"  grade {g} range over all {len(rows)} configs: "
              f"{float(min(v)):.4f} .. {float(max(v)):.4f}", flush=True)  # float64-ok: stdout display of exact Fraction

    any_consistent = any(v["consistent"] for v in replication.values())
    print(f"\n  ANY grade replicating across levels: {any_consistent}", flush=True)

    # ── is this grading the bond-product grading? ─────────────────────────
    print("\n=== grading identification: vary the BOND SET ===", flush=True)

    print("  control: keep-all must reproduce the canonical builder", flush=True)
    ctrl_n, ctrl_ok = 0, True
    for Z in range(0, a.bond_max_Z + 1):
        for N in range(0, a.bond_max_Z + 1):
            if Z + N == 0:
                continue
            ctrl_n += 1
            if build_atom_nf_bonds(Z, N, lambda p, k: True) != build_atom_nf_lau(Z, N):
                ctrl_ok = False
                print(f"    MISMATCH at Z={Z} N={N}", flush=True)
    print(f"    identical on all {ctrl_n} configurations: {ctrl_ok}", flush=True)

    sat = saturation_walk()
    print("  support growth (the ceiling is REACHED, not assumed):", flush=True)
    for s in sat:
        print(f"    after {s['crossings']} crossings: support {s['support']}"
              f"  terms {s['terms_by_grade']}", flush=True)

    sweep_rows, sweep_seen, collisions = [], {}, []
    for Z in range(0, a.bond_max_Z + 1):
        for N in range(0, a.bond_max_Z + 1):
            A = Z + N
            if A < 2:
                continue
            for m in range(0, comb(A, 2) + 1):
                t = _grade_terms(build_atom_nf_bonds(Z, N, _first_m(m)))
                tot = sum(t)
                sh = tuple(Fraction(x, tot) for x in t)
                sup = [g for g in range(MAX_GRADE + 1) if t[g] > 0]
                sweep_rows.append({"Z": Z, "N": N, "bonds_kept": m,
                                   "bonds_total": comb(A, 2),
                                   "support": sup, "terms_by_grade": t,
                                   "shape": [str(x) for x in sh]})
                if sh in sweep_seen:
                    collisions.append({"config": [Z, N, m],
                                       "collides_with": list(sweep_seen[sh])})
                else:
                    sweep_seen[sh] = (Z, N, m)

    sup_always_full = all(len(r["support"]) == MAX_GRADE + 1 for r in sweep_rows)
    z2n2 = [r for r in sweep_rows if r["Z"] == 2 and r["N"] == 2]
    z2n2_distinct = len({tuple(r["shape"]) for r in z2n2})
    print(f"  bond sweep: {len(sweep_rows)} configurations, "
          f"{len(sweep_seen)} distinct shapes, {len(collisions)} collisions",
          flush=True)
    print(f"  at Z=2,N=2: {z2n2_distinct} distinct shapes for "
          f"{len(z2n2)} bond counts", flush=True)
    print(f"  support is all 4 grades at EVERY bond count: {sup_always_full}",
          flush=True)
    print(f"  H_3 grades {MAX_GRADE + 1} vs bond-product grades at A=4: "
          f"{comb(4, 2) + 1}, at A=20: {comb(20, 2) + 1}"
          "  -> different cardinality, no bijection", flush=True)

    for r in rows:
        r.pop("_f", None)
    payload = {
        "probe": "gs_filtration_jet_shape_magic",
        "question": "does the Groebner-Shirshov filtration grading -- the jet "
                    "vertical degree, indexed by Coxeter length of the normal-"
                    "form word -- separate magic from non-magic nucleon "
                    "configurations?",
        "why_distinct_from_q_degree": "symbolic_nf_q_degree_magic_probe measured "
                                      "degree in q; this measures the filtration "
                                      "by NF word length, a different grading",
        "ceiling": {
            "h3_quotient_grades": MAX_GRADE + 1,
            "full_tower_max_coxeter_length": {str(A): comb(3 * A, 2)
                                              for A in range(2, a.max_A + 1)},
            "note": "unconditional arithmetic; NOT an exclusion of many-body "
                    "structure. The GS word-length grading is NOT the "
                    "bond-product grading -- see grading_identification: "
                    "different cardinality (4 vs C(A,2)+1) and the folding is "
                    "many-to-one on bond count. "
                    "QOU.Mass.BodyOrderJetGrading.body_eq_graded IS discharged "
                    "for the bond-product model by "
                    "body_eq_graded_of_bond_product; an earlier draft of this "
                    "probe wrongly called it assumed, and wrongly claimed the "
                    "two models index in opposite directions (the complement "
                    "bijection esymm_eq_compl_sum absorbs that).",
        },
        "grading_identification": {
            "question": "is the GS word-length filtration (0..3) identifiable "
                        "with the bond-product / Mayer grading (0..|s|)?",
            "answer": "no -- different cardinality, and the folding loses "
                      "bond count",
            "control_keep_all_reproduces_canonical_builder": ctrl_ok,
            "control_configurations": ctrl_n,
            "h3_grades": MAX_GRADE + 1,
            "bond_product_grades": {str(A): comb(A, 2) + 1
                                    for A in (2, 4, 8, 20)},
            "saturation_walk": sat,
            "support_full_at_every_bond_count": sup_always_full,
            "bond_sweep_configurations": len(sweep_rows),
            "bond_sweep_distinct_shapes": len(sweep_seen),
            "bond_sweep_collisions": len(collisions),
            "z2n2_distinct_shapes": z2n2_distinct,
            "z2n2_bond_counts": len(z2n2),
            "collisions": collisions,
            "rows": sweep_rows,
        },
        "control": "exhaustive at each level: every Z in 0..A",
        "arithmetic": "exact over Q (fractions.Fraction); no float, no "
                      "evaluation at any numerical q",
        "configurations": rows,
        "per_level": {str(k): v for k, v in per_level.items()},
        "observed_clean_separations": observed,
        "expected_under_null": str(expected),
        "cross_level_replication": replication,
        "grade_ranges": spreads,
        "any_grade_replicates": any_consistent,
    }
    try:
        from qou_substrate.witness import WitnessBuilder
        wb = WitnessBuilder.wrap_legacy(
            "gs-filtration-jet-shape-magic", payload,
            script_path=__file__, engine="python+fractions",
            output_dir=os.path.dirname(os.path.abspath(__file__)),
            start_time=t0,
        )
        wb.add_assertion("h3_quotient_jet_grades",
                         computed=str(MAX_GRADE + 1), expected="4")
        # The control, not the verdict: if keep-all ever stops reproducing the
        # canonical builder, the whole bond sweep is measuring a lookalike.
        wb.add_assertion("bond_sweep_control_reproduces_canonical_builder",
                         computed=str(ctrl_ok), expected="True")
        wb.add_assertion("h3_grades_vs_bond_product_grades_at_A4",
                         computed=f"{MAX_GRADE + 1} vs {comb(4, 2) + 1}",
                         expected="4 vs 7")
        wb.add_assertion("bond_sweep_distinct_shapes_over_configurations",
                         computed=str(0 < len(sweep_seen) < len(sweep_rows)),
                         expected="True")
        wb.add_assertion("z2n2_shapes_over_bond_counts",
                         computed=str(0 < z2n2_distinct < len(z2n2)),
                         expected="True")
        for A, exp_grade in ((2, 15), (20, 1770)):
            wb.add_assertion(f"full_tower_max_grade_at_A{A}",
                             computed=str(comb(3 * A, 2)),
                             expected=str(exp_grade))
        for A, v in per_level.items():
            wb.add_assertion(f"both_groups_non_empty_at_A{A}",
                             computed=str(v["n_magic"] > 0 and v["n_non_magic"] > 0),
                             expected="True")
        out = wb.save(extra={"auditOnly": True})
        print(f"\nWrote {out}", flush=True)
    except Exception as exc:  # pragma: no cover
        print(f"\n(witness not written: {exc})", flush=True)
    return 0


if __name__ == "__main__":
    sys.exit(main())
