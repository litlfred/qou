#!/usr/bin/env python3
"""hecke_gs_confluence_range — is the Bokut–Shiao-completed Hecke rewriting
system confluent at every rank up to `n = 12`, and what is the shape of the
hardest family?

`hecke_gs_confluence_n4.py` answers the confluence question at `n = 4`, the rank
the Lean development enumerates by `decide`. Its own caveat says "n = 4 only.
Bokut & Shiao's theorem is for all n, and nothing here bears on n > 4." This
script removes that caveat as far as computation can: it runs the same engine at
every rank from 2 to 12 and finds no failing composition anywhere.

It also answers a question the Lean side ran into. `UGB.GrobnerShirshov.HeckeCompletion`
proves all 92 compositions at `n = 4`, and every family general in `n` **except**
the four "corner" cases, where both rules are Bokut–Shiao at general depth. Those
four are proved at fixed depths `(a,b) ∈ {(2,2),(3,2),(2,3),(3,3)}`, and it was
not clear what a general treatment would have to look like. Writing
`a = i − j₁` and `b = i − j₂` for the two depths, this script measures the corner
across ranks and finds it splits into **two regimes**:

    a ≤ b :  2ab − a² + 5a + 1 steps,  and the quadratic rule is used twice
    a > b :  b² + 3b + 5     steps,  and the quadratic rule is not used at all

Both are exact across every rank and every `i` tested. The `a > b` regime does
not depend on `a` at all — extra depth in the first rule adds no work — which is
why `(3,2)`, `(4,2)` and `(5,2)` are all fifteen steps. The chain length is
therefore *quadratic* in the depths, so no fixed script can cover the corner and
a general proof needs an induction on both depths with the two regimes separated.

A corollary the script checks: the longest chain at rank `n` is always the
deepest corner, `a = b = n − 1`, giving `n² + 3n − 3` — matching the observed
maximum at every rank.

## Method and faithfulness

The rule set, the S-polynomial conventions and the reduction strategy are
`hecke_gs_confluence_n4`'s, imported unchanged and re-parametrised by rank; see
that script's docstring for the correspondence with the Lean declarations.
Exact over ℤ[h] with `h = q − q⁻¹` a free symbol; no float is ever formed.

Emits `hecke-gs-confluence-range.witness.json`. Bean qou-auq3.
"""

from __future__ import annotations

import importlib.util
import sys
import time
from pathlib import Path

import sympy as sp

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
sys.path.insert(0, str(HERE / "substrate"))

from witness_base import WitnessBuilder  # noqa: E402

_spec = importlib.util.spec_from_file_location(
    "hecke_gs_confluence_n4", HERE / "hecke_gs_confluence_n4.py")
eng = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(eng)

N_MAX = 12


def retune(n: int) -> None:
    """Re-parametrise the imported engine to rank `n`."""
    eng.N = n
    eng.RULES = eng.build_rules()
    eng.LM = {name: lm for name, _, lm in eng.RULES}
    eng.REL = {name: rel for name, rel, _ in eng.RULES}
    eng.LC = {name: eng.REL[name][eng.LM[name]] for name in eng.LM}


def corner_chain(i: int, a: int, b: int):
    """The Bokut–Shiao × Bokut–Shiao composition at depths `a`, `b` below `i`.

    Returns `(steps, quadratic_steps, reduces_to_zero)`.
    """
    j1, j2 = i - a, i - b
    d1 = eng.desc_word(i, j1)
    e2 = eng.desc_word(i - 1, j2)
    n1 = f"B{i - 1}{i}{j1}"
    n2 = f"B{i - 1}{i}{j2}"
    s = eng.combine(
        {w: eng.LC[n2] * c
         for w, c in eng.context_mul((), eng.REL[n1], e2 + (i,)).items()},
        {w: eng.LC[n1] * c
         for w, c in eng.context_mul(d1, eng.REL[n2], ()).items()},
        -1)
    nf, chain = eng.reduce_to_normal_form(dict(eng.clean(s)))
    quad = sum(1 for step in chain if step[1][0] == "Q")
    return len(chain), quad, not eng.clean(nf)


def corner_predicted(a: int, b: int) -> tuple:
    """`(steps, quadratic_steps)` predicted by the two-regime formulas."""
    if a <= b:
        return 2 * a * b - a * a + 5 * a + 1, 2
    return b * b + 3 * b + 5, 0


