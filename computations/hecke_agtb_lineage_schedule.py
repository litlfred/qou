#!/usr/bin/env python3
"""hecke_agtb_lineage_schedule — the `a > b` corner, per lineage, exact words.

`CornerLe.prefixChain{,₁,₂,₃}` (PR #5454) prove the Bokut–Shiao corner's
`a ≤ b` prefix for every `a`. `hecke_agtb_corner_shape.py` on that branch then
measured the *other* corner and found it is **strictly easier**: the `a > b`
S-polynomial reduces **completely to zero**, the element never exceeds two
terms, and the chain uses **no quadratic step** — so `quadPair`, `trio`,
`TOpen` and `ofTerms_cancel_split` are all unnecessary here.

That settles the shape. It does **not** give a Lean chain. This probe measures
what a chain actually needs: for each of the two lineages, the ordered list of
rule applications with the **exact source and target words**, so each step can
be matched to `monicStep` / `bsStep` / `farComm_transport_left_sources` before
any Lean is written.

Self-contained: it drives `hecke_gs_confluence_n4` directly rather than
importing the `a ≤ b` arc's helper probes, which live only on that branch.

Two things it checks that a count alone would not:

  * **the two lineages are independent** — no step's source is a word the other
    lineage also carries, so the `_sources` (source-only) hypotheses suffice and
    the chain can be reordered freely, exactly as the `a ≤ b` opening phase and
    the `a = 1` chain both had to be;
  * **where the two lineages meet** — the final word, reached from both sides,
    is what makes the element vanish.

All arithmetic is exact (sympy rationals in `q`); nothing here touches a float.

Emits `hecke-agtb-lineage-schedule.witness.json`. Bean qou-auq3.
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
    below must run against THIS module object -- a second
    `spec_from_file_location` load would return a fresh, untuned copy whose
    empty `LM` finds no redex and reports zero steps rather than erroring."""
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


def start_element(i, a, b):
    """The S-polynomial of the two Bokut-Shiao rules at top `i-1`, bottoms
    `j1 = i-a` and `j2 = i-b`, cross-multiplied to a common leading word."""
    j1, j2 = i - a, i - b
    d1, e2 = eng.desc_word(i, j1), eng.desc_word(i - 1, j2)
    n1, n2 = f"B{i-1}{i}{j1}", f"B{i-1}{i}{j2}"
    return dict(eng.clean(eng.combine(
        {w: eng.LC[n2] * c
         for w, c in eng.context_mul((), eng.REL[n1], e2 + (i,)).items()},
        {w: eng.LC[n1] * c
         for w, c in eng.context_mul(d1, eng.REL[n2], ()).items()}, -1)))


def redex_on(f, word):
    """The deg-lex-first redex lying inside `word`, or None."""
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


def run_lineage(f, seed, ids, other, cap=80):
    """Reduce ONLY the term descending from `seed`, recording each step's rule,
    source and target. With no quadratic step the lineage never branches, so
    unlike the `a <= b` arc there is no forest here and no ambiguity about
    which image word is the successor -- which this asserts rather than assumes
    by requiring exactly one image word per step."""
    cur, steps = seed, []
    for _ in range(cap):
        t = redex_on(f, cur)
        if t is None:
            break
        w, name, kk = t
        src_only = w not in other
        f, img = apply(f, t)
        new = [u for u in img if u != w]
        steps.append({
            "rule": list(ids.get(name)), "at": kk,
            "src": w, "images": len(new),
            "tgt": new[0] if len(new) == 1 else None,
            "src_only": src_only,
        })
        if len(new) != 1:
            break
        cur = new[0]
        if cur not in f:          # the two lineages met and cancelled
            break
    return f, cur, steps


