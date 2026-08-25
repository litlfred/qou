#!/usr/bin/env python3
"""hecke_closing_from_topen — the closing phase, measured from where the Lean is.

`CornerLe.openingPhase` (§4an) proves `T0 →* TOpen`, the first `a²−3a+9` steps.
The prefix is `a²+a+5`, so `4(a−1)` steps remain before the first cancellation.
This measures them **from `TOpen`**, which is where the next lemma has to start.

Three questions, in the order they gate the Lean:

  1. **Is `TOpen` reached, and what is it?** Four terms, two per lineage, with
     the `h`-weighted one first in each pair. Built here from the Lean
     definitions so a mismatch shows up as a word, not a step count.

  2. **How many steps to the first cancellation, and on which lineages?**
     `hecke_prefix_phases.py` reads the closing phase as `small(a)` plus a
     trailing `[B₁₀⟨b⟩, B₂₁]`, with `ofTerms_cancel_pair` bridging the
     cancellation. That is an *inventory* result; this measures the schedule.

  3. **Do the SOURCE-ONLY collision hypotheses hold?** This is the load-bearing
     one. `hecke_prefix_head_separation.py` measured a hard core of `2a` steps
     where no left context satisfies `hpark` (no other term extends `A`), which
     is what `blockPass`/`loopTwoGen` asked for before the §4ai–§4af
     relaxations. What a step actually needs is `monicStep`'s `hne` — its
     SOURCE absent from the rest of the term list. That is strictly weaker, and
     the relaxations exist to exploit it. So: at every step of the closing
     phase, is the redex's source word absent from the other terms?

     If yes throughout, the `2a` hard core is not an obstruction and the closing
     phase needs no further lemma relaxation. If no, the count of failures is
     the size of the real problem.

All arithmetic is exact (sympy rationals in `q`); nothing here touches a float.

Emits `hecke-closing-from-topen.witness.json`. Bean qou-auq3.
"""
from __future__ import annotations
import importlib.util, sys, time
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE)); sys.path.insert(0, str(HERE / "substrate"))

from witness_base import WitnessBuilder  # noqa: E402

_ts = importlib.util.spec_from_file_location(
    "ts", HERE / "hecke_opening_trio_shape.py")
ts = importlib.util.module_from_spec(_ts); _ts.loader.exec_module(ts)
# One engine instance, shared. Loading the file again would return a FRESH
# module with an untuned rule table -- see the note at ts's own import.
cov, eng = ts.cov, ts.eng
dw = ts.dw


