#!/usr/bin/env python3
"""hecke_small_a_decomposition — what `a = 1` and `a = 2` need, measured.

`CornerLe.prefixChain` and `prefixChain₃` prove the corner's `a ≤ b` prefix for
`a ≥ 3`. `oc` requires only `j₁ ≤ i₁`, i.e. `a ≥ 1`, so `a = 1` and `a = 2` are
valid corners in this regime and were not covered.

**CORRECTION (supersedes this probe's first version).** The first version
measured where the `a = 2` U lineage *ends* — its normal form — and reported
that as the prefix's U endpoint. It is not. The normal form is reached well
past the first cancellation, and the prefix never gets there: the U branch that
the first version followed is not even touched before the prefix ends. The
conclusion drawn from it, *"neither route nor target transfers, so `a = 2` is a
construction and not a substitution"*, was **wrong about the prefix**. Measured
to the first cancellation instead:

  * the prefix is **11 steps for every `b`**, and `a² + a + 5 = 11` — the
    general count formula holds at `a = 2`;
  * so does the phase split, `a² − 3a + 9 = 7` and `4(a − 1) = 4`;
  * the closing phase is the **same three calls** as `a ≥ 3` — `fRun`,
    `closingBs`, `fRun` — landing on the **same word**, `WStar`.

`CornerLe.prefixChain₂` now proves it, and `prefixChain₁` proves `a = 1`, so
the corner's `a ≤ b` prefix is proved for **every** `a`. This is the fourth
time in this arc that
a structural claim went into a durable artifact having been measured against
the wrong question, so the check is stated as a question this time: run to the
first cancellation, not to a normal form.

What it establishes, per case:

  * **the prefix's length and phase split**, against `a² + a + 5` and its two
    halves;
  * **the rule-kind schedule**, and for `a = 2` the closing schedule `FBYF`;
  * **the cancellation word**, against `WStar` built from the Lean definition;
  * **source-only at every step** — `monicStep`'s `hne`, the hypothesis the
    `_sources` relaxations actually need;
  * whether `quadPair`'s redex is already in `U0`, which is the structural
    reason `a = 2` needs no loop;
  * whether the Bokut–Shiao rule at `j = i′` **is** Yang–Baxter, which is why
    `closingBs`'s second step appears in the trace under the name `Y`.

All arithmetic is exact (sympy rationals in `q`); nothing here touches a float.

Emits `hecke-small-a-decomposition.witness.json`. Bean qou-auq3.
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


def run_to_first_cancellation(f, ids, cap=60):
    """Reduce under deg-lex until a word that was already carried is landed on
    and leaves the support.  Returns (steps, elem, cancelled-word).

    A cancellation is NOT a drop in the term count: a far-commutation is
    2-word and a quadratic 3-word, so counting terms fires on ordinary steps.
    It is a word the step lands on that was already there and then goes."""
    prev, script = set(f), []
    for _ in range(cap):
        t = ts.next_redex(f)
        if t is None:
            return script, f, None
        w, name, kk = t
        others = [u for u in f if u != w]
        f2, img = ts.apply(f, t)
        gone = [u for u in img if u != w and u in prev and u not in f2]
        script.append({"rule": list(ids.get(name)), "src_only": w not in others})
        f, prev = f2, set(f2)
        if gone:
            return script, f, gone[0]
    return script, f, None


def main():
    started = time.monotonic()
    rows = []
    for a in (1, 2):
        for b in (a, a + 1, a + 2, a + 3):
            n, i = a + b + 6, a + b + 3
            if i - b < 0 or i >= n:
                continue
            cov.retune(n)
            j1, j2, i1, i2 = i - a, i - b, i - 1, i - 2
            jp, jpp, jm = j1 + 1, j1 + 2, j1 - 1
            ids = cov.rule_ids(n)
            rel = lambda w: [i - x for x in w]

            f = cov.start_element(i, a, b)
            t0 = sorted(f, key=eng.deglex_key)
            V0, U0 = t0[0], t0[1]
            script, _end, cancelled = run_to_first_cancellation(dict(f), ids)
            kinds = "".join(r["rule"][0] for r in script)
            n_open, n_close = a * a - 3 * a + 9, 4 * (a - 1)

            # `WStar i i1 i2 j1 j2 = bsWord2 i2 i1 j1 ++ (s_i :: descWord i1 j2)`
            WStar = (i2, i1) + dw(i2, j1) + (i,) + dw(i1, j2)
            # quadPair's redex `[s_jp, s_j1, s_jp] ++ (s_j1 :: R)`, in U0
            quad_at = next((k for k in range(len(U0) - 3)
                            if U0[k:k + 4] == (jp, j1, jp, j1)), None)
            rows.append({
                "a": a, "b": b, "i": i, "n": n,
                "j1_eq_i2": j1 == i2, "j1_eq_i1": j1 == i1,
                "prefix_steps": len(script),
                "prefix_formula_a2_plus_a_plus_5": a * a + a + 5,
                "prefix_matches_formula": len(script) == a * a + a + 5,
                "schedule": kinds,
                "opening_formula": n_open, "closing_formula": n_close,
                "opening_schedule": kinds[:n_open],
                "closing_schedule": kinds[n_open:],
                "all_steps_source_only": all(r["src_only"] for r in script),
                "steps_not_source_only":
                    sum(0 if r["src_only"] else 1 for r in script),
                "cancelled_rel_i": rel(cancelled) if cancelled else None,
                "cancelled_is_WStar": cancelled == WStar,
                "quadPair_redex_already_in_U0": quad_at is not None,
                "quadPair_L_rel_i":
                    list(rel(U0[:quad_at])) if quad_at is not None else None,
                "U0_rel_i": rel(U0), "V0_rel_i": rel(V0),
                "descWord_i_j1_len": len(dw(i, j1)),
                "script": script,
            })

    # Is the Bokut-Shiao rule at `j = i'` literally Yang-Baxter?  This is why
    # `closingBs`'s second step reads as `Y` in the trace.  Compare the whole
    # relation, not just the leading word: same leading word with a different
    # image would be a genuine ambiguity rather than a coincidence.
    cov.retune(9)
    bs_y = {"pairs": 0, "same_leading_word": 0, "same_relation": 0}
    for x in range(8):
        bn, yn = f"B{x}{x+1}{x}", f"Y{x}{x+1}"
        if bn not in eng.LM or yn not in eng.LM:
            continue
        bs_y["pairs"] += 1
        bs_y["same_leading_word"] += int(eng.LM[bn] == eng.LM[yn])
        bs_y["same_relation"] += int(eng.REL[bn] == eng.REL[yn])

    a2 = [r for r in rows if r["a"] == 2]
    a1 = [r for r in rows if r["a"] == 1]

    w = WitnessBuilder("hecke-small-a-decomposition", engine="sympy",
                       start_time=started)
    w.add_parameter("scope", "a in {1,2}, b in {a..a+3}; a >= 3 is proved")
    w.add_parameter(
        "why", "three probes carried the caveat 'a = 2 is excluded throughout "
        "this arc' and none recorded a reason; and this probe's own first "
        "version answered the wrong question -- it measured the U lineage's "
        "NORMAL FORM, reached past the first cancellation, and reported it as "
        "the prefix's endpoint")
    w.add_assertion(
        "a2_cases_whose_prefix_is_NOT_a2_plus_a_plus_5_steps",
        computed=str(sum(0 if r["prefix_matches_formula"] else 1 for r in a2)),
        expected="0")
    w.add_assertion(
        "a2_cases_whose_closing_schedule_is_NOT_FBYF",
        computed=str(sum(0 if r["closing_schedule"] == "FBYF" else 1
                         for r in a2)), expected="0")
    w.add_assertion(
        "a2_cases_whose_cancelled_word_is_NOT_WStar",
        computed=str(sum(0 if r["cancelled_is_WStar"] else 1 for r in a2)),
        expected="0")
    w.add_assertion(
        "a2_steps_whose_source_is_NOT_absent_from_the_other_terms",
        computed=str(sum(r["steps_not_source_only"] for r in a2)),
        expected="0")
    w.add_assertion(
        "a2_cases_where_quadPair's_redex_is_NOT_already_in_U0",
        computed=str(sum(0 if r["quadPair_redex_already_in_U0"] else 1
                         for r in a2)), expected="0")
    # a = 1 is genuinely different: 6 steps, not 7
    w.add_assertion(
        "a1_cases_whose_prefix_DOES_match_a2_plus_a_plus_5",
        computed=str(sum(1 if r["prefix_matches_formula"] else 0 for r in a1)),
        expected="0")
    w.add_assertion(
        "a1_cases_whose_prefix_is_NOT_6_steps",
        computed=str(sum(0 if r["prefix_steps"] == 6 else 1 for r in a1)),
        expected="0")
    w.add_assertion(
        "bs_at_j_eq_iprime_pairs_NOT_sharing_a_leading_word_with_yang_baxter",
        computed=str(bs_y["pairs"] - bs_y["same_leading_word"]), expected="0")
    w.add_assertion(
        "bs_at_j_eq_iprime_pairs_whose_relation_EQUALS_yang_baxter's",
        computed=str(bs_y["same_relation"]), expected="0")
    w.add_data("cases_checked", len(rows))
    w.add_data("bokut_shiao_vs_yang_baxter_at_j_eq_iprime", bs_y)
    w.add_data("cases", rows)
    w.add_caveat(
        "The prefix ends at the FIRST cancellation, which is what the Lean "
        "chain proves and is NOT a normal form. Running further is a different "
        "question and answering it does not answer this one -- that confusion "
        "is what the correction in the docstring records.")
    w.add_caveat(
        "Reaching an endpoint is necessary, not sufficient: a stretch that "
        "transfers still has to compose on the nose. Here it did -- both "
        "`prefixChain2` and `prefixChain1` are proved, lean-direct exit 0, "
        "axiom-clean -- so this caveat is discharged rather than outstanding. "
        "`oc` requires only j1 <= i1, i.e. a >= 1, so with a >= 3 already "
        "proved there is no uncovered corner left in this regime.")
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
        print(f"a={r['a']} b={r['b']}: {r['prefix_steps']} steps "
              f"(formula {r['prefix_formula_a2_plus_a_plus_5']}, "
              f"match {r['prefix_matches_formula']})"
              f"  open={r['opening_schedule']} close={r['closing_schedule']}"
              f"  srcOnly {r['all_steps_source_only']}")
        print(f"     cancelled {r['cancelled_rel_i']}"
              f"  =WStar {r['cancelled_is_WStar']}"
              f"  quad-in-U0 {r['quadPair_redex_already_in_U0']}"
              f" at L={r['quadPair_L_rel_i']}")
    print(f"\nBS(j=i') vs Yang-Baxter: {bs_y}")
    print(f"{len(rows)} cases measured")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
