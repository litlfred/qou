#!/usr/bin/env python3
"""hecke_small_a_decomposition — what `a = 1` and `a = 2` need, measured.

`CornerLe.prefixChain` and `prefixChain₃` prove the corner's `a ≤ b` prefix for
`a ≥ 3`. `oc` requires only `j₁ ≤ i₁`, i.e. `a ≥ 1`, so `a = 1` and `a = 2` are
valid corners in this regime and are not covered.

Three probes in this arc carry the caveat *"a = 2 is excluded throughout this
arc"* and **none records a reason**. This measures what the two cases actually
need, so the caveat can be replaced by a fact.

What it establishes, per case:

  * **which of the five `a ≥ 3` stretches transfer** — `s1`,`s2` reaching `V2`;
    the U loop reaching `U0L`; the V loop reaching `V2L`;
  * **the U lineage's actual script and endpoint**, since that is where `a = 2`
    diverges;
  * whether `quadPair`'s redex is present in `U0` from the start — which is the
    structural reason `a = 2` cannot use the loop.

**The headline is a negative and it is the point.** At `a = 2` the U side opens
with `quadPair` where `a ≥ 3` opens with a loop, because `descWord i j₁` is only
three letters when `j₁ = i₂`, so `U0` already carries the braid redex the loop
exists to build. Its endpoint is `bsWord₂ i₂ i₁ j₂ ++ [σᵢ, σᵢ₋₁]`, not `WStar`.
Neither route nor target transfers, so `a = 2` is a construction and not a
substitution — which is the opposite of what a target-word comparison alone
would suggest.

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


def main():
    started = time.monotonic()
    rows, bad = [], 0
    for a in (1, 2):
        for b in (a, a + 1, a + 2):
            n, i = a + b + 6, a + b + 3
            if i - b < 0 or i >= n:
                continue
            cov.retune(n)
            j1, j2, i1, i2 = i - a, i - b, i - 1, i - 2
            jp, jpp, jm, jppp = j1 + 1, j1 + 2, j1 - 1, j1 + 3
            ids = cov.rule_ids(n)
            rel = lambda w: [i - x for x in w]

            V2 = (i2,) + dw(i, j1) + dw(i, j2)
            U0L = (i1,) + dw(i2, jpp) + dw(i, j1) + dw(jpp, j2) + (i,)
            V2L = (i2,) + dw(i1, jpp) + dw(i, j1) + dw(jpp, j2)

            f = cov.start_element(i, a, b)
            t0 = sorted(f, key=eng.deglex_key)
            V0, U0 = t0[0], t0[1]

            # (1) which stretches transfer
            f2, s12, okV2 = ts.run_to(f, V0, V2)
            _f3, uL, okU0L = ts.run_to(f2, U0, U0L)
            _f4, vL, okV2L = ts.run_to(f2, V2, V2L)

            # (2) the U lineage's script, followed in isolation
            cur, g, script = U0, dict(f2), []
            for _ in range(14):
                t = ts.redex_on(g, cur)
                if t is None:
                    break
                g, img = ts.apply(g, t)
                script.append(ids.get(t[1]))
                nxt = [u for u in img if u != cur and u in g]
                if not nxt:
                    break
                cur = sorted(nxt, key=eng.deglex_key)[-1]

            # (3) is quadPair's redex already in U0?
            #     L ++ [s_jp, s_j1, s_jp] ++ (s_j1 :: R)
            quad_at = next((k for k in range(len(U0) - 3)
                            if U0[k:k + 4] == (jp, j1, jp, j1)), None)
            quad_L = list(rel(U0[:quad_at])) if quad_at is not None else None
            quad_R = list(rel(U0[quad_at + 4:])) if quad_at is not None else None
            # the a>=3 U-side trio's L is A ++ [s_jp, s_jpp]; at a = 2, A = []
            quad_L_is_jp_jpp = (quad_at is not None
                                and U0[:quad_at] == (jp, jpp))
            # (4) the U endpoint, against WStar and against the measured form
            WStar = (i2, i1) + dw(i2, j1) + (i,) + dw(i1, j2)
            Uend_form = (i2, i1) + dw(i2, j2) + (i, i1)
            rows.append({
                "a": a, "b": b, "i": i, "n": n,
                "j1_eq_i2": j1 == i2, "jp_eq_i1": jp == i1, "jpp_eq_i": jpp == i,
                "prefix_formula_a2_plus_a_plus_5": a * a + a + 5,
                "s1_s2_reach_V2": okV2, "s1_s2_steps": s12,
                "uLoop_reaches_U0L": okU0L, "uLoop_steps": uL,
                "vLoop_reaches_V2L": okV2L, "vLoop_steps": vL,
                "V2L_equals_V2": V2L == V2,
                "U0L_equals_U0": U0L == U0,
                "U_script": [list(r) if r else None for r in script],
                "U_opens_with_quadPair": script[:2] == [("Y", j1, jp), ("Q", j1)],
                "quadPair_redex_already_in_U0": quad_at is not None,
                "quadPair_L_rel_i": quad_L,
                "quadPair_R_rel_i": quad_R,
                "quadPair_L_is_sigma_jp_jpp": quad_L_is_jp_jpp,
                "U_end_rel_i": list(rel(cur)),
                "U_end_is_WStar": cur == WStar,
                "U_end_is_bsWord2_i2_i1_j2_plus_si_si1": cur == Uend_form,
                "descWord_i_j1_len": len(dw(i, j1)),
            })
    # a = 2 is the case with a partial transfer; a = 1 transfers nothing
    a2 = [r for r in rows if r["a"] == 2]
    a1 = [r for r in rows if r["a"] == 1]

    w = WitnessBuilder("hecke-small-a-decomposition", engine="sympy",
                       start_time=started)
    w.add_parameter("scope", "a in {1,2}, b in {a, a+1, a+2}; a >= 3 is proved")
    w.add_parameter(
        "why", "three probes carry the caveat 'a = 2 is excluded throughout "
        "this arc' and none records a reason; this measures what the two "
        "cases need so the caveat can be replaced by a fact")
    w.add_assertion(
        "a2_cases_where_s1_s2_do_NOT_reach_V2",
        computed=str(sum(0 if r["s1_s2_reach_V2"] else 1 for r in a2)),
        expected="0")
    w.add_assertion(
        "a2_cases_where_the_V_loop_is_NOT_trivial",
        computed=str(sum(0 if r["V2L_equals_V2"] else 1 for r in a2)),
        expected="0")
    w.add_assertion(
        "a2_cases_where_the_U_loop_DOES_reach_U0L",
        computed=str(sum(1 if r["uLoop_reaches_U0L"] else 0 for r in a2)),
        expected="0")
    w.add_assertion(
        "a2_cases_where_the_U_side_does_NOT_open_with_quadPair",
        computed=str(sum(0 if r["U_opens_with_quadPair"] else 1 for r in a2)),
        expected="0")
    w.add_assertion(
        "a2_cases_where_quadPair's_redex_is_NOT_already_in_U0",
        computed=str(sum(0 if r["quadPair_redex_already_in_U0"] else 1
                         for r in a2)), expected="0")
    w.add_assertion(
        "a2_cases_where_the_U_endpoint_IS_WStar",
        computed=str(sum(1 if r["U_end_is_WStar"] else 0 for r in a2)),
        expected="0")
    w.add_assertion(
        "a1_cases_where_s1_s2_DO_reach_V2",
        computed=str(sum(1 if r["s1_s2_reach_V2"] else 0 for r in a1)),
        expected="0")
    w.add_data("cases_checked", len(rows))
    w.add_data("cases", rows)
    w.add_caveat(
        "The U script is followed in isolation, taking the deg-lex-greatest "
        "image word as each step's successor. That is a heuristic for 'which "
        "word did this term become' and is sound only while the lineage has "
        "not split -- which the quadratic step does, so read the script past "
        "its Q step as one branch of two.")
    w.add_caveat(
        "Reaching an endpoint is necessary, not sufficient: a stretch that "
        "transfers still has to compose on the nose, and this arc's record on "
        "'remaining work is just wiring' is poor.")
    path = w.save()
    print(f"witness -> {path}")
    for r in rows:
        print(f"a={r['a']} b={r['b']}: s1s2->V2 {r['s1_s2_reach_V2']}"
              f"  U->U0L {r['uLoop_reaches_U0L']}"
              f"  V2L==V2 {r['V2L_equals_V2']}"
              f"  quad-in-U0 {r['quadPair_redex_already_in_U0']}"
              f"  L=[jp,jpp] {r['quadPair_L_is_sigma_jp_jpp']}")
        print(f"     U script: {r['U_script']}")
        print(f"     U end   : {r['U_end_rel_i']}"
              f"  =WStar {r['U_end_is_WStar']}"
              f"  =measured-form {r['U_end_is_bsWord2_i2_i1_j2_plus_si_si1']}")
    print(f"\n{len(rows)} cases measured")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