def run() -> dict:
    ranks = []
    for n in range(2, N_MAX + 1):
        retune(n)
        res = eng.run()
        ov, inc = res["overlap"], res["inclusion"]
        ranks.append({
            "n": n,
            "rules": len(eng.RULES),
            "leading_monomials": len(res["words"]),
            "overlap_shapes": len(res["shapes"]),
            "overlap_compositions": len(ov),
            "inclusion_compositions": len(inc),
            "overlap_failing": sum(1 for x in ov if not x["reduces_to_zero"]),
            "inclusion_failing": sum(1 for x in inc if not x["reduces_to_zero"]),
            "total_steps": sum(x["steps"] for x in ov),
            "max_chain": max((x["steps"] for x in ov), default=0),
            "max_chain_predicted": n * n + 3 * n - 3,
        })

    corner = []
    for n in range(5, 10):
        retune(n)
        for i in range(3, n):
            for a in range(2, i + 1):
                for b in range(2, i + 1):
                    steps, quad, ok = corner_chain(i, a, b)
                    p_steps, p_quad = corner_predicted(a, b)
                    corner.append({
                        "n": n, "i": i, "a": a, "b": b,
                        "steps": steps, "quadratic_steps": quad,
                        "predicted_steps": p_steps, "predicted_quadratic": p_quad,
                        "reduces_to_zero": ok,
                    })
    return {"ranks": ranks, "corner": corner}


def main() -> int:
    started = time.monotonic()
    r = run()
    ranks, corner = r["ranks"], r["corner"]

    failing = sum(x["overlap_failing"] + x["inclusion_failing"] for x in ranks)
    max_chain_mismatch = sum(
        1 for x in ranks if x["n"] >= 3 and x["max_chain"] != x["max_chain_predicted"])
    corner_bad = sum(1 for x in corner if not x["reduces_to_zero"])
    corner_step_mismatch = sum(
        1 for x in corner if x["steps"] != x["predicted_steps"])
    corner_quad_mismatch = sum(
        1 for x in corner if x["quadratic_steps"] != x["predicted_quadratic"])

    w = WitnessBuilder("hecke-gs-confluence-range", engine="sympy",
                       start_time=started)
    w.set_description(
        "Every overlap and inclusion composition of the Bokut-Shiao-completed "
        "Hecke rewriting system reduces to zero at every rank from 2 to 12, and "
        "the Bokut-Shiao-against-Bokut-Shiao corner obeys two exact "
        "closed-form regimes in the two depths. Exact over Z[h], "
        "h = q - q^-1; no float is formed."
    )

    w.add_parameter("n_min", 2)
    w.add_parameter("n_max", N_MAX)
    w.add_parameter("deformation_symbol", "h = q - q^{-1}")
    w.add_parameter("lean_module", "UGB.GrobnerShirshov.HeckeCompletion")
    w.add_parameter("corner_formula_a_le_b", "2ab - a^2 + 5a + 1 steps, 2 quadratic")
    w.add_parameter("corner_formula_a_gt_b", "b^2 + 3b + 5 steps, 0 quadratic")

    w.add_assertion("compositions_failing_to_reduce_any_rank",
                    computed=str(failing), expected="0")
    w.add_assertion("max_chain_differs_from_n2_plus_3n_minus_3",
                    computed=str(max_chain_mismatch), expected="0")
    w.add_assertion("corner_compositions_failing_to_reduce",
                    computed=str(corner_bad), expected="0")
    w.add_assertion("corner_step_count_differs_from_formula",
                    computed=str(corner_step_mismatch), expected="0")
    w.add_assertion("corner_quadratic_count_differs_from_formula",
                    computed=str(corner_quad_mismatch), expected="0")

    w.add_data("ranks", ranks)
    w.add_data("corner_cases_checked", len(corner))
    w.add_data("corner", corner)

    w.add_caveat(
        "Computational witness, not a proof. It establishes that the "
        "obligation set is discharge-able at every rank tested and measures the "
        "shape of the corner family; it proves nothing for n > 12, and the "
        "closed forms are fitted-and-checked, not derived."
    )
    w.add_caveat(
        "The rule set, S-polynomial conventions and reduction strategy are "
        "imported unchanged from hecke_gs_confluence_n4.py; faithfulness to the "
        "Lean definitions rests on that script's docstring table, checked by "
        "inspection rather than mechanically."
    )

    path = w.save()

    print(f"{'n':>3} {'rules':>6} {'overlap':>8} {'incl':>5} {'fail':>5} "
          f"{'maxchain':>9} {'predicted':>10}")
    for x in ranks:
        print(f"{x['n']:>3} {x['rules']:>6} {x['overlap_compositions']:>8} "
              f"{x['inclusion_compositions']:>5} "
              f"{x['overlap_failing'] + x['inclusion_failing']:>5} "
              f"{x['max_chain']:>9} {x['max_chain_predicted']:>10}")
    print(f"corner cases checked           : {len(corner)}  "
          f"failing: {corner_bad}  step mismatches: {corner_step_mismatch}  "
          f"quadratic mismatches: {corner_quad_mismatch}")
    print(f"witness -> {path}")
    bad = failing or corner_bad or corner_step_mismatch or corner_quad_mismatch \
        or max_chain_mismatch
    return 0 if not bad else 1


if __name__ == "__main__":
    raise SystemExit(main())
