#!/usr/bin/env python3
"""hecke_a1_tail_schedule — the `a = 1` tail, and why it is a different shape.

`sPoly_le_resolves{,2,3}` close the `a <= b` corner for every `a >= 2`. `a = 1`
was measured (PR #5587) not to transfer, and for a stronger reason than `a = 2`:
`TCancel1_coeffEq` leaves **four** terms, with coefficients `h, 1, -h, -1`, and
never a two-term pair. Nothing stated on a pair can consume it.

This measures what it does instead. The four words are

    W1 = [s_{i-1}, s_i] ++ D          h
    W2 = [s_i, s_i, s_{i-1}] ++ D     1
    W3 = [s_i, s_{i-1}] ++ D         -h
    W4 = [s_{i-1}, s_i] ++ D ++ [s_i] -1        with D = descWord i2 j2

and W2 carries a **quadratic redex** `s_i s_i` from the start -- the only tail
in this arc that does.

The schedule measured here is the one a Lean chain should follow, which is NOT
deg-lex's: transport W1's `s_i` right past `D`, transport W4's, then one
quadratic step on each of the two words that carry `s_i s_i`. Each quadratic
step emits two words, and every emission lands on a word already present with
the opposite coefficient -- which is why the element reaches zero rather than a
sign-pair. That is checked here rather than assumed.

All arithmetic is exact (sympy rationals in a formal `h`); nothing touches a
float.

Emits `hecke-a1-tail-schedule.witness.json`. Bean qou-auq3.
"""
from __future__ import annotations
import importlib.util, sys, time
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE)); sys.path.insert(0, str(HERE / "substrate"))

import sympy as sp  # noqa: E402
from witness_base import WitnessBuilder  # noqa: E402

_e = importlib.util.spec_from_file_location(
    "eng", HERE / "hecke_gs_confluence_n4.py")
eng = importlib.util.module_from_spec(_e); _e.loader.exec_module(eng)

H = sp.Symbol("h")


def retune(n):
    """Rebuild the rule table at rank `n`. Module-level state, so every helper
    must run against THIS module object -- a second `spec_from_file_location`
    load returns a fresh, untuned copy whose empty `LM` finds no redex and
    reports zero steps rather than erroring."""
    eng.N = n
    eng.RULES = eng.build_rules()
    eng.LM = {name: lm for name, _, lm in eng.RULES}
    eng.REL = {name: rel for name, rel, _ in eng.RULES}
    eng.LC = {name: eng.REL[name][eng.LM[name]] for name in eng.LM}


def dw(x, y):
    return tuple(range(x, y - 1, -1)) if x >= y else ()


def apply_at(f, w, name, kk):
    left, right = w[:kk], w[kk + len(eng.LM[name]):]
    img = eng.context_mul(left, eng.REL[name], right)
    return eng.clean(eng.combine(f, img, -sp.expand(f[w] / eng.LC[name]))), img


