#!/usr/bin/env python3
"""hecke_opening_trio_shape — what follows the two loops, measured from TL.

`CornerLe.openingLoops` (§4an) proves `T0 →* TL` under the loops-first
schedule: `s1`, `s2`, then `uLoop`, then `vLoop`. That schedule is **not** the
one the confluence engine takes, so the existing coverage probe
(`hecke_opening_coverage.py`) cannot answer what comes next: it replays under
deg-lex, where the U trio runs before the V loop.

This probe measures the continuation from `TL` itself. Two questions:

  1. **Is `TL` reachable at all?** Independently of the Lean, replay `T0` under
     a *forced* loops-first schedule — always reduce the U lineage until it
     reaches `U0L`, then the V lineage until it reaches `V2L` — and check the
     element then equals `TL` built from the lemmas' own formulas. This is a
     numerical cross-check of a proved statement, which is worth having: the
     Lean proves the reduction exists, the engine confirms it is the reduction
     the rewriting system actually performs.

  2. **What are the two trios?** From `TL`, replay under deg-lex and record the
     rule identities and the *term count* at each step. The term count is the
     load-bearing measurement: every loop lemma in the file is stated for a
     two-term element, so a trio that splits a term determines what lemma shape
     the rest of the phase needs.

The scheduling claim in `openingLoops`' docstring — that both loops must precede
both trios — was measured under the engine's order. Here it is measured from the
other side: if the trios really do split terms, the count from `TL` says by how
much and when.

All arithmetic is exact (sympy rationals in `q`); nothing here touches a float.

Emits `hecke-opening-trio-shape.witness.json`. Bean qou-auq3.
"""
from __future__ import annotations
import importlib.util, sys, time
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE)); sys.path.insert(0, str(HERE / "substrate"))

import sympy as sp  # noqa: E402
from witness_base import WitnessBuilder  # noqa: E402

_cov = importlib.util.spec_from_file_location(
    "cov", HERE / "hecke_opening_coverage.py")
cov = importlib.util.module_from_spec(_cov); _cov.loader.exec_module(cov)

# Use *cov's* engine instance, not a second load of the same file. `cov.retune`
# mutates module-level state (`eng.N`, `eng.RULES`, `eng.LM`, `eng.REL`,
# `eng.LC`), and `importlib.util.spec_from_file_location` returns a fresh module
# each time -- so a second load would leave this probe reading an untuned `LM`.
# It did, on the first run: every rule table was empty, so no redex was ever
# found, every stretch measured 0 steps, and the run reported 0/6 rather than
# erroring. Same shape as the two wrong-index bugs earlier in this arc -- a
# check that finds nothing reads as a measurement.
eng = cov.eng


def dw(x, y):
    return tuple(range(x, y - 1, -1)) if x >= y else ()


def next_redex(f):
    for w in sorted(f.keys(), key=eng.deglex_key):
        for name in eng.LM:
            pos = eng.infix_positions(w, eng.LM[name])
            if pos:
                return w, name, pos[0]
    return None


def redex_on(f, target):
    """The deg-lex-first redex lying inside the single word `target`."""
    if target not in f:
        return None
    for name in eng.LM:
        pos = eng.infix_positions(target, eng.LM[name])
        if pos:
            return target, name, pos[0]
    return None


def apply(f, t):
    w, name, kk = t
    left, right = w[:kk], w[kk + len(eng.LM[name]):]
    img = eng.context_mul(left, eng.REL[name], right)
    return eng.clean(eng.combine(f, img, -sp.expand(f[w] / eng.LC[name]))), img


