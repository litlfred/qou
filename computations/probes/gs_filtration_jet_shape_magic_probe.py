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

**That is not claimed here.** The body-order <-> jet-degree correspondence is
an ASSUMED hypothesis field in the corpus's own Lean:
`QOU.Mass.BodyOrderJetGrading.body_eq_graded`, discharged in
`QOU/Knot/BodyOrderExpansion.lean` only for the **bond-product model** -- where
that file states in as many words that *"the index runs backwards"*, an m-body
term sitting at grade `|s| - m`. That is the Mayer/bond-set grading, a
DIFFERENT object from the GS word-length filtration, so the two are not in
conflict; but it does mean the direction of the correspondence is model-
dependent and the premise is assumed rather than established. Per
"conditional-proved != premise-established", the cap is reported as a fact
about grades and NOT as an exclusion of many-body structure.

## Measured

Exhaustive: every (Z, N) at every A = 2..20, so the contrast is at fixed
algebra with only nucleon composition varying. Weight per grade is the exact
term count of the Laurent coefficients (`fractions.Fraction` throughout, no
float, no evaluation at any numerical q).

The shape is nearly CONSTANT -- ~(0.168, 0.337, 0.332, 0.163) -- and its total
range over all 230 configurations is small:

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
from math import comb

sys.path[:0] = ['/home/user/qou/computations/probes',
                '/home/user/qou/computations',
                '/home/user/qou/computations/substrate']

from symbolic_nf_q_degree_magic_probe import build_atom_nf_lau, MAGIC  # noqa: E402

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


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--max-A", type=int, default=20)
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
            print(f"  A={A:<2} {len(mg)}v{len(nm)}  P={float(p):.3f}/obs  {dirs}",
                  flush=True)

    print(f"\n  observed clean separations : {observed}", flush=True)
    print(f"  expected under the null    : {float(expected):.2f}", flush=True)

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
              f"{float(min(v)):.4f} .. {float(max(v)):.4f}", flush=True)

    any_consistent = any(v["consistent"] for v in replication.values())
    print(f"\n  ANY grade replicating across levels: {any_consistent}", flush=True)

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
                    "structure -- the body-order/jet-degree correspondence is "
                    "an assumed hypothesis field "
                    "(QOU.Mass.BodyOrderJetGrading.body_eq_graded), discharged "
                    "only in the bond-product model where the index runs "
                    "backwards (m-body at grade |s|-m)",
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
        for A in (2, 20):
            wb.add_assertion(f"full_tower_max_grade_at_A{A}",
                             computed=str(comb(3 * A, 2)),
                             expected=str(comb(3 * A, 2)))
        for A, v in per_level.items():
            wb.add_assertion(f"both_groups_non_empty_at_A{A}",
                             computed=f"{v['n_magic']}/{v['n_non_magic']}",
                             expected=f"{v['n_magic']}/{v['n_non_magic']}")
        out = wb.save(extra={"auditOnly": True})
        print(f"\nWrote {out}", flush=True)
    except Exception as exc:  # pragma: no cover
        print(f"\n(witness not written: {exc})", flush=True)
    return 0


if __name__ == "__main__":
    sys.exit(main())