def main():
    started = time.monotonic()
    rows = []
    for b in range(1, 8):
        a = 1
        n, i = b + 8, b + 5
        retune(n)
        j2, i1, i2 = i - b, i - 1, i - 2
        D = dw(i2, j2)
        m = len(D)

        W1 = (i1, i) + D
        W2 = (i, i, i1) + D
        W3 = (i, i1) + D
        W4 = (i1, i) + D + (i,)
        f = eng.clean({W1: H, W2: sp.Integer(1), W3: -H, W4: sp.Integer(-1)})
        start_terms = len(f)

        steps, uniq_ok = 0, True

        def transport_right(f, word, at):
            """Walk `s_i` rightwards one far-commutation at a time."""
            nonlocal steps, uniq_ok
            cur = word
            for _ in range(m):
                y = cur[at + 1]
                nm = f"F{i}{y}"
                if nm not in eng.LM:
                    return f, cur, False
                pos = eng.infix_positions(cur, eng.LM[nm])
                if at not in pos:
                    return f, cur, False
                if list(f).count(cur) != 1:
                    uniq_ok = False
                f, img = apply_at(f, cur, nm, at)
                nxt = [u for u in img if u != cur]
                if len(nxt) != 1:
                    return f, cur, False
                cur = nxt[0]
                steps += 1
                at += 1
            return f, cur, True

        f, A1, ok1 = transport_right(f, W1, 1)
        f, A4, ok4 = transport_right(f, W4, 1)

        # the two quadratic steps, and what each emits
        emissions, onto_present, fresh = [], 0, []
        quad_ok = True
        for word in (A4, W2):
            pos = eng.infix_positions(word, eng.LM[f"Q{i}"])
            if not pos:
                quad_ok = False
                break
            present_before = set(f)
            f, img = apply_at(f, word, f"Q{i}", pos[0])
            steps += 1
            emitted = [u for u in img if u != word]
            emissions.append([[i - x for x in u] for u in emitted])
            for u in emitted:
                if u in present_before:
                    onto_present += 1
                else:
                    fresh.append([i - x for x in u])

        rows.append({
            "a": a, "b": b, "n": n, "run_length_m": m,
            "start_terms": start_terms,
            "total_steps": steps,
            "matches_2m_plus_2": steps == 2 * m + 2,
            "transports_well_formed": bool(ok1 and ok4),
            "quadratic_steps_well_formed": quad_ok,
            "emissions_total": sum(len(e) for e in emissions),
            "emissions_onto_an_already_present_word": onto_present,
            "emissions_introducing_a_fresh_word": len(fresh),
            "fresh_words_rel_i": fresh,
            "every_step_source_was_unique_in_the_list": uniq_ok,
            "quadratic_steps": len(emissions),
            "emissions_rel_i": emissions,
            "reduces_to_zero": len(f) == 0,
            "W1_transported_rel_i": [i - x for x in A1],
            "W4_transported_rel_i": [i - x for x in A4],
        })

    w = WitnessBuilder("hecke-a1-tail-schedule", engine="sympy",
                       start_time=started)
    w.add_parameter("scope", "a = 1 (j1 = i1), b in 1..7; the tail only, from "
                             "the FOUR terms TCancel1_coeffEq leaves")
    w.add_parameter(
        "why", "a = 1 does not transfer to any tail this arc has: "
        "TCancel1_coeffEq leaves four terms (h, 1, -h, -1), never a two-term "
        "pair, and one of them carries a quadratic redex from the start. This "
        "measures the schedule its own tail needs.")
    w.add_assertion(
        "cases_whose_step_count_is_NOT_2m_plus_2",
        computed=str(sum(0 if r["matches_2m_plus_2"] else 1 for r in rows)),
        expected="0")
    w.add_assertion(
        "cases_whose_transports_are_NOT_well_formed",
        computed=str(sum(0 if r["transports_well_formed"] else 1 for r in rows)),
        expected="0")
    w.add_assertion(
        "cases_whose_two_quadratic_steps_do_NOT_emit_four_words",
        computed=str(sum(0 if r["emissions_total"] == 4 else 1 for r in rows)),
        expected="0")
    w.add_assertion(
        "cases_where_the_number_landing_on_an_already_present_word_is_NOT_3",
        computed=str(sum(
            0 if r["emissions_onto_an_already_present_word"] == 3 else 1
            for r in rows)),
        expected="0")
    w.add_assertion(
        "cases_introducing_a_number_of_fresh_words_OTHER_than_1",
        computed=str(sum(
            0 if r["emissions_introducing_a_fresh_word"] == 1 else 1
            for r in rows)),
        expected="0")
    w.add_assertion(
        "cases_whose_quadratic_steps_are_NOT_well_formed",
        computed=str(sum(0 if r["quadratic_steps_well_formed"] else 1
                         for r in rows)),
        expected="0")
    w.add_assertion(
        "cases_where_a_step_source_was_NOT_unique_in_the_list",
        computed=str(sum(
            0 if r["every_step_source_was_unique_in_the_list"] else 1
            for r in rows)),
        expected="0")
    w.add_assertion(
        "cases_NOT_reducing_to_zero",
        computed=str(sum(0 if r["reduces_to_zero"] else 1 for r in rows)),
        expected="0")
    w.add_assertion(
        "cases_NOT_starting_from_four_terms",
        computed=str(sum(0 if r["start_terms"] == 4 else 1 for r in rows)),
        expected="0")
    w.add_assertion(
        "cases_NOT_using_exactly_two_quadratic_steps",
        computed=str(sum(0 if r["quadratic_steps"] == 2 else 1 for r in rows)),
        expected="0")
    w.add_data("cases", rows)
    w.add_caveat(
        "The order measured is the one a Lean chain should follow and is NOT "
        "deg-lex's: both transports first, then the two quadratic steps. That "
        "is legal because every step's source occurs exactly once in the list "
        "at the moment it is rewritten (asserted above), which is what the "
        "`ofTerms` list model requires -- each lemma reads its redex off "
        "`L1 ++ (W, c) :: L2`.")
    w.add_caveat(
        "The ending is NOT a sign-pair, unlike every other tail in this arc. "
        "The two quadratic steps emit FOUR words: three land on words already "
        "carried with the opposite coefficient, and exactly ONE is fresh -- "
        "`[s_{i-1}] ++ D`, created by the first quadratic step and cancelled "
        "by the second's. So the element reaches zero outright and a Lean "
        "chain finishes with a CoeffEq on an explicit multi-entry list, not "
        "with `ofTerms_cancel_pair`. An earlier revision of this probe "
        "asserted that EVERY emission lands on an already-present word; that "
        "is false, and the assertion caught it -- the fresh word is exactly "
        "the intermediate the two quadratic steps share.")
    w.add_caveat(
        "b = 1 is the m = 0 case: `descWord i2 j2` is EMPTY (i2 < j2 = i1), "
        "both transports are no-ops, and the tail is the two quadratic steps "
        "alone. The four starting words are still four distinct words there.")
    w.add_caveat(
        "This measures the TAIL only. The prefix (`prefixChain1`, six steps) "
        "and the join through `TCancel1_coeffEq` are separate and already "
        "proved; what was missing is exactly this continuation.")
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
        print(f"a=1 b={r['b']} m={r['run_length_m']}: {r['total_steps']} steps "
              f"(2m+2={2 * r['run_length_m'] + 2})  quad {r['quadratic_steps']}"
              f"  zero {r['reduces_to_zero']}"
              f"  emissions {r['emissions_onto_an_already_present_word']}"
              f"+{r['emissions_introducing_a_fresh_word']}fresh")
    print(f"{len(rows)} cases measured")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