def run_to(f, start_word, goal_word, cap=200):
    """Reduce only the lineage descending from `start_word` until `goal_word`
    appears. Returns (element, steps, reached)."""
    cur, steps = start_word, 0
    while steps < cap:
        if goal_word in f:
            return f, steps, True
        t = redex_on(f, cur)
        if t is None:
            return f, steps, False
        f, img = apply(f, t)
        steps += 1
        # follow the heaviest image word (the lineage's successor)
        nxt = [u for u in img if u != cur and u in f]
        if not nxt:
            return f, steps, goal_word in f
        cur = sorted(nxt, key=eng.deglex_key)[-1]
    return f, steps, False


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
            jppp, jpp = j1 + 3, j1 + 2
            opening = a * a - 3 * a + 9

            # --- the two lemma endpoints, from the Lean definitions themselves
            V2 = (i2,) + dw(i, j1) + dw(i, j2)
            U0L = (i1,) + dw(i2, jpp) + dw(i, j1) + dw(jpp, j2) + (i,)
            V2L = (i2,) + dw(i1, jpp) + dw(i, j1) + dw(jpp, j2)

            # --- (1) is TL reachable under the loops-first schedule?
            f = cov.start_element(i, a, b)
            terms0 = sorted(f, key=eng.deglex_key)
            # V0 is the deg-lex-lesser of the two starting words (it is the
            # one s1 acts on); U0 the other.
            V0, U0 = terms0[0], terms0[1]
            f2, s12, hit_V2 = run_to(f, V0, V2)
            f3, uL, hit_U0L = run_to(f2, U0, U0L)
            f4, vL, hit_V2L = run_to(f3, V2, V2L)
            TL_reached = hit_V2 and hit_U0L and hit_V2L
            TL_is_two_terms = len(f4) == 2 if TL_reached else None
            TL_exact = (TL_reached and set(f4) == {V2L, U0L})

            # --- (2) what follows TL, under deg-lex
            ids = cov.RMAP_CACHE.setdefault(n, cov.rule_ids(n))
            tail_rules, tail_counts = [], []
            g = dict(f4)
            for _ in range(12):
                t = next_redex(g)
                if t is None:
                    break
                g, _img = apply(g, t)
                tail_rules.append(ids.get(t[1]))
                tail_counts.append(len(g))

            jp_ = j1 + 1
            trio = [("B", jp_, jpp, j1), ("Y", j1, jp_), ("Q", j1)]
            first_trio = tail_rules[:3] == trio
            second_trio = tail_rules[3:6] == trio
            splits_at = next((k for k, c in enumerate(tail_counts) if c > 2), None)

            # --- (3) the trio's decomposition into bsStep + quadPair, built
            # from the LEAN-side formulas and checked against the engine's
            # words. Deriving this by hand and writing the Lean off the
            # derivation is exactly the move this arc keeps punishing -- and it
            # punished it again here: the first version of this block tested a
            # V-side formula against the FIRST trio, which is the U side's.
            # deg-lex reaches U0L before V2L, so U's trio runs first.
            jm = j1 - 1
            bsw1 = dw(jpp, j1) + (jpp,)          # bsWord1 jpp j1
            bsw2 = (jp_, jpp) + dw(jp_, j1)      # bsWord2 jp jpp j1

            def trio_words_for(A_bs, B_bs):
                """The three words one trio touches, from (A, B) alone."""
                L_q = A_bs + (jp_, jpp)
                R_q = dw(jm, j2) + B_bs[len(dw(jp_, j2)):]
                return dict(
                    pre=A_bs + bsw1 + B_bs,
                    mid=A_bs + bsw2 + B_bs,
                    quad_src=L_q + (jp_, j1, jp_) + (j1,) + R_q,
                    out_h=L_q + (j1, jp_) + (j1,) + R_q,
                    out_1=L_q + (j1, jp_) + R_q,
                    L=L_q, R=R_q)

            # U trio: A = [s_i1] ++ descWord i2 jpp ++ descWord i jppp,
            #         B = descWord jp j2 ++ [s_i]
            U_tr = trio_words_for((i1,) + dw(i2, jpp) + dw(i, jppp),
                                  dw(jp_, j2) + (i,))
            # V trio: A = [s_i2] ++ descWord i1 jpp ++ descWord i jppp,
            #         B = descWord jp j2          (no trailing s_i)
            V_tr = trio_words_for((i2,) + dw(i1, jpp) + dw(i, jppp),
                                  dw(jp_, j2))

            gt = dict(f4)
            seen = []
            for _ in range(6):
                t = next_redex(gt)
                if t is None:
                    break
                seen.append(t[0])
                gt, _img = apply(gt, t)
            u_pre_ok = len(seen) > 0 and seen[0] == U0L == U_tr["pre"]
            u_mid_ok = len(seen) > 1 and seen[1] == U_tr["mid"] == U_tr["quad_src"]
            v_pre_ok = len(seen) > 3 and seen[3] == V2L == V_tr["pre"]
            v_mid_ok = len(seen) > 4 and seen[4] == V_tr["mid"] == V_tr["quad_src"]
            outs_ok = all(w in gt for w in (U_tr["out_h"], U_tr["out_1"],
                                            V_tr["out_h"], V_tr["out_1"]))
            trio_decomposition_ok = (u_pre_ok and u_mid_ok and v_pre_ok
                                     and v_mid_ok and outs_ok)
            u_first = len(seen) > 3 and seen[0] == U0L and seen[3] == V2L

            ok = TL_exact and TL_reached and trio_decomposition_ok
            bad += not ok
            rows.append({
                "a": a, "b": b, "i": i, "n": n,
                "opening_phase_steps": opening,
                # (1) the cross-check of openingLoops
                "s1_s2_steps": s12,
                "uLoop_steps": uL,
                "vLoop_steps": vL,
                "loops_first_total": s12 + uL + vL,
                "V2_reached": hit_V2,
                "U0L_reached": hit_U0L,
                "V2L_reached": hit_V2L,
                "TL_is_exactly_the_two_lemma_words": TL_exact,
                "TL_term_count": len(f4) if TL_reached else None,
                "uLoop_m": i1 - jppp,
                "vLoop_m": i - jppp,
                "vLoop_is_one_deeper": (vL == uL + 1) if TL_reached else None,
                # (2) the continuation
                "rules_after_TL": [list(r) if r else None for r in tail_rules],
                "term_count_after_each": tail_counts,
                "first_trio_is_BS_Y_Q": first_trio,
                "second_trio_is_BS_Y_Q": second_trio,
                "term_count_first_exceeds_two_at_step": splits_at,
                # (3) the hand decomposition, tested on BOTH trios
                "U_trio_runs_first": u_first,
                "U_bsStep_source_matches_engine": u_pre_ok,
                "U_bsStep_target_is_quadPair_source": u_mid_ok,
                "V_bsStep_source_matches_engine": v_pre_ok,
                "V_bsStep_target_is_quadPair_source": v_mid_ok,
                "all_four_quadPair_outputs_present": outs_ok,
                "trio_decomposition_ok": trio_decomposition_ok,
                "U_trio_R_rel_i": [i - x for x in U_tr["R"]],
                "V_trio_R_rel_i": [i - x for x in V_tr["R"]],
                "steps_left_in_opening_after_TL": opening - (s12 + uL + vL),
            })

    w = WitnessBuilder("hecke-opening-trio-shape", engine="sympy",
                       start_time=started)
    w.add_parameter("schedule", "loops-first: s1, s2, then uLoop, then vLoop")
    w.add_parameter("TL", "the two-term element [(V2L, 1), (U0L, -1)]")
    w.add_parameter(
        "why_from_TL",
        "hecke_opening_coverage.py replays under deg-lex, where the U trio "
        "precedes the V loop. openingLoops uses the other (legal) order, so "
        "what follows TL cannot be read off that trace and is measured here.")
    w.add_assertion("cases_where_TL_is_not_reached_exactly",
                    computed=str(sum(
                        0 if r["TL_is_exactly_the_two_lemma_words"] else 1
                        for r in rows)), expected="0")
    w.add_assertion("cases_where_the_element_at_TL_is_not_two_terms",
                    computed=str(sum(0 if r["TL_term_count"] == 2 else 1
                                     for r in rows)), expected="0")
    w.add_assertion(
        "cases_where_the_V_loop_is_not_one_step_deeper_than_the_U_loop",
        computed=str(sum(0 if r["vLoop_is_one_deeper"] else 1 for r in rows)),
        expected="0")
    w.add_assertion("cases_where_the_first_trio_is_not_BS_Y_Q",
                    computed=str(sum(0 if r["first_trio_is_BS_Y_Q"] else 1
                                     for r in rows)), expected="0")
    w.add_assertion(
        "cases_where_the_U_trio_does_not_run_before_the_V_trio",
        computed=str(sum(0 if r["U_trio_runs_first"] else 1 for r in rows)),
        expected="0")
    w.add_assertion(
        "cases_where_the_hand_decomposition_of_the_trio_fails",
        computed=str(sum(0 if r["trio_decomposition_ok"] else 1 for r in rows)),
        expected="0")
    w.add_assertion("cases_where_the_second_trio_is_not_BS_Y_Q",
                    computed=str(sum(0 if r["second_trio_is_BS_Y_Q"] else 1
                                     for r in rows)), expected="0")
    w.add_data("cases_checked", len(rows))
    w.add_data("cases", rows)
    w.add_caveat(
        "a >= 4 only. a = 3 has no loop pass (m would be -1) and needs its "
        "own treatment; a = 2 is excluded throughout this arc.")
    w.add_caveat(
        "The forced schedule follows each lineage by taking the deg-lex-"
        "greatest image word as the successor. That is a heuristic for "
        "'which word did this term become', and it is only sound while the "
        "lineage has not split -- which is exactly what the term-count column "
        "records.")
    w.add_caveat(
        "Confirming a proved reduction numerically adds no logical strength. "
        "It is recorded because it checks the Lean's WORDS against the "
        "engine's: a lemma can be sorry-free and still be about the wrong "
        "monomial.")
    path = w.save()
    print(f"witness -> {path}")
    for r in rows:
        print(f"a={r['a']} b={r['b']}  loops={r['loops_first_total']}"
              f" (s12={r['s1_s2_steps']} U={r['uLoop_steps']} V={r['vLoop_steps']})"
              f"  TL_exact={r['TL_is_exactly_the_two_lemma_words']}"
              f"  left={r['steps_left_in_opening_after_TL']}")
        print(f"      after TL: {r['rules_after_TL'][:8]}")
        print(f"      terms   : {r['term_count_after_each'][:8]}"
              f"  trio1={r['first_trio_is_BS_Y_Q']}"
              f" trio2={r['second_trio_is_BS_Y_Q']}")
        print(f"      decomp  : U_first={r['U_trio_runs_first']}"
              f" U=({r['U_bsStep_source_matches_engine']},"
              f"{r['U_bsStep_target_is_quadPair_source']})"
              f" V=({r['V_bsStep_source_matches_engine']},"
              f"{r['V_bsStep_target_is_quadPair_source']})"
              f" outs={r['all_four_quadPair_outputs_present']}")
    print(f"\n{len(rows) - bad}/{len(rows)} cases clean")
    return 0 if bad == 0 else 1


if __name__ == "__main__":
    raise SystemExit(main())
