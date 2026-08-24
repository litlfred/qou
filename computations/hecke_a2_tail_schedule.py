#!/usr/bin/env python3
"""hecke_a2_tail_schedule — the `a = 2` tail, from the surviving pair to zero.

`sPoly_le_resolves` (PR #5586) joins the `a <= b` prefix to its tail for every
`a >= 3`. `a = 2` was measured there NOT to transfer, and the reason is a single
index bound: `tailPair`'s second word carries a leading `sigma_{i-1}` that comes
from the peel `descWord i1 jpp = sigma_{i-1} :: descWord i2 jpp`, which needs
`jpp <= i1` -- and at `a = 2`, `jpp = i`. That same bound is `hjppid` in both
general tail statements, so neither applies.

So `a = 2` needs its own tail, and this measures it: the exact schedule from the
pair `TCancel2_coeffEq` leaves to the point where the two lineages meet.

What it checks that a step count alone would not:

  * **the two lineages are independent** -- no step's source is a word the other
    lineage also carries, so source-only hypotheses suffice and the chain may be
    run one lineage at a time rather than in deg-lex order;
  * **no step splits a term** -- exactly one image word per step, so no
    quadratic step and no coefficient ever moves, which is what makes the
    meeting a cancellation;
  * **both closing steps are Bokut-Shiao** -- the engine labels them `Y`, and
    each is `B(x, x+1, x)` with the same leading word and the identical
    resulting element, so `bsStep` covers them and no Yang-Baxter lemma is
    needed. This is the same coincidence measured 16/16 for the `a > b` corner.

All arithmetic is exact (sympy rationals in a formal `h`); nothing here touches
a float.

Emits `hecke-a2-tail-schedule.witness.json`. Bean qou-auq3.
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


def rule_ids(n):
    out = {}
    for x in range(n):
        out[f"Q{x}"] = ("Q", x)
    for x in range(n - 1):
        out[f"Y{x}{x+1}"] = ("Y", x, x + 1)
    for x in range(n):
        for y in range(n):
            if y + 1 < x:
                out[f"F{x}{y}"] = ("F", x, y)
    for x in range(n - 1):
        for y in range(n):
            if y <= x:
                out[f"B{x}{x+1}{y}"] = ("B", x, x + 1, y)
    return out


def dw(x, y):
    return tuple(range(x, y - 1, -1)) if x >= y else ()


def redex_on(f, word):
    if word not in f:
        return None
    for name in eng.LM:
        pos = eng.infix_positions(word, eng.LM[name])
        if pos:
            return word, name, pos[0]
    return None


def apply(f, t):
    w, name, kk = t
    left, right = w[:kk], w[kk + len(eng.LM[name]):]
    img = eng.context_mul(left, eng.REL[name], right)
    return eng.clean(eng.combine(f, img, -sp.expand(f[w] / eng.LC[name]))), img


def main():
    started = time.monotonic()
    rows = []
    for b in range(2, 8):
        a = 2
        n, i = b + 8, b + 5
        retune(n)
        ids = rule_ids(n)
        j1, j2, i1, i2 = i - a, i - b, i - 1, i - 2
        jm = j1 - 1
        D = dw(jm, j2)                      # descWord jm j2
        m = len(D)
        # the two words `TCancel2_coeffEq` leaves, with j1 = i2
        P1 = (i2, i1, i, j1, i1) + D
        P2 = (i1, i, j1, i1) + D + (i,)
        f = eng.clean({P1: sp.Integer(1), P2: sp.Integer(-1)})

        y_tot = y_same = 0
        sched, ends, multi, shared = {}, {}, 0, 0
        for tag, seed, other in (("P1", P1, [P2]), ("P2", P2, None)):
            cur, steps = seed, []
            oth = other if other is not None else [w for w in f if w != seed]
            for _ in range(80):
                t = redex_on(f, cur)
                if t is None:
                    break
                w, name, kk = t
                if w in oth:
                    shared += 1
                rid = ids.get(name)
                if rid and rid[0] == "Y":
                    # is it B(x, x+1, x) -- same leading word, same element?
                    y_tot += 1
                    bn = f"B{rid[1]}{rid[1] + 1}{rid[1]}"
                    if bn in eng.LM and eng.LM[bn] == eng.LM[name] and \
                            apply(f, (w, name, kk))[0] == apply(f, (w, bn, kk))[0]:
                        y_same += 1
                f, img = apply(f, t)
                new = [u for u in img if u != w]
                steps.append((rid[0],) + tuple(i - x for x in rid[1:]))
                if len(new) != 1:
                    multi += 1
                    break
                cur = new[0]
                if cur not in f:
                    break
            sched[tag] = steps
            ends[tag] = cur
        meet = (i2, i1, i2) + D + (i, i1)   # bsWord2 i2 i1 j2 ++ [sigma_i, sigma_{i-1}]
        rows.append({
            "a": a, "b": b, "n": n, "run_length_m": m,
            "P1_steps": len(sched["P1"]), "P2_steps": len(sched["P2"]),
            "total_steps": len(sched["P1"]) + len(sched["P2"]),
            "P1_matches_2m_plus_1": len(sched["P1"]) == 2 * m + 1,
            "P2_matches_2m_plus_3": len(sched["P2"]) == 2 * m + 3,
            "total_matches_4m_plus_4":
                len(sched["P1"]) + len(sched["P2"]) == 4 * m + 4,
            "P1_schedule": [list(s) for s in sched["P1"]],
            "P2_schedule": [list(s) for s in sched["P2"]],
            "steps_with_more_than_one_image": multi,
            "steps_whose_source_the_other_lineage_carries": shared,
            "reduces_to_zero": len(f) == 0,
            "meeting_word_rel_i": [i - x for x in meet],
            "P1_ends_at_meet": ends["P1"] == meet,
            "y_labelled_steps": y_tot,
            "y_steps_giving_identical_element": y_same,
        })

    w = WitnessBuilder("hecke-a2-tail-schedule", engine="sympy",
                       start_time=started)
    w.add_parameter("scope", "a = 2 (j1 = i2), b in 2..7; the tail only, from "
                             "the pair TCancel2_coeffEq leaves")
    w.add_parameter(
        "why", "a = 2 was measured NOT to transfer to the general tail: the "
        "peel descWord i1 jpp = sigma_{i-1} :: descWord i2 jpp needs "
        "jpp <= i1, and at a = 2, jpp = i. This measures the schedule its own "
        "tail needs.")
    w.add_assertion(
        "cases_whose_P1_count_is_NOT_2m_plus_1",
        computed=str(sum(0 if r["P1_matches_2m_plus_1"] else 1 for r in rows)),
        expected="0")
    w.add_assertion(
        "cases_whose_P2_count_is_NOT_2m_plus_3",
        computed=str(sum(0 if r["P2_matches_2m_plus_3"] else 1 for r in rows)),
        expected="0")
    w.add_assertion(
        "cases_whose_total_is_NOT_4m_plus_4",
        computed=str(sum(0 if r["total_matches_4m_plus_4"] else 1 for r in rows)),
        expected="0")
    w.add_assertion(
        "steps_with_more_than_one_image_word",
        computed=str(sum(r["steps_with_more_than_one_image"] for r in rows)),
        expected="0")
    w.add_assertion(
        "steps_whose_source_the_other_lineage_also_carries",
        computed=str(sum(r["steps_whose_source_the_other_lineage_carries"]
                         for r in rows)),
        expected="0")
    w.add_assertion(
        "cases_NOT_reducing_to_zero",
        computed=str(sum(0 if r["reduces_to_zero"] else 1 for r in rows)),
        expected="0")
    w.add_assertion(
        "cases_where_the_first_lineage_does_NOT_end_at_the_meeting_word",
        computed=str(sum(0 if r["P1_ends_at_meet"] else 1 for r in rows)),
        expected="0")
    w.add_assertion(
        "y_labelled_steps_NOT_equal_to_the_bokut_shiao_rule",
        computed=str(sum(r["y_labelled_steps"] - r["y_steps_giving_identical_element"]
                         for r in rows)),
        expected="0")
    w.add_data("cases", rows)
    w.add_caveat(
        "The step counts are for THIS order -- the first lineage run to its "
        "end, then the second. That order is legal precisely because no step's "
        "source is carried by the other lineage (asserted above), and it is "
        "NOT deg-lex's. A Lean chain may group the same steps differently; "
        "what transfers is the rule sequence per lineage and the meeting word.")
    w.add_caveat(
        "Both lineages are the SAME two rightward transports -- sigma_{i-1} "
        "past the run, then sigma_i past it -- separated by one "
        "far-commutation sigma_i sigma_{i-2} -> sigma_{i-2} sigma_i. The "
        "second lineage then closes with two Bokut-Shiao steps. So the Lean "
        "needs `farComm_transport_right_sources`, `monicStep` and `bsStep`, "
        "and no lemma this arc does not already have.")
    w.add_caveat(
        "b = 2 is the diagonal and is the m = 0 case: `descWord jm j2` is "
        "EMPTY there (jm < j1 = j2), so both transports are no-ops and the "
        "tail is four steps. It is not a separate shape, unlike the diagonal "
        "in the a >= 3 tail, where the two general tail statements have "
        "genuinely different sources.")
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
        print(f"a=2 b={r['b']} m={r['run_length_m']}: "
              f"P1 {r['P1_steps']} + P2 {r['P2_steps']} = {r['total_steps']} "
              f"(4m+4={4 * r['run_length_m'] + 4})  zero {r['reduces_to_zero']}"
              f"  meet-ok {r['P1_ends_at_meet']}")
    ytot = sum(r["y_labelled_steps"] for r in rows)
    yok = sum(r["y_steps_giving_identical_element"] for r in rows)
    print(f"\nY-labelled steps: {yok}/{ytot} are the Bokut-Shiao rule at a "
          f"degenerate bottom, giving the identical element")
    print(f"{len(rows)} cases measured")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
