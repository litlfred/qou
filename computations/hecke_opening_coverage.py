#!/usr/bin/env python3
"""hecke_opening_coverage — does the planned lemma set cover the opening phase?

The `a ≤ b` corner's opening phase is the `a²−3a+9` steps before the first
collision clash (`hecke_prefix_head_separation.py`). The plan for assembling it,
after two rounds of finding that pieces were already in the corpus, is:

    V0 --s1, s2-->            V2            (CornerGeneral, j₂-independent)
    U0 --loopTwoGen at m-->   U_loop        (§4af)

with the level parameters solved by `hecke_prefix_loop_fit.py`: `k = i₁`,
`e = jppp`, hence **m = a − 4**. That m is why `a = 3` has no loop pass — it
would need m = −1 — and why `CornerLe.uHead` turned out to be `loopTwoGen` at
m = 0, which is the `a = 4` case.

This measures whether that plan actually covers the phase, rather than assuming
it. For each `(a, b)` it replays the chain and checks:

  * the first two steps act on `V0` and land it on `V2` exactly;
  * the next stretch acts on `U0` alone;
  * that stretch ends on `loopTwoGen`'s target word, computed from the lemma's
    own formula `A ++ descWord kd ed ++ descWord i j₁ ++ descWord ed j₂ ++ S`
    at `A = [σᵢ₋₁]`, `S = [σᵢ]`, `k = i₁`, `e = jppp`;
  * how many of the `a²−3a+9` opening steps that accounts for, and what is left.

**The residue is the point.** If the two applications cover the phase, the
opening assembles in two lemma calls. If they do not, the number left over says
how much more is needed — and this arc's record says to expect a remainder
rather than a clean fit.

Emits `hecke-opening-coverage.witness.json`. Bean qou-auq3.
"""
from __future__ import annotations
import importlib.util, sys, time
from pathlib import Path
import sympy as sp

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE)); sys.path.insert(0, str(HERE / "substrate"))

from witness_base import WitnessBuilder  # noqa: E402
_spec = importlib.util.spec_from_file_location("eng", HERE / "hecke_gs_confluence_n4.py")
eng = importlib.util.module_from_spec(_spec); _spec.loader.exec_module(eng)


def retune(n):
    eng.N = n
    eng.RULES = eng.build_rules()
    eng.LM = {name: lm for name, _, lm in eng.RULES}
    eng.REL = {name: rel for name, rel, _ in eng.RULES}
    eng.LC = {name: eng.REL[name][eng.LM[name]] for name in eng.LM}


def dw(x, y):
    return tuple(range(x, y - 1, -1)) if x >= y else ()


def start_element(i, a, b):
    j1, j2 = i - a, i - b
    d1, e2 = eng.desc_word(i, j1), eng.desc_word(i - 1, j2)
    n1, n2 = f"B{i-1}{i}{j1}", f"B{i-1}{i}{j2}"
    return dict(eng.clean(eng.combine(
        {w: eng.LC[n2] * c
         for w, c in eng.context_mul((), eng.REL[n1], e2 + (i,)).items()},
        {w: eng.LC[n1] * c
         for w, c in eng.context_mul(d1, eng.REL[n2], ()).items()}, -1)))


def next_redex(f):
    for w in sorted(f.keys(), key=eng.deglex_key):
        for name in eng.LM:
            pos = eng.infix_positions(w, eng.LM[name])
            if pos:
                return w, name, pos[0]
    return None


RMAP_CACHE = {}


def rule_ids(n):
    """rule name -> ('B'|'Y'|'Q'|'F', indices...) for the current tuning."""
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


def replay(i, a, b, upto):
    f = start_element(i, a, b)
    lineage = {w: k for k, w in enumerate(sorted(f, key=eng.deglex_key))}
    trace = []
    for _ in range(upto):
        t = next_redex(f)
        if t is None:
            break
        w, name, kk = t
        tag = lineage[w]
        left, right = w[:kk], w[kk + len(eng.LM[name]):]
        img = eng.context_mul(left, eng.REL[name], right)
        f = eng.clean(eng.combine(f, img, -sp.expand(f[w] / eng.LC[name])))
        for u in img:
            if u != w:
                lineage.setdefault(u, tag)
        trace.append({"lineage": tag, "terms": dict(f), "lin": dict(lineage),
                      "rule": name})
    return trace


