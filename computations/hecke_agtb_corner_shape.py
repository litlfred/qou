#!/usr/bin/env python3
"""hecke_agtb_corner_shape — the `a > b` corner is EASIER, not parallel.

`CornerLe.prefixChain{,₁,₂,₃}` prove the Bokut–Shiao corner's `a ≤ b` prefix
for every `a`. The obvious next front is `a > b`, and this arc's PR body and
its own follow-up notes described that as *"a new construction, not an
extension"* — asserted from the fact that `trio`'s `hj₂ : j₂ ≤ j₁` cannot
instantiate there. That is true and it is **not** the useful statement.
Measured, `a > b` is *strictly easier* than `a ≤ b`:

  * the S-polynomial reduces **completely to zero** — 10/10 cases. `a ≤ b`
    ends its prefix at a *partial* cancellation with two terms surviving; here
    there is no residue at all;
  * the element **never exceeds two terms**, because the chain uses **no
    quadratic step**. `Q` (`σ² = hσ + 1`) is the only rule that splits one term
    into two, so with zero `Q`s the whole 4-term apparatus this arc built —
    `quadPair`, `trio`, `TOpen`, `ofTerms_cancel_split` — is unnecessary;
  * the step count is `b² + 3b + 5` and **does not depend on `a` at all**
    (9 steps for every `b = 1`, whatever `a` is).

So the two regimes are not two parallel builds. `a ≤ b` is the hard one and is
done; `a > b` is a 2-term convergence over `monicStep` / `bsStep` /
`farComm_transport_left_sources`, ending at the zero element.

They are related, which the "new construction" framing also understated. The
cancellation word is the **same shape at the other bottom**:

    a ≤ b :  WStar = bsWord₂ i₂ i₁ j₁       ++ descWord i j₂
    a > b :          bsWord₂ i₂ i₁ (j₂ − 1) ++ descWord i j₁

— the same two-run shape with the **bottoms swapped** (and the first shifted by
one). I first wrote that middle run as `descWord i₂ j₁`, which is right exactly
when `b = a − 1` or `b = 1` — every case a quick eyeball lands on. Extending the
sweep to `a = 6` broke it, and this probe's own assertion caught it before it
reached a durable artifact. Both counts are quadratic in `min(a, b)` —
`m² + m + 5` for `m = a ≤ b`, `m² + 3m + 5` for `m = b < a`. They differ by
`2m`, so they do **not** meet on the diagonal; the diagonal belongs to `a ≤ b`.

Method note. This probe runs to the first cancellation AND to the normal form,
and reports both, because in this arc a claim measured to a normal form was
once written up as a claim about the prefix (see the correction in
`hecke_small_a_decomposition.py`). Here the two coincide — the first
cancellation IS the end — and that coincidence is itself the finding, so it is
measured rather than assumed.

All arithmetic is exact (sympy rationals in `q`); nothing here touches a float.

Emits `hecke-agtb-corner-shape.witness.json`. Bean qou-auq3.
"""
from __future__ import annotations
import importlib.util, sys, time
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE)); sys.path.insert(0, str(HERE / "substrate"))

from witness_base import WitnessBuilder  # noqa: E402

_cl = importlib.util.spec_from_file_location(
    "cl", HERE / "hecke_closing_from_topen.py")
cl = importlib.util.module_from_spec(_cl); _cl.loader.exec_module(cl)
# one engine instance, shared -- a second load returns a FRESH module with an
# untuned rule table (see the note at that file's own import)
ts, cov, eng, dw = cl.ts, cl.cov, cl.eng, cl.dw