def main():
    started = time.monotonic()
    rows = []
    for a in range(2, 7):
        for b in range(1, a):
            n, i = a + b + 6, a + b + 3
            if i - a < 0 or i >= n:
                continue
            retune(n)
            ids = rule_ids(n)
            j1, j2, i1, i2 = i - a, i - b, i - 1, i - 2
            rel = lambda w: [i - x for x in w]

            f0 = start_element(i, a, b)
            seeds = sorted(f0, key=eng.deglex_key)
            V0, U0 = seeds[0], seeds[1]

            # V first, then U -- the order is free (no shared sources), and
            # this asserts that rather than relying on it
            f1, vend, vsteps = run_lineage(dict(f0), V0, ids, [U0])
            f2, uend, usteps = run_lineage(f1, U0, ids,
                                           [w for w in f1 if w != U0])

            meet = vend if vend == uend else None
            rows.append({
                "a": a, "b": b, "i": i, "n": n,
                "V0_rel_i": rel(V0), "U0_rel_i": rel(U0),
                "V_steps": len(vsteps), "U_steps": len(usteps),
                "total_steps": len(vsteps) + len(usteps),
                "b_formula_b2_plus_3b_plus_5": b * b + 3 * b + 5,
                "matches_b_formula":
                    len(vsteps) + len(usteps) == b * b + 3 * b + 5,
                "V_schedule": "".join(s["rule"][0] for s in vsteps),
                "U_schedule": "".join(s["rule"][0] for s in usteps),
                "V_rules": [s["rule"] for s in vsteps],
                "U_rules": [s["rule"] for s in usteps],
                "V_words_rel_i": [rel(s["src"]) for s in vsteps]
                                 + ([rel(vend)] if vend else []),
                "U_words_rel_i": [rel(s["src"]) for s in usteps]
                                 + ([rel(uend)] if uend else []),
                "quadratic_steps":
                    sum(1 for s in vsteps + usteps if s["rule"][0] == "Q"),
                "steps_with_more_than_one_image":
                    sum(1 for s in vsteps + usteps if s["images"] != 1),
                "steps_not_source_only":
                    sum(0 if s["src_only"] else 1 for s in vsteps + usteps),
                "lineages_meet": meet is not None,
                "meeting_word_rel_i": rel(meet) if meet else None,
                "final_terms": len(f2),
                "reduces_to_zero": len(f2) == 0,
                # the shape hecke_agtb_corner_shape.py identified
                "meet_is_bsWord2_j2m1_plus_descWord_i_j1":
                    meet == (i2, i1) + dw(i2, j2 - 1) + (i,) + dw(i1, j1),
            })

    w = WitnessBuilder("hecke-agtb-lineage-schedule", engine="sympy",
                       start_time=started)
    w.add_parameter("scope", "a > b, i.e. j1 < j2; a in 2..6, b in 1..a-1")
    w.add_parameter(
        "why", "hecke_agtb_corner_shape.py established the a>b corner's SHAPE "
        "(reduces to zero, 2 terms, no quadratic step); this measures the "
        "per-lineage schedule with exact words, which is what a Lean chain "
        "needs and a count does not give")
    w.add_assertion(
        "cases_whose_total_step_count_does_NOT_match_b2_plus_3b_plus_5",
        computed=str(sum(0 if r["matches_b_formula"] else 1 for r in rows)),
        expected="0")
    w.add_assertion(
        "steps_producing_more_than_one_image_word",
        computed=str(sum(r["steps_with_more_than_one_image"] for r in rows)),
        expected="0")
    w.add_assertion(
        "steps_whose_source_is_NOT_absent_from_the_other_terms",
        computed=str(sum(r["steps_not_source_only"] for r in rows)),
        expected="0")
    w.add_assertion(
        "cases_using_ANY_quadratic_step",
        computed=str(sum(1 if r["quadratic_steps"] else 0 for r in rows)),
        expected="0")
    w.add_assertion(
        "cases_where_the_two_lineages_do_NOT_meet",
        computed=str(sum(0 if r["lineages_meet"] else 1 for r in rows)),
        expected="0")
    w.add_assertion(
        "cases_whose_meeting_word_is_NOT_bsWord2_i2_i1_j2m1_++_descWord_i_j1",
        computed=str(sum(0 if r["meet_is_bsWord2_j2m1_plus_descWord_i_j1"]
                         else 1 for r in rows)), expected="0")
    w.add_assertion(
        "cases_that_do_NOT_reduce_to_zero",
        computed=str(sum(0 if r["reduces_to_zero"] else 1 for r in rows)),
        expected="0")
    w.add_data("cases_checked", len(rows))
    w.add_data("cases", rows)
    w.add_caveat(
        "Running V before U is a CHOICE, not the deg-lex order. It is legal "
        "because no step's source is carried by the other lineage (asserted "
        "above), so the two commute. The a <= b opening phase and the a = 1 "
        "chain both had to reorder for the same reason, and in the a = 1 case "
        "the deg-lex order was actively worse -- it made two words collide in "
        "both length and prefix.")
    w.add_caveat(
        "Per-lineage step counts are for THIS order. A Lean chain may group "
        "the same steps differently; what transfers is the rule sequence per "
        "lineage, the words, and the meeting word.")
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
        print(f"a={r['a']} b={r['b']}: V {r['V_steps']:2} + U {r['U_steps']:2} "
              f"= {r['total_steps']:2} (b^2+3b+5={r['b_formula_b2_plus_3b_plus_5']})"
              f"  V:{r['V_schedule']}  U:{r['U_schedule']}"
              f"  zero {r['reduces_to_zero']}")
        print(f"     meet {r['meeting_word_rel_i']}"
              f"  = bsWord2 i2 i1 (j2-1) ++ descWord i j1: "
              f"{r['meet_is_bsWord2_j2m1_plus_descWord_i_j1']}")
    print(f"\n{len(rows)} cases measured")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