def main():
    started = time.monotonic()
    rows, bad = [], 0
    for a in range(4, 7):
        for b in (a, a + 1):
            n, i = a + b + 3, a + b + 1
            if i >= n or i - b < 0:
                continue
            retune(n)
            j1, j2, i1, i2 = i - a, i - b, i - 1, i - 2
            jppp = j1 + 3
            opening = a * a - 3 * a + 9
            tr = replay(i, a, b, opening)
            rel = lambda w: tuple(i - x for x in w)

            V2 = (i2,) + dw(i, j1) + dw(i, j2)
            # loopTwoGen's target: A ++ descWord kd ed ++ descWord i j1
            #                        ++ descWord ed j2 ++ S,  kd = k-1 = i2
            e_, ed_ = jppp, jppp - 1
            U_loop = (i1,) + dw(i2, ed_) + dw(i, j1) + dw(ed_, j2) + (i,)

            head = [s["lineage"] for s in tr[:2]]
            v_ok = head == [0, 0] and V2 in tr[1]["terms"]
            # the U stretch: consecutive lineage-1 steps after the head
            u_len = 0
            for s in tr[2:]:
                if s["lineage"] != 1:
                    break
                u_len += 1
            # Where does loopTwoGen's target actually appear?  NOT at the end
            # of the contiguous U run: that run continues PAST the loop into
            # the bare Bokut-Shiao step and the quadratic pair.  Locating it
            # rather than assuming its index is the whole correction here --
            # the same wrong-index bug the tail's collision check had.
            loop_end = next((kk for kk in range(2, 2 + u_len)
                             if U_loop in tr[kk]["terms"]), None)
            u_end_ok = loop_end is not None
            loop_steps = (loop_end - 1) if loop_end is not None else 0
            after_loop = u_len - loop_steps
            covered = 2 + loop_steps
            # --- the V side.  The fit witness solves it with A_len = 2 and
            # S_len = 0, which V2 itself cannot supply (it has ONE letter
            # before descWord i j1), so the V loop must start later than V2.
            # Find where lineage 0 resumes and where its loop target lands.
            v_resume = next((kk for kk in range(2 + u_len, len(tr))
                             if tr[kk]["lineage"] == 0), None)
            V_loop = None
            v_loop_end = None
            if v_resume is not None:
                # loopTwoGen's target with A = 2 letters, S = []
                for A2 in {(i2, i), (i2, i1), (i, i2), (i1, i2)}:
                    cand = A2 + dw(i2, ed_) + dw(i, j1) + dw(ed_, j2)
                    hit = next((kk for kk in range(v_resume, len(tr))
                                if cand in tr[kk]["terms"]), None)
                    if hit is not None:
                        V_loop, v_loop_end = A2, hit
                        break
            # --- the trailing trio, by RULE IDENTITY rather than by shape.
            # Measured uniform in a and b: bokutShiaoRelation jp jpp j1, then
            # Yang-Baxter at (j1, jp), then the quadratic at j1 -- and the last
            # two are exactly quadPair's redex.
            ids = RMAP_CACHE.setdefault(n, rule_ids(n))
            jp_, jpp_ = j1 + 1, j1 + 2
            trio = None
            if loop_end is not None and loop_end + 3 <= len(tr):
                names = [tr[kk]["rule"] for kk in range(loop_end + 1,
                                                        loop_end + 4)]
                got = [ids.get(nm) for nm in names]
                trio = got == [("B", jp_, jpp_, j1), ("Y", j1, jp_), ("Q", j1)]
            # --- Can both loops run BEFORE either trio?
            # `loopTwoGen` is stated for a TWO-term element; `quadPair` takes
            # general L1/L2 and tolerates any number of bystanders.  Under the
            # engine's order the U trio (whose quadratic step SPLITS U in two)
            # precedes the V loop, so the V loop would face three terms and
            # `loopTwoGen` could not be applied at all.  Running both loops
            # first keeps each at two terms.  Same lesson as the tail: the
            # engine's schedule is an accident, not a constraint.
            Vt = (i2,) + dw(i1, ed_) + dw(i, j1) + dw(ed_, j2)
            u_split = next((kk for kk in range(len(tr))
                            if len(tr[kk]["terms"]) > 2), None)
            v_loop_at = next((kk for kk in range(len(tr))
                              if Vt in tr[kk]["terms"]), None)
            engine_forces_three = (u_split is not None
                                   and v_loop_at is not None
                                   and u_split < v_loop_at)
            ok = v_ok and u_end_ok
            bad += not ok
            rows.append({
                "a": a, "b": b, "i": i, "n": n,
                "opening_phase_steps": opening,
                "m_predicted": a - 4,
                "first_two_are_V0_landing_on_V2": v_ok,
                "U_stretch_steps": u_len,
                "loopTwoGen_target_reached": u_end_ok,
                "loop_steps": loop_steps,
                "U_steps_after_the_loop": after_loop,
                "steps_covered_by_s1_s2_and_loop": covered,
                "steps_remaining_in_opening": opening - covered,
                "V_side_resumes_at_step": v_resume,
                "V_loop_A_rel_i": [i - x for x in V_loop] if V_loop else None,
                "V_loop_target_at_step": v_loop_end,
                "trailing_trio_is_BS_jp_jpp_j1__Y_j1_jp__Q_j1": trio,
                "V_loop_m": i - jppp,
                "U_loop_m": i1 - jppp,
                "U_splits_at_step": u_split,
                "V_loop_completes_at_step": v_loop_at,
                "engine_order_forces_a_three_term_loop": engine_forces_three,
                # the full decomposition: 2 (s1,s2) + L (U loop) + 3 (U bare
                # BS + quadPair) + (L+1) (V loop, one level deeper) + 3
                "V_loop_steps": (v_loop_end - v_resume + 1)
                    if v_loop_end is not None else None,
                "decomposition_total": (2 + loop_steps + 3
                    + (v_loop_end - v_resume + 1) + 3)
                    if v_loop_end is not None else None,
                "decomposition_closes": (v_loop_end is not None
                    and 2 + loop_steps + 3 + (v_loop_end - v_resume + 1) + 3
                        == opening),
            })

    w = WitnessBuilder("hecke-opening-coverage", engine="sympy",
                       start_time=started)
    w.set_description(
        "Does the planned lemma set cover the a <= b opening phase? Plan: "
        "s1/s2 carry V0 to V2 (both j2-independent, already in the corpus), "
        "then loopTwoGen carries U0 at m = a-4, with k = i1 and e = jppp as "
        "hecke-prefix-loop-fit solved them. Measured against the chain: "
        "whether the first two steps really are V0's and land on V2, whether "
        "the next stretch is U0's alone, whether it ends on loopTwoGen's own "
        "target formula, and HOW MANY of the a^2-3a+9 opening steps that "
        "accounts for. The remainder is the point -- it says what else the "
        "opening needs. Measured: s1/s2 and the loop DO fit, but the "
        "contiguous U-run continues past the loop's endpoint by exactly 3 "
        "steps (a bare Bokut-Shiao, then the Yang-Baxter and quadratic pair "
        "that §4al's quadPair covers), so the loop's endpoint must be LOCATED "
        "rather than read off the end of the run -- the first version of this "
        "probe assumed the latter and reported a false negative in all six "
        "cases, the same wrong-index bug the tail's collision check had. "
        "With that fixed the phase decomposes EXACTLY into five stretches: "
        "s1/s2, the U loop, three trailing U steps, the V loop one level "
        "deeper, and three trailing V steps -- 2L+9 = a^2-3a+9, asserted per "
        "case. Every stretch is covered by a lemma that already exists.")
    w.add_parameter("m", "a - 4 (so a = 3 would need m = -1: no loop pass)")
    w.add_parameter("loop_levels", "k = i1 down to e = jppp")
    w.add_parameter(
        "opening_phase_decomposition",
        "2 (s1, s2: V0 -> V2) + L (U loop, A = [s_{i-1}], S = [s_i]) + 3 (U "
        "bare Bokut-Shiao, then quadPair) + (L+1) (V loop, A = "
        "[s_{i-2}, s_{i-1}], S = []; one level deeper because the V side has "
        "descended one further) + 3 (the same trailing trio) = 2L + 9, which "
        "is a^2-3a+9 exactly")
    w.add_parameter(
        "scheduling_constraint",
        "loopTwoGen is stated for a TWO-term element; quadPair takes general "
        "L1/L2 and tolerates any number of bystanders. Under the engine's "
        "deg-lex order the U trio -- whose quadratic step SPLITS U in two -- "
        "runs BEFORE the V loop, so the V loop would face three terms and "
        "loopTwoGen could not be applied at all. Measured per case. Both "
        "loops must therefore precede both trios, which is legal because "
        "steps on different terms commute. Same lesson as the tail: the "
        "engine's schedule is an accident, not a constraint on the Lean.")
    w.add_parameter(
        "V_loop", "loopTwoGen with A = [s_{i-2}], k = i, S = [], m = a-3 -- "
        "one level MORE than the U loop's a-4, which is what 'one level "
        "deeper' means concretely")
    w.add_parameter(
        "trailing_trio",
        "bokutShiaoRelation jp jpp j1, then Yang-Baxter at (j1, jp), then the "
        "quadratic at j1 -- uniform in a AND b, and the last two are exactly "
        "quadPair's redex [s_jp, s_j1, s_jp] ++ (s_j1 :: R). So each lineage's "
        "trio is one bsStep followed by quadPair; no new lemma.")
    w.add_assertion("cases_where_the_two_applications_do_not_fit",
                    computed=str(bad), expected="0")
    w.add_assertion(
        "cases_where_the_five-stretch_decomposition_does_not_close",
        computed=str(sum(0 if r["decomposition_closes"] else 1 for r in rows)),
        expected="0")
    w.add_assertion(
        "cases_where_the_engine_order_does_NOT_force_a_three-term_loop",
        computed=str(sum(0 if r["engine_order_forces_a_three_term_loop"] else 1
                         for r in rows)),
        expected="0")
    w.add_assertion(
        "cases_where_the_V_loop_m_is_not_one_more_than_the_U_loop_m",
        computed=str(sum(0 if r["V_loop_m"] == r["U_loop_m"] + 1 else 1
                         for r in rows)),
        expected="0")
    w.add_assertion(
        "cases_where_the_trailing_trio_is_not_BS(jp,jpp,j1)_Y(j1,jp)_Q(j1)",
        computed=str(sum(0 if r["trailing_trio_is_BS_jp_jpp_j1__Y_j1_jp__Q_j1"]
                         else 1 for r in rows)),
        expected="0")
    w.add_assertion(
        "cases_where_the_V_loop_is_not_one_level_deeper_than_the_U_loop",
        computed=str(sum(0 if r["V_loop_steps"] == r["loop_steps"] + 1 else 1
                         for r in rows)),
        expected="0")
    w.add_data("cases_checked", len(rows))
    w.add_data("cases", rows)
    w.add_caveat(
        "a >= 4 only. a = 3 has no loop pass (m would be -1) and needs its own "
        "treatment (`prefixChain3`); a = 2 has no loop pass either, for the "
        "opposite reason -- `descWord i j1` is three letters, so `U0` already "
        "carries quadPair's redex and the loop's output pre-exists. Its prefix "
        "is nonetheless the same 11 = a^2+a+5 steps and the same lemmas: "
        "`prefixChain2`, measured in hecke_small_a_decomposition.py. a = 1 is "
        "measured there too and is genuinely different (6 steps, and its "
        "cancellation word is not WStar); it is not yet proved.")
    w.add_caveat(
        "The 3 steps after the loop are the bare Bokut-Shiao step plus the "
        "Y-then-Q pair; §4al's quadPair covers the latter two, so the U side "
        "needs one more named step beyond loop + quadPair.")
    w.add_caveat(
        "Fitting the applications is not assembling the phase. The "
        "remainder column says how much is left, and the collision "
        "hypotheses are discharged here by head separation rather than "
        "checked lemma by lemma.")
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

    print("  a   b  opening   m  V0->V2  U-run  loop  after-loop  covered  left")
    for r in rows:
        print(f" {r['a']:>2}  {r['b']:>2} {r['opening_phase_steps']:>8}"
              f" {r['m_predicted']:>3}  {str(r['first_two_are_V0_landing_on_V2']):<6}"
              f" {r['U_stretch_steps']:>6} {r['loop_steps']:>5}"
              f" {r['U_steps_after_the_loop']:>11}"
              f" {r['steps_covered_by_s1_s2_and_loop']:>8}"
              f" {r['steps_remaining_in_opening']:>5}"
              f"   V@{r['V_side_resumes_at_step']}"
              f" A={r['V_loop_A_rel_i']} end={r['V_loop_target_at_step']}")
    print(f"\ncases: {len(rows)}   not fitting: {bad}")
    print(f"witness -> {path}")
    return 0 if not bad else 1


if __name__ == "__main__":
    raise SystemExit(main())