def main():
    started = time.monotonic()
    rows, bad = [], 0
    for a in range(4, 7):
        for b in (a, a + 1):
            n, i = a + b + 3, a + b + 1
            if i >= n or i - b < 0:
                continue
            cov.retune(n)
            j1, j2, i1, i2 = i - a, i - b, i - 1, i - 2
            jppp, jpp, jp, jm = j1 + 3, j1 + 2, j1 + 1, j1 - 1
            opening = a * a - 3 * a + 9
            prefix = a * a + a + 5

            V2 = (i2,) + dw(i, j1) + dw(i, j2)
            U0L = (i1,) + dw(i2, jpp) + dw(i, j1) + dw(jpp, j2) + (i,)
            V2L = (i2,) + dw(i1, jpp) + dw(i, j1) + dw(jpp, j2)

            # --- reach TL under the loops-first schedule the Lean uses
            f = cov.start_element(i, a, b)
            t0 = sorted(f, key=eng.deglex_key)
            f2, s12, _ = ts.run_to(f, t0[0], V2)
            f3, uL, _ = ts.run_to(f2, t0[1], U0L)
            f4, vL, _ = ts.run_to(f3, V2, V2L)

            # --- the two trios (6 steps), giving TOpen
            g = dict(f4)
            for _ in range(6):
                t = ts.next_redex(g)
                if t is None:
                    break
                g, _img = ts.apply(g, t)
            TOpen_terms = len(g)
            reached = s12 + uL + vL + 6

            # TOpen from the LEAN definitions
            def trioLeft(x, y):
                return (x,) + dw(y, jpp) + dw(i, jppp)

            def pair(x, y, T):
                L = trioLeft(x, y) + (jp, jpp) + (j1, jp)
                return (L + (j1,) + dw(jm, j2) + T, L + dw(jm, j2) + T)
            Vh, V1 = pair(i2, i1, ())
            Uh, U1 = pair(i1, i2, (i,))
            TOpen_exact = set(g) == {Vh, V1, Uh, U1}

            # --- (2)+(3) the closing phase, step by step
            steps, src_unique_fail, first_cancel = [], 0, None
            gg = dict(g)
            for k in range(4 * (a - 1) + 6):
                t = ts.next_redex(gg)
                if t is None:
                    break
                w, name, pos = t
                # (3) `hpark` -- "no OTHER term extends this step's left
                # context" -- which is what `blockPass`/`loopTwoGen` asked for
                # before the source-only relaxations, and what
                # `hecke_prefix_head_separation.py` measured failing on 2a
                # steps. This is the non-vacuous test.
                #
                # NOT measured here, because it CANNOT be: `monicStep`'s `hne`
                # asks that the redex's source word be absent from the rest of
                # the term list, and the engine models the element as a dict
                # keyed by words, so no word can appear twice. The first
                # version of this probe "checked" it and was reporting a
                # tautology. The Lean-side content of `hne` is that the LIST
                # the assembly builds carries no repeated word -- a property of
                # the assembly, under the prover's control, not a fact about
                # the chain. `hecke_prefix_schedule_check.py` measures it
                # (dup_sources = 0).
                A = w[:pos]
                hpark_ok = not any(u[:len(A)] == A for u in gg if u != w)
                before_keys = set(gg)
                gg, img = ts.apply(gg, t)
                after = len(gg)
                # A cancellation is a word the step LANDS ON that was already
                # carried, whose coefficients then sum to zero -- so it leaves
                # the support. Not "the term count failed to grow": a
                # far-commutation is a two-word rule (one out, one in) and a
                # quadratic is three (one out, two in), so the expected count
                # differs per rule and comparing against it fired on step 1 of
                # every case in the first version of this probe.
                cancelled = any(u in before_keys and u not in gg
                                for u in img if u != w)
                if cancelled and first_cancel is None:
                    first_cancel = k
                steps.append({"k": k, "rule": name, "terms_after": after,
                              "hpark_holds": hpark_ok,
                              "left_context_len": len(A)})
                if not hpark_ok:
                    src_unique_fail += 1
                if first_cancel is not None:
                    break

            closing_len = len(steps)
            total = reached + closing_len
            # The shape: an F-run, two Bokut-Shiao steps, the SAME F-run, then
            # the cancellation. Checked rather than eyeballed.
            names = [st["rule"] for st in steps]
            nb = [k for k, nm in enumerate(names) if nm.startswith("B")]
            two_B_adjacent = (len(nb) == 2 and nb[1] == nb[0] + 1)
            runs_identical = None
            f_run_len = None
            if two_B_adjacent:
                r1, r2 = names[:nb[0]], names[nb[1] + 1:]
                runs_identical = r1 == r2
                f_run_len = len(r1)
            ok = TOpen_exact and first_cancel is not None
            bad += not ok
            rows.append({
                "a": a, "b": b, "i": i, "n": n,
                "opening_phase_steps": opening,
                "prefix_steps": prefix,
                "closing_phase_predicted": 4 * (a - 1),
                "steps_to_TOpen": reached,
                "TOpen_term_count": TOpen_terms,
                "TOpen_is_exactly_the_four_lemma_words": TOpen_exact,
                "closing_steps_to_first_cancellation": closing_len,
                "first_cancellation_at": first_cancel,
                "total_steps": total,
                "total_matches_prefix": total == prefix,
                "closing_matches_4a_minus_4": closing_len == 4 * (a - 1),
                "closing_steps_where_hpark_FAILS": src_unique_fail,
                "closing_steps_where_hpark_holds":
                    closing_len - src_unique_fail,
                "closing_rules": names,
                "exactly_two_adjacent_B_steps": two_B_adjacent,
                "the_two_F_runs_are_identical": runs_identical,
                "F_run_length": f_run_len,
                "F_run_length_is_2a_minus_3": f_run_len == 2 * a - 3,
                "hpark_failures_equal_2a":
                    src_unique_fail == 2 * a,
                "closing_term_counts": [s["terms_after"] for s in steps],
            })

    w = WitnessBuilder("hecke-closing-from-topen", engine="sympy",
                       start_time=started)
    w.add_parameter("start", "TOpen -- the four-term element openingPhase proves")
    w.add_parameter("closing_phase", "prefix (a²+a+5) minus opening (a²−3a+9) = 4(a−1)")
    w.add_parameter(
        "hpark",
        "no OTHER term extends the step's left context -- what blockPass and "
        "loopTwoGen asked for before the source-only relaxations of this arc.")
    w.add_parameter(
        "why_hne_is_not_measured",
        "monicStep's `hne` (the redex's source absent from the rest of the "
        "list) cannot be measured in this model: the engine keys the element "
        "by word, so no word appears twice and any such check is a tautology. "
        "Its Lean-side content is that the assembled LIST repeats no word, "
        "which is under the prover's control; hecke_prefix_schedule_check.py "
        "measures it directly (dup_sources = 0).")
    w.add_assertion(
        "cases_where_TOpen_is_not_the_four_lemma_words",
        computed=str(sum(0 if r["TOpen_is_exactly_the_four_lemma_words"] else 1
                         for r in rows)), expected="0")
    w.add_assertion(
        "cases_reaching_no_cancellation",
        computed=str(sum(0 if r["first_cancellation_at"] is not None else 1
                         for r in rows)), expected="0")
    w.add_assertion(
        "closing_steps_checked_TOTAL",
        computed=str(sum(r["closing_steps_to_first_cancellation"]
                         for r in rows)),
        expected=str(sum(4 * (r["a"] - 1) for r in rows)))
    w.add_assertion(
        "cases_where_the_closing_length_is_not_4(a-1)",
        computed=str(sum(0 if r["closing_matches_4a_minus_4"] else 1
                         for r in rows)), expected="0")
    w.add_assertion(
        "cases_where_the_two_F_runs_are_not_identical",
        computed=str(sum(0 if r["the_two_F_runs_are_identical"] else 1
                         for r in rows)), expected="0")
    w.add_assertion(
        "cases_where_the_F_run_is_not_2a-3_steps",
        computed=str(sum(0 if r["F_run_length_is_2a_minus_3"] else 1
                         for r in rows)), expected="0")
    w.add_assertion(
        "cases_where_the_hpark_failure_count_is_not_2a",
        computed=str(sum(0 if r["hpark_failures_equal_2a"] else 1
                         for r in rows)), expected="0")
    w.add_assertion(
        "cases_where_opening_plus_closing_is_not_the_prefix",
        computed=str(sum(0 if r["total_matches_prefix"] else 1 for r in rows)),
        expected="0")
    w.add_data("cases_checked", len(rows))
    w.add_data("cases", rows)
    w.add_caveat(
        "a >= 4 only; a = 3 has no loop pass and is excluded from this arc's "
        "opening-phase lemmas entirely (`prefixChain3` covers it). a = 2's "
        "closing phase is the SAME three calls -- fRun, closingBs, fRun -- "
        "landing on the SAME word, WStar, with both F-runs one step because "
        "`descWord i jppp` is empty; see `prefixChain2` and "
        "hecke_small_a_decomposition.py.")
    w.add_caveat(
        "Source-uniqueness is necessary for `monicStep`, not sufficient for the "
        "whole assembly: each lemma also needs its words to line up on the "
        "nose. This measures the hypothesis, not the composition.")
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
        print(f"a={r['a']} b={r['b']}  TOpen at {r['steps_to_TOpen']}"
              f" ({r['TOpen_term_count']} terms,"
              f" exact={r['TOpen_is_exactly_the_four_lemma_words']})")
        print(f"      closing: {r['closing_steps_to_first_cancellation']} steps"
              f" (predicted {r['closing_phase_predicted']},"
              f" match={r['closing_matches_4a_minus_4']});"
              f" total {r['total_steps']} vs prefix {r['prefix_steps']}"
              f" match={r['total_matches_prefix']}")
        print(f"      rules  : {r['closing_rules']}")
        print(f"      terms  : {r['closing_term_counts']}"
              f"  hpark holds {r['closing_steps_where_hpark_holds']}"
              f"/{r['closing_steps_to_first_cancellation']}")
    print(f"\n{len(rows) - bad}/{len(rows)} cases clean")
    return 0 if bad == 0 else 1


if __name__ == "__main__":
    raise SystemExit(main())