def main():
    started = time.monotonic()
    rows = []
    for a in range(2, 7):
        for b in range(1, a):
            n, i = a + b + 6, a + b + 3
            if i - a < 0 or i >= n:
                continue
            cov.retune(n)
            ids = cov.rule_ids(n)
            j1, j2, i1, i2 = i - a, i - b, i - 1, i - 2
            rel = lambda w: [i - x for x in w]

            f = cov.start_element(i, a, b)
            prev, kinds, counts = set(f), [], [len(f)]
            first_cancel_at, cancelled = None, None
            for _ in range(200):
                t = ts.next_redex(f)
                if t is None:
                    break
                w, name, _kk = t
                f2, img = ts.apply(f, t)
                gone = [u for u in img if u != w and u in prev and u not in f2]
                kinds.append(ids.get(name)[0])
                f, prev = f2, set(f2)
                counts.append(len(f))
                if gone and first_cancel_at is None:
                    first_cancel_at, cancelled = len(kinds), gone[0]

            # `bsWord2 i2 i1 (j2-1) ++ descWord i j1`.  NOT `descWord i2 j1`
            # in the middle: that agrees only when b = a-1 (and at b = 1),
            # which is every case a quick eyeball happens to land on.
            target = (i2, i1) + dw(i2, j2 - 1) + (i,) + dw(i1, j1)
            WStar = (i2, i1) + dw(i2, j1) + (i,) + dw(i1, j2)
            rows.append({
                "a": a, "b": b, "i": i, "n": n,
                "steps_to_normal_form": len(kinds),
                "steps_to_first_cancellation": first_cancel_at,
                "first_cancellation_is_the_end":
                    first_cancel_at == len(kinds),
                "b_formula_b2_plus_3b_plus_5": b * b + 3 * b + 5,
                "matches_b_formula": len(kinds) == b * b + 3 * b + 5,
                "a_le_b_formula_a2_plus_a_plus_5": a * a + a + 5,
                "matches_a_le_b_formula": len(kinds) == a * a + a + 5,
                "schedule": "".join(kinds),
                "quadratic_steps": kinds.count("Q"),
                "max_terms": max(counts),
                "final_terms": len(f),
                "reduces_to_zero": len(f) == 0,
                "cancelled_rel_i": rel(cancelled) if cancelled else None,
                "cancelled_is_bsWord2_j2m1_plus_descWord_i_j1":
                    cancelled == target,
                "middle_run_bottom_rel_i": i - (j2 - 1),
                "b_eq_a_minus_1": b == a - 1,
                "cancelled_is_WStar_at_j2": cancelled == WStar,
            })

    w = WitnessBuilder("hecke-agtb-corner-shape", engine="sympy",
                       start_time=started)
    w.add_parameter("scope", "a > b, i.e. j1 < j2; a in 2..6, b in 1..a-1")
    w.add_parameter(
        "why", "the a > b corner was described in a PR body and a follow-up "
        "note as 'a new construction, not an extension', asserted from trio's "
        "hj2 not instantiating and never measured; measured, it is strictly "
        "EASIER than a <= b, not parallel to it")
    w.add_assertion(
        "cases_whose_S_polynomial_does_NOT_reduce_to_zero",
        computed=str(sum(0 if r["reduces_to_zero"] else 1 for r in rows)),
        expected="0")
    w.add_assertion(
        "cases_using_ANY_quadratic_step",
        computed=str(sum(1 if r["quadratic_steps"] else 0 for r in rows)),
        expected="0")
    w.add_assertion(
        "cases_where_the_element_EXCEEDS_two_terms",
        computed=str(sum(1 if r["max_terms"] > 2 else 0 for r in rows)),
        expected="0")
    w.add_assertion(
        "cases_whose_step_count_does_NOT_match_b2_plus_3b_plus_5",
        computed=str(sum(0 if r["matches_b_formula"] else 1 for r in rows)),
        expected="0")
    w.add_assertion(
        "cases_whose_step_count_DOES_match_the_a<=b_formula",
        computed=str(sum(1 if r["matches_a_le_b_formula"] else 0
                         for r in rows)), expected="0")
    w.add_assertion(
        "cases_whose_first_cancellation_is_NOT_the_end_of_the_chain",
        computed=str(sum(0 if r["first_cancellation_is_the_end"] else 1
                         for r in rows)), expected="0")
    w.add_assertion(
        "cases_whose_cancelled_word_is_NOT_bsWord2_i2_i1_j2m1_++_descWord_i_j1",
        computed=str(sum(0 if r["cancelled_is_bsWord2_j2m1_plus_descWord_i_j1"]
                         else 1 for r in rows)), expected="0")
    w.add_assertion(
        "cases_whose_cancelled_word_IS_WStar_at_j2_the_a<=b_target",
        computed=str(sum(1 if r["cancelled_is_WStar_at_j2"] else 0
                         for r in rows)), expected="0")
    w.add_data("cases_checked", len(rows))
    w.add_data("cases", rows)
    w.add_caveat(
        "Step counts are the DEG-LEX schedule's. The Lean is not obliged to "
        "that order -- both a = 1 and the a <= b opening phase reorder it -- "
        "so a Lean chain may group these steps differently. What transfers is "
        "the count, the absence of quadratic steps, and the target word.")
    w.add_caveat(
        "'Easier' is measured as: fewer terms (2 vs 4), no quadratic step, and "
        "a complete rather than partial cancellation. It is NOT a claim that "
        "the Lean will be short -- the a <= b transports were the bulk of that "
        "work and the b-dependent runs here are longer, up to 33 steps at "
        "b = 4. The claim is that the 4-term cancellation apparatus is not "
        "needed, not that nothing is.")
    path = w.save({
        "q0Anchor": "independent",
        "q0AnchorReason":
            "Grobner-Shirshov rewriting in the Hecke algebra over the FORMAL "
            "parameter h = q - q^-1 (a sympy Symbol). The reduction is "
            "combinatorial in the braid word and its coefficients are rational "
            "functions of that symbol; no substrate q0 is read anywhere in the "
            "import cone (verified: no qou_substrate constants import, no "
            "q_parameter / q_at / Q_50_DIGIT reference, in this file or in "
            "hecke_gs_confluence_n4.py which supplies the rule table).",
    })
    print(f"witness -> {path}")
    for r in rows:
        print(f"a={r['a']} b={r['b']}: {r['steps_to_normal_form']:2} steps "
              f"(b^2+3b+5 = {r['b_formula_b2_plus_3b_plus_5']}, "
              f"match {r['matches_b_formula']})  Qs {r['quadratic_steps']}"
              f"  maxTerms {r['max_terms']}  ZERO {r['reduces_to_zero']}")
        print(f"     {r['schedule']}")
        print(f"     cancelled {r['cancelled_rel_i']}"
              f"  = bsWord2 i2 i1 (j2-1) ++ descWord i j1: "
              f"{r['cancelled_is_bsWord2_j2m1_plus_descWord_i_j1']}")
    print(f"\n{len(rows)} cases measured")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
